# extract-constructive-movement
## Purpose
Convert an absurd or destructive provocation into concrete useful directions.
## Input contract
```yaml
required: [provocation, target_problem]
optional: [current_frame, movement_types]
constraints: [each movement must preserve a useful intent while changing the frame]
```
## Procedure
1. Describe what the provocation makes possible, impossible, or newly visible.
2. Extract moment-to-moment, principle, focus-difference, and positive-aspect movements where applicable.
3. Translate selected movements into testable candidate directions.
## Output contract
```yaml
produces: [movement_set, constructive_directions, translation_notes]
delta_fields: [findings, hypothesis_updates, decisions, recommended_jumps]
```
## Quality gates
- Every direction traces to a provocation and states the constructive change; absurdity alone is not an output.
## Failure and counterexamples
Reject ideas that merely repeat the provocation or cannot state a testable target change.
## Provenance map
- `creative-ideation/movement-operation`: resolved.
- `creative-ideation/movement-extraction`: resolved.
- `creative-ideation/stepping-stone`: resolved.
