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
Do not perform called SOP operations inline; each loaded SOP owns its contract and thresholds.

1. You MUST load skill `drill-five-whys` to drill repeated whys.
2. You MUST load skill `decompose-ishikawa` to decompose six causal categories.
3. You MUST load skill `build-current-reality-tree` to build the current-reality tree.
4. You MUST load skill `validate-causal-link` to validate its causal links.
   If the root-cause chain depends on untested assumptions, consider `assumption-stress-test` as the next tactic.
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
