---
name: specify-metrics
description: "Define primary/secondary metrics, estimands, directionality, uncertainty reporting, and decision thresholds before analysis."
---

# specify-metrics

## Purpose

Define primary/secondary metrics, estimands, directionality, uncertainty reporting, and decision thresholds before analysis.

## Input contract

```yaml
required: [research_object, operation_parameters]
optional: [evidence, assumptions, constraints]
constraints: [use named scientific objects; retain provenance and missingness; α = 0.05 and power = 0.8 where applicable]
```

## Procedure

1. Name the primary and secondary estimands, measurement units, directionality, and population or comparison they describe.
2. Set uncertainty reporting, missing-data handling, and decision thresholds before observing outcomes.
3. Check metric validity against the claim and return the predeclared reporting and interpretation rules.

## Output contract

```yaml
produces: [operation_result, evidence_trace, uncertainties]
delta_fields: [findings, evidence_updates, uncertainties]
```

## Quality gates

- The specify metrics decision is tied to its declared scientific object and source evidence.
- Missing values, assumptions, and boundary conditions remain visible.
- Statistical criteria stay exact where applicable: α 0.05 and power 0.8.

## Failure and counterexamples

Reject specify metrics when the target schema is incomplete, evidence is incompatible, or a counterexample defeats the stated interpretation.

## Provenance map

- resolved: metric-specification
