---
name: identify-inventive-contradiction
description: "Identify paired parameters or requirements where improving one worsens another, and distinguish technical from physical contradictions."
---

# identify-inventive-contradiction
## Purpose
Identify paired requirements where improving one worsens another, distinguishing technical from physical contradictions.
## Input contract
```yaml
required: [system_requirements, improvement_target, worsening_effect]
optional: [parameter_set, operating_conditions]
constraints: [both sides must refer to the same design decision or parameter]
```
## Procedure
1. State the desired improvement and the resulting worsening effect.
2. Determine whether distinct system states or one parameter must satisfy opposing properties.
3. Classify technical versus physical contradiction and record the implicated parameters.
## Output contract
```yaml
produces: [contradiction_statement, contradiction_type, implicated_parameters]
delta_fields: [findings, hypothesis_updates, uncertainties, decisions]
```
## Quality gates
- Improvement and worsening are measurable or operationalized; contradiction type is justified.
## Failure and counterexamples
Reject trade-offs that are merely competing objectives without a causal worsening relation.
## Provenance map
- `triz/contradiction-identification`: resolved.
