---
name: progress-quantification
description: Track performance progress over time, quantify remaining headroom — 30 methods, 100 data points, 40 web searches budget
used-by: baseline-establishment
---

# Progress Quantification


## Purpose

Construct temporal performance trajectories for the target task. Fit progress curves, identify inflection points (paradigm shifts), estimate theoretical/practical ceilings, and quantify remaining headroom. Produces actionable intelligence about where the field is plateauing and where breakthroughs are needed.

## Budget

| Resource | Floor | Target |
|----------|-------|--------|
| Methods tracked | 20 | 30 |
| Historical data points | 70 | 100 |
| Web searches | 25 | 40 |
| Time span covered (years) | 3 | 5+ |

## State Ledger

```
<HARD-GATE>
| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| Methods tracked | 0 | 30 | BLOCKED |
| Historical data points | 0 | 100 | BLOCKED |
| Web searches used | 0 | 40 | — |
| Progress curves built | 0 | 3 | — |
| Headroom estimates | 0 | 3 | — |
| Inflection points identified | 0 | 2 | — |
</HARD-GATE>
```

Cannot exit until historical_data_points >= 80 (80% of target).

## Available Tactics

- **progress-curve-construction** — Build temporal performance curves with inflection detection
- **leaderboard-harvesting** — Historical data collection

## Available SOPs

- **progress-curve-fitting** — Fit curves and extract trend parameters
- **headroom-estimation** — Estimate ceiling vs current SOTA gap
- **baseline-synthesis** — Produce final integrated report

## Execution Guidance

1. Arrange all extracted scores chronologically per dataset/metric
2. Use progress-curve-construction tactic for curve building
3. Identify paradigm shifts (method families that caused jumps)
4. Use headroom-estimation for ceiling analysis
5. Compare progress rates across different sub-tasks
6. Identify tasks approaching saturation vs. those with large headroom
7. Produce baseline-synthesis as the final integrated deliverable

## Output Format

```json
{
  "progress_curves": [
    {
      "dataset": "string",
      "metric": "string",
      "time_series": [{"date": "string", "method": "string", "score": 0.0}],
      "trend_type": "logarithmic|linear|sigmoid|stepped",
      "annual_improvement_rate": 0.0,
      "inflection_points": [{"date": "string", "method": "string", "cause": "string"}]
    }
  ],
  "headroom_analysis": [
    {
      "dataset": "string",
      "metric": "string",
      "current_sota": 0.0,
      "human_performance": 0.0,
      "theoretical_ceiling": 0.0,
      "remaining_headroom_pct": 0.0,
      "saturation_status": "saturating|active_progress|early_stage"
    }
  ],
  "paradigm_shifts": [
    {
      "year": 2024,
      "method_family": "string",
      "improvement_magnitude": 0.0,
      "description": "string"
    }
  ]
}
```
