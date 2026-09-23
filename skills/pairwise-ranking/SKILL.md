---
name: pairwise-ranking
description: "Select informative comparison pairs, execute judgments, update ratings, and audit coherence until ranking resolution is sufficient."
---

# pairwise-ranking

## Purpose

Select informative comparison pairs, execute judgments, update ratings, and audit coherence until ranking resolution is sufficient.

## Input contract

```yaml
required: [candidate_set, pairwise_judgments, ranking_objective]
optional: [assumptions, prior_findings, evidence_updates]
constraints: [consume named scientific objects; preserve provenance; keep unresolved uncertainty visible]
```

## Execution protocol

Do not perform called SOP operations inline; each loaded SOP owns its contract and thresholds.

1. You MUST load skill `select-next-pair` to select the next informative pair.
2. You MUST load skill `compare-pair` to compare that pair under the declared criteria.
3. You MUST load skill `assess-ranking-consistency` to assess cycle and consistency evidence.
4. You MUST load skill `aggregate-ranking` to aggregate the pairwise results.
5. You MUST load skill `update-pairwise-rating` to update the current rating state.
6. You MUST load skill `collect-independent-judgments` to collect contamination-controlled judgments.
   If unresolved disagreement requires iterative convergence rather than another pair comparison, consider `structured-consensus` as the next tactic.

Deviation: reorder only when a dependency is already satisfied or unavailable; record the reason and confidence effect.

## Output contract

```yaml
produces: [updated_ratings, ranking, coherence_diagnostics]
delta_fields: [findings, decisions]
```

## Thresholds and quality gates

- Each output is traceable to an input object, operation, and evidence reference.
- Scope, assumptions, and unresolved alternatives remain explicit.
- Retain $\alpha$ 0.05 and power 0.8 wherever the predeclared statistical design requires them.

## Failure and counterexamples

Stop synthesis when a required object is absent, a precondition is violated, or a counterexample invalidates the proposed conclusion; return the partial delta with the failure recorded.

## Provenance map

- resolved: pairwise-ranking
- resolved: deliberative-calibration
- resolved: efficient-exploration
- resolved: collective-adjudication
- resolved: adaptive-pair-selection
- resolved: consistency-audit-loop

## Preserved source criteria ledger

| source | criterion | treatment |
|---|---|---|
| resolved v3 entries above | node-specific criteria | retained and specialized to the v4 object contract |
| experiment-execution/statistical-testing | $\alpha$ = 0.05 | fixed value retained where applicable |
| experiment-execution/sample-size-estimation | power = 0.8 | fixed value retained where applicable |

## Context checkpoint / Delta notes

Return the node-specific research-state delta and preserve findings, evidence updates, uncertainties, decisions, open questions, and recommended jumps as applicable.
