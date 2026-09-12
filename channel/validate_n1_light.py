import json
import pathlib
import re

BASE = pathlib.Path(__file__).resolve().parents[1]
ARCH = json.loads((BASE / "refactory/2026-08-23-22-16-dare-v4-architecture.json").read_text(encoding="utf-8"))
PART = json.loads((BASE / "channel/_partition.json").read_text(encoding="utf-8"))
ids = []
for group in PART.values():
    for item in group:
        if item[0] not in ids:
            ids.append(item[0])
for p in (BASE / "channel/deliverables/R5/pilot").glob("*/body.md"):
    if p.parent.name not in ids:
        ids.append(p.parent.name)
assert len(ids) == 267
types = {x["id"]: "tactic" for x in ARCH["tactics"]}
types.update({x["id"]: "sop" for x in ARCH["sops"]})
allowed_delta = {"findings", "evidence_updates", "hypothesis_updates", "assumption_updates", "uncertainties", "decisions", "open_questions", "recommended_jumps"}
bad = []
counts = {"tactic": 0, "sop": 0}
for node in ids:
    p = BASE / "v4/skills" / node / "SKILL.md"
    if not p.exists():
        continue
    text = p.read_text(encoding="utf-8")
    counts[types[node]] += 1
    if not re.match(r"^---\nname: [^\n]+\ndescription: \".*\"\n---\n", text, re.S):
        bad.append((node, "frontmatter"))
    if any(x in text for x in ("dependencies:", "used-by:", "tags:")):
        bad.append((node, "forbidden-frontmatter-field"))
    required = ["## Purpose", "## Input contract", "## Output contract", "## Provenance map"]
    required += ["## Execution protocol", "## Thresholds and quality gates", "## Preserved source criteria ledger", "## Context checkpoint / Delta notes"] if types[node] == "tactic" else ["## Procedure", "## Quality gates", "## Failure and counterexamples"]
    for heading in required:
        if heading not in text:
            bad.append((node, f"missing:{heading}"))
    if "```yaml\nrequired: [source_state, task_object]" in text or "```yaml\nrequired: [source_state, task_object]" in text:
        bad.append((node, "placeholder-input"))
    m = re.search(r"delta_fields: \[([^]]*)\]", text)
    if m and any(x.strip() not in allowed_delta for x in m.group(1).split(",") if x.strip()):
        bad.append((node, "delta-field"))
for node in ids:
    if types[node] == "sop":
        p = BASE / "v4/skills" / node / "SKILL.md"
        if not p.exists():
            continue
        text = p.read_text(encoding="utf-8")
        proc = text.split("## Procedure", 1)[1].split("## Output contract", 1)[0] if "## Procedure" in text else ""
        quality = text.split("## Quality gates", 1)[1].split("## Failure and counterexamples", 1)[0] if "## Quality gates" in text else ""
        if proc.strip() and len(set(x.strip() for x in proc.splitlines() if x.strip() and not x.startswith("#"))) < 3:
            bad.append((node, "procedure-too-thin"))
        if quality.count("- ") > 0 and len(set(x.strip() for x in quality.splitlines() if x.strip().startswith("- "))) < quality.count("- "):
            bad.append((node, "quality-duplicate"))
print(f"checked={len(ids)} tactics={counts['tactic']} sops={counts['sop']} failures={len(bad)}")
for item in bad[:20]:
    print(item)
raise SystemExit(1 if bad else 0)
