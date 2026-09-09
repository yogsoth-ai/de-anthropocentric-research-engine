"""Mechanical fidelity gate for numeric and textual source criteria."""
from __future__ import annotations
import json, re, sys
from pathlib import Path

ARCH = Path(r"D:\YOGSOTH-AI\file-transfer\2026-08-23-22-16-dare-v4-architecture.json")
SKILLS = Path(r"D:\YOGSOTH-AI\de-anthropocentric-research-engine\skills")
PILOT = Path(__file__).parent / "pilot"
IDS = ["synthesize-meta-analytic-evidence", "design-experiment", "formulate-hypotheses", "analyze-constraints-readiness", "rank-candidates", "establish-empirical-baseline", "audit-benchmark-validity"]

# Shared semantics: each named pattern is used for both counting and ledger generation.
PATTERNS = [
    ("symbolic-comparator", re.compile(r"(?:>=|<=|≥|≤|±)"), "symbolic comparator"),
    ("at-least", re.compile(r"\bat\s+least\s+\d+\b", re.I), "at least N"),
    ("top-n", re.compile(r"\btop[- ]?\d+\b", re.I), "top-N"),
    ("percentage", re.compile(r"\b\d+(?:\.\d+)?\s*%"), "percentage"),
    ("numeric-range", re.compile(r"\b\d+\s*[-–]\s*\d+\b"), "numeric range"),
    ("angle-comparator", re.compile(r"(?:<|>)\s*\d+\b"), "< N / > N"),
    ("table-digits", re.compile(r"^\s*\|.*\d"), "table row containing digits"),
    ("mandatory", re.compile(r"\b(?:must|cannot|required|minimum)\b", re.I), "mandatory predicate"),
    ("preregistration", re.compile(r"pre[- ]?registr|post[- ]hoc", re.I), "preregistration predicate"),
    ("fair-comparison", re.compile(r"same\s+(?:compute|tuning|conditions?)|fair\s+comparison|control\s+all\s+confounds|comparab(?:le|ility)", re.I), "same-condition/fair-comparison predicate"),
    ("reproducibility", re.compile(r"reproducib|random\s+seeds?|software\s+environment|non[- ]determin|verification\s+protocol", re.I), "reproducibility predicate"),
    ("entry-gate", re.compile(r"HARD[- ]GATE|before entering|quality gate|budget gate|minimum yield|cannot exit", re.I), "explicit entry-gate phrase"),
]
RELATIVE_PATTERNS = [
    ("coverage-ratio", re.compile(r"coverage\s+ratio|coverage_ratio", re.I)),
    ("independent-source-ratio", re.compile(r"independent[- ]source\s+ratio|independent_source_ratio", re.I)),
    ("marginal-information-gain", re.compile(r"marginal\s+information\s+gain|marginal_information_gain", re.I)),
    ("saturation-state", re.compile(r"saturation\s+state|saturation_state", re.I)),
    ("declared-universe", re.compile(r"declared\s+(?:eligible\s+)?(?:universe|evidence\s+pool)|(?:eligible|evidence)\s+(?:evidence\s+)?universe|evidence\s+pool", re.I)),
    ("audit-numerator-denominator", re.compile(r"numerator.*denominator|denominator.*numerator", re.I)),
    ("batch-increment", re.compile(r"batch\s+increment|batch_delta", re.I)),
    ("stopping-reason", re.compile(r"stopping\s+reason|stop(?:ping)?\s+reason", re.I)),
]

def source_files():
    return {p.parent.name: p for p in SKILLS.rglob("SKILL.md")}

def criteria(src):
    out = []
    lines = src.read_text(encoding="utf-8").splitlines()
    in_frontmatter = bool(lines and lines[0].strip() == "---")
    for no, line in enumerate(lines, 1):
        if in_frontmatter:
            if no > 1 and line.strip() == "---": in_frontmatter = False
            continue
        if "<!-- BEGIN available-tables (generated) -->" in line: break
        hit = next(((name, label) for name, rx, label in PATTERNS if rx.search(line)), None)
        if hit:
            name, _ = hit
            numeric = name in {"symbolic-comparator", "at-least", "top-n", "percentage", "numeric-range", "angle-comparator"}
            out.append((no, "numeric-table" if name == "table-digits" else ("numeric" if numeric else "textual"), line.strip()))
    return out

def body_text(path):
    text = path.read_text(encoding="utf-8")
    if text.startswith("---"):
        parts = text.split("---", 2)
        text = parts[2] if len(parts) == 3 else text
    return text.split("<!-- BEGIN available-tables (generated) -->", 1)[0]

def contains(body, criterion):
    normalize = lambda s: " ".join(s.replace("\\\\|", "|").replace("\\|", "|").split())
    return normalize(criterion) in normalize(body)

def main():
    graph = json.loads(ARCH.read_text(encoding="utf-8"))
    by_name, missing, total = source_files(), [], 0
    for node_id in IDS:
        node = next(n for n in graph["tactics"] if n["id"] == node_id)
        body, node_total, node_missing = body_text(PILOT / node_id / "body.md"), 0, 0
        for old in node.get("old", []):
            name = old.rsplit("/", 1)[-1].split(" [", 1)[0].strip()
            src = by_name.get(name)
            if src is None:
                continue
            for line_no, _, line in criteria(src):
                node_total += 1; total += 1
                if not contains(body, line):
                    node_missing += 1; missing.append(f"{node_id}: {src}:{line_no}: {line}")
        print(f"{node_id}: source criteria={node_total}, missing={node_missing}")
        relative_hits = sum(bool(rx.search(body)) for _, rx in RELATIVE_PATTERNS)
        print(f"{node_id}: relative-patterns={relative_hits}/{len(RELATIVE_PATTERNS)}")
    print("Known blind spots: number words/non-English thresholds; implicit domain criteria without cue words; qualitative adjectives (adequate/relevant/representative); formulas or constraints outside matched forms; zero/low-count nodes require manual review.")
    if missing:
        print("MISSING source criteria:", file=sys.stderr); print("\n".join(missing), file=sys.stderr); return 1
    print(f"OK: {total} matched source criteria present"); return 0

if __name__ == "__main__":
    raise SystemExit(main())
