# synthesize-meta-analytic-evidence

## Purpose

Design or execute quantitative evidence synthesis while preserving study-level quality, heterogeneity, bias, and sensitivity logic.

## When to use / not applicable

Use when multiple studies or comparable effect estimates must be combined. Not applicable when evidence is a single case or no comparable outcome can be defined.

## Input contract

```yaml
required: [study_records, outcome_definition, effect_measure]
optional: [comparison_network, subgroup_plan, prior_quality_assessments]
constraints: [study-level provenance required]
```

## Execution protocol

1. Define outcome, effect measure, inclusion boundary, and study-level quality fields.
2. Extract or calculate effect sizes and record condition, sample, uncertainty, and provenance.
3. Select one mode: pairwise, network, cumulative, heterogeneity, or bias.
4. Run sensitivity checks and synthesize estimates with uncertainty and exclusions.

## Mode branches

- `pairwise`: combine direct comparisons.
- `network`: compare N>=3 methods using direct and indirect evidence.
- `cumulative`: update the estimate as studies arrive; retain order and stopping state.
- `heterogeneity`: investigate between-study variation; preserve I2 interpretation bands.
- `bias`: test publication, selection, and small-study bias; do not treat absence of evidence as absence of bias.

## Output contract

```yaml
produces: [effect_estimate, uncertainty, heterogeneity_report, bias_report, sensitivity_results]
delta_fields: [findings, evidence_updates, uncertainties, decisions, open_questions]
```

## Thresholds and quality gates

- Budget gate: source pairwise/network/cumulative/heterogeneity/bias SOPs cannot exit until 80% of the declared floor is met.
- `effect-size-extraction`: at least 5 studies processed and at least 5 effect sizes extracted or calculation planned.
- `quality-assessment-protocol`: at least 5 studies assessed.
- If k >= 10, pre-specified subgroup/meta-regression investigation is required where applicable.
- I2 interpretation bands are retained: 0-40% low, 30-60% moderate, 50-90% substantial, 75-100% considerable; overlaps are source wording and must not be silently normalized.

## Failure and counterexamples

Reject synthesis when study identity, outcome definition, or effect measure is missing. Flag disconnected network, incomparable conditions, unplanned subgrouping, and bias tests with insufficient studies.

## Provenance map

`meta-analysis`, `pairwise-synthesis`, `network-comparison`, `cumulative-tracking`, `heterogeneity-investigation`, `bias-detection`, `effect-size-extraction`, `quality-assessment-protocol`, `evidence-synthesis-planning`; all source gates kept, repeated provider details compressed.

## Context checkpoint / Delta notes

Append study set, extraction table, estimate, uncertainty, heterogeneity/bias decisions, and unresolved comparability questions.

## Preserved source criteria ledger

| source | source line | kind | source criterion |
|---|---:|---|---|
| meta-analysis | 29 | numeric | \\| Multi-method comparison \\| network-comparison \\| Comparing N>=3 methods with indirect evidence \\| |
| meta-analysis | 62 | numeric-table | \\| risk-of-bias-assessment \\| Assess methodological bias (RoB2/PROBAST/QUADAS-2) \\| |
| meta-analysis | 73 | numeric-table | \\| pairwise-synthesis \\| 30 \\| 30 \\| 40 \\| |
| meta-analysis | 74 | numeric-table | \\| network-comparison \\| 50 \\| 80 \\| 60 \\| |
| meta-analysis | 75 | numeric-table | \\| cumulative-tracking \\| 40 \\| 40 \\| 30 \\| |
| meta-analysis | 76 | numeric-table | \\| heterogeneity-investigation \\| 30 \\| 30 \\| 50 \\| |
| meta-analysis | 77 | numeric-table | \\| bias-detection \\| 40 \\| 40 \\| 40 \\| |
| pairwise-synthesis | 33 | numeric-table | \\| Studies identified \\| 20 \\| 30 \\| |
| pairwise-synthesis | 34 | numeric-table | \\| Effect sizes extracted \\| 20 \\| 30 \\| |
| pairwise-synthesis | 35 | numeric-table | \\| Web searches \\| 25 \\| 40 \\| |
| pairwise-synthesis | 36 | numeric-table | \\| Quality assessments \\| 15 \\| 30 \\| |
| pairwise-synthesis | 38 | numeric | Budget gate: cannot exit until 80% of floor met. |
| pairwise-synthesis | 43 | textual | <HARD-GATE> |
| pairwise-synthesis | 46 | numeric-table | \\| Studies found \\| 0 \\| 20 \\| 30 \\| BLOCKED \\| |
| pairwise-synthesis | 47 | numeric-table | \\| Effect sizes planned \\| 0 \\| 20 \\| 30 \\| BLOCKED \\| |
| pairwise-synthesis | 48 | numeric-table | \\| Web searches done \\| 0 \\| 25 \\| 40 \\| BLOCKED \\| |
| pairwise-synthesis | 49 | numeric-table | \\| Quality assessed \\| 0 \\| 15 \\| 30 \\| BLOCKED \\| |
| pairwise-synthesis | 50 | textual | </HARD-GATE> |
| pairwise-synthesis | 84 | numeric | Iterate steps 3-5 until budget floor is met. Check state ledger before each iteration. |
| network-comparison | 25 | numeric | Design a network meta-analysis (NMA) protocol comparing N>=3 methods simultaneously, leveraging both direct and indirect evidence. |
| network-comparison | 35 | numeric-table | \\| Studies identified \\| 35 \\| 50 \\| |
| network-comparison | 36 | numeric-table | \\| Effect sizes extracted \\| 55 \\| 80 \\| |
| network-comparison | 37 | numeric-table | \\| Web searches \\| 40 \\| 60 \\| |
| network-comparison | 38 | numeric-table | \\| Network nodes (methods) \\| 3 \\| N \\| |
| network-comparison | 39 | numeric-table | \\| Quality assessments \\| 25 \\| 50 \\| |
| network-comparison | 41 | numeric | Budget gate: cannot exit until 80% of floor met. |
| network-comparison | 46 | textual | <HARD-GATE> |
| network-comparison | 49 | numeric-table | \\| Studies found \\| 0 \\| 35 \\| 50 \\| BLOCKED \\| |
| network-comparison | 50 | numeric-table | \\| Effect sizes planned \\| 0 \\| 55 \\| 80 \\| BLOCKED \\| |
| network-comparison | 51 | numeric-table | \\| Web searches done \\| 0 \\| 40 \\| 60 \\| BLOCKED \\| |
| network-comparison | 52 | numeric-table | \\| Network nodes \\| 0 \\| 3 \\| N \\| BLOCKED \\| |
| network-comparison | 53 | numeric-table | \\| Quality assessed \\| 0 \\| 25 \\| 50 \\| BLOCKED \\| |
| network-comparison | 54 | textual | </HARD-GATE> |
| network-comparison | 92 | numeric | Iterate steps 3-6 until budget floor met. Verify network connectivity after each batch. |
| cumulative-tracking | 34 | numeric-table | \\| Studies identified \\| 28 \\| 40 \\| |
| cumulative-tracking | 35 | numeric-table | \\| Effect sizes extracted \\| 28 \\| 40 \\| |
| cumulative-tracking | 36 | numeric-table | \\| Web searches \\| 20 \\| 30 \\| |
| cumulative-tracking | 37 | numeric-table | \\| Temporal coverage (years) \\| 5 \\| 10+ \\| |
| cumulative-tracking | 38 | numeric-table | \\| Quality assessments \\| 20 \\| 40 \\| |
| cumulative-tracking | 40 | numeric | Budget gate: cannot exit until 80% of floor met. |
| cumulative-tracking | 45 | textual | <HARD-GATE> |
| cumulative-tracking | 48 | numeric-table | \\| Studies found \\| 0 \\| 28 \\| 40 \\| BLOCKED \\| |
| cumulative-tracking | 49 | numeric-table | \\| Effect sizes planned \\| 0 \\| 28 \\| 40 \\| BLOCKED \\| |
| cumulative-tracking | 50 | numeric-table | \\| Web searches done \\| 0 \\| 20 \\| 30 \\| BLOCKED \\| |
| cumulative-tracking | 51 | numeric-table | \\| Year range covered \\| 0 \\| 5 \\| 10+ \\| BLOCKED \\| |
| cumulative-tracking | 52 | numeric-table | \\| Quality assessed \\| 0 \\| 20 \\| 40 \\| BLOCKED \\| |
| cumulative-tracking | 53 | textual | </HARD-GATE> |
| heterogeneity-investigation | 28 | numeric | When a meta-analysis reveals substantial heterogeneity (I2 > 50%, significant Q-test, large tau2), this strategy designs the investigation protocol: subgroup analyses, meta-regression, moderator identification, and outlier diagnostics. Produces the investigation plan, not the computation. |
| heterogeneity-investigation | 34 | numeric-table | \\| Studies identified \\| 20 \\| 30 \\| |
| heterogeneity-investigation | 35 | numeric-table | \\| Effect sizes extracted \\| 20 \\| 30 \\| |
| heterogeneity-investigation | 36 | numeric-table | \\| Web searches \\| 35 \\| 50 \\| |
| heterogeneity-investigation | 37 | numeric-table | \\| Moderator candidates \\| 5 \\| 10+ \\| |
| heterogeneity-investigation | 38 | numeric-table | \\| Quality assessments \\| 15 \\| 30 \\| |
| heterogeneity-investigation | 40 | numeric | Budget gate: cannot exit until 80% of floor met. |
| heterogeneity-investigation | 45 | textual | <HARD-GATE> |
| heterogeneity-investigation | 48 | numeric-table | \\| Studies found \\| 0 \\| 20 \\| 30 \\| BLOCKED \\| |
| heterogeneity-investigation | 49 | numeric-table | \\| Effect sizes planned \\| 0 \\| 20 \\| 30 \\| BLOCKED \\| |
| heterogeneity-investigation | 50 | numeric-table | \\| Web searches done \\| 0 \\| 35 \\| 50 \\| BLOCKED \\| |
| heterogeneity-investigation | 51 | numeric-table | \\| Moderators identified \\| 0 \\| 5 \\| 10+ \\| BLOCKED \\| |
| heterogeneity-investigation | 52 | numeric-table | \\| Quality assessed \\| 0 \\| 15 \\| 30 \\| BLOCKED \\| |
| heterogeneity-investigation | 53 | textual | </HARD-GATE> |
| heterogeneity-investigation | 70 | textual | \\| effect-size-planning \\| Standardize for comparability \\| |
| bias-detection | 35 | numeric-table | \\| Studies identified \\| 28 \\| 40 \\| |
| bias-detection | 36 | numeric-table | \\| Effect sizes extracted \\| 28 \\| 40 \\| |
| bias-detection | 37 | numeric-table | \\| Web searches \\| 28 \\| 40 \\| |
| bias-detection | 38 | numeric-table | \\| Bias domains assessed \\| 5 \\| 8 \\| |
| bias-detection | 39 | numeric-table | \\| Quality assessments \\| 20 \\| 40 \\| |
| bias-detection | 41 | numeric | Budget gate: cannot exit until 80% of floor met. |
| bias-detection | 46 | textual | <HARD-GATE> |
| bias-detection | 49 | numeric-table | \\| Studies found \\| 0 \\| 28 \\| 40 \\| BLOCKED \\| |
| bias-detection | 50 | numeric-table | \\| Effect sizes planned \\| 0 \\| 28 \\| 40 \\| BLOCKED \\| |
| bias-detection | 51 | numeric-table | \\| Web searches done \\| 0 \\| 28 \\| 40 \\| BLOCKED \\| |
| bias-detection | 52 | numeric-table | \\| Bias domains assessed \\| 0 \\| 5 \\| 8 \\| BLOCKED \\| |
| bias-detection | 53 | numeric-table | \\| Quality assessed \\| 0 \\| 20 \\| 40 \\| BLOCKED \\| |
| bias-detection | 54 | textual | </HARD-GATE> |
| bias-detection | 62 | numeric-table | \\| quality-assessment-protocol \\| Full RoB2 assessment per study \\| |
| effect-size-extraction | 77 | textual | ## Minimum Yield |
| effect-size-extraction | 80 | numeric | - At least 5 studies processed |
| effect-size-extraction | 81 | numeric | - At least 5 effect sizes extracted or calculation planned |
| quality-assessment-protocol | 24 | numeric-table | \\| RCT \\| RoB 2.0 \\| Randomization, deviations, missing data, measurement, selection \\| |
| quality-assessment-protocol | 26 | numeric-table | \\| Diagnostic accuracy \\| QUADAS-2 \\| Patient selection, index test, reference standard, flow/timing \\| |
| quality-assessment-protocol | 28 | textual | \\| Observational \\| Newcastle-Ottawa \\| Selection, comparability, outcome/exposure \\| |
| quality-assessment-protocol | 56 | textual | ## Minimum Yield |
| quality-assessment-protocol | 59 | numeric | - At least 5 studies assessed |
| evidence-synthesis-planning | 41 | numeric | - **Knapp-Hartung adjustment**: recommended when k < 20 studies |
| evidence-synthesis-planning | 51 | numeric | - **Investigation**: pre-specified subgroups, meta-regression (if k >= 10) |
| evidence-synthesis-planning | 52 | numeric | - **Thresholds**: I2 interpretation (0-40% low, 30-60% moderate, 50-90% substantial, 75-100% considerable) |
| evidence-synthesis-planning | 80 | textual | ## Minimum Yield |
| evidence-synthesis-planning | 86 | numeric | - At least 3 sensitivity analyses designed |
