---
name: select-statistical-method
description: "Select statistical inference/estimation method from design, distribution, sample size, pairing, multiplicity, and decision objective."
---

# select-statistical-method

## Purpose

Select statistical inference/estimation method from design, distribution, sample size, pairing, multiplicity, and decision objective.

## Input contract

```yaml
required: [design_structure, outcome_type, sample_size, decision_objective]
optional: [evidence, assumptions, prior_results]
constraints: [use named scientific objects; retain provenance and missingness; α = 0.05 and power = 0.8 where applicable]
```

## Procedure

1. Validate the typed inputs and state the decision this operation must support.
2. Apply the declared operation to the named object; record intermediate values that affect interpretation.
3. Check boundary conditions and counterexamples, then emit the result with uncertainty and source links.

## Output contract

```yaml
produces: [select_statistical_method_result, evidence_trace, uncertainties]
delta_fields: [evidence_updates, uncertainties]
```

## Quality gates

- Inputs are named scientific objects with compatible schemas.
- Every material result has a derivation or source reference.
- Fixed statistical criteria remain exact where applicable: α 0.05 and power 0.8.

## Failure and counterexamples

Return a failed operation with the violated precondition when inputs are incomplete, assumptions are unsupported, or a counterexample defeats the result.

## Provenance map

- intermediate: experiment-execution/statistical-method-selection [tactic]
