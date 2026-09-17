---
name: estimate-sample-size
description: "Estimate sample/repetition requirements from detectable effect, uncertainty, power/precision target, and design structure."
---

# estimate-sample-size

## Purpose

Estimate sample/repetition requirements from detectable effect, uncertainty, power/precision target, and design structure.

## Input contract

```yaml
required: [effect_target, uncertainty_model, power_target, design_structure]
optional: [evidence, assumptions, prior_results]
constraints: [use named scientific objects; retain provenance and missingness; $\alpha$ = 0.05 and power = 0.8 where applicable]
```

## Procedure

1. Validate the typed inputs and state the decision this operation must support.
2. Apply the declared operation to the named object; record intermediate values that affect interpretation.
3. Check boundary conditions and counterexamples, then emit the result with uncertainty and source links.

If the precision or power requirement is fixed, consider `select-statistical-method` as the next tactic.

## Output contract

```yaml
produces: [estimate_sample_size_result, evidence_trace, uncertainties]
delta_fields: [evidence_updates, uncertainties]
```

## Quality gates

- Inputs are named scientific objects with compatible schemas.
- Every material result has a derivation or source reference.
- Fixed statistical criteria remain exact where applicable: $\alpha$ 0.05 and power 0.8.

## Failure and counterexamples

Return a failed operation with the violated precondition when inputs are incomplete, assumptions are unsupported, or a counterexample defeats the result.

## Provenance map

- intermediate: experiment-execution/sample-size-estimation
