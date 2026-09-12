---
name: select-statistical-method
description: "Select statistical inference/estimation method from design, distribution, sample size, pairing, multiplicity, and decision objective."
---

# select-statistical-method

## Purpose

Select statistical inference/estimation method from design, distribution, sample size, pairing, multiplicity, and decision objective.

## Input contract

```yaml
required: [research_object, operation_parameters]
optional: [evidence, assumptions, constraints]
constraints: [use named scientific objects; retain provenance and missingness; α = 0.05 and power = 0.8 where applicable]
```

## Procedure

1. Read the predeclared design, outcome scale, pairing, sample size, multiplicity plan, and decision objective.
2. Compare eligible inferential or estimation procedures against distributional and dependence assumptions; preserve α = 0.05.
3. Choose the method, state diagnostics and fallback boundaries, and explain why alternatives do not fit the design.

## Output contract

```yaml
produces: [operation_result, evidence_trace, uncertainties]
delta_fields: [findings, evidence_updates, uncertainties]
```

## Quality gates

- The select statistical method decision is tied to its declared scientific object and source evidence.
- Missing values, assumptions, and boundary conditions remain visible.
- Statistical criteria stay exact where applicable: α 0.05 and power 0.8.

## Failure and counterexamples

Reject select statistical method when the target schema is incomplete, evidence is incompatible, or a counterexample defeats the stated interpretation.

## Provenance map

- resolved: statistical-method-selection
