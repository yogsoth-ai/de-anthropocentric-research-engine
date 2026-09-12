---
name: decompose-research-question
description: "Decompose a complex RQ into MECE subquestions, map dependencies, and schedule the answering order."
---

# decompose-research-question

## Purpose

Decompose a complex RQ into MECE subquestions, map dependencies, and schedule the answering order.

## Input contract

```yaml
required: [research_object, objective, constraints]
optional: [evidence, assumptions, prior_results]
constraints: [consume named scientific objects; preserve provenance; keep unresolved uncertainty visible]
```

## Execution protocol

1. State the research question, scope, and answerability constraints that delimit decomposition. (`generate-subquestions`)
2. Generate MECE subquestions, map dependencies, and identify which subquestion each dependency enables. (`map-dependencies`)
3. Sequence the work by prerequisite and information value, flagging overlaps and unanswerable branches. (`sequence-work`)

Deviation: reorder only when a dependency is already satisfied or unavailable; record the reason and confidence effect.

## Output contract

```yaml
produces: [subquestion_set, dependency_map, answering_sequence]
delta_fields: [findings, uncertainties]
```

## Thresholds and quality gates

- Every output is traceable to a named input, called operation, and evidence reference.
- Scope, assumptions, and unresolved alternatives remain explicit.
- Retain α 0.05 and power 0.8 wherever the predeclared statistical design requires them.

## Failure and counterexamples

Stop synthesis when a required object is absent, a precondition is violated, or a counterexample invalidates the conclusion; return the partial delta with the failure recorded.

## Provenance map

- resolved: decomposition-formulation
- resolved: sub-question-decomposition

## Preserved source criteria ledger

| source | criterion | treatment |
|---|---|---|
| resolved v3 entries above | node-specific scientific criteria | retained and specialized to the v4 object contract |
| experiment-execution/statistical-testing | α = 0.05 | fixed value retained where applicable |
| experiment-execution/sample-size-estimation | power = 0.8 | fixed value retained where applicable |

## Context checkpoint / Delta notes

Return only the node-specific research-state delta and preserve findings, evidence updates, uncertainties, decisions, open questions, and recommended jumps as applicable.
