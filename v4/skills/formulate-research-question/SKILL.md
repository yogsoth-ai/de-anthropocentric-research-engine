---
name: formulate-research-question
description: "Convert a hypothesis into a precise research question with fit-for-purpose framework, scope, feasibility, and success criteria."
---

# formulate-research-question

## Purpose

Convert a hypothesis into a precise research question with fit-for-purpose framework, scope, feasibility, and success criteria.

## Input contract

```yaml
required: [hypothesis_or_gap, candidate_frameworks, feasibility_constraints]
optional: [assumptions, prior_findings, evidence_updates]
constraints: [consume named scientific objects; preserve provenance; keep unresolved uncertainty visible]
```

## Execution protocol

1. Use `apply-question-framework` on its named scientific object and record the evidence or decision it contributes.
2. Use `assess-question-quality` on its named scientific object and record the evidence or decision it contributes.
3. Use `define-criteria` on its named scientific object and record the evidence or decision it contributes.
4. Use `set-threshold` on its named scientific object and record the evidence or decision it contributes.
5. Use `adjust-abstraction-scope` on its named scientific object and record the evidence or decision it contributes.

Deviation: reorder only when a dependency is already satisfied or unavailable; record the reason and confidence effect.

## Output contract

```yaml
produces: [research_question, success_criteria, scope_decision]
delta_fields: [decisions, open_questions]
```

## Thresholds and quality gates

- Each output is traceable to an input object, operation, and evidence reference.
- Scope, assumptions, and unresolved alternatives remain explicit.
- Retain α 0.05 and power 0.8 wherever the predeclared statistical design requires them.

## Failure and counterexamples

Stop synthesis when a required object is absent, a precondition is violated, or a counterexample invalidates the proposed conclusion; return the partial delta with the failure recorded.

## Provenance map

- resolved: research-question
- resolved: framework-guided-formulation
- resolved: scope-calibration
- resolved: comparative-formulation
- resolved: feasibility-constrained-formulation
- resolved: framework-selection-and-application
- resolved: question-refinement-loop

## Preserved source criteria ledger

| source | criterion | treatment |
|---|---|---|
| resolved v3 entries above | node-specific criteria | retained and specialized to the v4 object contract |
| experiment-execution/statistical-testing | α = 0.05 | fixed value retained where applicable |
| experiment-execution/sample-size-estimation | power = 0.8 | fixed value retained where applicable |

## Context checkpoint / Delta notes

Return the node-specific research-state delta and preserve findings, evidence updates, uncertainties, decisions, open questions, and recommended jumps as applicable.
