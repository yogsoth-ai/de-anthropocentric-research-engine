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

1. Use `select-next-pair` on its named scientific object and record the evidence or decision it contributes.
2. Use `compare-pair` on its named scientific object and record the evidence or decision it contributes.
3. Use `assess-ranking-consistency` on its named scientific object and record the evidence or decision it contributes.
4. Use `aggregate-ranking` on its named scientific object and record the evidence or decision it contributes.
5. Use `update-pairwise-rating` on its named scientific object and record the evidence or decision it contributes.
6. Use `collect-independent-judgments` on its named scientific object and record the evidence or decision it contributes.

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
