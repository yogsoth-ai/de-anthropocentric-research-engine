---
name: construct-design-matrix
description: "Construct a balanced/randomized/orthogonal experimental design matrix appropriate to the chosen design mode."
---

# construct-design-matrix

## Purpose

Construct a balanced/randomized/orthogonal experimental design matrix appropriate to the chosen design mode.

## Input contract

```yaml
required: [factor_schema, design_mode, run_budget, randomization_constraints]
optional: [evidence, assumptions, prior_results]
constraints: [use named scientific objects; retain provenance and missingness; α = 0.05 and power = 0.8 where applicable]
```

## Procedure

1. Validate the typed inputs and state the decision this operation must support.
2. Apply the declared operation to the named object; record intermediate values that affect interpretation.
3. Check boundary conditions and counterexamples, then emit the result with uncertainty and source links.

## Output contract

```yaml
produces: [construct_design_matrix_result, evidence_trace, uncertainties]
delta_fields: [evidence_updates, uncertainties]
```

## Quality gates

- Inputs are named scientific objects with compatible schemas.
- Every material result has a derivation or source reference.
- Fixed statistical criteria remain exact where applicable: α 0.05 and power 0.8.

## Failure and counterexamples

Return a failed operation with the violated precondition when inputs are incomplete, assumptions are unsupported, or a counterexample defeats the result.

## Provenance map

- intermediate: experiment-execution/design-matrix-construction
