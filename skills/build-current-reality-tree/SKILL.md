---
name: build-current-reality-tree
description: "Build a sufficient-cause Current Reality Tree linking undesirable effects to a small root set."
---

# build-current-reality-tree
## Purpose
Build a sufficient-cause Current Reality Tree linking undesirable effects to a small root set.
## Input contract
```yaml
required: [undesirable_effects, causal_evidence]
optional: [candidate_causes, system_boundary]
constraints: [each AND/OR connection requires a stated causal rationale]
```
## Procedure
1. Normalize undesirable effects into observable statements.
2. Connect effects with sufficient-cause relationships, marking AND requirements.
3. Trace converging chains to a small root set and test each link.
## Output contract
```yaml
produces: [current_reality_tree, root_cause_candidates, causal_rationale]
delta_fields: [findings, assumption_updates, uncertainties, decisions]
```
## Quality gates
- Every effect has an incoming explanation or is marked unexplained; root candidates explain multiple effects where evidence supports it.
## Failure and counterexamples
Do not infer causality from co-occurrence, and do not force a single root when independent roots remain.
## Provenance map
- `deep-insight/current-reality-tree`: resolved.
