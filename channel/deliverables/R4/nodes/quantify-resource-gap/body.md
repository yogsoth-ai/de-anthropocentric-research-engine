# quantify-resource-gap

## Purpose

Perform quantify resource gap as a bounded experimental transformation.

## Input contract

```yaml
required: [resource_demand, resource_supply]
optional: [provenance, assumptions, uncertainty_register]
constraints: [inputs are typed, units and conditions are explicit, provenance is retained]
```

## Procedure

1. Validate the required fields and normalize units without changing their meaning.
2. Apply the operation specific to quantify resource gap: Report demand, supply, gap severity, and uncertainty on a common unit basis.
3. Emit gap_estimate with each decision tied to evidence, assumptions, or uncertainty.

## Output contract

```yaml
produces: [gap_estimate]
delta_fields: [findings, evidence_updates, uncertainties, decisions]
```

## Quality gates

- Report demand, supply, gap severity, and uncertainty on a common unit basis.
- Preserve nulls, contradictions, and boundary cases instead of smoothing them away.
- Record the stopping condition and unresolved questions when the operation cannot conclude.

## Failure and counterexamples

Mark the artifact unresolved when required fields conflict, provenance is absent, or the result exceeds scope. Retain counterexamples and failed checks.

## Provenance map

- resolved: quantify-resource-gap <- v3 refactory_source.json nodes[].name (normalized lookup)
- concept: experiment-execution/quantify-resource-gap <- architecture semantic consolidation
