# propagate-uncertainty
## Purpose
Propagate input uncertainty through a model or reasoning chain to estimate output distributions, tails, and contributions.
## Input contract
```yaml
required: [model, uncertain_inputs, output_variables]
optional: [sampling_plan, dependency_structure, tail_metrics]
constraints: [input distributions, dependencies, and sampling method must be declared]
```
## Procedure
1. Represent each uncertain input with its distribution and dependencies.
2. Sample or propagate the inputs through the model.
3. Summarize output distributions, tail behavior, and dominant uncertainty contributors.
## Output contract
```yaml
produces: [output_distributions, tail_summary, uncertainty_contributions]
delta_fields: [findings, evidence_updates, uncertainties]
```
## Quality gates
- Output uncertainty is traceable to input distributions and sampling assumptions; tails are not replaced by point estimates.
## Failure and counterexamples
Do not claim propagated uncertainty when dependencies or model validity are unknown.
## Provenance map
- `deep-insight/uncertainty-cascade`: resolved.
- `monte-carlo-propagation`: concept (no exact pool entry).
