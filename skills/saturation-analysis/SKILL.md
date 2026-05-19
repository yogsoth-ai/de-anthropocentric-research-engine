---
name: saturation-analysis
description: Track score trajectories, detect saturation/failure points — 15 benchmarks, 50 papers, 60 web searches
used-by: benchmark-archaeology
---

# Saturation Analysis Strategy

Track benchmark score trajectories over time to detect saturation signals, ceiling effects, and inflection points that indicate a benchmark has lost discriminative power.

## Purpose

Determine which benchmarks are approaching or have reached saturation, quantify remaining headroom, estimate time-to-ceiling, and identify the specific failure modes that remain unsolved even at high aggregate scores.

## Budget

| Resource | Floor | Target |
|----------|-------|--------|
| Benchmarks analyzed | 10 | 15 |
| Papers read | 35 | 50 |
| Web searches | 40 | 60 |

## State Ledger

```
<HARD-GATE>
| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| Benchmarks analyzed | 0 | 15 | PENDING |
| Score trajectories built | 0 | 15 | PENDING |
| Papers fetched | 0 | 50 | PENDING |
| Papers read | 0 | 35 | PENDING |
| Web searches | 0 | 60 | PENDING |
| Saturation detections run | 0 | 15 | PENDING |
| Leaderboard analyses done | 0 | 10 | PENDING |
| Failure mode catalogs built | 0 | 5 | PENDING |
</HARD-GATE>
```

Cannot exit until 80% of all targets met.

## Available Tactics

- **score-trajectory-analysis** — Collect historical scores, fit saturation curves, detect inflection points

## Available SOPs

- **benchmark-inventory** — Identify target benchmarks in domain
- **metric-decomposition** — Analyze metric properties (ceiling effects, granularity)
- **leaderboard-dynamics-analysis** — Analyze score distributions and compression
- **saturation-detection** (shared from literature-survey) — Detect saturation signals
- **benchmark-synthesis** — Produce cross-benchmark saturation report

## Execution Guidance

1. **Inventory Phase**: Use benchmark-inventory to identify 15 benchmarks spanning different maturity levels
2. **Data Collection** (per benchmark):
   a. Search leaderboards (Papers With Code, official sites) for historical scores
   b. Collect papers reporting SOTA results chronologically
   c. Note human baselines, random baselines, and theoretical ceilings
3. **Trajectory Analysis** (per benchmark):
   a. Run score-trajectory-analysis tactic to build time-series and fit curves
   b. Run saturation-detection to classify saturation status
   c. Run leaderboard-dynamics-analysis for score compression analysis
4. **Failure Mode Mining**: For saturated benchmarks, identify remaining hard subsets
5. **Synthesis**: Cross-benchmark comparison of saturation timelines and patterns

## Output Format

```yaml
saturation_report:
  benchmark_name: string
  saturation_status: pre-saturation|approaching|saturated|supersaturated
  current_sota: float
  human_baseline: float
  theoretical_ceiling: float
  headroom_remaining: float
  estimated_time_to_ceiling: string  # e.g., "6-12 months"
  inflection_points: list[{date, score, cause}]
  score_compression: float  # top-10 score range
  remaining_hard_subsets: list[string]
  successor_benchmarks: list[string]
```
