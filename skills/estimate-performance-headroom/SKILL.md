---
name: estimate-performance-headroom
description: "Estimate practical/human/theoretical ceilings and remaining performance headroom under stated assumptions."
---

# estimate-performance-headroom

## Purpose

Estimate practical, human, or theoretical ceilings and remaining performance headroom under stated assumptions.

## Input contract

```yaml
required: [current_performance, ceiling_reference, metric_schema]
optional: [human_baseline, oracle_bound, task_constraints, uncertainty_model]
constraints: [each ceiling must name its population, conditions, and assumptions]
```

## Procedure

1. Define the relevant ceiling and align its metric and conditions with current performance.
2. Estimate the gap and uncertainty to each applicable ceiling.
3. Separate attainable, theoretical, and assumption-dependent headroom.
4. Identify evidence needed to reduce the dominant uncertainty.

## Output contract

```yaml
produces: [ceiling_estimates, headroom_estimates, assumption_register, uncertainty_priorities]
delta_fields: [findings, evidence_updates, uncertainties, recommended_jumps]
```

## Quality gates

- Ceiling and current score are comparable.
- Headroom is not reported as an absolute fact when assumptions dominate.

## Failure and counterexamples

Do not use an upper-bound theorem as a practical ceiling or equate benchmark maximum with human or task optimum.

## Provenance map

- `resolved: headroom-estimation`
