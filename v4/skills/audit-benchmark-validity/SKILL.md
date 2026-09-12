---
name: audit-benchmark-validity
description: "Treat benchmarks as scientific measurement instruments: audit construct validity, contamination, metric pathology, coverage, leaderboard dynamics, and protocol drift."
---

# audit-benchmark-validity

## Purpose

Treat benchmarks as scientific measurement instruments: audit construct validity, contamination, metric pathology, coverage, leaderboard dynamics, and protocol drift.

## Input contract

```yaml
required: [benchmark_spec, task_definition, metric_definition, evaluation_records]
optional: [leaderboard_history, protocol_versions, coverage_target]
constraints: [claims must be linked to benchmark evidence]
```

## Execution protocol

1. Reconstruct benchmark construct, task boundary, metric, data coverage, and protocol versions.
2. Select validity, contamination, saturation, coverage, protocol-forensics, or evaluation-comparison mode.
3. Probe artifacts and shortcut paths; compare protocol/metric variants.
4. Return validity verdict with threats, evidence, and required repairs.

## Output contract

```yaml
produces: [validity_verdict, threat_register, contamination_findings, coverage_map, protocol_drift_report, repair_actions]
delta_fields: [findings, evidence_updates, uncertainties, decisions, open_questions, recommended_jumps]
```

## Thresholds and quality gates

- Every source HARD-GATE remains mandatory; no exit with an untested construct, contamination path, metric pathology, coverage claim, or protocol change.
- Resource and sampling gates use relative benchmark/target/evidence coverage rather than fixed benchmark, paper, or web counts. Declare the eligible universe, record numerator, denominator, batch increment, stopping reason, and source references.
- Saturation claims require an explicit stopping criterion and evidence that additional search/testing no longer changes the conclusion; report marginal information gain and saturation state.
- BetterBench-style criterion lists remain content checklists. Their item count is not converted into a percentage; the audit reports criterion coverage ratio over the declared applicable set and an independent-source ratio.
- Evaluation comparisons must state the controlled protocol difference and its expected impact.

## Failure and counterexamples

Reject “valid” when benchmark artifact probes are absent, contamination is unknown but ignored, or leaderboard gains cannot be separated from protocol drift. A high score is not evidence of construct validity by itself.

## Provenance map

7 architecture `old` entries: archaeology, audit, saturation, validity probing, coverage mapping, protocol forensics, evaluation comparison. Provider-specific retrieval compressed.

## Context checkpoint / Delta notes

Append benchmark version, construct claims, probes, contamination evidence, coverage gaps, protocol diffs, verdict, and repair decisions.

## Preserved source criteria ledger

| source | source line | kind | source criterion |
|---|---:|---|---|
| benchmark-archaeology | 39 | numeric-table | \\| benchmark-audit \\| Systematic quality assessment using BetterBench 46-criterion framework \\| |
| benchmark-archaeology | 72 | numeric-table | \\| benchmark-audit \\| 5 \\| 30 \\| 40 \\| |
| benchmark-archaeology | 73 | numeric-table | \\| saturation-analysis \\| 15 \\| 50 \\| 60 \\| |
| benchmark-archaeology | 74 | numeric-table | \\| validity-probing \\| 3 \\| 40 \\| 30 \\| |
| benchmark-archaeology | 75 | numeric-table | \\| coverage-mapping \\| 20 \\| 30 \\| 50 \\| |
| benchmark-archaeology | 76 | numeric-table | \\| protocol-forensics \\| 5 \\| 60 \\| 30 \\| |
| benchmark-archaeology | 77 | numeric-table | \\| **Total** \\| **48** \\| **210** \\| **210** \\| |
| benchmark-audit | 28 | numeric-table | \\| Benchmarks audited \\| 3 \\| 5 \\| |
| benchmark-audit | 29 | numeric-table | \\| Papers read \\| 20 \\| 30 \\| |
| benchmark-audit | 30 | numeric-table | \\| Web searches \\| 25 \\| 40 \\| |
| benchmark-audit | 35 | textual | <HARD-GATE> |
| benchmark-audit | 38 | numeric-table | \\| Benchmarks audited \\| 0 \\| 5 \\| PENDING \\| |
| benchmark-audit | 39 | numeric-table | \\| Papers fetched \\| 0 \\| 30 \\| PENDING \\| |
| benchmark-audit | 40 | numeric-table | \\| Papers read \\| 0 \\| 20 \\| PENDING \\| |
| benchmark-audit | 41 | numeric-table | \\| Web searches \\| 0 \\| 40 \\| PENDING \\| |
| benchmark-audit | 42 | numeric-table | \\| Documentation audits complete \\| 0 \\| 5 \\| PENDING \\| |
| benchmark-audit | 43 | numeric-table | \\| Metric decompositions complete \\| 0 \\| 5 \\| PENDING \\| |
| benchmark-audit | 44 | numeric-table | \\| Contamination checks complete \\| 0 \\| 5 \\| PENDING \\| |
| benchmark-audit | 45 | numeric-table | \\| Synthesis reports produced \\| 0 \\| 5 \\| PENDING \\| |
| benchmark-audit | 46 | textual | </HARD-GATE> |
| benchmark-audit | 49 | numeric | Cannot exit until 80% of all targets met. |
| benchmark-audit | 81 | numeric | betterbench_score: float  # 0-1, proportion of 46 criteria met |
| saturation-analysis | 28 | numeric-table | \\| Benchmarks analyzed \\| 10 \\| 15 \\| |
| saturation-analysis | 29 | numeric-table | \\| Papers read \\| 35 \\| 50 \\| |
| saturation-analysis | 30 | numeric-table | \\| Web searches \\| 40 \\| 60 \\| |
| saturation-analysis | 35 | textual | <HARD-GATE> |
| saturation-analysis | 38 | numeric-table | \\| Benchmarks analyzed \\| 0 \\| 15 \\| PENDING \\| |
| saturation-analysis | 39 | numeric-table | \\| Score trajectories built \\| 0 \\| 15 \\| PENDING \\| |
| saturation-analysis | 40 | numeric-table | \\| Papers fetched \\| 0 \\| 50 \\| PENDING \\| |
| saturation-analysis | 41 | numeric-table | \\| Papers read \\| 0 \\| 35 \\| PENDING \\| |
| saturation-analysis | 42 | numeric-table | \\| Web searches \\| 0 \\| 60 \\| PENDING \\| |
| saturation-analysis | 43 | numeric-table | \\| Saturation detections run \\| 0 \\| 15 \\| PENDING \\| |
| saturation-analysis | 44 | numeric-table | \\| Leaderboard analyses done \\| 0 \\| 10 \\| PENDING \\| |
| saturation-analysis | 45 | numeric-table | \\| Failure mode catalogs built \\| 0 \\| 5 \\| PENDING \\| |
| saturation-analysis | 46 | textual | </HARD-GATE> |
| saturation-analysis | 49 | numeric | Cannot exit until 80% of all targets met. |
| saturation-analysis | 87 | numeric | estimated_time_to_ceiling: string  # e.g., "6-12 months" |
| saturation-analysis | 89 | numeric | score_compression: float  # top-10 score range |
| validity-probing | 28 | numeric-table | \\| Benchmarks probed \\| 2 \\| 3 \\| |
| validity-probing | 29 | numeric-table | \\| Papers read \\| 30 \\| 40 \\| |
| validity-probing | 30 | numeric-table | \\| Web searches \\| 20 \\| 30 \\| |
| validity-probing | 35 | textual | <HARD-GATE> |
| validity-probing | 38 | numeric-table | \\| Benchmarks probed \\| 0 \\| 3 \\| PENDING \\| |
| validity-probing | 39 | numeric-table | \\| Papers fetched \\| 0 \\| 40 \\| PENDING \\| |
| validity-probing | 40 | numeric-table | \\| Papers read \\| 0 \\| 30 \\| PENDING \\| |
| validity-probing | 41 | numeric-table | \\| Web searches \\| 0 \\| 30 \\| PENDING \\| |
| validity-probing | 42 | numeric-table | \\| Construct validity assessments \\| 0 \\| 3 \\| PENDING \\| |
| validity-probing | 43 | numeric-table | \\| Artifact detection runs \\| 0 \\| 3 \\| PENDING \\| |
| validity-probing | 44 | numeric-table | \\| Alternative explanation catalogs \\| 0 \\| 3 \\| PENDING \\| |
| validity-probing | 45 | numeric-table | \\| Convergent validity checks \\| 0 \\| 3 \\| PENDING \\| |
| validity-probing | 46 | textual | </HARD-GATE> |
| validity-probing | 49 | numeric | Cannot exit until 80% of all targets met. |
| coverage-mapping | 21 | textual | Build a comprehensive map of "what we can and cannot measure" for a given AI capability domain. Identify white spaces where important capabilities lack rigorous evaluation, and redundancies where multiple benchmarks test the same narrow skill. |
| coverage-mapping | 27 | numeric-table | \\| Benchmarks mapped \\| 15 \\| 20 \\| |
| coverage-mapping | 28 | numeric-table | \\| Papers read \\| 20 \\| 30 \\| |
| coverage-mapping | 29 | numeric-table | \\| Web searches \\| 35 \\| 50 \\| |
| coverage-mapping | 34 | textual | <HARD-GATE> |
| coverage-mapping | 37 | numeric-table | \\| Benchmarks mapped \\| 0 \\| 20 \\| PENDING \\| |
| coverage-mapping | 38 | numeric-table | \\| Capability taxonomy nodes \\| 0 \\| 30 \\| PENDING \\| |
| coverage-mapping | 39 | numeric-table | \\| Papers fetched \\| 0 \\| 30 \\| PENDING \\| |
| coverage-mapping | 40 | numeric-table | \\| Papers read \\| 0 \\| 20 \\| PENDING \\| |
| coverage-mapping | 41 | numeric-table | \\| Web searches \\| 0 \\| 50 \\| PENDING \\| |
| coverage-mapping | 42 | numeric-table | \\| Coverage annotations complete \\| 0 \\| 20 \\| PENDING \\| |
| coverage-mapping | 43 | numeric-table | \\| White spaces identified \\| 0 \\| 5 \\| PENDING \\| |
| coverage-mapping | 44 | numeric-table | \\| Redundancy clusters found \\| 0 \\| 3 \\| PENDING \\| |
| coverage-mapping | 45 | textual | </HARD-GATE> |
| coverage-mapping | 48 | numeric | Cannot exit until 80% of all targets met. |
| protocol-forensics | 20 | textual | Expose the "reproducibility gap" in benchmark evaluation by documenting how papers differ in their implementation of supposedly standardized evaluation protocols. Quantify the score variance attributable to protocol differences rather than model improvements. |
| protocol-forensics | 26 | numeric-table | \\| Benchmarks forensically analyzed \\| 3 \\| 5 \\| |
| protocol-forensics | 27 | numeric-table | \\| Papers read \\| 45 \\| 60 \\| |
| protocol-forensics | 28 | numeric-table | \\| Web searches \\| 20 \\| 30 \\| |
| protocol-forensics | 33 | textual | <HARD-GATE> |
| protocol-forensics | 36 | numeric-table | \\| Benchmarks analyzed \\| 0 \\| 5 \\| PENDING \\| |
| protocol-forensics | 37 | numeric-table | \\| Papers fetched \\| 0 \\| 60 \\| PENDING \\| |
| protocol-forensics | 38 | numeric-table | \\| Papers read \\| 0 \\| 45 \\| PENDING \\| |
| protocol-forensics | 39 | numeric-table | \\| Web searches \\| 0 \\| 30 \\| PENDING \\| |
| protocol-forensics | 40 | numeric-table | \\| Protocol extractions complete \\| 0 \\| 60 \\| PENDING \\| |
| protocol-forensics | 41 | numeric-table | \\| Difference matrices built \\| 0 \\| 5 \\| PENDING \\| |
| protocol-forensics | 42 | numeric-table | \\| Variance attributions done \\| 0 \\| 5 \\| PENDING \\| |
| protocol-forensics | 43 | numeric-table | \\| Impact assessments complete \\| 0 \\| 5 \\| PENDING \\| |
| protocol-forensics | 44 | textual | </HARD-GATE> |
| protocol-forensics | 47 | numeric | Cannot exit until 80% of all targets met. |
| protocol-forensics | 61 | textual | 1. **Target Selection**: Choose 5 benchmarks with known reproducibility issues or high paper volume |
| protocol-forensics | 63 | numeric | a. Collect 10-15 papers that report results on the same benchmark |
| protocol-forensics | 76 | textual | 6. **Synthesis**: Produce per-benchmark forensics report with reproducibility recommendations |
| protocol-forensics | 98 | textual | reproducibility_grade: A\\|B\\|C\\|D\\|F |
| evaluation-protocol-comparison | 12 | textual | Compare how different papers implement the same benchmark to expose hidden protocol variance that undermines cross-paper score comparability. |
| evaluation-protocol-comparison | 18 | numeric | Collect 10-15 papers that report results on the target benchmark: |
| evaluation-protocol-comparison | 36 | numeric-table | \\| **Infrastructure** \\| Framework, precision (fp16/bf16/fp32), batch size, hardware \\| |
| evaluation-protocol-comparison | 48 | textual | - **Low**: Minor variations (e.g., different random seeds) |
| evaluation-protocol-comparison | 82 | textual | cross_paper_comparability: high\\|moderate\\|low\\|unreliable |
| evaluation-protocol-comparison | 91 | textual | \\| Metric \\| Minimum \\| |
| evaluation-protocol-comparison | 93 | numeric-table | \\| Papers compared \\| 8 \\| |
| evaluation-protocol-comparison | 94 | numeric-table | \\| Protocol elements extracted per paper \\| 10 \\| |
| evaluation-protocol-comparison | 95 | numeric-table | \\| High-variance elements identified \\| 2 \\| |
| evaluation-protocol-comparison | 96 | numeric-table | \\| Impact estimates produced \\| 3 \\| |
