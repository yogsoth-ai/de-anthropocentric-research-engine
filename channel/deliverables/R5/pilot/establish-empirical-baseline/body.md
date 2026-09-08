# establish-empirical-baseline

## Purpose

Establish a fair empirical baseline by inventorying methods, extracting comparable performance, normalizing conditions/compute, checking discrepancies, and estimating progress/headroom.

## Input contract

```yaml
required: [method_records, benchmark_or_task, performance_measure]
optional: [historical_series, compute_metadata, condition_schema]
constraints: [comparability fields and source provenance required]
```

## Execution protocol

1. Inventory methods and define the comparison condition schema.
2. Extract performance data and normalize units, data, compute, and evaluation protocol.
3. Analyze discrepancies, progress trajectory, leaderboard state, and headroom.
4. Synthesize baseline with uncertainty and known incomparable records.

## Output contract

```yaml
produces: [method_inventory, normalized_baseline, discrepancy_report, progress_curve, headroom_estimate]
delta_fields: [findings, evidence_updates, uncertainties, decisions, open_questions]
```

## Thresholds and quality gates

- `method-inventory`: methods_discovered >= 40 (80% of target).
- `performance-extraction`: data_points >= 120 (80% of target).
- `condition-standardization`: data_points_standardized >= 48 (80% of target).
- `discrepancy-analysis`: score_pairs_compared >= 36 (80% of target).
- `progress-quantification`: historical_data_points >= 80 (80% of target).
- Normalization must expose condition, compute, metric, and unit transformations.

## Failure and counterexamples

Do not call a baseline fair when conditions are missing, metrics are incomparable, or leaderboard values are copied without protocol verification. Mark headroom unknown when the historical series is below its floor.

## Provenance map

9 architecture `old` entries: baseline, inventory, extraction, standardization, discrepancy, progress, leaderboard, normalization, curve construction. Repeated reporting prose compressed.

## Context checkpoint / Delta notes

Append method IDs, normalized records, excluded records with reasons, discrepancy pairs, progress model, and headroom uncertainty.

## Preserved source criteria ledger

| source | source line | kind | source criterion |
|---|---:|---|---|
| baseline-establishment | 28 | textual | \\| Check reproducibility / discrepancies \\| discrepancy-analysis \\| |
| baseline-establishment | 40 | textual | \\| discrepancy-analysis \\| Identify discrepancies between reported and reproducible scores \\| |
| baseline-establishment | 58 | textual | \\| reproducibility-checklist-audit \\| Assess paper against ML Reproducibility Checklist \\| |
| baseline-establishment | 70 | numeric-table | \\| method-inventory \\| 50 \\| 0 \\| 60 \\| |
| baseline-establishment | 71 | numeric-table | \\| performance-extraction \\| 30 \\| 150 \\| 40 \\| |
| baseline-establishment | 72 | numeric-table | \\| condition-standardization \\| 20 \\| 60 \\| 30 \\| |
| baseline-establishment | 73 | numeric-table | \\| discrepancy-analysis \\| 15 \\| 45 \\| 30 \\| |
| baseline-establishment | 74 | numeric-table | \\| progress-quantification \\| 30 \\| 100 \\| 40 \\| |
| baseline-establishment | 75 | numeric-table | \\| **TOTAL** \\| **145** \\| **355** \\| **200** \\| |
| method-inventory | 23 | numeric-table | \\| Methods discovered \\| 30 \\| 50 \\| |
| method-inventory | 24 | numeric-table | \\| Web searches \\| 40 \\| 60 \\| |
| method-inventory | 25 | numeric-table | \\| Papers consulted \\| 20 \\| 40 \\| |
| method-inventory | 30 | textual | <HARD-GATE> |
| method-inventory | 33 | numeric-table | \\| Methods discovered \\| 0 \\| 50 \\| BLOCKED \\| |
| method-inventory | 34 | numeric-table | \\| Web searches used \\| 0 \\| 60 \\| — \\| |
| method-inventory | 35 | numeric-table | \\| Papers consulted \\| 0 \\| 40 \\| — \\| |
| method-inventory | 36 | numeric-table | \\| Leaderboard sources \\| 0 \\| 5 \\| — \\| |
| method-inventory | 37 | numeric-table | \\| Citation chains traced \\| 0 \\| 10 \\| — \\| |
| method-inventory | 38 | textual | </HARD-GATE> |
| method-inventory | 41 | numeric | Cannot exit until methods_discovered >= 40 (80% of target). |
| performance-extraction | 18 | textual | Extract structured performance data from papers, leaderboards, and reproducibility studies. Each data point is a (Task, Dataset, Metric, Score, Conditions) tuple with full provenance. Prioritizes primary sources (original papers) but cross-references against leaderboards and third-party reproductions. |
| performance-extraction | 24 | numeric-table | \\| Methods covered \\| 20 \\| 30 \\| |
| performance-extraction | 25 | numeric-table | \\| Data points extracted \\| 100 \\| 150 \\| |
| performance-extraction | 26 | numeric-table | \\| Web searches \\| 25 \\| 40 \\| |
| performance-extraction | 27 | numeric-table | \\| Papers read \\| 15 \\| 30 \\| |
| performance-extraction | 32 | textual | <HARD-GATE> |
| performance-extraction | 35 | numeric-table | \\| Methods covered \\| 0 \\| 30 \\| BLOCKED \\| |
| performance-extraction | 36 | numeric-table | \\| Data points extracted \\| 0 \\| 150 \\| BLOCKED \\| |
| performance-extraction | 37 | numeric-table | \\| Web searches used \\| 0 \\| 40 \\| — \\| |
| performance-extraction | 38 | numeric-table | \\| Papers read \\| 0 \\| 30 \\| — \\| |
| performance-extraction | 39 | numeric-table | \\| Datasets covered \\| 0 \\| 5 \\| — \\| |
| performance-extraction | 40 | numeric-table | \\| Metrics tracked \\| 0 \\| 3 \\| — \\| |
| performance-extraction | 41 | textual | </HARD-GATE> |
| performance-extraction | 44 | numeric | Cannot exit until data_points >= 120 (80% of target). |
| condition-standardization | 25 | numeric-table | \\| Methods analyzed \\| 15 \\| 20 \\| |
| condition-standardization | 26 | numeric-table | \\| Data points standardized \\| 40 \\| 60 \\| |
| condition-standardization | 27 | numeric-table | \\| Web searches \\| 20 \\| 30 \\| |
| condition-standardization | 28 | numeric-table | \\| Condition dimensions cataloged \\| 5 \\| 10 \\| |
| condition-standardization | 33 | textual | <HARD-GATE> |
| condition-standardization | 36 | numeric-table | \\| Methods analyzed \\| 0 \\| 20 \\| BLOCKED \\| |
| condition-standardization | 37 | numeric-table | \\| Data points standardized \\| 0 \\| 60 \\| BLOCKED \\| |
| condition-standardization | 38 | numeric-table | \\| Condition dimensions \\| 0 \\| 10 \\| — \\| |
| condition-standardization | 39 | numeric-table | \\| Normalization rules defined \\| 0 \\| 5 \\| — \\| |
| condition-standardization | 40 | numeric-table | \\| Fair comparison sets \\| 0 \\| 3 \\| — \\| |
| condition-standardization | 41 | textual | </HARD-GATE> |
| condition-standardization | 44 | numeric | Cannot exit until data_points_standardized >= 48 (80% of target). |
| condition-standardization | 60 | textual | 3. Group methods by comparable condition sets |
| condition-standardization | 63 | textual | 6. Produce fair comparison subsets where conditions are controlled |
| discrepancy-analysis | 24 | numeric-table | \\| Methods analyzed \\| 10 \\| 15 \\| |
| discrepancy-analysis | 25 | numeric-table | \\| Data points compared \\| 30 \\| 45 \\| |
| discrepancy-analysis | 26 | numeric-table | \\| Web searches \\| 20 \\| 30 \\| |
| discrepancy-analysis | 27 | numeric-table | \\| Reproduction studies consulted \\| 5 \\| 10 \\| |
| discrepancy-analysis | 32 | textual | <HARD-GATE> |
| discrepancy-analysis | 35 | numeric-table | \\| Methods analyzed \\| 0 \\| 15 \\| BLOCKED \\| |
| discrepancy-analysis | 36 | numeric-table | \\| Score pairs compared \\| 0 \\| 45 \\| BLOCKED \\| |
| discrepancy-analysis | 37 | numeric-table | \\| Discrepancies flagged \\| 0 \\| — \\| — \\| |
| discrepancy-analysis | 38 | numeric-table | \\| Reproduction studies found \\| 0 \\| 10 \\| — \\| |
| discrepancy-analysis | 39 | numeric-table | \\| Reliability ratings assigned \\| 0 \\| 15 \\| — \\| |
| discrepancy-analysis | 40 | textual | </HARD-GATE> |
| discrepancy-analysis | 43 | numeric | Cannot exit until score_pairs_compared >= 36 (80% of target). |
| discrepancy-analysis | 52 | textual | - **reproducibility-checklist-audit** — Assess paper reproducibility completeness |
| discrepancy-analysis | 59 | textual | 4. Apply reproducibility-checklist-audit to papers with large discrepancies |
| discrepancy-analysis | 85 | textual | "reproducibility_checklist_score": 0, |
| progress-quantification | 26 | numeric-table | \\| Methods tracked \\| 20 \\| 30 \\| |
| progress-quantification | 27 | numeric-table | \\| Historical data points \\| 70 \\| 100 \\| |
| progress-quantification | 28 | numeric-table | \\| Web searches \\| 25 \\| 40 \\| |
| progress-quantification | 29 | numeric-table | \\| Time span covered (years) \\| 3 \\| 5+ \\| |
| progress-quantification | 34 | textual | <HARD-GATE> |
| progress-quantification | 37 | numeric-table | \\| Methods tracked \\| 0 \\| 30 \\| BLOCKED \\| |
| progress-quantification | 38 | numeric-table | \\| Historical data points \\| 0 \\| 100 \\| BLOCKED \\| |
| progress-quantification | 39 | numeric-table | \\| Web searches used \\| 0 \\| 40 \\| — \\| |
| progress-quantification | 40 | numeric-table | \\| Progress curves built \\| 0 \\| 3 \\| — \\| |
| progress-quantification | 41 | numeric-table | \\| Headroom estimates \\| 0 \\| 3 \\| — \\| |
| progress-quantification | 42 | numeric-table | \\| Inflection points identified \\| 0 \\| 2 \\| — \\| |
| progress-quantification | 43 | textual | </HARD-GATE> |
| progress-quantification | 46 | numeric | Cannot exit until historical_data_points >= 80 (80% of target). |
| leaderboard-harvesting | 43 | numeric | - Flag discrepancies > 1 standard deviation |
| leaderboard-harvesting | 58 | textual | ## Minimum Yield |
| leaderboard-harvesting | 62 | numeric-table | \\| Leaderboard sources checked \\| 3 \\| |
| leaderboard-harvesting | 63 | numeric-table | \\| Methods with scores \\| 15 \\| |
| leaderboard-harvesting | 64 | numeric-table | \\| Cross-validated score pairs \\| 10 \\| |
| leaderboard-harvesting | 65 | numeric-table | \\| Deduplication conflicts resolved \\| 5 \\| |
| condition-normalization | 28 | textual | - Random seeds: number of runs, seed selection, variance reported |
| condition-normalization | 51 | textual | ### Stage 4: Fair Comparison Baseline |
| condition-normalization | 53 | textual | Apply normalization to produce fair comparison subsets: |
| condition-normalization | 58 | textual | **Yield**: Fair comparison tables with methodology notes. |
| condition-normalization | 60 | textual | ## Minimum Yield |
| condition-normalization | 64 | numeric-table | \\| Condition dimensions cataloged \\| 5 \\| |
| condition-normalization | 65 | numeric-table | \\| Methods with full condition vectors \\| 10 \\| |
| condition-normalization | 66 | numeric-table | \\| Normalization rules defined \\| 3 \\| |
| condition-normalization | 67 | numeric-table | \\| Fair comparison sets produced \\| 2 \\| |
| progress-curve-construction | 62 | textual | ## Minimum Yield |
| progress-curve-construction | 66 | numeric-table | \\| Progress curves constructed \\| 2 \\| |
| progress-curve-construction | 67 | numeric-table | \\| Years of history covered \\| 3 \\| |
| progress-curve-construction | 68 | numeric-table | \\| Inflection points identified \\| 1 \\| |
| progress-curve-construction | 69 | numeric-table | \\| Headroom estimates produced \\| 2 \\| |
| progress-curve-construction | 73 | numeric | - progress-curve-fitting (for Stages 2-3) |
