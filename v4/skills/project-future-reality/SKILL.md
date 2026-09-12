---
name: project-future-reality
description: "Project the downstream consequences of a proposed constraint-breaking intervention and detect new undesirable effects."
---

# project-future-reality

## Purpose

Project the downstream consequences of a proposed constraint-breaking intervention and detect new undesirable effects.

## Input contract

```yaml
required: [research_object, operation_parameters]
optional: [evidence, assumptions, constraints]
constraints: [use named scientific objects; retain provenance and missingness; α = 0.05 and power = 0.8 where applicable]
```

## Procedure

1. Insert the proposed intervention into the supplied causal or constraint model and state the expected immediate effects.
2. Propagate consequences through downstream links, including new undesirable effects, side effects, and displaced bottlenecks.
3. Return the projected tree with evidence status and a verdict on whether the intervention breaks the target constraint.

## Output contract

```yaml
produces: [operation_result, evidence_trace, uncertainties]
delta_fields: [findings, evidence_updates, uncertainties]
```

## Quality gates

- The project future reality decision is tied to its declared scientific object and source evidence.
- Missing values, assumptions, and boundary conditions remain visible.
- Statistical criteria stay exact where applicable: α 0.05 and power 0.8.

## Failure and counterexamples

Reject project future reality when the target schema is incomplete, evidence is incompatible, or a counterexample defeats the stated interpretation.

## Provenance map

- resolved: future-reality-projection
