# project-future-reality

## Purpose

Perform project future reality as a bounded experimental transformation.

## Input contract

```yaml
required: [intervention, causal_model]
optional: [provenance, assumptions, uncertainty_register]
constraints: [inputs are typed, units and conditions are explicit, provenance is retained]
```

## Procedure

1. Validate the required fields and normalize units without changing their meaning.
2. Apply the operation specific to project future reality: Propagate directional effects and enumerate new undesirable effects.
3. Emit consequence_projection with each decision tied to evidence, assumptions, or uncertainty.

## Output contract

```yaml
produces: [consequence_projection]
delta_fields: [findings, evidence_updates, uncertainties, decisions]
```

## Quality gates

- Propagate directional effects and enumerate new undesirable effects.
- Preserve nulls, contradictions, and boundary cases instead of smoothing them away.
- Record the stopping condition and unresolved questions when the operation cannot conclude.

## Failure and counterexamples

Mark the artifact unresolved when required fields conflict, provenance is absent, or the result exceeds scope. Retain counterexamples and failed checks.

## Provenance map

- resolved: project-future-reality <- v3 refactory_source.json nodes[].name (normalized lookup)
- concept: experiment-execution/project-future-reality <- architecture semantic consolidation
