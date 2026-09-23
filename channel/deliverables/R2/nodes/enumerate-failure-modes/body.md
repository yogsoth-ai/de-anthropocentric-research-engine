# enumerate-failure-modes
## Purpose
Convert functions, process steps, or scenarios into explicit failure modes.
## Input contract
```yaml
required: [functions_or_steps, intended_outcomes, operating_conditions]
optional: [failure_history, stakeholders]
constraints: [failure mode must state deviation from intended outcome]
```
## Procedure
1. Decompose functions or steps.
2. Enumerate plausible deviations and affected outcomes.
3. Record causes, effects, detectability, and evidence gaps.
## Output contract
```yaml
produces: [failure_mode_register, cause_candidates, effect_candidates, detection_notes]
delta_fields: [findings, evidence_updates, uncertainties, open_questions]
```
## Quality gates
- Each mode has a function/step, deviation, effect, and provenance.
## Failure and counterexamples
Do not list generic risks without a specific function or operating condition.
## Provenance map
- resolved: failure-mode-extraction
