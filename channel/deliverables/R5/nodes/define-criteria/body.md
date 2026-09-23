# define-criteria

## Purpose
Derive explicit evaluation criteria from the research objective and candidate set.

## Input contract
```yaml
required: [research_objective, candidate_set, decision_context]
optional: [stakeholder_priorities, measurement_constraints, candidate_domains]
constraints: [criteria must be mutually interpretable across candidates]
```

## Procedure
1. Extract desired outcomes and constraints from the objective.
2. Translate them into candidate-discriminating criteria with definitions and units.
3. Check completeness, overlap, direction, and measurability.
4. Return the criterion schema and unresolved measurement questions.

## Output contract
```yaml
produces: [criterion_schema, measurement_definitions, direction_labels, coverage_notes]
delta_fields: [findings, open_questions, uncertainties]
```

## Quality gates
- Criteria count is between 3 and 12 unless caller explicitly authorizes another range.
- Every criterion has name, definition, unit, and higher/lower-is-better direction.
- Criteria are non-overlapping enough that double counting is documented.

## Parameterization
Caller supplies objective schema, candidate schema, criterion count bounds, measurement units, direction vocabulary, and overlap policy.

## Failure and counterexamples
Reject vague criteria lacking an observable measurement or criteria that cannot distinguish any candidate.

## Provenance map
- resolved: criterion-definition
- concept: hypothesis-formation/scoring-matrix-construction (criteria-extraction core)
- resolved: hypothesis-formation-scoring-matrix-construction
- intermediate: Pass4/define-success-criteria

## Preserved source criteria ledger

| source | criterion |
|---|---|
| criterion-definition | Criteria count is between 3–12. |
| criterion-definition | Each criterion includes name, definition, unit of measurement, and direction (higher-is-better/lower-is-better). |
| convergence-scoring-matrix-construction | Normalization method matches the aggregation method. |
| convergence-scoring-matrix-construction | Sensitivity testing perturbs at least 3 weight parameters by ±10%. |
