---
name: quantify-information-value
description: "Estimate the value of resolving uncertainty (e.g., EVPI/EVSI or qualitative equivalent) to prioritize which unknowns justify further evidence or experiments."
---

# quantify-information-value
## Purpose
Estimate the value of resolving an uncertainty to prioritize evidence or experiments.
## Input contract
```yaml
required: [decision_problem, uncertain_variables, decision_options]
optional: [probability_model, utility_model, evidence_costs]
constraints: [value estimate must state decision consequences and uncertainty assumptions]
```
## Procedure
1. Define current uncertainty and decision consequences.
2. Estimate value under perfect or sample information, or state a qualitative equivalent.
3. Compare information value with acquisition or experiment cost.
4. Rank unknowns for follow-up.
## Output contract
```yaml
produces: [information_value_estimates, priority_ranking, acquisition_recommendations]
delta_fields: [findings, uncertainties, decisions, recommended_jumps]
```
## Quality gates
- Each estimate links an unknown to a decision and records model/cost assumptions.
## Failure and counterexamples
Do not rank information as valuable when it cannot change a decision or when utility assumptions are unstated.
## Provenance map
- `deep-insight/decision-sensitivity`: resolved.
- `value-of-information`: concept (no exact pool entry).
