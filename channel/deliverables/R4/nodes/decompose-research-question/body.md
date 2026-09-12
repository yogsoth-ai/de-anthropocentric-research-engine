# decompose-research-question

## Purpose

Decompose a complex RQ into MECE subquestions, map dependencies, and schedule the answering order.

## Input contract

~~~yaml
required: [source_state, task_object]
optional: [constraints, prior_evidence]
constraints: [typed inputs, provenance-bearing evidence, explicit uncertainty]
~~~

## Execution protocol

1. Apply `generate-subquestions` and record its typed result.
2. Apply `map-dependencies` and record its typed result.
3. Apply `sequence-work` and record its typed result.

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

- concept: decomposition-formulation <- decomposition-formulation [strategy]
- concept: sub-question-decomposition <- sub-question-decomposition [tactic]

## Preserved source criteria ledger

| source | source line | kind | source criterion |
|---|---:|---|---|
| v3 refactory source | n/a | textual | Exact normalized provenance retained; unresolved entries remain marked. |

## Context checkpoint / Delta notes

Append artifacts, evidence updates, assumptions, uncertainties, decisions, open questions, and recommended jumps.
