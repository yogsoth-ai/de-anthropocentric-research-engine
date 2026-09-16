---
name: explore-dimensional-space
description: "Represent a problem/research space as validated dimensions and values, enumerate compatible combinations, and optionally map occupancy, detect gaps, prioritize regions, or synthesize candidate questions/ideas."
---

# explore-dimensional-space
## Purpose
Represent a problem space as validated dimensions and values, enumerate compatible combinations, map occupancy, detect gaps, and synthesize candidate questions or ideas.
## Input contract
```yaml
mode_contracts:
  morphological-generation: &dimensional_input
    required: [target_space, dimensions, values]
    optional: [coverage_matrix, compatibility_rules, objective]
    constraints: [dimension_semantics_and_independence_posture_must_be_declared]
  research-space-mapping: *dimensional_input
  gap-mapping: *dimensional_input
```
## Execution protocol
Do not perform called SOP operations inline; each loaded SOP owns its contract and thresholds.

1. You MUST load skill `define-analysis-dimensions` to define the exploration axes. You MUST load skill `enumerate-dimension-values` to enumerate meaningful values.
2. Apply the selected mode's combination, compatibility, and coverage operations.
3. Retain axis dependencies and uncovered regions exposed by the selected mode.
4. When the task is not descriptive mapping, You MUST load skill `score-object` to score the retained regions. When a research question is in scope, You MUST load skill `generate-subquestions` to derive questions from those regions.
   If deliberate disruption is needed to escape the declared axes, consider `destructive-ideation`. If the main objective becomes systematic coverage repair, `coverage-white-space-search` may be the better next tactic.
Deviation: skip scoring when the task is descriptive mapping; skip subquestions when no research question is in scope.
## Output contract
```yaml
mode_contracts:
  morphological-generation:
    produces: [dimension_schema, value_catalog, combination_map, compatibility_report]
    delta_fields: [findings, evidence_updates, hypothesis_updates, uncertainties, decisions, recommended_jumps]
  research-space-mapping:
    produces: [dimension_schema, value_catalog, coverage_gaps, prioritized_regions, subquestions]
    delta_fields: [findings, evidence_updates, hypothesis_updates, uncertainties, decisions, recommended_jumps]
  gap-mapping:
    produces: [coverage_gaps, prioritized_regions, subquestions]
    delta_fields: [findings, evidence_updates, hypothesis_updates, uncertainties, decisions, recommended_jumps]
```
## Thresholds and quality gates
- Axis independence, compatibility rules, and gap representation must be inspectable.
- Scores require a declared rubric and evidence.
## Failure and counterexamples
Do not call a sparse matrix a white space until compatibility and coverage semantics are checked. Merge redundant axes rather than double-counting them.
## Provenance map
- resolved: morphological-exploration
- resolved: general-morphological-analysis
- resolved: cross-consistency-analysis
- concept: combination-mapping [tactic]
- concept: consistency-checking [tactic]
- resolved: dimensional-analysis
- concept: axis-identification [strategy]
- concept: combination-mapping [strategy]
- concept: gap-prioritization [strategy]
- resolved: matrix-generation
- intermediate: Pass5/morphological-search
- intermediate: Pass5/map-dimensional-research-space
## Preserved source criteria ledger
| source | source line | kind | source criterion |
|---|---:|---|---|
| v4 architecture | node desc | textual | Enumerate compatible combinations, validate axes, map occupancy and detect gaps. |
## Context checkpoint / Delta notes
Append dimensions, values, combinations, pruned regions, gaps, scores, and derived questions.

## Mode branches
- `morphological-generation`: emphasize unconstrained combination generation before pruning. You MUST load skill `enumerate-combinations` to enumerate the combinations. You MUST load skill `evaluate-compatibility` to prune incompatible combinations.
- `research-space-mapping`: emphasize typed dimensions, occupancy, and coverage. You MUST load skill `validate-axis-independence` to identify dependent axes.
- `gap-mapping`: emphasize absent/thin/disconnected regions and their implications. You MUST load skill `detect-coverage-gap` to identify absent, thin, and disconnected regions.
