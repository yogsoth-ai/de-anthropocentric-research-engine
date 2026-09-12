---
name: drill-root-causes
description: "Move from symptoms to causal structure using complementary root-cause representations and causal-validity checks."
---

# drill-root-causes
## Purpose
Move from symptoms to causal structure using complementary root-cause representations and validity checks.
## Input contract
```yaml
required: [symptoms_or_undesirable_effects]
optional: [evidence, system_boundary, known_causes]
constraints: [each causal edge needs an evidence or assumption label]
```
## Execution protocol
1. Drill repeated whys (`drill-five-whys`).
2. Decompose six causal categories (`decompose-ishikawa`).
3. Build a current-reality tree (`build-current-reality-tree`).
4. Validate causal links (`validate-causal-link`).
Deviation: use fewer representations only when the input explicitly limits scope; record omitted views and reason.
## Output contract
```yaml
produces: [why_chain, ishikawa_map, current_reality_tree, root_cause_set]
delta_fields: [findings, assumption_updates, uncertainties, decisions, open_questions]
```
## Thresholds and quality gates
- B: at least one symptom-to-root path is represented in each selected model; every retained edge is checked for direction and support.
## Failure and counterexamples
Do not call a correlation a root cause, or stop at a label that cannot explain the observed effects.
## Provenance map
- `root-cause-drilling`, `causal-tree-building`, `five-whys-drilling`, `ishikawa-decomposition`, `current-reality-tree`: resolved/concept per exact lookup.
- Status: all five exact names resolved.
## Preserved source criteria ledger
- Preserve five-whys, 6M Ishikawa, TOC current-reality-tree, and causal-link validation.
## Context checkpoint / Delta notes
Append symptom changes, causal edges, competing roots, and validation failures.
