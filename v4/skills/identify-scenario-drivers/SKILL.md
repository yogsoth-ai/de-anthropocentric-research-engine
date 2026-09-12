---
name: identify-scenario-drivers
description: "Identify high-impact/high-uncertainty drivers and rank them for scenario construction."
---

# identify-scenario-drivers

## Purpose

Identify high-impact/high-uncertainty drivers and rank them for scenario construction.

## Input contract

```yaml
required: [research_object, operation_parameters]
optional: [evidence, assumptions, constraints]
constraints: [use named scientific objects; retain provenance and missingness; α = 0.05 and power = 0.8 where applicable]
```

## Procedure

1. Collect candidate drivers from the stated horizon and classify their impact direction, magnitude, and controllability.
2. Score uncertainty independently from impact and rank the drivers by their contribution to scenario divergence.
3. Select the smallest defensible driver set, explain exclusions, and expose dependencies or correlated drivers.

## Output contract

```yaml
produces: [operation_result, evidence_trace, uncertainties]
delta_fields: [findings, evidence_updates, uncertainties]
```

## Quality gates

- The identify scenario drivers decision is tied to its declared scientific object and source evidence.
- Missing values, assumptions, and boundary conditions remain visible.
- Statistical criteria stay exact where applicable: α 0.05 and power 0.8.

## Failure and counterexamples

Reject identify scenario drivers when the target schema is incomplete, evidence is incompatible, or a counterexample defeats the stated interpretation.

## Provenance map

- resolved: scenario-driver-identification
