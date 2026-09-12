---
name: select-experimental-baseline
description: "Select fair SOTA/simple/oracle/control baselines with provenance and rationale matched to the experimental claim."
---

# select-experimental-baseline

## Purpose

Select fair SOTA/simple/oracle/control baselines with provenance and rationale matched to the experimental claim.

## Input contract

```yaml
required: [research_object, operation_parameters]
optional: [evidence, assumptions, constraints]
constraints: [use named scientific objects; retain provenance and missingness; α = 0.05 and power = 0.8 where applicable]
```

## Procedure

1. Translate the experimental claim into the capabilities a fair baseline must share and the controls it must not receive.
2. Inventory SOTA, simple, oracle, and control candidates with protocol, data, compute, and provenance comparability.
3. Select the minimal baseline set that tests the claim and record exclusions, fairness risks, and rationale.

## Output contract

```yaml
produces: [operation_result, evidence_trace, uncertainties]
delta_fields: [findings, evidence_updates, uncertainties]
```

## Quality gates

- The select experimental baseline decision is tied to its declared scientific object and source evidence.
- Missing values, assumptions, and boundary conditions remain visible.
- Statistical criteria stay exact where applicable: α 0.05 and power 0.8.

## Failure and counterexamples

Reject select experimental baseline when the target schema is incomplete, evidence is incompatible, or a counterexample defeats the stated interpretation.

## Provenance map

- resolved: baseline-selection
