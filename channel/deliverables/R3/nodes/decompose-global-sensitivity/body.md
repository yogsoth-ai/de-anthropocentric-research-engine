# decompose-global-sensitivity
## Purpose
Estimate global main effects and interactions across uncertain inputs using screening and decomposition.
## Input contract
```yaml
required: [model, uncertain_inputs, output_metric]
optional: [input_distributions, screening_method, decomposition_method]
constraints: [input distributions and sampling design must be declared]
```
## Procedure
1. Define input ranges/distributions and the output metric.
2. Screen influential variables with Morris or an equivalent declared method.
3. Estimate main and interaction effects with Sobol or an equivalent variance decomposition.
4. Compare sensitivity rankings across sampling assumptions.
## Output contract
```yaml
produces: [screening_report, main_effects, interaction_effects, sensitivity_ranking]
delta_fields: [findings, evidence_updates, uncertainties, decisions]
```
## Quality gates
- Main and interaction effects use a declared sampling design; rankings include uncertainty and do not conflate screening with decomposition.
## Failure and counterexamples
Do not report global sensitivity when ranges are arbitrary, model evaluations are invalid, or interactions were omitted without notice.
## Provenance map
- `deep-insight/variance-decomposition`: resolved.
- `screening-then-decomposition`: resolved.
- `morris-screening`: resolved.
- `sobol-decomposition`: resolved.
