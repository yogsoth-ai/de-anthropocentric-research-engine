---
name: select-solution-variants
description: "Select candidate variants under fitness, novelty, constraint, and diversity criteria while avoiding premature population collapse."
---

# select-solution-variants
## Purpose
Select candidate variants under fitness, novelty, constraint, and diversity criteria without premature collapse.
## Input contract
```yaml
required: [variant_population, selection_criteria]
optional: [hard_constraints, diversity_target, protected_niches]
constraints: [criteria weights or vetoes must be explicit]
```
## Procedure
1. Remove variants violating hard constraints.
2. Score fitness, novelty, and diversity for the eligible set.
3. Select a portfolio and record excluded variants and reasons.
## Output contract
```yaml
produces: [selected_variants, exclusion_register, selection_scores]
delta_fields: [findings, uncertainties, decisions]
```
## Quality gates
- Selection criteria and exclusions are auditable; diversity is assessed before choosing a single winner.
## Failure and counterexamples
Reject a selection that hides vetoes or collapses a required niche.
## Provenance map
- `evolution-strategy/selection`: concept (no exact pool entry; related names are distinct).
