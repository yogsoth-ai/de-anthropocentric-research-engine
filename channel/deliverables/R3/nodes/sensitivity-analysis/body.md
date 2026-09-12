# sensitivity-analysis
## Purpose
Quantify which parameters, assumptions, interactions, or uncertainties dominate a conclusion.
## Input contract
```yaml
required: [model_or_reasoning_chain, uncertain_parameters, conclusion_metric]
optional: [input_distributions, perturbation_bounds, decision_options, sensitivity_mode]
constraints: [ranges, dependencies, and selected mode must be declared]
```
## Execution protocol
1. Define analysis dimensions (`define-analysis-dimensions`).
2. Run bounded perturbations (`apply-perturbation`).
3. Estimate local/global effects (`assess-sensitivity`).
4. Identify load-bearing factors (`identify-load-bearing-factors`).
5. Decompose interactions (`decompose-global-sensitivity`).
6. Propagate uncertainty (`propagate-uncertainty`).
7. Quantify information value for unresolved drivers (`quantify-information-value`).
Deviation: `local-perturbation`, `Morris`, `Sobol`, `Monte-Carlo`, and decision-value modes select subsets, but mode and omitted analyses must be recorded.
## Output contract
```yaml
produces: [sensitivity_profile, interaction_effects, uncertainty_contributions, information_value_ranking]
delta_fields: [findings, evidence_updates, uncertainties, decisions, recommended_jumps]
```
## Thresholds and quality gates
- B: dominant drivers, interactions, ranges, and uncertainty contributors are separated; local effects are not presented as global effects.
## Failure and counterexamples
Reject rankings based on arbitrary ranges, invalid model runs, or point estimates that hide distributional uncertainty.
## Provenance map
- `sensitivity-analysis`, `parameter-screening`, `variance-decomposition`, `assumption-criticality`, `uncertainty-propagation`, `decision-sensitivity`, `screening-then-decomposition`, `uncertainty-cascade`: resolved where exact names exist; otherwise concept.
## Preserved source criteria ledger
- Preserve perturbation, Morris/Sobol, uncertainty cascade, assumption criticality, and information-value modes.
## Context checkpoint / Delta notes
Append dimensions, perturbation results, driver rankings, uncertainty updates, and next evidence decisions.
