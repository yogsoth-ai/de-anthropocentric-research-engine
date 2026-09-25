---
name: analogical-discovery
description: "Abstract relational structure from source domains, map it to the target, validate depth, and instantiate transferable mechanisms."
---

# analogical-discovery
## Purpose
Transfer a validated relational structure from a source domain into a target research problem.
## Input contract
```yaml
required: [target_problem, source_domain]
optional: [candidate_sources, transfer_constraints]
constraints: [source and target roles must be explicit]
```
## Execution protocol
Do not perform called SOP operations inline; each loaded SOP owns its contract and thresholds.

1. You MUST load skill `abstract-structure` to abstract the relational structure.
2. You MUST load skill `map-analogy` to map source relations to the target.
3. You MUST load skill `instantiate-transfer` to instantiate and test the transferred mechanism.
   If the analogy should be expanded across a typed combination space, consider `explore-dimensional-space`. If biological mechanisms are the relevant source domain, consider `biomimetic-transfer`. If several source structures must be composed, consider `conceptual-blending`. If the claimed mapping requires a formal preservation audit, `audit-structural-equivalence` may be the better next tactic.
Deviation: skip source search only when a supplied source is structurally specified; never skip mapping or transfer validation.
## Output contract
```yaml
produces: [abstract_structure, structural_mapping, transfer_candidate]
delta_fields: [findings, hypothesis_updates, uncertainties, decisions, open_questions]
```
## Thresholds and quality gates
- B: every transfer records source/target correspondences, unmapped relations, and a depth check; surface similarity alone is insufficient.
## Failure and counterexamples
Reject transfers whose causal/relational roles do not map, whose target constraints are violated, or whose claimed mechanism is only lexical resemblance.
## Provenance map
- `creative-ideation/cross-domain-discovery`, `analogical-transfer`, `design-by-analogy`, `functional-analogy`, `analogy-extraction`, `bridge-validation`: resolved where exact v3 node exists; campaign/strategy labels remain concept provenance.
- Status: all six exact names resolved against the v3 source graph.
## Preserved source criteria ledger
- Preserve deep structural correspondence and transfer viability; do not collapse to keyword similarity.
## Context checkpoint / Delta notes
Append source relations, mapping gaps, transfer assumptions, and validation findings.
