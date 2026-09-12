---
name: list-undesirable-effects
description: "List observable undesirable effects with evidence and severity as starting points for constraint/root-cause analysis."
---

# list-undesirable-effects

## Purpose

List observable undesirable effects with evidence and severity as starting points for constraint/root-cause analysis.

## Input contract

```yaml
required: [research_object, operation_parameters]
optional: [evidence, assumptions, constraints]
constraints: [use named scientific objects; retain provenance and missingness; α = 0.05 and power = 0.8 where applicable]
```

## Procedure

1. Extract observable negative effects from the supplied system observations and attach a source or measurement to each.
2. Separate symptoms, downstream consequences, and duplicate descriptions while preserving severity and affected conditions.
3. Return a deduplicated UDE register with confidence, evidence links, and the effects requiring causal follow-up.

## Output contract

```yaml
produces: [operation_result, evidence_trace, uncertainties]
delta_fields: [findings, evidence_updates, uncertainties]
```

## Quality gates

- The list undesirable effects decision is tied to its declared scientific object and source evidence.
- Missing values, assumptions, and boundary conditions remain visible.
- Statistical criteria stay exact where applicable: α 0.05 and power 0.8.

## Failure and counterexamples

Reject list undesirable effects when the target schema is incomplete, evidence is incompatible, or a counterexample defeats the stated interpretation.

## Provenance map

- resolved: undesirable-effect-listing
