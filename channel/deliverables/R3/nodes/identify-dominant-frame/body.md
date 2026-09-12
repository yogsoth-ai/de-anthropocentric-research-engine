# identify-dominant-frame
## Purpose
Identify the framing or governing variable constraining the current problem representation.
## Input contract
```yaml
required: [problem_statement, current_representation]
optional: [stakeholder_views, governing_variables, historical_frames]
constraints: [frame claims must be evidenced by repeated language, choices, or exclusions]
```
## Procedure
1. Extract repeated goals, metaphors, variables, and excluded alternatives.
2. Compare stakeholder or historical formulations for frame convergence.
3. Name the dominant frame and the assumptions it makes salient or invisible.
## Output contract
```yaml
produces: [dominant_frame, frame_evidence, hidden_assumptions, escape_targets]
delta_fields: [findings, assumption_updates, uncertainties, decisions]
```
## Quality gates
- Frame is distinguished from the problem itself and supported by observable representation choices.
## Failure and counterexamples
Do not label a single phrase as a dominant frame without recurrence or consequence.
## Provenance map
- `deep-insight/dominant-idea-identification`: resolved.
- `deep-insight/governing-variable-surfacing`: resolved.
- `creative-ideation/escape-technique`: resolved.
