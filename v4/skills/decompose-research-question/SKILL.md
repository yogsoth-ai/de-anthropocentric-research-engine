---
name: decompose-research-question
description: "Decompose a complex RQ into MECE subquestions, map dependencies, and schedule the answering order."
---

# decompose-research-question

## Purpose

Decompose a complex RQ into MECE subquestions, map dependencies, and schedule the answering order.

## Input contract

```yaml
required: [research_question, scope_constraints, dependency_evidence]
optional: [assumptions, prior_findings, evidence_updates]
constraints: [consume named scientific objects; preserve provenance; keep unresolved uncertainty visible]
```

## Execution protocol

Do not perform called SOP operations inline; each loaded SOP owns its contract and thresholds.

1. You MUST load skill `generate-subquestions` to generate answerable subquestions.
2. You MUST load skill `map-dependencies` to map their evidence and logical dependencies.
3. You MUST load skill `sequence-work` to sequence the dependent research work.

Deviation: reorder only when a dependency is already satisfied or unavailable; record the reason and confidence effect.

## Output contract

```yaml
produces: [subquestion_set, dependency_map, answering_sequence]
delta_fields: [open_questions]
```

## Thresholds and quality gates

- Each output is traceable to an input object, operation, and evidence reference.
- Scope, assumptions, and unresolved alternatives remain explicit.
- Retain $\alpha$ 0.05 and power 0.8 wherever the predeclared statistical design requires them.

## Failure and counterexamples

Stop synthesis when a required object is absent, a precondition is violated, or a counterexample invalidates the proposed conclusion; return the partial delta with the failure recorded.

## Provenance map

- resolved: decomposition-formulation
- resolved: sub-question-decomposition

## Preserved source criteria ledger

| source | criterion | treatment |
|---|---|---|
| resolved v3 entries above | node-specific criteria | retained and specialized to the v4 object contract |
| experiment-execution/statistical-testing | $\alpha$ = 0.05 | fixed value retained where applicable |
| experiment-execution/sample-size-estimation | power = 0.8 | fixed value retained where applicable |

## Context checkpoint / Delta notes

Return the node-specific research-state delta and preserve findings, evidence updates, uncertainties, decisions, open questions, and recommended jumps as applicable.
