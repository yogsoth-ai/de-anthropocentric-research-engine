# generate-provocation
## Purpose
Generate a deliberate pattern-breaking perturbation that opens alternative reasoning paths.
## Input contract
```yaml
required: [target_pattern, provocation_mode, boundary_conditions]
optional: [random_stimulus_pool, intensity, safety_constraints]
constraints: [provocation must be traceable to the target pattern]
```
## Procedure
1. Describe the dominant pattern and its protected assumptions.
2. Apply the selected mode: PO, reversal, negation, random stimulus, exaggeration, or distortion.
3. Record the altered elements and generated questions.
4. Return candidate directions without premature selection.
## Output contract
```yaml
produces: [provocations, altered_assumptions, generated_questions, candidate_directions]
delta_fields: [findings, hypothesis_updates, open_questions]
```
## Quality gates
- Mode and intensity are recorded for each provocation.
- At least one altered assumption and one testable question accompany every item.
- Provocations remain within declared safety and scope boundaries.
## Parameterization
Caller supplies target schema, provocation modes, intensity scale, stimulus pool, and boundary constraints.
## Failure and counterexamples
Reject random outputs with no relation to the target or ideas presented as validated conclusions.
## Provenance map
- concept: creative-ideation/po-provocation
- concept: deep-insight/provocation-generation
- concept: creative-ideation/random-word-stimulus
