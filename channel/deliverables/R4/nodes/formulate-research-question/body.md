# formulate-research-question

## Purpose

Convert a hypothesis into a precise research question with fit-for-purpose framework, scope, feasibility, and success criteria.

## Input contract

~~~yaml
required: [source_state, task_object]
optional: [constraints, prior_evidence]
constraints: [typed inputs, provenance-bearing evidence, explicit uncertainty]
~~~

## Execution protocol

1. Apply `apply-question-framework` and record its typed result.
2. Apply `assess-question-quality` and record its typed result.
3. Apply `define-criteria` and record its typed result.
4. Apply `set-threshold` and record its typed result.
5. Apply `adjust-abstraction-scope` and record its typed result.

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

- concept: research-question <- research-question [campaign]
- concept: framework-guided-formulation <- framework-guided-formulation [strategy]
- concept: scope-calibration <- scope-calibration [strategy]
- concept: comparative-formulation <- comparative-formulation [strategy]
- concept: feasibility-constrained-formulation <- feasibility-constrained-formulation [strategy]
- concept: framework-selection-and-application <- framework-selection-and-application [tactic]
- concept: question-refinement-loop <- question-refinement-loop [tactic]

## Preserved source criteria ledger

| source | source line | kind | source criterion |
|---|---:|---|---|
| v3 refactory source | n/a | textual | Exact normalized provenance retained; unresolved entries remain marked. |

## Context checkpoint / Delta notes

Append artifacts, evidence updates, assumptions, uncertainties, decisions, open questions, and recommended jumps.
