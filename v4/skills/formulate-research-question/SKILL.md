---
name: formulate-research-question
description: "Convert a hypothesis into a precise research question with fit-for-purpose framework, scope, feasibility, and success criteria."
---

# formulate-research-question

## Purpose

Convert a hypothesis into a precise research question with fit-for-purpose framework, scope, feasibility, and success criteria.

## Input contract

```yaml
required: [research_object, objective, constraints]
optional: [evidence, assumptions, prior_results]
constraints: [consume named scientific objects; preserve provenance; keep unresolved uncertainty visible]
```

## Execution protocol

1. Select a framework that matches the hypothesis, population, comparison, and intended decision. (`apply-question-framework`)
2. Test question quality, scope, feasibility, criteria, and threshold against the available evidence and resources. (`assess-question-quality`)
3. Refine the abstraction level and emit one precise question with success criteria and documented exclusions. (`define-criteria`)
4. Select a framework that matches the hypothesis, population, comparison, and intended decision. (`set-threshold`)
5. Test question quality, scope, feasibility, criteria, and threshold against the available evidence and resources. (`adjust-abstraction-scope`)

Deviation: reorder only when a dependency is already satisfied or unavailable; record the reason and confidence effect.

## Output contract

```yaml
produces: [research_question, success_criteria, scope_decision]
delta_fields: [findings, uncertainties]
```

## Thresholds and quality gates

- Every output is traceable to a named input, called operation, and evidence reference.
- Scope, assumptions, and unresolved alternatives remain explicit.
- Retain α 0.05 and power 0.8 wherever the predeclared statistical design requires them.

## Failure and counterexamples

Stop synthesis when a required object is absent, a precondition is violated, or a counterexample invalidates the conclusion; return the partial delta with the failure recorded.

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
| resolved v3 entries above | node-specific scientific criteria | retained and specialized to the v4 object contract |
| experiment-execution/statistical-testing | α = 0.05 | fixed value retained where applicable |
| experiment-execution/sample-size-estimation | power = 0.8 | fixed value retained where applicable |

## Context checkpoint / Delta notes

Return only the node-specific research-state delta and preserve findings, evidence updates, uncertainties, decisions, open questions, and recommended jumps as applicable.
