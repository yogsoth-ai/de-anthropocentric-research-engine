# construct-causal-model

## Purpose

Construct and validate an explicit causal model with measurable variables, mechanism edges, evidence links, feedback loops, interventions, counterevidence, and confidence.

## Input contract

~~~yaml
required: [source_state, task_object]
optional: [constraints, prior_evidence]
constraints: [typed inputs, provenance-bearing evidence, explicit uncertainty]
~~~

## Execution protocol

1. Apply `identify-variables` and record its typed result.
2. Apply `extract-causal-structure` and record its typed result.
3. Apply `represent-mechanism-edge` and record its typed result.
4. Apply `attach-evidence-to-relation` and record its typed result.
5. Apply `detect-contradiction` and record its typed result.
6. Apply `detect-feedback-loop` and record its typed result.
7. Apply `trace-causal-chain` and record its typed result.
8. Apply `analyze-intervention` and record its typed result.
9. Apply `construct-counterfactual` and record its typed result.
10. Apply `validate-causal-link` and record its typed result.
11. Apply `update-confidence-from-evidence` and record its typed result.

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

- concept: knowledge-structuring-causal-modeling <- knowledge-structuring/causal-modeling [campaign]
- concept: variable-identification <- variable-identification [strategy]
- concept: mechanism-mapping <- mechanism-mapping [strategy]
- concept: evidence-collection <- evidence-collection [strategy]
- concept: intervention-analysis <- intervention-analysis [strategy]
- concept: model-validation <- model-validation [strategy]
- concept: counterfactual-reasoning <- counterfactual-reasoning [tactic]
- concept: evidence-weighing <- evidence-weighing [tactic]

## Preserved source criteria ledger

| source | source line | kind | source criterion |
|---|---:|---|---|
| v3 refactory source | n/a | textual | Exact normalized provenance retained; unresolved entries remain marked. |

## Context checkpoint / Delta notes

Append artifacts, evidence updates, assumptions, uncertainties, decisions, open questions, and recommended jumps.
