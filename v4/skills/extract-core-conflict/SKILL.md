---
name: extract-core-conflict
description: "Represent a core constraint conflict in an Evaporating-Cloud-like structure with explicit assumptions on every dependency."
---

# extract-core-conflict

## Purpose

Represent a core constraint conflict in an Evaporating-Cloud-like structure with explicit assumptions on every dependency.

## Input contract

```yaml
required: [research_object, operation_parameters]
optional: [evidence, assumptions, constraints]
constraints: [use named scientific objects; retain provenance and missingness; α = 0.05 and power = 0.8 where applicable]
```

## Procedure

1. List the observed undesirable effects and the two desired conditions that cannot be satisfied simultaneously.
2. Trace each condition through its prerequisite assumptions and mark which links are empirical, inferred, or disputed.
3. Return the typed conflict structure with candidate leverage points and the evidence needed to dissolve each assumption.

## Output contract

```yaml
produces: [operation_result, evidence_trace, uncertainties]
delta_fields: [findings, evidence_updates, uncertainties]
```

## Quality gates

- The extract core conflict decision is tied to its declared scientific object and source evidence.
- Missing values, assumptions, and boundary conditions remain visible.
- Statistical criteria stay exact where applicable: α 0.05 and power 0.8.

## Failure and counterexamples

Reject extract core conflict when the target schema is incomplete, evidence is incompatible, or a counterexample defeats the stated interpretation.

## Provenance map

- resolved: core-conflict-extraction
