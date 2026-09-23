# counterfactual-causal-analysis
## Purpose
Intervene on factors, construct counterfactual worlds, test necessity and sufficiency, and identify load-bearing causal factors.
## Input contract
```yaml
required: [causal_claim, variables, intervention_target]
optional: [mechanism_graph, baseline_world, comparison_conditions]
constraints: [intervention and outcome must be measurable or explicitly qualitative]
```
## Execution protocol
1. Extract causal structure and variables (`extract-causal-structure`, `identify-variables`).
2. Construct the counterfactual and identify load-bearing factors (`construct-counterfactual`, `identify-load-bearing-factors`).
3. Search the minimal conclusion flip and test necessity/sufficiency (`search-minimal-flip`, `evaluate-necessity-sufficiency`).
Deviation: use qualitative counterfactuals when intervention data are unavailable, but mark the inference uncertainty.
## Output contract
```yaml
produces: [causal_structure, counterfactual_map, load_bearing_factors, minimal_flip, necessity_sufficiency_report]
delta_fields: [findings, evidence_updates, hypothesis_updates, uncertainties, decisions]
```
## Thresholds and quality gates
- Every intervention must state changed variables, held-fixed conditions, predicted outcome, and evidence basis.
- Necessity and sufficiency are separate judgments; do not collapse them.
## Failure and counterexamples
Do not call a factor necessary when an untested substitute can produce the outcome. Mark counterfactuals underdetermined when held-fixed conditions are unspecified.
## Provenance map
- resolved: counterfactual-probing
- resolved: structural-counterfactual
- resolved: necessity-sufficiency
- resolved: systematic-factor-ablation
- resolved: causal-necessity-testing
- resolved: minimal-change-search
## Preserved source criteria ledger
| source | source line | kind | source criterion |
|---|---:|---|---|
| v4 architecture | node desc | textual | Intervene, construct counterfactual worlds, test necessity/sufficiency, identify load-bearing factors. |
## Context checkpoint / Delta notes
Append intervention worlds, held-fixed conditions, factor ranking, flip search, and necessity/sufficiency results.
