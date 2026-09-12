# build-domain-ontology

## Purpose

Construct a tool-independent domain ontology: scope the domain, atomize concepts, type relations, build hierarchy, audit consistency, detect gaps, and refine confidence.

## Input contract

~~~yaml
required: [source_state, task_object]
optional: [constraints, prior_evidence]
constraints: [typed inputs, provenance-bearing evidence, explicit uncertainty]
~~~

## Execution protocol

1. Apply `scope-domain` and record its typed result.
2. Apply `extract-concepts` and record its typed result.
3. Apply `atomize-concept` and record its typed result.
4. Apply `type-relation` and record its typed result.
5. Apply `construct-hierarchy` and record its typed result.
6. Apply `audit-structure-consistency` and record its typed result.
7. Apply `detect-coverage-gap` and record its typed result.
8. Apply `canonicalize-entity` and record its typed result.
9. Apply `update-confidence-from-evidence` and record its typed result.

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

- concept: knowledge-structuring-ontology-building <- knowledge-structuring/ontology-building [campaign]
- concept: domain-scoping <- domain-scoping [strategy]
- concept: concept-extraction <- concept-extraction [strategy]
- concept: relation-typing <- relation-typing [strategy]
- concept: taxonomy-validation <- taxonomy-validation [strategy]
- concept: ontology-refinement <- ontology-refinement [strategy]
- concept: hierarchy-construction <- hierarchy-construction [tactic]
- concept: consistency-checking <- consistency-checking [tactic]

## Preserved source criteria ledger

| source | source line | kind | source criterion |
|---|---:|---|---|
| v3 refactory source | n/a | textual | Exact normalized provenance retained; unresolved entries remain marked. |

## Context checkpoint / Delta notes

Append artifacts, evidence updates, assumptions, uncertainties, decisions, open questions, and recommended jumps.
