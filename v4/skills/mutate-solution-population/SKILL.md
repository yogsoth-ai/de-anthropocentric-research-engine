---
name: mutate-solution-population
description: "Generate controlled variants of a solution population through mutation/recombination operators while retaining lineage and changed dimensions."
---

# mutate-solution-population
## Purpose
Generate controlled solution variants through mutation or recombination while retaining lineage and changed dimensions.
## Input contract
```yaml
required: [solution_population, mutation_or_recombination_rules]
optional: [protected_features, variation_budget]
constraints: [each variant records parent lineage and changed dimensions]
```
## Procedure
1. Select parent solutions and dimensions eligible for change.
2. Apply declared mutation or recombination operations.
3. Validate variant coherence and record lineage, novelty, and protected features.
## Output contract
```yaml
produces: [variant_population, lineage_map, changed_dimensions, novelty_notes]
delta_fields: [findings, hypothesis_updates, uncertainties]
```
## Quality gates
- No variant lacks lineage; mutations are bounded and recombinations identify both parents.
## Failure and counterexamples
Reject untracked variants or mutations that alter protected features without an explicit override.
## Provenance map
- `evolution-strategy/variation`: concept (no exact pool entry; exact pool entry is `parameter-variation`).
