# predict-competitive-move

## Purpose

Perform predict competitive move as a bounded experimental transformation.

## Input contract

```yaml
required: [competitor_signals, temporal_context]
optional: [provenance, assumptions, uncertainty_register]
constraints: [inputs are typed, units and conditions are explicit, provenance is retained]
```

## Procedure

1. Validate the required fields and normalize units without changing their meaning.
2. Apply the operation specific to predict competitive move: Separate evidence-backed signals from assumptions and timing uncertainty.
3. Emit move_forecast with each decision tied to evidence, assumptions, or uncertainty.

## Output contract

```yaml
produces: [move_forecast]
delta_fields: [findings, evidence_updates, uncertainties, decisions]
```

## Quality gates

- Separate evidence-backed signals from assumptions and timing uncertainty.
- Preserve nulls, contradictions, and boundary cases instead of smoothing them away.
- Record the stopping condition and unresolved questions when the operation cannot conclude.

## Failure and counterexamples

Mark the artifact unresolved when required fields conflict, provenance is absent, or the result exceeds scope. Retain counterexamples and failed checks.

## Provenance map

- resolved: predict-competitive-move <- v3 refactory_source.json nodes[].name (normalized lookup)
- concept: experiment-execution/predict-competitive-move <- architecture semantic consolidation
