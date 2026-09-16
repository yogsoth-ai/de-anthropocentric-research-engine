---
name: sensitivity-analysis
description: "Quantify which parameters, assumptions, interactions, or uncertainties dominate the conclusion; select Morris/Sobol/perturbation/Monte-Carlo as modes."
---

# sensitivity-analysis
## Purpose
Quantify which parameters, assumptions, interactions, or uncertainties dominate a conclusion.
## Input contract
```yaml
mode_contracts:
  Morris: &sensitivity_input
    required: [model_or_reasoning_chain, uncertain_parameters, conclusion_metric]
    optional: [input_distributions, perturbation_bounds, decision_options]
    constraints: [ranges_and_dependencies_must_be_declared]
  Sobol: *sensitivity_input
  perturbation: *sensitivity_input
  Monte-Carlo: *sensitivity_input
```
## Execution protocol
Do not perform called SOP operations inline; each loaded SOP owns its contract and thresholds.

1. You MUST load skill `define-analysis-dimensions` to define the analysis dimensions.
2. Apply the selected mode's perturbation, decomposition, or propagation operation.
3. You MUST load skill `assess-sensitivity` to estimate the declared sensitivity effects.
4. You MUST load skill `identify-load-bearing-factors` to identify load-bearing factors.
5. You MUST load skill `quantify-information-value` to quantify information value for unresolved drivers.
   If the dominant sensitivity is caused by an unstable problem frame rather than an input value, consider `problem-reframing` as the next tactic.
Deviation: `local-perturbation`, `Morris`, `Sobol`, `Monte-Carlo`, and decision-value modes select subsets, but mode and omitted analyses must be recorded.

## Mode branches

- `Morris`: screen many uncertain inputs with elementary effects to identify influential factors and interactions before expensive global analysis. You MUST load skill `apply-perturbation` to generate elementary-effect trajectories. You MUST load skill `decompose-global-sensitivity` to separate influential factors and interactions.
- `Sobol`: decompose output variance into first-order and total-order contributions when the model can support global sampling. You MUST load skill `decompose-global-sensitivity` to compute the variance decomposition. You MUST load skill `propagate-uncertainty` to propagate the declared input distributions.
- `perturbation`: vary declared inputs around a baseline to expose local directional sensitivity and threshold crossings. You MUST load skill `apply-perturbation` to execute the bounded variations.
- `Monte-Carlo`: propagate input distributions through repeated draws to quantify outcome uncertainty rather than relying on a point estimate. You MUST load skill `propagate-uncertainty` to run and summarize the repeated draws.

## Output contract
```yaml
mode_contracts:
  Morris: &screening_sensitivity_output
    produces: [sensitivity_profile, interaction_effects]
    delta_fields: [findings, evidence_updates, uncertainties, decisions, recommended_jumps]
  Sobol:
    produces: [sensitivity_profile, interaction_effects, uncertainty_contributions]
    delta_fields: [findings, evidence_updates, uncertainties, decisions, recommended_jumps]
  perturbation: *screening_sensitivity_output
  Monte-Carlo:
    produces: [sensitivity_profile, uncertainty_contributions, information_value_ranking]
    delta_fields: [findings, evidence_updates, uncertainties, decisions, recommended_jumps]
```
## Thresholds and quality gates
- B: dominant drivers, interactions, ranges, and uncertainty contributors are separated; local effects are not presented as global effects.
## Failure and counterexamples
Reject rankings based on arbitrary ranges, invalid model runs, or point estimates that hide distributional uncertainty.
## Provenance map
- `sensitivity-analysis`: intermediate (exact pool names are package-prefixed variants).
- `parameter-screening`, `variance-decomposition`, `assumption-criticality`, `uncertainty-propagation`, `decision-sensitivity`, `screening-then-decomposition`, `uncertainty-cascade`: resolved.
## Preserved source criteria ledger
- Preserve perturbation, Morris/Sobol, uncertainty cascade, assumption criticality, and information-value modes.
## Context checkpoint / Delta notes
Append dimensions, perturbation results, driver rankings, uncertainty updates, and next evidence decisions.
