---
name: build-failure-chain
description: "Build multi-level cause -> failure mode -> effect chains and identify cascades/shared roots."
---

# build-failure-chain
## Purpose
Build cause → failure mode → effect chains and identify cascades and shared roots.
## Input contract
```yaml
required: [functions_or_process, failure_modes, observed_effects]
optional: [causal_evidence, dependency_graph]
constraints: [each edge needs a mechanism or evidence note]
```
## Procedure
1. Place causes, failure modes, and effects in typed levels.
2. Connect edges and record mechanism/evidence.
3. Mark cascades, shared roots, and unresolved links.
## Output contract
```yaml
produces: [failure_chain, cascade_map, shared_root_report]
delta_fields: [findings, evidence_updates, uncertainties, decisions]
```
## Quality gates
- Every effect has a traceable upstream path or is marked unexplained.
- Cycles and unsupported edges are flagged.
## Failure and counterexamples
Do not collapse correlation into a causal chain without an evidence or mechanism note.
## Provenance map
- resolved: failure-chain-construction
- resolved: failure-clustering
