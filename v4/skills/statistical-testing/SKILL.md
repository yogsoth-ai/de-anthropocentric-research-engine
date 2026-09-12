---
name: statistical-testing
description: "Apply the pre-declared statistical/estimation procedure and report effect size, uncertainty, model checks, and decision-relevant interpretation."
---

# statistical-testing

## Purpose

Apply the pre-declared statistical/estimation procedure and report effect size, uncertainty, model checks, and decision-relevant interpretation.

## Input contract

```yaml
required: [research_object, operation_parameters]
optional: [evidence, assumptions, constraints]
constraints: [use named scientific objects; retain provenance and missingness; α = 0.05 and power = 0.8 where applicable]
```

## Procedure

1. Lock the analysis to the predeclared test or estimator, outcome definition, comparison, and multiplicity rule.
2. Compute effect size and uncertainty, including the α = 0.05 decision rule, model checks, and any ROPE or equivalence criterion.
3. Interpret the result against the estimand and practical threshold without converting a non-significant result into evidence of no effect.

## Output contract

```yaml
produces: [operation_result, evidence_trace, uncertainties]
delta_fields: [findings, evidence_updates, uncertainties]
```

## Quality gates

- The statistical testing decision is tied to its declared scientific object and source evidence.
- Missing values, assumptions, and boundary conditions remain visible.
- Statistical criteria stay exact where applicable: α 0.05 and power 0.8.

## Failure and counterexamples

Reject statistical testing when the target schema is incomplete, evidence is incompatible, or a counterexample defeats the stated interpretation.

## Provenance map

- resolved: statistical-testing
