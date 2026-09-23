# identify-scenario-drivers

## Purpose

Perform identify scenario drivers as a bounded experimental transformation.

## Input contract

```yaml
required: [driver_candidates, impact_scores, uncertainty_scores]
optional: [provenance, assumptions, uncertainty_register]
constraints: [inputs are typed, units and conditions are explicit, provenance is retained]
```

## Procedure

1. Validate the required fields and normalize units without changing their meaning.
2. Apply the operation specific to identify scenario drivers: Rank by declared impact and uncertainty dimensions.
3. Emit ranked_drivers with each decision tied to evidence, assumptions, or uncertainty.

## Output contract

```yaml
produces: [ranked_drivers]
delta_fields: [findings, evidence_updates, uncertainties, decisions]
```

## Quality gates

- Rank by declared impact and uncertainty dimensions.
- Preserve nulls, contradictions, and boundary cases instead of smoothing them away.
- Record the stopping condition and unresolved questions when the operation cannot conclude.

## Failure and counterexamples

Mark the artifact unresolved when required fields conflict, provenance is absent, or the result exceeds scope. Retain counterexamples and failed checks.

## Provenance map

- resolved: identify-scenario-drivers <- v3 refactory_source.json nodes[].name (normalized lookup)
- concept: experiment-execution/identify-scenario-drivers <- architecture semantic consolidation
