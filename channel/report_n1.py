import json
import pathlib
import re

BASE = pathlib.Path(__file__).resolve().parents[1]
ARCH = json.loads((BASE / "refactory/2026-08-23-22-16-dare-v4-architecture.json").read_text(encoding="utf-8"))
nodes = [x["id"] for x in ARCH["tactics"] + ARCH["sops"]]
pending = set("adjudicate-exchange construct-defense construct-perspective-set construct-validity-envelope derive-consequences design-mitigation detect-breakpoint elicit-weights enumerate-combinations evaluate-scenario-impact evaluate-scenario-robustness generate-provocation generate-subquestions identify-bottleneck identify-obstacles map-coverage-space measure-portfolio-diversity normalize-comparison-scale rotate-perspective sequence-work trace-causal-chain verify-evidence-independence".split())
lines = ["# N1 v4 build batches", "", "All 267 node directories are installed under `v4/skills/<node-id>/SKILL.md`.", "R4 30 are rebuilt from `scripts/refactory_source.json`; 22 BASIS nodes are temporary source-preserving shells pending R5 body delivery.", "A/B/C counts below are N1-new classifications (0/0/0); source groups retain their own audit ledgers.", ""]
for start in range(0, len(nodes), 10):
    batch = nodes[start:start + 10]
    resolved = concept = intermediate = duplicate = 0
    for node in batch:
        text = (BASE / "v4/skills" / node / "SKILL.md").read_text(encoding="utf-8")
        resolved += len(re.findall(r"^- resolved:", text, re.M))
        concept += len(re.findall(r"^- concept:", text, re.M))
        intermediate += len(re.findall(r"^- intermediate:", text, re.M))
        for heading in ("## Procedure", "## Execution protocol", "## Quality gates", "## Thresholds and quality gates"):
            if heading not in text:
                continue
            section = text.split(heading, 1)[1].split("## ", 1)[0]
            rows = [x.strip() for x in section.splitlines() if x.strip() and not x.startswith("#") and not x.startswith("```")]
            if any(rows.count(row) >= 3 for row in set(rows)):
                duplicate += 1
                break
    status = "source/rebuilt"
    if any(node in pending for node in batch):
        status = "installed; 该批含待 R5 正文节点"
    lines += [f"## Batch {start // 10 + 1} ({len(batch)})", "", f"IDs: {', '.join(batch)}", "", "A/B/C: 0/0/0 (N1 new)", f"provenance: resolved={resolved}, concept={concept}, intermediate={intermediate}", f"intra-section duplicate self-check: {'FAIL' if duplicate else 'PASS'}", f"status: {status}", ""]
(BASE / "channel/13-n1-build.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")
print(f"batches={((len(nodes) + 9) // 10)} nodes={len(nodes)}")
