---
name: evaluate-falsifiability
description: "Determine what observation would falsify a hypothesis and flag unfalsifiable formulations."
---

# evaluate-falsifiability

## Purpose

Evaluate whether a claim or hypothesis exposes observations that could count against it.

## Input contract

```yaml
required: [claim, prediction_set, observation_domain]
optional: [auxiliary_assumptions, measurement_limits]
constraints: [falsifying conditions must be observable within the declared domain]
```

## Procedure

1. Translate the claim into testable predictions and boundary conditions.
2. Identify observations that would contradict the claim under its assumptions.
3. Check whether those observations are measurable and independent of the claim's definition.
4. Classify falsifiability and list needed operationalization.

## Output contract

```yaml
produces: [falsifiability_assessment, falsifying_observations, operationalization_gaps, assumption_dependencies]
delta_fields: [findings, hypothesis_updates, uncertainties, open_questions]
```

## Quality gates

- At least one non-vacuous potential counter-observation is explicit for a falsifiable claim.
- Auxiliary assumptions are separated from the core claim.

## Failure and counterexamples

Do not call a claim falsifiable merely because it can be criticized rhetorically.

## Provenance map

- `resolved: evaluate-falsifiability`

