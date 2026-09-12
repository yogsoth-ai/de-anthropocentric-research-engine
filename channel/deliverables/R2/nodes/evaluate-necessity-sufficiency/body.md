# evaluate-necessity-sufficiency
## Purpose
Test whether a proposed cause or mechanism is necessary and/or sufficient under controlled counterfactual or intervention comparisons.
## Input contract
```yaml
required: [cause_or_mechanism, outcome, comparison_conditions]
optional: [counterfactual_worlds, intervention_data]
constraints: [necessary and sufficient tests must be reported separately]
```
## Procedure
1. Define removal/absence and presence/intervention contrasts.
2. Compare outcomes under held-fixed conditions.
3. Report necessity, sufficiency, confounds, and uncertainty.
## Output contract
```yaml
produces: [necessity_result, sufficiency_result, comparison_table, confounds]
delta_fields: [findings, evidence_updates, uncertainties, decisions]
```
## Quality gates
- A necessity claim needs an absence/removal comparison; sufficiency needs a presence/intervention comparison.
## Failure and counterexamples
Do not infer necessity from correlation or sufficiency from one positive case.
## Provenance map
- resolved: causal-necessity-testing
