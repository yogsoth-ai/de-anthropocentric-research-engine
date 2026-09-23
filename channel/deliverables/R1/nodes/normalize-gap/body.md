# normalize-gap

## Purpose

Normalize heterogeneous research-gap records into a comparable schema before prioritization or decision operations.

## Input contract

```yaml
required: [gap_records, gap_schema]
optional: [evidence_records, domain_taxonomy, coding_rules]
constraints: [normalization preserves source wording, uncertainty, and gap type]
```

## Procedure

1. Map each record to problem, evidence, population, mechanism, and consequence fields.
2. Normalize terminology, units, and scope without erasing source distinctions.
3. Mark unknown, conflicting, and inferred fields.
4. Emit comparable gap records with traceability to originals.

## Output contract

```yaml
produces: [normalized_gap_records, field_mapping, conflict_log, traceability_map]
delta_fields: [findings, evidence_updates, uncertainties, open_questions]
```

## Quality gates

- Every normalized field traces to source text or is marked inferred.
- Conflicting gap definitions remain visible.

## Failure and counterexamples

Do not collapse different gaps because they share a label or convert missing evidence into a low-priority score.

## Provenance map

- `resolved: normalize-gap`

