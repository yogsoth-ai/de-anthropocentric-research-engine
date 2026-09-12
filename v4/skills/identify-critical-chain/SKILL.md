---
name: identify-critical-chain
description: "Identify the longest/limiting dependency path while accounting for resource contention and convergence points."
---

# identify-critical-chain

## Purpose

Identify the longest/limiting dependency path while accounting for resource contention and convergence points.

## Input contract

```yaml
required: [research_object, operation_parameters]
optional: [evidence, assumptions, constraints]
constraints: [use named scientific objects; retain provenance and missingness; α = 0.05 and power = 0.8 where applicable]
```

## Procedure

1. Normalize the dependency graph into tasks, durations, resources, and convergence points before calculating paths.
2. Find the longest resource-feasible dependency path and distinguish true criticality from a merely long branch.
3. Stress the path against contention and delay, then report bottlenecks, slack, and the evidence behind each risk.

## Output contract

```yaml
produces: [operation_result, evidence_trace, uncertainties]
delta_fields: [findings, evidence_updates, uncertainties]
```

## Quality gates

- The identify critical chain decision is tied to its declared scientific object and source evidence.
- Missing values, assumptions, and boundary conditions remain visible.
- Statistical criteria stay exact where applicable: α 0.05 and power 0.8.

## Failure and counterexamples

Reject identify critical chain when the target schema is incomplete, evidence is incompatible, or a counterexample defeats the stated interpretation.

## Provenance map

- resolved: critical-chain-identification
