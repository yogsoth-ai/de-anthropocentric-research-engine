---
name: statistical-testing
description: "Apply the pre-declared statistical/estimation procedure and report effect size, uncertainty, model checks, and decision-relevant interpretation."
---

# statistical-testing

## Purpose

Apply the pre-declared statistical/estimation procedure and report effect size, uncertainty, model checks, and decision-relevant interpretation.

## Input contract

```yaml
required: [predeclared_analysis_plan, observations, comparison_structure]
optional: [evidence, assumptions, prior_results]
constraints: [use named scientific objects; retain provenance and missingness; $\alpha$ = 0.05 and power = 0.8 where applicable]
```

## Procedure

1. Validate the typed inputs and state the decision this operation must support.
2. Apply the declared operation to the named object; record intermediate values that affect interpretation.
3. Check boundary conditions and counterexamples, then emit the result with uncertainty and source links.

If statistical results and analysis artifacts are complete, consider `verify-reproducibility` as the next tactic.

## Output contract

```yaml
produces: [statistical_testing_result, evidence_trace, uncertainties]
delta_fields: [evidence_updates, uncertainties]
```

## Quality gates

- Inputs are named scientific objects with compatible schemas.
- Every material result has a derivation or source reference.
- Fixed statistical criteria remain exact where applicable: $\alpha$ 0.05 and power 0.8.

## Failure and counterexamples

Return a failed operation with the violated precondition when inputs are incomplete, assumptions are unsupported, or a counterexample defeats the result.

## Provenance map

- intermediate: experiment-execution/statistical-testing
