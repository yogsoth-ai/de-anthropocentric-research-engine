# analyze-experiment-results

## Purpose

Interpret completed experimental outputs after host/runtime execution using pre-declared statistical tests, effect/uncertainty estimates, reproducibility checks, and calibrated synthesis.

## Input contract

~~~yaml
required: [source_state, task_object]
optional: [constraints, prior_evidence]
constraints: [typed inputs, provenance-bearing evidence, explicit uncertainty]
~~~

## Execution protocol

1. Apply `statistical-testing` and record its typed result.
2. Apply `verify-reproducibility` and record its typed result.

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

- concept: experiment-execution-result-analysis <- experiment-execution/result-analysis [strategy]
- concept: result-validation-loop <- result-validation-loop [tactic]
- concept: statistical-testing <- statistical-testing [sop]
- concept: reproducibility-verification <- reproducibility-verification [sop]
- concept: execution-synthesis <- execution-synthesis [sop]
- concept: result-collection <- result-collection [runtime input acquisition]

## Preserved source criteria ledger

| source | source line | kind | source criterion |
|---|---:|---|---|
| v3 refactory source | n/a | textual | Exact normalized provenance retained; unresolved entries remain marked. |

## Context checkpoint / Delta notes

Append artifacts, evidence updates, assumptions, uncertainties, decisions, open questions, and recommended jumps.
