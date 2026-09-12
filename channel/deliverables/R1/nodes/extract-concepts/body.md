# extract-concepts

## Purpose

Extract domain concepts, definitions, and relation candidates from a source while preserving source wording and scope.

## Input contract

```yaml
required: [source, extraction_scope]
optional: [concept_schema, domain_ontology, relation_cues]
constraints: [each concept requires a source span and an uncertainty state]
```

## Procedure

1. Identify repeated technical terms, defined entities, and salient constructs.
2. Capture source definitions, aliases, scope qualifiers, and examples.
3. Link candidate relations only when the source expresses them.
4. Emit a deduplicated concept set with unresolved meanings retained.

## Output contract

```yaml
produces: [concept_records, definition_map, alias_map, relation_candidates, ambiguity_log]
delta_fields: [findings, evidence_updates, uncertainties, open_questions]
```

## Quality gates

- Concepts are source-linked and distinct from inferred themes.
- Alias merging preserves conflicting definitions.

## Failure and counterexamples

Do not infer a concept solely from keyword frequency or merge terms with different operational meanings.

## Provenance map

- `resolved: extract-concepts`

