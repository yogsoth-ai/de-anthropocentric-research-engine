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
1. Abstract relational structure (`abstract-structure`).
2. Map source relations to target (`map-analogy`).
3. Instantiate and test the transferred mechanism (`instantiate-transfer`).
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
- Status: all six exact names resolved in `scripts/refactory_source.json`.
## Preserved source criteria ledger
- Preserve deep structural correspondence and transfer viability; do not collapse to keyword similarity.
## Context checkpoint / Delta notes
Append source relations, mapping gaps, transfer assumptions, and validation findings.
