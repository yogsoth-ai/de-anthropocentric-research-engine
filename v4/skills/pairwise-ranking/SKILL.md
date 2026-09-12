---
name: pairwise-ranking
description: "Select informative comparison pairs, execute judgments, update ratings, and audit coherence until ranking resolution is sufficient."
---

# pairwise-ranking

## Purpose

Select informative comparison pairs, execute judgments, update ratings, and audit coherence until ranking resolution is sufficient.

## Input contract

```yaml
required: [research_object, objective, constraints]
optional: [evidence, assumptions, prior_results]
constraints: [consume named scientific objects; preserve provenance; keep unresolved uncertainty visible]
```

## Execution protocol

1. Define the candidate set, comparison objective, and stopping rule before selecting a pair. (`select-next-pair`)
2. Choose informative pairs, collect independent judgments, update ratings, and preserve disagreement rather than averaging it invisibly. (`compare-pair`)
3. Audit ranking coherence and stop only when the resolution criterion is met or the remaining uncertainty is explicit. (`assess-ranking-consistency`)
4. Define the candidate set, comparison objective, and stopping rule before selecting a pair. (`aggregate-ranking`)
5. Choose informative pairs, collect independent judgments, update ratings, and preserve disagreement rather than averaging it invisibly. (`update-pairwise-rating`)
6. Audit ranking coherence and stop only when the resolution criterion is met or the remaining uncertainty is explicit. (`collect-independent-judgments`)

Deviation: reorder only when a dependency is already satisfied or unavailable; record the reason and confidence effect.

## Output contract

```yaml
produces: [updated_ratings, ranking, coherence_diagnostics]
delta_fields: [findings, uncertainties]
```

## Thresholds and quality gates

- Every output is traceable to a named input, called operation, and evidence reference.
- Scope, assumptions, and unresolved alternatives remain explicit.
- Retain α 0.05 and power 0.8 wherever the predeclared statistical design requires them.

## Failure and counterexamples

Stop synthesis when a required object is absent, a precondition is violated, or a counterexample invalidates the conclusion; return the partial delta with the failure recorded.

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
| resolved v3 entries above | node-specific scientific criteria | retained and specialized to the v4 object contract |
| experiment-execution/statistical-testing | α = 0.05 | fixed value retained where applicable |
| experiment-execution/sample-size-estimation | power = 0.8 | fixed value retained where applicable |

## Context checkpoint / Delta notes

Return only the node-specific research-state delta and preserve findings, evidence updates, uncertainties, decisions, open questions, and recommended jumps as applicable.
