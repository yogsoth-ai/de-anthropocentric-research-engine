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

Do not perform called SOP operations inline; each loaded SOP owns its contract and thresholds.

1. You MUST load skill `apply-question-framework` to construct the question under the selected framework.
2. You MUST load skill `assess-question-quality` to assess answerability, significance, and precision.
3. You MUST load skill `define-criteria` to define the question-quality criteria.
4. You MUST load skill `set-threshold` to set the acceptance thresholds.
5. You MUST load skill `adjust-abstraction-scope` to correct the abstraction level and scope.
   If the accepted question contains dependent subproblems, consider `decompose-research-question` as the next tactic.

Deviation: reorder only when a dependency is already satisfied or unavailable; record the reason and confidence effect.

## Output contract

```yaml
produces: [research_question, success_criteria, scope_decision]
delta_fields: [decisions, open_questions]
```

## Thresholds and quality gates

- Each output is traceable to an input object, operation, and evidence reference.
- Scope, assumptions, and unresolved alternatives remain explicit.
- Retain $\alpha$ 0.05 and power 0.8 wherever the predeclared statistical design requires them.

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
| experiment-execution/statistical-testing | $\alpha$ = 0.05 | fixed value retained where applicable |
| experiment-execution/sample-size-estimation | power = 0.8 | fixed value retained where applicable |

## Context checkpoint / Delta notes

Return the node-specific research-state delta and preserve findings, evidence updates, uncertainties, decisions, open questions, and recommended jumps as applicable.
