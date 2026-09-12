---
name: extract-evidence-record
description: "Extract a schema-declared evidence record from a source, including methods, datasets, metrics/results, conditions, limitations, provenance, and explicitly missing/ambiguous fields."
---

# extract-evidence-record

## Purpose

Extract a schema-declared evidence record containing methods, data, metrics, results, conditions, limitations, provenance, and explicit missing fields.

## Input contract

```yaml
required: [source, extraction_schema]
optional: [protocol_record, quality_rubric, condition_schema]
constraints: [each extracted value is source-linked and missing or ambiguous fields remain explicit]
```

## Procedure

1. Identify source identity, study design, population, intervention/exposure, comparator, and outcome.
2. Extract methods, data, evaluation conditions, metrics, estimates, and limitations into the schema.
3. Record units, uncertainty, provenance links, and missing/ambiguous fields.
4. Run schema and consistency checks before releasing the record.

## Output contract

```yaml
produces: [evidence_record, condition_record, source_links, missing_field_log, extraction_notes]
delta_fields: [evidence_updates, uncertainties, open_questions]
```

## Quality gates

- Results cannot be detached from their conditions and metric definitions.
- Missing data are distinct from zero or null results.
- Extraction notes preserve source wording where interpretation is uncertain.

## Failure and counterexamples

Do not infer unreported baselines or merge records from different study versions without lineage evidence.

## Provenance map

- `resolved: extract-data`
- `resolved: score-extraction`
- `resolved: condition-cataloging`
- `intermediate: Pass4/extract-study-data`
- `resolved: performance-extraction`
- `intermediate: Pass4/extract-performance-record`
- `intermediate: Pass4/catalog-evaluation-conditions`
