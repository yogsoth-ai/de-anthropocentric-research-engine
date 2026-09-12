# analyze-future-scenarios

## Purpose

Construct and compare plausible future/competitive/temporal/stress scenarios and test whether the research path remains robust across them.

## Input contract

~~~yaml
required: [source_state, task_object]
optional: [constraints, prior_evidence]
constraints: [typed inputs, provenance-bearing evidence, explicit uncertainty]
~~~

## Execution protocol

1. Apply `identify-scenario-drivers` and record its typed result.
2. Apply `enumerate-dimension-values` and record its typed result.
3. Apply `evaluate-compatibility` and record its typed result.
4. Apply `construct-scenario` and record its typed result.
5. Apply `evaluate-scenario-impact` and record its typed result.
6. Apply `evaluate-scenario-robustness` and record its typed result.
7. Apply `predict-competitive-move` and record its typed result.
8. Apply `analyze-temporal-trajectory` and record its typed result.

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

- concept: experiment-execution-scenario-planning <- experiment-execution/scenario-planning [campaign]
- concept: morphological-scenario <- morphological-scenario [strategy]
- concept: narrative-scenario <- narrative-scenario [strategy]
- concept: stress-scenario <- stress-scenario [strategy]
- concept: competitive-scenario <- competitive-scenario [strategy]
- concept: temporal-scenario <- temporal-scenario [strategy]
- concept: parameter-space-construction <- parameter-space-construction [tactic]
- concept: cross-consistency-filtering <- cross-consistency-filtering [tactic]
- concept: strategy-robustness-testing <- strategy-robustness-testing [tactic]

## Preserved source criteria ledger

| source | source line | kind | source criterion |
|---|---:|---|---|
| v3 refactory source | n/a | textual | Exact normalized provenance retained; unresolved entries remain marked. |

## Context checkpoint / Delta notes

Append artifacts, evidence updates, assumptions, uncertainties, decisions, open questions, and recommended jumps.
