# structured-consensus

## Purpose

Map disagreement, iterate evidence/argument refinement, and terminate with an output contract containing stable consensus, unresolved disagreements, confidence/probabilities, and threshold/stop rationale.

## Input contract

~~~yaml
required: [source_state, task_object]
optional: [constraints, prior_evidence]
constraints: [typed inputs, provenance-bearing evidence, explicit uncertainty]
~~~

## Execution protocol

1. Apply `map-disagreement` and record its typed result.
2. Apply `run-convergence-round` and record its typed result.
3. Apply `calibrate-probability-forecast` and record its typed result.
4. Apply `set-threshold` and record its typed result.

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

- concept: structured-consensus <- structured-consensus [campaign]
- concept: convergence-distillation <- convergence-distillation [strategy]
- concept: disagreement-cartography <- disagreement-cartography [strategy]
- concept: argument-crystallization <- argument-crystallization [strategy]
- concept: disagreement-mapping <- disagreement-mapping [tactic]
- concept: iterative-convergence-round <- iterative-convergence-round [tactic]

## Preserved source criteria ledger

| source | source line | kind | source criterion |
|---|---:|---|---|
| v3 refactory source | n/a | textual | Exact normalized provenance retained; unresolved entries remain marked. |

## Context checkpoint / Delta notes

Append artifacts, evidence updates, assumptions, uncertainties, decisions, open questions, and recommended jumps.
