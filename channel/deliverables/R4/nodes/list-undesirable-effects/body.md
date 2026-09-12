# list-undesirable-effects

## Purpose

Perform list undesirable effects as a bounded experimental transformation.

## Input contract

```yaml
required: [observations, severity_scale]
optional: [provenance, assumptions, uncertainty_register]
constraints: [inputs are typed, units and conditions are explicit, provenance is retained]
```

## Procedure

1. Validate the required fields and normalize units without changing their meaning.
2. Apply the operation specific to list undesirable effects: Each effect is observable, sourced, and severity-rated.
3. Emit effect_register with each decision tied to evidence, assumptions, or uncertainty.

## Output contract

```yaml
produces: [effect_register]
delta_fields: [findings, evidence_updates, uncertainties, decisions]
```

## Quality gates

- Each effect is observable, sourced, and severity-rated.
- Preserve nulls, contradictions, and boundary cases instead of smoothing them away.
- Record the stopping condition and unresolved questions when the operation cannot conclude.

## Failure and counterexamples

Mark the artifact unresolved when required fields conflict, provenance is absent, or the result exceeds scope. Retain counterexamples and failed checks.

## Provenance map

- resolved: list-undesirable-effects <- v3 refactory_source.json nodes[].name (normalized lookup)
- concept: experiment-execution/list-undesirable-effects <- architecture semantic consolidation
