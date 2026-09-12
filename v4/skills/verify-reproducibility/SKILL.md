---
name: verify-reproducibility
description: "Assess reproducibility across reruns/replications using the predeclared reproducibility target and suitable agreement/variance metrics."
---

# verify-reproducibility

## Purpose

Assess reproducibility across reruns/replications using the predeclared reproducibility target and suitable agreement/variance metrics.

## Input contract

```yaml
required: [research_object, operation_parameters]
optional: [evidence, assumptions, constraints]
constraints: [use named scientific objects; retain provenance and missingness; α = 0.05 and power = 0.8 where applicable]
```

## Procedure

1. Align rerun and replication outputs to the declared reproducibility target and verify that environments and inputs are comparable.
2. Compute suitable agreement, variance, or calibration metrics and report their uncertainty rather than a binary match alone.
3. Judge the target-specific verdict, diagnose divergence sources, and state whether another run or a revised target is required.

## Output contract

```yaml
produces: [operation_result, evidence_trace, uncertainties]
delta_fields: [findings, evidence_updates, uncertainties]
```

## Quality gates

- The verify reproducibility decision is tied to its declared scientific object and source evidence.
- Missing values, assumptions, and boundary conditions remain visible.
- Statistical criteria stay exact where applicable: α 0.05 and power 0.8.

## Failure and counterexamples

Reject verify reproducibility when the target schema is incomplete, evidence is incompatible, or a counterexample defeats the stated interpretation.

## Provenance map

- resolved: reproducibility-verification
