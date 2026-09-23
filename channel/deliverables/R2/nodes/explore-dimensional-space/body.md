# explore-dimensional-space
## Purpose
Represent a problem space as validated dimensions and values, enumerate compatible combinations, map occupancy, detect gaps, and synthesize candidate questions or ideas.
## Input contract
```yaml
required: [target_space, dimensions, values]
optional: [coverage_matrix, compatibility_rules, objective]
constraints: [dimension semantics and independence posture must be declared]
```
## Execution protocol
1. Define dimensions and enumerate meaningful values (`define-analysis-dimensions`, `enumerate-dimension-values`).
2. Enumerate combinations and prune incompatibilities (`enumerate-combinations`, `evaluate-compatibility`).
3. Validate axis independence and inspect gaps (`validate-axis-independence`, `detect-coverage-gap`).
4. Score regions and derive questions (`score-object`, `generate-subquestions`).
Deviation: skip scoring when the task is descriptive mapping; skip subquestions when no research question is in scope.
## Output contract
```yaml
produces: [dimension_schema, value_catalog, combination_map, compatibility_report, coverage_gaps, prioritized_regions, subquestions]
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
- `morphological-generation`: emphasize unconstrained combination generation before pruning.
- `research-space-mapping`: emphasize typed dimensions, occupancy, and coverage.
- `gap-mapping`: emphasize absent/thin/disconnected regions and their implications.
