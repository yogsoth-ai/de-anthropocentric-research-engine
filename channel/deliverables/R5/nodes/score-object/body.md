# score-object

## Purpose

Score one typed object against a caller-supplied rubric, attaching evidence, uncertainty, and rationale without inventing object-specific criteria.

## Input contract

```yaml
required: [object, object_schema, rubric, evidence, uncertainty_policy]
optional: [weights, aggregation_rule, missing_value_policy, score_scale, provenance]
constraints: [the parent tactic supplies the object schema and rubric; every dimension has an explicit scale and rationale requirement; evidence and uncertainty are attached per dimension]
```

## Procedure

1. Validate the object against the supplied schema and confirm the rubric dimensions, scale, weights, and missing-value policy are complete.
2. Extract evidence relevant to each dimension and record source references and uncertainty.
3. Assign a score per dimension with explicit reasoning; do not fill missing evidence with an unstated default.
4. Apply the caller-supplied aggregation rule and preserve the dimension scores, composite score, and unresolved uncertainty.
5. Return the scored object and a traceable rationale.

## Output contract

```yaml
produces: [scored_object, dimension_scores, composite_score, evidence_links, uncertainty_record, rationale]
delta_fields: [findings, evidence_updates, decisions, uncertainties]
```

## Quality gates

- `Parameterization` is complete before scoring; the SOP does not own a shared rubric catalogue.
- Every dimension has a score, evidence reference, and explicit rationale; missing values remain visible.
- Preserve caller-supplied fixed scales and weights exactly. Source rubrics include importance 1–5 with 40%/30%/30% weights, feasibility 1–5 with four equal dimensions and bottlenecks at score ≤2, impact 1–5 with two equal dimensions, strength 0–10 bands, and obstacle overcomability classes 1 week/1 month/6 months/fundamental.
- For relative evidence gates, declare universe, numerator, denominator, batch increment, stopping reason, source references, direction, and threshold rationale; otherwise do not claim completion.

## Parameterization

The caller must provide: typed object schema and identifier; rubric dimensions and definitions; score scale and any fixed bands; weights or aggregation rule; missing-value and veto policy; evidence set and source references; uncertainty representation; and the output field names expected by the caller. The 15 absorbed v3 scoring rubrics remain caller-owned rather than a shared directory. This avoids false comparability across gaps, candidates, claims, and obstacles; the cost is explicit rubric repetition in each of the six calling tactics.

## Failure and counterexamples

Reject scoring when the object schema or rubric is incomplete, a dimension lacks evidence or rationale, aggregation is undefined, or a fixed source scale is silently changed. Do not collapse a claim-strength score into an importance score.

## Provenance map

- resolved: hypothesis-formation/importance-scoring
- resolved: hypothesis-formation/feasibility-scoring
- concept: hypothesis-formation/novelty-scoring
- resolved: hypothesis-formation/impact-scoring
- resolved: convergence/alternative-scoring
- concept: deep-insight/multi-criteria-scoring
- intermediate: Pass4/score-candidate
- concept: knowledge-structuring/novelty-scoring
- intermediate: Pass4/score-gap-novelty
- concept: knowledge-structuring/gap-prioritization
- resolved: knowledge-structuring/strength-scoring
- resolved: knowledge-structuring/strength-assessment
- intermediate: Pass4/score-claim-strength
- resolved: north-star-crystallization/assess-obstacle-severity
- intermediate: Pass4/assess-obstacle-severity

## Verbatim source criteria excerpts

- `importance-scoring` lines 22-24: Input must be a complete GapRecord; composite score lies in [1, 5]; each sub-dimension has at least 1 sentence of rationale.
- `importance-scoring` line 33: Composite score is weighted 40%/30%/30% across domain impact, theoretical contribution, and practical value, to one decimal place.
- `feasibility-scoring` lines 22-24: Input status is complete; composite score is [1, 5]; bottlenecks list exists.
- `feasibility-scoring` line 35: Four dimensions are equal-weighted; dimensions with score ≤ 2 are bottlenecks.
- `impact-scoring` lines 22-24: Input status is complete; composite score is [1, 5]; beneficiaries list has at least 1 beneficiary.
- `impact-scoring` lines 32-33: Breadth and depth are scored on 1-5 dimensions.
- `alternative-scoring` line 27: Scoring matrix has no empty values, each score has a one-sentence rationale, and quantitative criteria use actual data.
- `strength-scoring` lines 24-28: Strength bands are 0-2, 3-4, 5-6, 7-8, and 9-10; explicit reasoning is mandatory.
- `strength-assessment` line 19: Must score ≥3 claims per invocation.
- `assess-obstacle-severity` line 33: Overcomability is 1-week learnable / 1-month effort / 6-month investment / fundamental blocker.

## Preserved source criteria ledger

| source | physical line | kind | source criterion |
|---|---:|---|---|
| hypothesis-formation/importance-scoring | 14 | numeric/rubric | Input must be a GapRecord with status: complete; output composite score [1, 5]; each sub-dimension has at least 1 sentence of rationale. |
| hypothesis-formation/importance-scoring | 25 | numeric/rubric | Domain impact, theoretical contribution, and practical value are scored 1–5; weighted 40%/30%/30%, to one decimal place. |
| hypothesis-formation/feasibility-scoring | 14 | numeric/rubric | Composite score is [1, 5]; bottlenecks exist; four dimensions are equal-weighted; dimensions with score ≤2 are bottlenecks. |
| hypothesis-formation/impact-scoring | 14 | numeric/rubric | Composite score is [1, 5]; beneficiaries list is non-empty; breadth and depth are equal-weighted 1–5 dimensions. |
| convergence/alternative-scoring | 22 | gate | No empty score cells; every cell has one sentence of rationale; quantitative criteria use real data. |
| knowledge-structuring/strength-scoring | 17 | numeric/rubric | Strength score is 0–10 with bands 0–2, 3–4, 5–6, 7–8, 9–10; explicit reasoning is mandatory. |
| north-star-crystallization/assess-obstacle-severity | 12 | rubric | Overcomability classes are 1 week, 1 month, 6 months, or fundamental; include time cost and workaround status. |
