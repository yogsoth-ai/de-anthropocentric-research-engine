# enumerate-combinations
## Purpose
Construct combinations across declared dimensions and values without prematurely judging them.
## Input contract
```yaml
required: [dimensions, value_sets, combination_policy]
optional: [exclusion_constraints, sampling_limit, random_seed]
constraints: [every emitted combination records its source values]
```
## Procedure
1. Validate dimensions, values, and exclusions.
2. Generate the Cartesian, constrained, or sampled combinations requested.
3. Preserve provenance of each component and mark omitted combinations.
4. Return the neutral combination set for downstream evaluation.
## Output contract
```yaml
produces: [combination_set, component_provenance, exclusions, omitted_space]
delta_fields: [findings, open_questions]
```
## Quality gates
- No combination is scored or filtered unless policy explicitly requests it.
- Exclusions are recorded with reasons.
- Sampled enumeration reports sampling rule and coverage limits.
## Parameterization
Caller supplies dimension schema, value sets, combination mode, exclusions, and sampling policy.
## Failure and counterexamples
Reject combinations with missing components, hidden exclusions, or premature quality judgments.
## Provenance map
- concept: creative-ideation/matrix-construction
- concept: creative-ideation/recombination-generation
- concept: creative-ideation/combination-generation
