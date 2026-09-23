---
name: build-domain-ontology
description: "Construct a tool-independent domain ontology: scope the domain, atomize concepts, type relations, build hierarchy, audit consistency, detect gaps, and refine confidence."
---

# build-domain-ontology

## Purpose

Construct a tool-independent domain ontology: scope the domain, atomize concepts, type relations, build hierarchy, audit consistency, detect gaps, and refine confidence.

## Input contract

```yaml
required: [domain_scope, concept_records, relation_evidence]
optional: [assumptions, prior_findings, evidence_updates]
constraints: [consume named scientific objects; preserve provenance; keep unresolved uncertainty visible]
```

## Execution protocol

Do not perform called SOP operations inline; each loaded SOP owns its contract and thresholds.

1. You MUST load skill `scope-domain` to freeze the domain question, inclusion boundary, granularity, and reopening trigger before extracting entities.
2. You MUST load skill `extract-concepts` to capture source-defined concepts and relation candidates while retaining aliases, qualifiers, and unresolved meanings.
3. You MUST load skill `atomize-concept` to split broad concepts into mechanism-, function-, level-, or context-specific facets.
4. You MUST load skill `type-relation` to type each in-scope relation while preserving direction, rejected alternatives, and evidence.
5. You MUST load skill `construct-hierarchy` to insert supported edges into an acyclic hierarchy and quarantine cycles, orphans, and missing levels.
6. You MUST load skill `audit-structure-consistency` to check node and relation schemas with hierarchy, dependency, cardinality, and cycle constraints.
7. You MUST load skill `detect-coverage-gap` to prioritize absent, thin, disconnected, or weak regions.
8. You MUST load skill `canonicalize-entity` to merge only semantically identical aliases and near-duplicates while retaining rejected merges.
9. You MUST load skill `update-confidence-from-evidence` to update confidence after identities and structure are stable.
   If the ontology is ready to express directed mechanisms, consider `construct-causal-model` as the next tactic.

Deviation: reorder only when a dependency is already satisfied or unavailable; record the reason and confidence effect.

## Output contract

```yaml
produces: [scoped_ontology, typed_relations, consistency_findings, coverage_gaps]
delta_fields: [findings, decisions]
```

## Thresholds and quality gates

- Each output is traceable to an input object, operation, and evidence reference.
- Scope, assumptions, and unresolved alternatives remain explicit.
- Retain $\alpha$ 0.05 and power 0.8 wherever the predeclared statistical design requires them.

## Failure and counterexamples

Stop synthesis when a required object is absent, a precondition is violated, or a counterexample invalidates the proposed conclusion; return the partial delta with the failure recorded.

## Provenance map

- intermediate: knowledge-structuring/ontology-building [campaign]
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
| resolved v3 entries above | node-specific criteria | retained and specialized to the v4 object contract |
| experiment-execution/statistical-testing | $\alpha$ = 0.05 | fixed value retained where applicable |
| experiment-execution/sample-size-estimation | power = 0.8 | fixed value retained where applicable |

## Context checkpoint / Delta notes

Return the node-specific research-state delta and preserve findings, evidence updates, uncertainties, decisions, open questions, and recommended jumps as applicable.
