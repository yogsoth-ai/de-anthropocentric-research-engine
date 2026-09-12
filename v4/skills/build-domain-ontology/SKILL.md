---
name: build-domain-ontology
description: "Construct a tool-independent domain ontology: scope the domain, atomize concepts, type relations, build hierarchy, audit consistency, detect gaps, and refine confidence."
---

# build-domain-ontology

## Purpose

Construct a tool-independent domain ontology: scope the domain, atomize concepts, type relations, build hierarchy, audit consistency, detect gaps, and refine confidence.

## Input contract

```yaml
required: [research_object, objective, constraints]
optional: [evidence, assumptions, prior_results]
constraints: [consume named scientific objects; preserve provenance; keep unresolved uncertainty visible]
```

## Execution protocol

1. Fix the domain boundary and seed vocabulary, excluding entities that cannot be placed in the stated scope. (`scope-domain`)
2. Extract concepts, type relations, and build hierarchy while preserving evidence for each non-trivial edge. (`extract-concepts`)
3. Audit consistency, coverage gaps, canonical identities, and confidence before returning the ontology. (`atomize-concept`)
4. Fix the domain boundary and seed vocabulary, excluding entities that cannot be placed in the stated scope. (`type-relation`)
5. Extract concepts, type relations, and build hierarchy while preserving evidence for each non-trivial edge. (`construct-hierarchy`)
6. Audit consistency, coverage gaps, canonical identities, and confidence before returning the ontology. (`audit-structure-consistency`)
7. Fix the domain boundary and seed vocabulary, excluding entities that cannot be placed in the stated scope. (`detect-coverage-gap`)
8. Extract concepts, type relations, and build hierarchy while preserving evidence for each non-trivial edge. (`canonicalize-entity`)
9. Audit consistency, coverage gaps, canonical identities, and confidence before returning the ontology. (`update-confidence-from-evidence`)

Deviation: reorder only when a dependency is already satisfied or unavailable; record the reason and confidence effect.

## Output contract

```yaml
produces: [scoped_ontology, typed_relations, consistency_findings, coverage_gaps]
delta_fields: [findings, uncertainties]
```

## Thresholds and quality gates

- Every output is traceable to a named input, called operation, and evidence reference.
- Scope, assumptions, and unresolved alternatives remain explicit.
- Retain α 0.05 and power 0.8 wherever the predeclared statistical design requires them.

## Failure and counterexamples

Stop synthesis when a required object is absent, a precondition is violated, or a counterexample invalidates the conclusion; return the partial delta with the failure recorded.

## Provenance map

- resolved: ontology-building
- resolved: domain-scoping
- resolved: concept-extraction
- resolved: relation-typing
- resolved: taxonomy-validation
- resolved: ontology-refinement
- resolved: hierarchy-construction
- intermediate: consistency-checking [tactic]

## Preserved source criteria ledger

| source | criterion | treatment |
|---|---|---|
| resolved v3 entries above | node-specific scientific criteria | retained and specialized to the v4 object contract |
| experiment-execution/statistical-testing | α = 0.05 | fixed value retained where applicable |
| experiment-execution/sample-size-estimation | power = 0.8 | fixed value retained where applicable |

## Context checkpoint / Delta notes

Return only the node-specific research-state delta and preserve findings, evidence updates, uncertainties, decisions, open questions, and recommended jumps as applicable.
