# screen-evidence-multistage

## Purpose

Apply explicit staged inclusion and exclusion screening with reasons and an auditable flow.

## Input contract

```yaml
required: [candidate_records, inclusion_rules, exclusion_reasons]
optional: [title_abstract_fields, full_text_fields, duplicate_rules]
constraints: [each stage records in/out counts and a primary exclusion reason]
```

## Procedure

1. Deduplicate and record the identification universe.
2. Screen title/abstract or equivalent shallow fields against inclusion rules.
3. Screen full evidence for retained candidates and record exclusions.
4. Emit the final included set and stage-by-stage audit flow.

## Output contract

```yaml
produces: [screening_flow, included_records, excluded_records, exclusion_reason_log, coverage_summary]
delta_fields: [findings, evidence_updates, uncertainties, decisions, open_questions]
```

## Quality gates

- Stage counts reconcile to the candidate universe.
- Full-text or equivalent evidence is distinguished from abstract-only evidence.

## Failure and counterexamples

Do not hide duplicate removal or use a final included count without the exclusion flow.

## Provenance map

- `resolved: systematic-survey`
- `resolved: prisma-screening`
