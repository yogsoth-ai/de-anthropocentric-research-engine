# rank-candidates

## Purpose

Rank, classify, screen, or select typed candidates under explicit criteria and hard constraints.

## Input contract

```yaml
required: [candidates, criteria, decision_rule]
optional: [weights, evidence, hard_constraints, object_schema]
constraints: [criterion direction and missing-value policy explicit]
```

## Execution protocol

1. Normalize candidate and criterion schemas; separate hard constraints from preferences.
2. Select `gap-prioritization`, `direction-selection`, `mcda-best-choice`, `full-ranking`, `category-sorting`, `non-compensatory-screening`, `rapid-triage`, or `stakeholder-weighted`.
3. Elicit/validate weights, score with evidence, aggregate or apply veto/threshold rules.
4. Run sensitivity scenarios and return ordered or categorized candidates with rationale.

## Output contract

```yaml
produces: [ranking_or_categories, scores, weights, eliminated_candidates, sensitivity_results, recommendation]
delta_fields: [findings, decisions, uncertainties, recommended_jumps]
```

## Thresholds and quality gates

- Full ranking: select >=2 ranking methods when the source protocol calls for method comparison.
- Weight elicitation: select >=2 weighting methods where required.
- Priority sensitivity: perturbation scenarios cover the declared weight space at a justified relative floor, each scenario annotated; retain the observed ranking-stability verdict.
- Direction narrowing imports report candidate/evidence-pool coverage, full-text coverage, independent-source ratio, batch increment, stopping reason, and source references rather than fixed paper/page counts.
- For every relative gate, declare the eligible candidate/evidence universe (denominator) and record the covered candidates or evidence items (numerator), the batch increment, the stopping reason, and source references; a gate is not passable when any audit field is missing.
- Stop direction search when marginal information gain falls below the justified floor across batches; report the resulting saturation state alongside coverage ratio and independent-source ratio.
- Non-compensatory and category modes must expose threshold/veto values; never hide them in prose.

## Failure and counterexamples

Reject rankings with undefined criterion direction, unhandled missing values, or hard constraints treated as compensable scores. Do not collapse pairwise active ranking into scalar ranking.

## Provenance map

20 architecture `old` entries; shared criteria→score→aggregate kernel retained. Portfolio and pairwise operations remain separate nodes, not silently absorbed.

## Context checkpoint / Delta notes

Append candidate set hash, criteria/weights, rule, ranking, sensitivity scenarios, exclusions, and unresolved trade-offs.

## Preserved source criteria ledger

| source | source line | kind | source criterion |
|---|---:|---|---|
| multi-criteria-ranking | 49 | numeric | Each dimension is scored independently (1–5) to avoid cross-contamination between dimensions. Weights are set by AHP (Analytic Hierarchy Process) or specified by the user. Final score = Σ(dimension score × dimension weight). |
| multi-criteria-ranking | 51 | numeric | **Sensitivity check**: perturb weights by ±20%; if the ranking is unchanged the conclusion is robust; if the ranking flips it must be flagged as "weight-sensitive". |
| multi-criteria-ranking | 53 | textual | ## Budget Gate |
| multi-criteria-ranking | 57 | numeric | \\| S \\| 5–8 \\| ≥3 dimensions \\| Optional \\| Ranking table + attack suggestions for top 2 gaps \\| |
| multi-criteria-ranking | 58 | numeric | \\| M \\| 9–15 \\| ≥4 dimensions \\| Required \\| Ranking table + attack suggestions for top 3 gaps \\| |
| multi-criteria-ranking | 59 | numeric | \\| L \\| 16–20 \\| ≥5 dimensions \\| Required (multi-weight scenarios) \\| Ranking table + attack suggestions for top 5 gaps + weight-sensitivity report \\| |
| evidence-based-prioritization | 51 | textual | ## Budget Gate |
| evidence-based-prioritization | 55 | numeric | \\| S \\| 3–8 \\| all 6 dimensions \\| ≥2 supporting references per gap \\| ranking table + evidence-void report \\| |
| evidence-based-prioritization | 56 | numeric | \\| M \\| 9–15 \\| all 6 dimensions \\| ≥3 supporting references per gap \\| ranking table + evidence-void report + attack suggestions for top 3 gaps \\| |
| evidence-based-prioritization | 57 | numeric | \\| L \\| 16–20 \\| all 6 dimensions \\| ≥5 supporting references per gap \\| ranking table + detailed evidence map + attack suggestions for top 5 gaps \\| |
| stakeholder-weighted-ranking | 35 | textual | - A consensus must be built across parties, or the ranking differences across perspectives must be shown |
| stakeholder-weighted-ranking | 58 | textual | ## Budget Gate |
| stakeholder-weighted-ranking | 62 | numeric | \\| S \\| 5–10 \\| 2–3 classes \\| Simple average \\| Per-perspective rankings + consensus top-3 \\| |
| stakeholder-weighted-ranking | 63 | numeric | \\| M \\| 11–20 \\| 3–5 classes \\| Borda count \\| Per-perspective rankings + consensus top-5 + divergence analysis \\| |
| stakeholder-weighted-ranking | 64 | numeric-table | \\| L \\| 20+ \\| 5+ classes \\| Weighted Borda + sensitivity \\| Full perspective matrix + consensus ranking + divergence heatmap \\| |
| rapid-triage | 49 | numeric | **Round 2: light scoring (1–3 points, two dimensions)** |
| rapid-triage | 51 | numeric | - Importance (1–3): a rough estimate of field impact |
| rapid-triage | 52 | numeric | - Feasibility (1–3): whether progress can be made within 6 months with existing resources |
| rapid-triage | 56 | textual | **Key insight**: the three round-1 questions must be answered quickly (no more than 30 seconds per gap); no deep analysis allowed. Speed is the core value of this strategy. |
| rapid-triage | 58 | textual | ## Budget Gate |
| rapid-triage | 60 | numeric-table | \\| Tier \\| Input gap count \\| Round-1 retention rate \\| Round-2 output \\| Final output \\| |
| rapid-triage | 62 | numeric | \\| S \\| 50–80 \\| ≤60% \\| top-15 \\| Candidate set + elimination-rationale summary \\| |
| rapid-triage | 63 | numeric | \\| M \\| 81–150 \\| ≤50% \\| top-20 \\| Candidate set + elimination-rationale summary \\| |
| rapid-triage | 64 | numeric | \\| L \\| 150+ \\| ≤40% \\| top-30 \\| Candidate set + elimination-rationale summary + category statistics \\| |
| rapid-triage | 71 | numeric | 4. Call the `importance-scoring` SOP on the Keep set (1–3 coarse score) |
| rapid-triage | 72 | numeric | 5. Call the `feasibility-scoring` SOP on the Keep set (1–3 coarse score) |
| priority-sensitivity-testing | 28 | numeric | This tactic first establishes baseline weights (AHP or equal weights), then systematically perturbs the weights (±20%), observes the ranking changes, and finally gives a stability verdict. |
| priority-sensitivity-testing | 35 | numeric | \\| weight-perturbation \\| Apply ±20% perturbations to each dimension weight and recompute the ranking \\| Second step, systematic perturbation \\| |
| priority-sensitivity-testing | 42 | numeric | 2. weight-perturbation: apply +20% and -20% perturbations to each dimension in turn (the remaining dimensions are adjusted proportionally to keep the sum at 1), producing a ranking for each perturbation scenario |
| priority-sensitivity-testing | 47 | numeric | - Perturb only the highest-weight dimension (±20%), producing 2 perturbation scenarios |
| priority-sensitivity-testing | 52 | numeric | - weight-perturbation expands the perturbation range to ±30% and adds extreme scenarios (one dimension's weight set to 0) |
| priority-sensitivity-testing | 55 | textual | ## Minimum Yield |
| priority-sensitivity-testing | 58 | numeric | - Ranking results for at least 3 perturbation scenarios (each scenario annotated with its perturbation content) |
| priority-sensitivity-testing | 60 | numeric | - A final stability verdict: **Stable** (top N unchanged across all scenarios) / **Partially Sensitive** (1-2 changes in the top N) / **Highly Sensitive** (more than 2 changes in the top N) |
| best-option-selection | 17 | numeric | - Moderate number of candidates (3-15) |
| best-option-selection | 21 | numeric | \\| Base SOP \\| Target \\| ±10% Range \\| |
| best-option-selection | 23 | numeric | \\| criterion-definition \\| 5-8 criteria \\| 4-9 \\| |
| best-option-selection | 24 | numeric-table | \\| weight-elicitation-sop \\| 1 weight vector \\| 1 \\| |
| best-option-selection | 25 | numeric-table | \\| alternative-scoring \\| 1 score matrix \\| 1 \\| |
| best-option-selection | 26 | numeric-table | \\| normalization \\| 1 normalized matrix \\| 1 \\| |
| best-option-selection | 27 | numeric-table | \\| scoring-synthesis \\| 1 recommendation \\| 1 \\| |
| full-ranking | 22 | numeric | \\| Base SOP \\| Target \\| ±10% Range \\| |
| full-ranking | 24 | numeric | \\| criterion-definition \\| 5-8 criteria \\| 4-9 \\| |
| full-ranking | 25 | numeric-table | \\| weight-elicitation-sop \\| 1 weight vector \\| 1 \\| |
| full-ranking | 26 | numeric-table | \\| alternative-scoring \\| 1 score matrix \\| 1 \\| |
| full-ranking | 27 | numeric-table | \\| normalization \\| 1 normalized matrix \\| 1 \\| |
| full-ranking | 28 | numeric-table | \\| rank-comparison \\| 1 agreement matrix \\| 1 \\| |
| full-ranking | 29 | numeric-table | \\| scoring-synthesis \\| 1 full ranking \\| 1 \\| |
| full-ranking | 64 | numeric | 2. Select >=2 ranking methods (recommended: PROMETHEE II + MAVT) |
| full-ranking | 66 | textual | 4. Pay attention to incomparable pairs in partial orders (specific to ELECTRE III) |
| category-sorting | 22 | numeric | \\| Base SOP \\| Target \\| ±10% Range \\| |
| category-sorting | 24 | numeric | \\| criterion-definition \\| 5-8 criteria \\| 4-9 \\| |
| category-sorting | 25 | numeric-table | \\| weight-elicitation-sop \\| 1 weight vector \\| 1 \\| |
| category-sorting | 26 | numeric-table | \\| threshold-setting \\| 1 threshold set \\| 1 \\| |
| category-sorting | 27 | numeric-table | \\| alternative-scoring \\| 1 score matrix \\| 1 \\| |
| category-sorting | 28 | numeric-table | \\| scoring-synthesis \\| 1 classification \\| 1 \\| |
| non-compensatory-screening | 27 | numeric | \\| Base SOP \\| Target \\| ±10% Range \\| |
| non-compensatory-screening | 29 | numeric | \\| criterion-definition \\| 3-5 screening criteria \\| 2-6 \\| |
| non-compensatory-screening | 30 | numeric-table | \\| threshold-setting \\| 1 threshold set \\| 1 \\| |
| non-compensatory-screening | 31 | numeric-table | \\| conjunctive-filter \\| 1 pass/fail list \\| 1 \\| |
| non-compensatory-screening | 32 | numeric-table | \\| dominance-check \\| 1 dominance report \\| 1 \\| |
| non-compensatory-screening | 65 | textual | 2. Invoke threshold-setting to define minimum thresholds for each criterion |
| non-compensatory-screening | 75 | textual | **Screening Rule:** Conjunctive rule (all criteria must be met) |
| weight-elicitation | 23 | numeric | \\| Base SOP \\| Target \\| ±10% Range \\| |
| weight-elicitation | 25 | numeric | \\| criterion-definition \\| 5-8 criteria \\| 4-9 \\| |
| weight-elicitation | 26 | numeric | \\| weight-elicitation-sop \\| ≥2 methods \\| 2-3 \\| |
| weight-elicitation | 27 | numeric-table | \\| rank-comparison \\| 1 comparison \\| 1 \\| |
| weight-elicitation | 60 | numeric | 2. Select >=2 weighting methods (recommended: AHP + BWM or Swing + Simos) |
| weight-elicitation | 76 | numeric | - AHP CR: [value] (< 0.1 ✓) |
| direction-narrowing | 36 | numeric | - `broad-paper-search`: at least 80 papers scanned |
| direction-narrowing | 37 | numeric | - `deep-web-search`: at least 30 web pages read in full |
| present-and-ask | 29 | numeric | User's selected 1-2 fields of interest + reasoning. |
