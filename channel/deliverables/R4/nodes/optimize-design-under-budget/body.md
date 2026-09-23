# optimize-design-under-budget

## Purpose

Perform optimize design under budget as a bounded experimental transformation.

## Input contract

```yaml
required: [run_costs, resource_budget, validity_constraints]
optional: [provenance, assumptions, uncertainty_register]
constraints: [inputs are typed, units and conditions are explicit, provenance is retained]
```

## Procedure

1. Validate the required fields and normalize units without changing their meaning.
2. Apply the operation specific to optimize design under budget: Maximize information per cost without violating validity constraints.
3. Emit feasible_design with each decision tied to evidence, assumptions, or uncertainty.

## Output contract

```yaml
produces: [feasible_design]
delta_fields: [findings, evidence_updates, uncertainties, decisions]
```

## Quality gates

- Maximize information per cost without violating validity constraints.
- Preserve nulls, contradictions, and boundary cases instead of smoothing them away.
- Record the stopping condition and unresolved questions when the operation cannot conclude.

## Failure and counterexamples

Mark the artifact unresolved when required fields conflict, provenance is absent, or the result exceeds scope. Retain counterexamples and failed checks.

## Provenance map

- resolved: optimize-design-under-budget <- v3 refactory_source.json nodes[].name (normalized lookup)
- concept: experiment-execution/optimize-design-under-budget <- architecture semantic consolidation
