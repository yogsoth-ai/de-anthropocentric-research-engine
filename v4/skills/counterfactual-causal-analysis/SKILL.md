---
name: counterfactual-causal-analysis
description: "Intervene on factors, construct counterfactual worlds, test necessity/sufficiency, and identify load-bearing causal factors."
---

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
Do not perform called SOP operations inline; each loaded SOP owns its contract and thresholds.

1. You MUST load skill `extract-causal-structure` to extract the causal structure. You MUST load skill `identify-variables` to type its variables.
2. You MUST load skill `construct-counterfactual` to construct the counterfactual. You MUST load skill `identify-load-bearing-factors` to identify load-bearing factors.
3. You MUST load skill `search-minimal-flip` to search the minimal conclusion flip. You MUST load skill `evaluate-necessity-sufficiency` to test necessity and sufficiency.
   If the conclusion should instead be tested by contradiction and counterexample, consider `reductio-counterexample-analysis` as the next tactic.
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
