# synthesize-field-panorama

## Purpose

Summarize candidate fields by maturity, competition, entry barrier, tractability, and opportunity structure.

## Input contract

```yaml
required: [candidate_fields, evidence_records, comparison_dimensions]
optional: [actor_profile, constraints, time_window]
constraints: [each dimension requires supporting evidence or an explicit missing marker]
```

## Procedure

1. Normalize evidence for each candidate field and comparison dimension.
2. Assess maturity, competition, entry barriers, tractability, and opportunity.
3. Record direct opportunities, limiting barriers, and boundary-crossing rationale.
4. Compare candidates while preserving uncertainty and evidence gaps.

## Output contract

```yaml
produces: [field_panorama, maturity_map, competition_map, barrier_map, opportunity_structure, evidence_gaps]
delta_fields: [findings, evidence_updates, uncertainties, decisions, open_questions]
```

## Quality gates

- Every candidate has at least one opportunity and one barrier assessment.
- Publication volume is not used as a maturity proxy without quality or mechanism evidence.

## Failure and counterexamples

Do not call a field tractable because it is popular or call a sparse field an opportunity without checking evidence quality and competition.

## Provenance map

- `resolved: north-star-crystallization/landscape-synthesis`

