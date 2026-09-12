# construct-argument-map

## Purpose

Atomize claims, expose premises and counterclaims, attach evidence/defeaters, score claim strength, and construct an inspectable argument graph independent of storage format.

## Input contract

~~~yaml
required: [source_state, task_object]
optional: [constraints, prior_evidence]
constraints: [typed inputs, provenance-bearing evidence, explicit uncertainty]
~~~

## Execution protocol

1. Apply `atomize-claim` and record its typed result.
2. Apply `surface-assumptions` and record its typed result.
3. Apply `attach-evidence-to-relation` and record its typed result.
4. Apply `document-counterclaim` and record its typed result.
5. Apply `score-object` and record its typed result.
6. Apply `construct-critique` and record its typed result.
7. Apply `detect-contradiction` and record its typed result.

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

- concept: knowledge-structuring-argument-mapping <- knowledge-structuring/argument-mapping [campaign]
- concept: claim-extraction <- claim-extraction [strategy]
- concept: premise-identification <- premise-identification [strategy]
- concept: counterargument-mapping <- counterargument-mapping [strategy]
- concept: evidence-linking-arg <- evidence-linking-arg [strategy]
- concept: argument-synthesis <- argument-synthesis [strategy]
- concept: claim-decomposition <- claim-decomposition [tactic]
- concept: strength-assessment <- strength-assessment [tactic]

## Preserved source criteria ledger

| source | source line | kind | source criterion |
|---|---:|---|---|
| v3 refactory source | n/a | textual | Exact normalized provenance retained; unresolved entries remain marked. |

## Context checkpoint / Delta notes

Append artifacts, evidence updates, assumptions, uncertainties, decisions, open questions, and recommended jumps.
