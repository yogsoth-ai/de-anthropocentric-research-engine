# type-relation
## Purpose
Classify relations among entities with an explicit relation ontology and evidence for the chosen type.
## Input contract
```yaml
required: [entity_pair, relation_ontology, evidence_register]
optional: [candidate_relation_types, scope_ledger, prior_edges]
constraints: [relation type, direction, scope, and evidence are explicit]
```
## Procedure
1. Verify that both entities are in scope and normalize their identifiers.
2. Enumerate candidate relation types and test each against its defining conditions.
3. Select the best-supported type or record ambiguity, then state direction and evidence.
4. Emit the typed relation, rejected types, and follow-up evidence needed to resolve uncertainty.
## Output contract
```yaml
produces: [typed_relation, rejected_relation_types, evidence_links, unresolved_relation_questions]
delta_fields: [findings, evidence_updates, uncertainties, decisions, open_questions]
```
## Quality gates
- Each relation has a type definition, direction, entity pair, and at least one evidence link or explicit unknown status.
- Do not assign a hierarchical relation when the evidence only supports co-occurrence.
## Failure and counterexamples
Do not infer relation type from entity names. If multiple relation types remain plausible, preserve the alternatives.
## Provenance map
- resolved: relation-typing
- resolved: edge-batch-creation (semantic core)
