# optimize-design-under-budget

## Purpose

Given cost per run and resource budget, choose the most information-efficient feasible design while preserving essential validity constraints.

## Input contract

~~~yaml
required: [source_state, task_object]
optional: [constraints, prior_evidence]
constraints: [typed inputs, provenance-bearing evidence, explicit uncertainty]
~~~

## Procedure

1. Parse the typed input and identify the transformation target.
2. Apply the operation while preserving assumptions and provenance.
3. Emit the result with unresolved uncertainty explicit.

## Output contract

~~~yaml
produces: [analysis_artifact, decision_rationale]
delta_fields: [findings, evidence_updates, hypothesis_updates, assumption_updates, uncertainties, decisions, open_questions, recommended_jumps]
~~~

## Quality gates

- Output is typed, traceable to inputs, and complete for the declared scope.
- No unsupported numeric threshold or mechanism is introduced.

## Failure and counterexamples

Mark the result unresolved when evidence is missing, contradictory, or outside scope; retain counterexamples.

## Provenance map

- concept: experiment-execution-budget-constrained-design <- experiment-execution/budget-constrained-design [tactic]
