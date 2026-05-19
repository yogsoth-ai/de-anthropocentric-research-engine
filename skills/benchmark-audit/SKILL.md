---
name: benchmark-audit
description: Systematic quality assessment using BetterBench 46-criterion framework — 5 benchmarks, 30 papers, 40 web searches
used-by: benchmark-archaeology
---

# Benchmark Audit Strategy

Systematic quality assessment of AI/ML benchmarks using the BetterBench 46-criterion framework, Datasheets for Datasets standards, and established psychometric evaluation principles.

## Purpose

Produce a structured quality report for each target benchmark covering: documentation completeness, construct validity indicators, statistical robustness, maintenance status, and known failure modes.

## Budget

| Resource | Floor | Target |
|----------|-------|--------|
| Benchmarks audited | 3 | 5 |
| Papers read | 20 | 30 |
| Web searches | 25 | 40 |

## State Ledger

```
<HARD-GATE>
| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| Benchmarks audited | 0 | 5 | PENDING |
| Papers fetched | 0 | 30 | PENDING |
| Papers read | 0 | 20 | PENDING |
| Web searches | 0 | 40 | PENDING |
| Documentation audits complete | 0 | 5 | PENDING |
| Metric decompositions complete | 0 | 5 | PENDING |
| Contamination checks complete | 0 | 5 | PENDING |
| Synthesis reports produced | 0 | 5 | PENDING |
</HARD-GATE>
```

Cannot exit until 80% of all targets met.

## Available Tactics

- **artifact-detection** — Probe for annotation artifacts and dataset shortcuts

## Available SOPs

- **benchmark-inventory** — Identify target benchmarks in domain
- **metric-decomposition** — Decompose composite metrics into constituent signals
- **contamination-audit** — Detect train-test data leakage
- **documentation-audit** — Assess documentation completeness (BetterBench/Datasheets)
- **benchmark-synthesis** — Produce final structured audit report

## Execution Guidance

1. **Inventory Phase**: Use benchmark-inventory to identify 5 benchmarks in target domain
2. **Per-Benchmark Loop** (repeat for each benchmark):
   a. Gather benchmark paper, documentation, leaderboard via web searches
   b. Run documentation-audit against BetterBench 46 criteria
   c. Run metric-decomposition on primary metric(s)
   d. Run contamination-audit checking known training corpora
   e. Run artifact-detection tactic if annotation-based benchmark
   f. Collect findings into per-benchmark report
3. **Synthesis Phase**: Run benchmark-synthesis to produce cross-benchmark comparison

## Output Format

```yaml
benchmark_audit:
  benchmark_name: string
  version: string
  betterbench_score: float  # 0-1, proportion of 46 criteria met
  documentation_grade: A|B|C|D|F
  metric_analysis:
    primary_metric: string
    ceiling_effects: boolean
    polarity_issues: list
  contamination_risk: low|medium|high|critical
  artifact_risk: low|medium|high
  maintenance_status: active|stale|abandoned
  key_findings: list[string]
  recommendations: list[string]
```
