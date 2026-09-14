"""Mechanical v4 graph and skill validator. Exit 0 only when every gate passes."""
from __future__ import annotations

import argparse
import contextlib
import io
import json
import os
import re
import runpy
import shutil
import sys
import tempfile
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
PROV_SUFFIX = re.compile(r"\s*(?:\([^)]*\)|\[[^]]*\])\s*$")
CJK_OR_REPLACEMENT = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\U00020000-\U0002fa1f\ufffd]")
NON_ASCII_TYPO = re.compile(r"[≥≤≠≈±×→←—–“”‘’•…]")
HARNESS_CONTROL = re.compile(
    r"\bsubagents?\b|\bpause\s+and\s+report\s+partial\b|"
    r"\bcontext\s+tokens\b|\btoken\s+budget\b|\bspawn\s+fresh\b|"
    r"\bsummarize\s+and\s+spawn\b|<=\s*\d+\s*k\b",
    re.I,
)


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


def mode_branches(lines: list[str], sections: dict[str, tuple[int, int]]) -> tuple[list[tuple[str, int]], int] | None:
    """Read declared mode names and their source lines from ## Mode branches."""
    if "Mode branches" not in sections:
        return None
    start, end = sections["Mode branches"]
    declared: list[tuple[str, int]] = []
    for index in range(start, end):
        line = lines[index]
        match = re.match(r"^\s*[-*]\s+`([^`]+)`", line)
        if match:
            declared.append((match.group(1).strip(), index + 1))
            continue
        match = re.match(r"^\s*[-*]\s+([A-Za-z0-9][A-Za-z0-9_/-]*)\s*:", line)
        if match:
            declared.append((match.group(1).strip(), index + 1))
    return declared, start


def inline_yaml_list(value: str) -> list[str] | None:
    """Parse the locked contract format's inline YAML sequence subset."""
    value = value.strip()
    if not (value.startswith("[") and value.endswith("]")):
        return None
    body = value[1:-1].strip()
    if not body:
        return []
    items, current, quote = [], [], None
    for char in body:
        if char in "'\"":
            if quote == char:
                quote = None
            elif quote is None and not "".join(current).strip():
                quote = char
            else:
                current.append(char)
        elif char == "," and quote is None:
            item = "".join(current).strip()
            if not item:
                return None
            items.append(item.strip("'\""))
            current = []
        else:
            current.append(char)
    if quote is not None:
        return None
    item = "".join(current).strip()
    if not item:
        return None
    items.append(item.strip("'\""))
    return items


def contract_yaml(
    text: str,
    base_line: int,
    path: Path,
    checker: Checker,
    field_names: tuple[str, ...],
    registry_modes: list[str],
) -> tuple[dict[str, dict[str, list[str]]], dict[str, int], dict[tuple[str, str], int]]:
    """Parse one locked contract block and return values plus source lines."""
    lines = text.splitlines()
    fences = [i for i, line in enumerate(lines) if line.strip().startswith("```")]
    if len(fences) != 2 or lines[fences[0]].strip() != "```yaml":
        checker.error(path, base_line, "contract section must contain exactly one ```yaml block")
        return {}, {}, {}
    start, end = fences
    for i, line in enumerate(lines):
        if (i < start or i > end) and line.strip():
            checker.error(path, base_line + i, "contract section may contain only one YAML block")
    body = [(line, base_line + i) for i, line in enumerate(lines[start + 1:end], start + 1) if line.strip()]
    if not body:
        checker.error(path, base_line + start, "contract YAML block is empty")
        return {}, {}, {}

    expected = set(field_names)
    if not registry_modes:
        values: dict[str, list[str]] = {}
        field_lines: dict[tuple[str, str], int] = {}
        for line, line_no in body:
            match = re.fullmatch(r"([a-z_]+):\s*(.*)", line)
            if not match:
                checker.error(path, line_no, "flat contract entries must be unindented key: [list]")
                continue
            key, raw = match.groups()
            if key in values:
                checker.error(path, line_no, f"duplicate contract key {key!r}")
                continue
            parsed = inline_yaml_list(raw)
            if parsed is None:
                checker.error(path, line_no, f"contract field {key!r} must be an inline list")
                continue
            values[key] = parsed
            field_lines[("", key)] = line_no
        missing, extra = expected - set(values), set(values) - expected
        if missing:
            checker.error(path, base_line + start, f"flat contract missing keys: {sorted(missing)}")
        if extra:
            checker.error(path, field_lines.get(("", sorted(extra)[0]), base_line + start), f"flat contract has extra keys: {sorted(extra)}")
        return {"": values}, {"": base_line + start + 1}, field_lines

    first, first_line = body[0]
    if first != "mode_contracts:":
        checker.error(path, first_line, "mode-bearing contract must have only the top-level key mode_contracts")
        return {}, {}, {}

    contracts: dict[str, dict[str, list[str]]] = {}
    mode_lines: dict[str, int] = {}
    field_lines: dict[tuple[str, str], int] = {}
    anchors: dict[str, tuple[dict[str, list[str]], dict[str, int]]] = {}
    order: list[str] = []
    i = 1
    while i < len(body):
        line, line_no = body[i]
        match = re.fullmatch(r"  ([A-Za-z0-9][A-Za-z0-9_/-]*):(?:\s*([&*][A-Za-z0-9_-]+))?", line)
        if not match:
            checker.error(path, line_no, "mode contract entry must use two-space indentation")
            i += 1
            continue
        mode, marker = match.groups()
        if mode in contracts:
            checker.error(path, line_no, f"duplicate mode contract {mode!r}")
        else:
            order.append(mode)
            mode_lines[mode] = line_no
        i += 1
        if marker and marker.startswith("*"):
            anchor = marker[1:]
            if anchor not in anchors:
                checker.error(path, line_no, f"unknown YAML contract alias {marker!r}")
                values, source_lines = {}, {}
            else:
                values, source_lines = anchors[anchor]
                values, source_lines = dict(values), dict(source_lines)
            contracts.setdefault(mode, values)
            for key in values:
                field_lines[(mode, key)] = line_no
            continue

        values: dict[str, list[str]] = {}
        source_lines: dict[str, int] = {}
        while i < len(body) and body[i][0].startswith("    "):
            child, child_line = body[i]
            child_match = re.fullmatch(r"    ([a-z_]+):\s*(.*)", child)
            if not child_match:
                checker.error(path, child_line, "mode contract field must use four-space indentation")
                i += 1
                continue
            key, raw = child_match.groups()
            if key in values:
                checker.error(path, child_line, f"duplicate contract key {key!r} in mode {mode!r}")
                i += 1
                continue
            parsed = inline_yaml_list(raw)
            if parsed is None:
                checker.error(path, child_line, f"contract field {key!r} in mode {mode!r} must be an inline list")
            else:
                values[key] = parsed
                source_lines[key] = child_line
                field_lines[(mode, key)] = child_line
            i += 1
        contracts.setdefault(mode, values)
        if marker and marker.startswith("&"):
            anchors[marker[1:]] = (dict(values), dict(source_lines))

    actual = set(contracts)
    missing, extra = set(registry_modes) - actual, actual - set(registry_modes)
    if missing:
        checker.error(path, first_line, f"mode_contracts missing registry modes: {sorted(missing)}")
    if extra:
        checker.error(path, mode_lines.get(sorted(extra)[0], first_line), f"mode_contracts has modes absent from registry: {sorted(extra)}")
    if not missing and not extra and order != registry_modes:
        checker.error(path, first_line, "mode_contracts keys must follow registry mode order")
    for mode, values in contracts.items():
        missing_fields, extra_fields = expected - set(values), set(values) - expected
        if missing_fields:
            checker.error(path, mode_lines.get(mode, first_line), f"mode {mode!r} contract missing keys: {sorted(missing_fields)}")
        if extra_fields:
            checker.error(path, field_lines.get((mode, sorted(extra_fields)[0]), mode_lines.get(mode, first_line)), f"mode {mode!r} contract has extra keys: {sorted(extra_fields)}")
    return contracts, mode_lines, field_lines


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


def provenance_variants(value: str) -> set[str]:
    """Return exact lookup forms after removing provenance-only suffixes."""
    value = value.strip()
    stripped = value
    while True:
        next_value = PROV_SUFFIX.sub("", stripped).strip()
        if next_value == stripped:
            break
        stripped = next_value
    basename = stripped.rsplit("/", 1)[-1]
    variants = {value, stripped, basename}
    if "/" in stripped:
        package, name = stripped.rsplit("/", 1)
        variants.add(f"{package}-{name}")
    return {x for x in variants if x}


def check_text_encoding(path: Path, checker: Checker) -> None:
    data = path.read_bytes()
    if data.startswith(b"\xef\xbb\xbf"):
        checker.error(path, 1, "UTF-8 BOM is not allowed")
    lines = data.decode("utf-8").splitlines()
    fm_end = 0
    if lines and lines[0].strip() == "---":
        fm_end = next((i for i, line in enumerate(lines[1:], 1) if line.strip() == "---"), 0)
    for no, line in enumerate(lines[fm_end + 1:], fm_end + 2):
        if CJK_OR_REPLACEMENT.search(line):
            checker.error(path, no, "v4正文 contains CJK or replacement character")
        if NON_ASCII_TYPO.search(line):
            checker.error(path, no, "non-ASCII mathematical/typographic symbol; use ASCII equivalents (>=, <=, +/-, *, ->, <-, - or ...)")


def check_harness_decoupling(path: Path, lines: list[str], checker: Checker) -> None:
    for no, line in enumerate(lines, 1):
        if HARNESS_CONTROL.search(line):
            checker.error(path, no, "runtime/harness control is not allowed in v4 skill bodies")


def run_r5_against_v4() -> tuple[int, str, str]:
    """Run unchanged R5 against its own ledgers, adding only missing v4 bodies."""
    with tempfile.TemporaryDirectory(prefix="v4-r5-") as temp_name:
        root = Path(temp_name) / "R5"
        pilot, nodes = root / "pilot", root / "nodes"
        shutil.copytree(R5.parent / "pilot", pilot)
        shutil.copytree(R5.parent / "nodes", nodes)
        graph_data = json.loads(GRAPH.read_text(encoding="utf-8"))
        for node in graph_data.get("nodes", []):
            target_root = pilot if node.get("type") == "tactic" else nodes
            target = target_root / node["id"] / "body.md"
            source = SKILLS / node["id"] / "SKILL.md"
            if not target.exists() and source.exists():
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, target)
        ns = runpy.run_path(str(R5), run_name="r5_validator")
        ns["main"].__globals__["PILOT"] = pilot
        ns["main"].__globals__["NODES"] = nodes
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = ns["main"]()
        return code, out.getvalue(), err.getvalue()


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
    if actual != {"nodes": 267, "tactics": 51, "sops": 216, "calls": 317, "jumps": 157, "edges": 474, "capability_contracts": 147}:
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
        check_text_encoding(path, c)
        lines, sections = lines_and_sections(path)
        check_harness_decoupling(path, lines, c)
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
        # Gate 15: the executable mode vocabulary is shared by graph metadata
        # and the body.  Missing sections, extra declarations, and spelling
        # drift all invalidate the node and point back to the body line.
        declared_modes = mode_branches(lines, sections)
        graph_modes = [str(mode) for mode in (node.get("modes") or [])]
        if graph_modes and declared_modes is None:
            c.error(path, 1, f"Mode branches missing; graph declares modes: {', '.join(graph_modes)}")
        elif not graph_modes and declared_modes is not None:
            declarations, heading_line = declared_modes
            names = [mode for mode, _ in declarations]
            c.error(path, heading_line, f"Mode branches declares {names}, but graph declares no modes")
        elif declared_modes is not None:
            declarations, heading_line = declared_modes
            declared_names = {mode for mode, _ in declarations}
            graph_names = set(graph_modes)
            if len(declared_names) != len(declarations):
                c.error(path, heading_line, "Mode branches contains duplicate mode names")
            for mode, line_no in declarations:
                if mode not in graph_names:
                    c.error(path, line_no, f"mode {mode!r} is not declared in graph registry")
            for mode in graph_modes:
                if mode not in declared_names:
                    c.error(path, heading_line, f"graph mode {mode!r} missing from Mode branches")
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
        if inp:
            input_contracts, input_mode_lines, input_field_lines = contract_yaml(inp, inp_line, path, c, ("required", "optional", "constraints"), graph_modes)
        else:
            input_contracts, input_mode_lines, input_field_lines = {}, {}, {}
        if out:
            output_contracts, output_mode_lines, output_field_lines = contract_yaml(out, out_line, path, c, ("produces", "delta_fields"), graph_modes)
        else:
            output_contracts, output_mode_lines, output_field_lines = {}, {}, {}

        for mode, fields in input_contracts.items():
            required = fields.get("required", [])
            line_no = input_field_lines.get((mode, "required"), input_mode_lines.get(mode, inp_line))
            if any(GENERIC.search(x) for x in required):
                c.error(path, line_no, "generic required input placeholder")
        for mode, fields in output_contracts.items():
            delta = fields.get("delta_fields", [])
            line_no = output_field_lines.get((mode, "delta_fields"), output_mode_lines.get(mode, out_line))
            if "assumptions_updates" in delta:
                c.error(path, line_no, "delta_fields uses assumptions_updates; use assumption_updates (singular)")
            bad = set(delta) - DELTA
            if bad:
                c.error(path, line_no, f"delta_fields outside fixed eight: {sorted(bad)}")

        # Gate 17: the output contract is the executable per-mode result map.
        # Keep this separate from Gate 15, which compares body vocabulary to graph metadata.
        if graph_modes:
            declarations = declared_modes[0] if declared_modes is not None else []
            branch_names = {mode for mode, _ in declarations}
            contract_names = set(output_contracts)
            for mode, line_no in declarations:
                if mode not in contract_names:
                    c.error(path, line_no, f"Mode branches mode {mode!r} has no Output contract mode_contracts entry")
            for mode in sorted(contract_names - branch_names):
                c.error(path, output_mode_lines.get(mode, out_line), f"Output contract mode {mode!r} has no Mode branches declaration")
        sentences = [normalize_sentence(x) for x in proc.splitlines() if normalize_sentence(x)]
        counts_sent = Counter(sentences)
        for sent, n in counts_sent.items():
            if n >= 3: c.error(path, proc_line, f"same Procedure sentence occurs {n} times after SOP-id removal: {sent}")

    if SOURCE.exists():
        try:
            source_nodes = json.loads(SOURCE.read_text(encoding="utf-8")).get("nodes", [])
            source_names = {n.get("name", "") for n in source_nodes}
            source_names |= {x.rsplit("/", 1)[-1] for x in source_names}
            source_names |= {
                f"{n.get('package')}-{n.get('name')}"
                for n in source_nodes
                if n.get("package") and n.get("name")
            }
        except Exception:
            source_names = set()
        for node in nodes:
            for old in node.get("old", []):
                status = node.get("provenance_status", {}).get(old)
                if status != "concept":
                    continue
                if any(candidate in source_names for candidate in provenance_variants(old)):
                    c.error(GRAPH, 1, f"provenance is searchable but still marked concept: {old}")
    if caps.get("count") != len(caps.get("contracts", [])):
        c.error(CAPS, 1, "capability count does not match contracts")
    if not args.skip_threshold and R5.exists():
        result_code, result_stdout, result_stderr = run_r5_against_v4()
        if result_code:
            c.error(R5, 1, "R5 threshold fidelity gate failed; see its output")
            sys.stderr.write(result_stdout + result_stderr)
    return report(c)


def report(c: Checker) -> int:
    for line in c.warnings + c.errors: print(line, file=sys.stderr if line.startswith("ERROR") else sys.stdout)
    if c.errors:
        print(f"FAIL: {len(c.errors)} error(s), {len(c.warnings)} warning(s)", file=sys.stderr)
        return 1
    print(f"OK: graph validation passed ({len(c.warnings)} warning(s))")
    return 0


if __name__ == "__main__":
    # Normalize every non-zero or missing status to a failing process exit.
    raise SystemExit(0 if main() == 0 else 1)
