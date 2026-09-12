# categorize-evidence

## Purpose

Cluster an evidence corpus by a declared thematic, methodological, chronological, mechanistic, or other schema.

## Input contract

```yaml
required: [evidence_records, category_schema]
optional: [coding_rules, multi_label_policy, seed_categories]
constraints: [category assignments require record evidence and allow explicit multi-label or unknown states]
```

## Procedure

1. Define category semantics and assignment rules.
2. Code each record using the declared evidence fields.
3. Review boundary cases and preserve multi-label or unresolved assignments.
4. Summarize category coverage and representative records.

## Output contract

```yaml
produces: [categorized_corpus, category_definitions, boundary_cases, coverage_summary]
delta_fields: [findings, evidence_updates, uncertainties, open_questions]
```

## Quality gates

- Categories are mutually interpretable even when not mutually exclusive.
- Every assignment is traceable to record fields.

## Failure and counterexamples

Do not force records into categories whose definitions do not fit, and do not confuse frequency with evidential importance.

## Provenance map

- `resolved: knowledge-acquisition-categorize-papers`
- `concept: knowledge-structuring/source-categorization-patterns`
- `intermediate: Pass4/map-field-taxonomy`

