# pairwise-ranking

## Purpose

Select informative comparison pairs, execute judgments, update ratings, and audit coherence until ranking resolution is sufficient.

## Input contract

~~~yaml
required: [source_state, task_object]
optional: [constraints, prior_evidence]
constraints: [typed inputs, provenance-bearing evidence, explicit uncertainty]
~~~

## Execution protocol

1. Apply `select-next-pair` and record its typed result.
2. Apply `compare-pair` and record its typed result.
3. Apply `assess-ranking-consistency` and record its typed result.
4. Apply `aggregate-ranking` and record its typed result.
5. Apply `update-pairwise-rating` and record its typed result.
6. Apply `collect-independent-judgments` and record its typed result.

Deviation: Skip a step only when its artifact is already present or the decision objective excludes it; record the reason and uncertainty.

## Output contract

~~~yaml
produces: [analysis_artifact, decision_rationale]
delta_fields: [findings, evidence_updates, hypothesis_updates, assumption_updates, uncertainties, decisions, open_questions, recommended_jumps]
~~~

## Thresholds and quality gates

- Tie each conclusion to evidence, assumptions, or uncertainty.
- Coverage gates declare universe, numerator, denominator, batch increment, stopping reason, and source references.
- Fixed statistical values remain fixed where applicable, including α 0.05 and power 0.8.

## Failure and counterexamples

Reject unsupported, circular, untyped, or out-of-scope conclusions; preserve counterexamples.

## Provenance map

- concept: pairwise-ranking <- pairwise-ranking [campaign]
- concept: deliberative-calibration <- deliberative-calibration [strategy]
- concept: efficient-exploration <- efficient-exploration [strategy]
- concept: collective-adjudication <- collective-adjudication [strategy]
- concept: adaptive-pair-selection <- adaptive-pair-selection [tactic]
- concept: consistency-audit-loop <- consistency-audit-loop [tactic]

## Preserved source criteria ledger

| source | source line | kind | source criterion |
|---|---:|---|---|
| v3 refactory source | n/a | textual | Exact normalized provenance retained; unresolved entries remain marked. |

## Context checkpoint / Delta notes

Append artifacts, evidence updates, assumptions, uncertainties, decisions, open questions, and recommended jumps.
