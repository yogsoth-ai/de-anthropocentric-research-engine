---
name: design-study-inclusion
description: "Define study inclusion/exclusion criteria and explicit rules for borderline cases."
---

# design-study-inclusion

## Purpose

Define study inclusion and exclusion criteria with explicit rules for borderline cases.

## Input contract

```yaml
required: [research_question, eligible_population, study_scope]
optional: [outcome_rules, design_rules, date_language_limits]
constraints: [criteria must be observable from source records]
```

## Procedure

1. Translate the question into population, intervention/exposure, comparator, outcome, design, and context criteria.
2. Define exclusion reasons and precedence for overlapping rules.
3. Specify borderline-case adjudication and missing-information handling.
4. Test criteria against representative included, excluded, and ambiguous records.

## Output contract

```yaml
produces: [inclusion_criteria, exclusion_reasons, borderline_rules, pilot_adjudications]
delta_fields: [decisions, assumption_updates, uncertainties, open_questions]
```

## Quality gates

- Criteria are applicable without knowing the study result.
- Each exclusion has one primary reason.

## Failure and counterexamples

Do not make inclusion depend on favorable findings or exclude a study solely because metadata are incomplete when the design remains eligible.

## Provenance map

- `resolved: inclusion-criteria-design`
