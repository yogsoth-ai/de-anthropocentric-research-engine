# design-data-extraction

## Purpose

Define a structured extraction form, field semantics, coding rules, and missing-data handling for evidence synthesis.

## Input contract

```yaml
required: [evidence_question, record_schema]
optional: [coding_guidance, unit_rules, quality_fields]
constraints: [field definitions and missing-data states must be explicit]
```

## Procedure

1. Derive fields from the evidence question and synthesis outputs.
2. Define types, units, allowed values, coding rules, and provenance fields.
3. Specify unknown, not reported, not applicable, and ambiguous states.
4. Pilot the form on boundary records and revise only documented ambiguities.

## Output contract

```yaml
produces: [extraction_schema, coding_rules, missing_data_policy, pilot_issues]
delta_fields: [decisions, assumption_updates, uncertainties, open_questions]
```

## Quality gates

- Every output field has an extraction source and semantic definition.
- Missingness is not conflated with a negative finding.

## Failure and counterexamples

Do not add fields that cannot affect the synthesis, and do not collapse incomparable units.

## Provenance map

- `concept: knowledge-acquisition-data-extraction-form`
