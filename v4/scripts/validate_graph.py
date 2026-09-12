"""Mechanical v4 graph and skill validator. Exit 0 only when every gate passes."""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections import Counter, defaultdict, deque
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
V4 = ROOT / "v4"
GRAPH = V4 / "registry" / "graph.json"
CAPS = V4 / "registry" / "capabilities.json"
SKILLS = V4 / "skills"
ARCH = Path(r"D:\YOGSOTH-AI\file-transfer\2026-08-23-22-16-dare-v4-architecture.json")
SOURCE = ROOT / "scripts" / "refactory_source.json"
R5 = ROOT / "channel" / "deliverables" / "R5" / "validate_threshold_fidelity.py"
DELTA = {"findings", "evidence_updates", "hypothesis_updates", "assumption_updates", "uncertainties", "decisions", "open_questions", "recommended_jumps"}
GENERIC = re.compile(r"\b(?:source_state|task_object|input_object)\b", re.I)
SOP_ID = re.compile(r"\(([A-Za-z0-9][\w-]*)\)")


class Checker:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, path: Path, line: int | None, msg: str) -> None:
        loc = f"{path}:{line}" if line else str(path)
        self.errors.append(f"ERROR {loc}: {msg}")

    def warn(self, path: Path, line: int | None, msg: str) -> None:
        loc = f"{path}:{line}" if line else str(path)
        self.warnings.append(f"WARN {loc}: {msg}")


def lines_and_sections(path: Path) -> tuple[list[str], dict[str, tuple[int, int]]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    heads = []
    in_fm = bool(lines and lines[0].strip() == "---")
    in_fence = False
    for i, line in enumerate(lines):
        if in_fm:
            if i and line.strip() == "---": in_fm = False
            continue
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if not in_fence and (m := re.match(r"^##\s+(.+?)\s*$", line)):
            heads.append((i, m.group(1).strip()))
    sections = {}
    for pos, (start, name) in enumerate(heads):
        sections[name] = (start + 1, heads[pos + 1][0] if pos + 1 < len(heads) else len(lines))
    return lines, sections


def block(lines: list[str], sections: dict[str, tuple[int, int]], name: str) -> tuple[str, int]:
    if name not in sections:
        return "", 0
    start, end = sections[name]
    return "\n".join(lines[start:end]), start + 1


def yaml_list(text: str, key: str) -> tuple[list[str], int] | None:
    m = re.search(rf"^\s*{re.escape(key)}:\s*\[([^]]*)\]", text, re.M)
    if not m:
        return None
    vals = [x.strip().strip("'\"") for x in m.group(1).split(",") if x.strip()]
    return vals, text[:m.start()].count("\n") + 1


def frontmatter(lines: list[str]) -> tuple[dict[str, str], int]:
    if not lines or lines[0].strip() != "---":
        return {}, 1
    out = {}
    for no, line in enumerate(lines[1:], 2):
        if line.strip() == "---":
            return out, no
        if ":" in line:
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip().strip("'\"")
    return out, len(lines)


def normalize_sentence(line: str) -> str:
    line = re.sub(r"\([^)]*\)", "", line)
    line = re.sub(r"^\s*(?:[-*]|\d+[.)])\s*", "", line)
    return " ".join(line.split()).strip().lower()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--skip-threshold", action="store_true")
    args = ap.parse_args()
    c = Checker()
    try:
        graph = json.loads(GRAPH.read_text(encoding="utf-8"))
        caps = json.loads(CAPS.read_text(encoding="utf-8"))
    except Exception as exc:
        c.error(GRAPH, 1, f"cannot read registry: {exc}")
        return report(c)

    nodes = graph.get("nodes", [])
    by_id = {n.get("id"): n for n in nodes}
    tactics = {n["id"] for n in nodes if n.get("type") == "tactic"}
    sops = {n["id"] for n in nodes if n.get("type") == "sop"}
    if len(by_id) != len(nodes): c.error(GRAPH, 1, "duplicate node id")
    expected = {p.name for p in SKILLS.iterdir() if p.is_dir()} if SKILLS.exists() else set()
    if expected:
        if expected != set(by_id):
            for x in sorted(expected - set(by_id)): c.error(SKILLS / x, 1, "skill directory missing from graph")
            for x in sorted(set(by_id) - expected): c.error(GRAPH, 1, f"node {x!r} missing skill directory")
    else:
        c.warn(SKILLS, 1, "v4 skills are not present yet; registry-only validation")
    counts = graph.get("counts", {})
    actual = {"nodes": len(nodes), "tactics": len(tactics), "sops": len(sops), "calls": len(graph.get("calls", [])), "jumps": len(graph.get("jumps", [])), "edges": len(graph.get("edges", [])), "capability_contracts": caps.get("count")}
    for k, v in actual.items():
        if counts.get(k) != v: c.error(GRAPH, 1, f"count {k}={counts.get(k)!r}, actual {v}")
    if actual != {"nodes": 267, "tactics": 51, "sops": 216, "calls": 317, "jumps": 157, "edges": 474, "capability_contracts": 146}:
        c.error(GRAPH, 1, f"authoritative counts mismatch: {actual}")

    for i, e in enumerate(graph.get("calls", []), 1):
        if e.get("source") not in tactics or e.get("target") not in sops:
            c.error(GRAPH, i, f"illegal calls edge {e}")
    for i, e in enumerate(graph.get("jumps", []), 1):
        a, b = by_id.get(e.get("source")), by_id.get(e.get("target"))
        if not a or not b or a["type"] != b["type"]:
            c.error(GRAPH, i, f"jump must stay within tactic or sop type: {e}")
        if any(x in str(e).lower() for x in ("provider", "tool")):
            c.error(GRAPH, i, "provider/tool edge is forbidden")
    adj = defaultdict(list)
    for e in graph.get("calls", []): adj[e["source"]].append(e["target"])
    for e in graph.get("jumps", []): adj[e["source"]].append(e["target"])
    seen, q = set(tactics), deque(tactics)
    while q:
        for nxt in adj[q.popleft()]:
            if nxt not in seen: seen.add(nxt); q.append(nxt)
    for x in sorted(set(by_id) - seen): c.error(GRAPH, 1, f"unreachable node {x}")

    for node_id, node in by_id.items():
        path = SKILLS / node_id / "SKILL.md"
        if not path.exists(): continue
        lines, sections = lines_and_sections(path)
        fm, fm_end = frontmatter(lines)
        if set(fm) != {"name", "description"}:
            c.error(path, 1, f"frontmatter keys must be name + description, got {sorted(fm)}")
        if fm.get("description") != node.get("desc"):
            c.error(path, next((i for i,l in enumerate(lines,1) if l.startswith("description:")), 1), "description differs from graph desc")
        if node["type"] == "tactic":
            required = ["Purpose", "Input contract", "Execution protocol", "Output contract", "Thresholds and quality gates", "Failure and counterexamples", "Provenance map", "Preserved source criteria ledger", "Context checkpoint / Delta notes"]
        else:
            required = ["Purpose", "Input contract", "Procedure", "Output contract", "Quality gates", "Failure and counterexamples", "Provenance map"]
        positions = []
        for name in required:
            if name not in sections: c.error(path, 1, f"missing section ## {name}")
            else: positions.append((sections[name][0], name))
        if positions != sorted(positions): c.error(path, 1, "template sections are out of order")
        proc_name = "Execution protocol" if node["type"] == "tactic" else "Procedure"
        proc, proc_line = block(lines, sections, proc_name)
        if node["type"] == "tactic":
            refs = re.findall(r"\b[a-z][a-z0-9-]+\b", proc)
            declared = set(graph.get("calls_by_tactic", {}).get(node_id, []))
            declared = {e["target"] for e in graph.get("calls", []) if e["source"] == node_id}
            for ref in set(refs) & sops:
                if ref not in declared: c.error(path, proc_line, f"Execution protocol references SOP {ref} not in calls")
        if node.get("scope") == "shared-basis" and "Parameterization" not in sections:
            c.error(path, 1, "shared-basis SOP requires ## Parameterization")
        inp, inp_line = block(lines, sections, "Input contract")
        out, out_line = block(lines, sections, "Output contract")
        req = yaml_list(inp, "required")
        if req and any(GENERIC.search(x) for x in req[0]): c.error(path, inp_line + req[1] - 1, "generic required input placeholder")
        delta = yaml_list(out, "delta_fields")
        prod = yaml_list(out, "produces")
        if delta:
            bad = set(delta[0]) - DELTA
            if bad: c.error(path, out_line + delta[1] - 1, f"delta_fields outside fixed eight: {sorted(bad)}")
        sentences = [normalize_sentence(x) for x in proc.splitlines() if normalize_sentence(x)]
        counts_sent = Counter(sentences)
        for sent, n in counts_sent.items():
            if n >= 3: c.error(path, proc_line, f"same Procedure sentence occurs {n} times after SOP-id removal: {sent}")

    if SOURCE.exists():
        try:
            source_names = {n.get("name", "") for n in json.loads(SOURCE.read_text(encoding="utf-8")).get("nodes", [])}
            source_names |= {x.rsplit("/", 1)[-1] for x in source_names}
        except Exception:
            source_names = set()
        for node in nodes:
            for old in node.get("old", []):
                candidates = (old.split(" [",1)[0], old.rsplit("/",1)[-1].split(" [",1)[0])
                if "concept" in old.lower() and not any(x in source_names or x.replace("/", "-") in source_names for x in candidates):
                    c.error(GRAPH, 1, f"concept provenance not found in refactory source: {old}")
    if caps.get("count") != len(caps.get("contracts", [])):
        c.error(CAPS, 1, "capability count does not match contracts")
    if not args.skip_threshold and R5.exists():
        result = subprocess.run([sys.executable, str(R5)], cwd=ROOT, capture_output=True, text=True)
        if result.returncode:
            c.error(R5, 1, "R5 threshold fidelity gate failed; see its output")
            sys.stderr.write(result.stdout + result.stderr)
    return report(c)


def report(c: Checker) -> int:
    for line in c.warnings + c.errors: print(line, file=sys.stderr if line.startswith("ERROR") else sys.stdout)
    if c.errors:
        print(f"FAIL: {len(c.errors)} error(s), {len(c.warnings)} warning(s)", file=sys.stderr)
        return 1
    print(f"OK: graph validation passed ({len(c.warnings)} warning(s))")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
