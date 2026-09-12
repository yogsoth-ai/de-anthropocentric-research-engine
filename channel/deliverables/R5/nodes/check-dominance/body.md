# check-dominance

## Purpose
Identify Pareto-dominated and non-dominated alternatives under strict dominance.

## Input contract
```yaml
required: [alternative_set, score_matrix, criterion_directions]
optional: [missing_value_policy, equality_tolerance]
constraints: [all compared scores share declared direction and scale]
```

## Procedure
1. Normalize criterion direction and validate comparable rows.
2. Compare each ordered pair: no worse on every criterion and strictly better on at least one.
3. Record each dominated alternative with its dominator and witness criterion.
4. Return the non-dominated front and unresolved comparisons.

## Output contract
```yaml
produces: [dominance_relations, dominated_set, nondominated_front, comparison_gaps]
delta_fields: [findings, evidence_updates, uncertainties]
```

## Quality gates
- Every dominated label names a dominating alternative and strict witness.
- No alternative is both dominated and on the non-dominated front under the same tolerance.
- Missing or incomparable scores are never treated as dominance.

## Parameterization
Caller supplies alternative schema, criterion direction, tolerance, missingness policy, and whether strict or weak dominance is allowed.

## Failure and counterexamples
Reject dominance claims when a criterion direction is unknown or a strict improvement cannot be exhibited.

## Provenance map
- resolved: dominance-check

