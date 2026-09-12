---
name: estimate-sample-size
description: "Estimate sample/repetition requirements from detectable effect, uncertainty, power/precision target, and design structure."
---

# estimate-sample-size

## Purpose

Estimate sample/repetition requirements from detectable effect, uncertainty, power/precision target, and design structure.

## Input contract

```yaml
required: [research_object, operation_parameters]
optional: [evidence, assumptions, constraints]
constraints: [use named scientific objects; retain provenance and missingness; α = 0.05 and power = 0.8 where applicable]
```

## Procedure

1. State the estimand, detectable effect, variance or prior uncertainty, design structure, and whether the target is power or precision.
2. Calculate the required observations or repetitions under power = 0.8, recording α = 0.05 and the formula or simulation used.
3. Vary the uncertain inputs, report sensitivity and attrition allowance, and reject a plan whose feasible budget cannot meet the target.

## Output contract

```yaml
produces: [operation_result, evidence_trace, uncertainties]
delta_fields: [findings, evidence_updates, uncertainties]
```

## Quality gates

- The estimate sample size decision is tied to its declared scientific object and source evidence.
- Missing values, assumptions, and boundary conditions remain visible.
- Statistical criteria stay exact where applicable: α 0.05 and power 0.8.

## Failure and counterexamples

Reject estimate sample size when the target schema is incomplete, evidence is incompatible, or a counterexample defeats the stated interpretation.

## Provenance map

- resolved: sample-size-estimation
