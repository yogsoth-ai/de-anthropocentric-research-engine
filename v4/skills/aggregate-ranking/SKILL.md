---
name: aggregate-ranking
description: "Aggregate criterion or comparison results into an ordered recommendation under an explicit rule."
---

# aggregate-ranking

## Purpose
Aggregate criterion or comparison results into an ordered recommendation under an explicit rule.

## Input contract
```yaml
required: [candidate_set, criterion_results, aggregation_rule]
optional: [tie_break_rule, missing_value_policy, uncertainty_annotations]
constraints: [criterion directions and scales must be declared; no silent imputation]
```

## Procedure
1. Align candidate identifiers, criterion directions, units, and validity flags.
2. Apply the supplied aggregation rule without changing weights or directions.
3. Propagate missingness and uncertainty; apply the declared tie-break only after aggregation.
4. Return ordered candidates with component contributions and recommendation status.

## Output contract
```yaml
produces: [ordered_recommendation, aggregate_scores, contribution_table, unresolved_comparisons]
delta_fields: [findings, evidence_updates, decisions, uncertainties]
```

## Quality gates
- Every ranked candidate has a traceable value for each required criterion or an explicit unresolved marker.
- Aggregation reproduces the supplied rule and preserves criterion direction.
- Ties and sensitivity to tie-breaks are reported.

## Parameterization
Caller supplies candidate schema, criterion scales/directions, weights or aggregation formula, tie-break rule, and missing/uncertainty policy.

## Failure and counterexamples
Reject mixed units without normalization; reject a recommendation when a hard criterion is unresolved.

## Provenance map
- resolved: priority-synthesis
- resolved: scoring-synthesis

## Preserved source criteria ledger

| source | criterion |
|---|---|
| priority-synthesis | All scoring dimensions are present for every gap. |
| priority-synthesis | Weight vector sums to 1.0 within ±0.001. |
| priority-synthesis | Priority list is sorted descending; ties use feasibility sub-score. |
| priority-synthesis | Top N is N=min(3,total gaps) and includes attack-path suggestions. |
| scoring-synthesis | Final recommendation includes recommended alternative, confidence, key assumptions, and risk warnings. |
