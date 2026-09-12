# extract-core-conflict

## Purpose

Perform extract core conflict as a bounded experimental transformation.

## Input contract

```yaml
required: [undesirable_effects, constraint_relations]
optional: [provenance, assumptions, uncertainty_register]
constraints: [inputs are typed, units and conditions are explicit, provenance is retained]
```

## Procedure

1. Validate the required fields and normalize units without changing their meaning.
2. Apply the operation specific to extract core conflict: Every dependency carries an explicit assumption and polarity.
3. Emit conflict_graph with each decision tied to evidence, assumptions, or uncertainty.

## Output contract

```yaml
produces: [conflict_graph]
delta_fields: [findings, evidence_updates, uncertainties, decisions]
```

## Quality gates

- Every dependency carries an explicit assumption and polarity.
- Preserve nulls, contradictions, and boundary cases instead of smoothing them away.
- Record the stopping condition and unresolved questions when the operation cannot conclude.

## Failure and counterexamples

Mark the artifact unresolved when required fields conflict, provenance is absent, or the result exceeds scope. Retain counterexamples and failed checks.

## Provenance map

- resolved: extract-core-conflict <- v3 refactory_source.json nodes[].name (normalized lookup)
- concept: experiment-execution/extract-core-conflict <- architecture semantic consolidation
