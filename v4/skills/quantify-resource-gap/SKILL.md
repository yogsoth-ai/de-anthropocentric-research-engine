---
name: quantify-resource-gap
description: "Quantify resource demand, available supply, gap, severity, and uncertainty for a research/experiment plan."
---

# quantify-resource-gap

## Purpose

Quantify resource demand, available supply, gap, severity, and uncertainty for a research/experiment plan.

## Input contract

```yaml
required: [research_object, operation_parameters]
optional: [evidence, assumptions, constraints]
constraints: [use named scientific objects; retain provenance and missingness; α = 0.05 and power = 0.8 where applicable]
```

## Procedure

1. Define the plan scope and units, then estimate demand for people, compute, data, time, and materials.
2. Record available supply, committed allocations, and uncertainty bounds before subtracting supply from demand.
3. Classify gap severity, identify the binding resource, and show which assumption or mitigation would change the result.

## Output contract

```yaml
produces: [operation_result, evidence_trace, uncertainties]
delta_fields: [findings, evidence_updates, uncertainties]
```

## Quality gates

- The quantify resource gap decision is tied to its declared scientific object and source evidence.
- Missing values, assumptions, and boundary conditions remain visible.
- Statistical criteria stay exact where applicable: α 0.05 and power 0.8.

## Failure and counterexamples

Reject quantify resource gap when the target schema is incomplete, evidence is incompatible, or a counterexample defeats the stated interpretation.

## Provenance map

- resolved: resource-quantification
