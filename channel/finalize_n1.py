import json
import pathlib
import shutil

BASE = pathlib.Path(__file__).resolve().parents[1]
ARCH = json.loads((BASE / "refactory/2026-08-23-22-16-dare-v4-architecture.json").read_text(encoding="utf-8"))
PART = json.loads((BASE / "channel/_partition.json").read_text(encoding="utf-8"))
r4 = {
    "analyze-experiment-results", "analyze-future-scenarios", "build-domain-ontology",
    "construct-argument-map", "construct-causal-model", "decompose-research-question",
    "falsifiability-audit", "formulate-research-question", "pairwise-ranking",
    "portfolio-optimization", "structured-consensus", "construct-design-matrix",
    "design-randomness-protocol", "estimate-sample-size", "extract-core-conflict",
    "identify-critical-chain", "identify-scenario-drivers", "list-undesirable-effects",
    "map-ablation-components", "optimize-design-under-budget", "predict-competitive-move",
    "project-future-reality", "quantify-resource-gap", "select-experimental-baseline",
    "select-statistical-method", "specify-execution-environment", "specify-metrics",
    "specify-reproducibility-protocol", "statistical-testing", "verify-reproducibility",
}
ids = set(r4)
for group in ("R1", "R2", "R3", "R5"):
    for p in (BASE / f"channel/deliverables/{group}").rglob("body.md"):
        ids.add(p.parent.name)
for p in (BASE / "channel/deliverables/R5/pilot").glob("*/body.md"):
    ids.add(p.parent.name)
ids = sorted(ids)
all_nodes = sorted({x["id"] for x in ARCH["tactics"] + ARCH["sops"]})
accepted = set(r4)
for group in ("R1", "R2", "R3", "R5"):
    for p in (BASE / f"channel/deliverables/{group}").rglob("body.md"):
        if p.parent.name in all_nodes:
            accepted.add(p.parent.name)
for p in (BASE / "channel/deliverables/R5/pilot").glob("*/body.md"):
    accepted.add(p.parent.name)
pending = sorted(set(all_nodes) - accepted)

lines = ["# N1 v4 build log", "", "Source policy: accepted R1/R2/R3/R5/pilot bodies copied with architecture descriptions; R4 30 rebuilt from refactory_source.json; 42 R4 old shells ignored.", "", f"Delivered: {len(accepted)}", f"Pending R5 source bodies: {len(pending)}", ""]
for node in all_nodes:
    if node in accepted:
        lines.append(f"- {node}: delivered ({'R4-rebuilt' if node in r4 else 'source-body'})")
    else:
        lines.append(f"- {node}: pending R5 body")
(BASE / "v4/_build-log-N1.md").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")

batch_lines = ["# N1 build batches", "", f"Delivered nodes: {len(accepted)}", f"Pending nodes: {len(pending)}", ""]
for i in range(0, len(all_nodes), 10):
    batch = all_nodes[i:i + 10]
    batch_lines.append(f"## Batch {i // 10 + 1} ({len(batch)})")
    batch_lines.append(", ".join(batch))
    batch_lines.append(f"status: {'delivered' if all(x in accepted for x in batch) else 'pending R5 source'}")
    batch_lines.append("")
(BASE / "channel/13-n1-build.md").write_text("\n".join(batch_lines), encoding="utf-8", newline="\n")
print(f"delivered={len(accepted)} pending={len(pending)}")
print("pending=" + ",".join(pending))
