# identify-critical-chain

## Purpose

Perform identify critical chain as a bounded experimental transformation.

## Input contract

```yaml
required: [dependency_graph, resource_limits]
optional: [provenance, assumptions, uncertainty_register]
constraints: [inputs are typed, units and conditions are explicit, provenance is retained]
```

## Procedure

1. Validate the required fields and normalize units without changing their meaning.
2. Apply the operation specific to identify critical chain: Select the longest resource-constrained path and identify convergence points.
3. Emit critical_chain with each decision tied to evidence, assumptions, or uncertainty.

## Output contract

```yaml
produces: [critical_chain]
delta_fields: [findings, evidence_updates, uncertainties, decisions]
```

## Quality gates

- Select the longest resource-constrained path and identify convergence points.
- Preserve nulls, contradictions, and boundary cases instead of smoothing them away.
- Record the stopping condition and unresolved questions when the operation cannot conclude.

## Failure and counterexamples

Mark the artifact unresolved when required fields conflict, provenance is absent, or the result exceeds scope. Retain counterexamples and failed checks.

## Provenance map

- resolved: identify-critical-chain <- v3 refactory_source.json nodes[].name (normalized lookup)
- concept: experiment-execution/identify-critical-chain <- architecture semantic consolidation
