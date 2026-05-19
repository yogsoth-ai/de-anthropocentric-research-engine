---
name: progress-curve-fitting
description: Construct performance-over-time visualization data
execution: subagent
prompt: ./prompt.md
input: historical_scores (method, score, date)
used-by: baseline-establishment
---

# Progress Curve Fitting


## Purpose

Fit parametric curves to historical SOTA performance data, identify inflection points representing paradigm shifts, and extrapolate future progress trajectories. Produces structured data suitable for visualization and trend analysis.

## Input Schema

| Field | Type | Description |
|-------|------|-------------|
| historical_scores | object[] | Array of {method, score, date, dataset, metric} sorted chronologically |

## Output Schema

```json
{
  "dataset": "string",
  "metric": "string",
  "time_range": {"start": "string", "end": "string"},
  "sota_frontier": [
    {"date": "string", "method": "string", "score": 0.0, "is_new_sota": true}
  ],
  "curve_fit": {
    "best_model": "logarithmic|linear|sigmoid|exponential|piecewise",
    "parameters": {},
    "r_squared": 0.0,
    "residual_std": 0.0
  },
  "inflection_points": [
    {
      "date": "string",
      "method": "string",
      "score_before": 0.0,
      "score_after": 0.0,
      "jump_magnitude": 0.0,
      "paradigm_shift": "string"
    }
  ],
  "trend_metrics": {
    "annual_improvement_rate": 0.0,
    "improvement_accelerating": false,
    "years_since_last_major_jump": 0.0,
    "current_plateau_duration": null
  },
  "extrapolation": {
    "predicted_1yr": 0.0,
    "predicted_3yr": 0.0,
    "confidence_band_1yr": [0.0, 0.0],
    "confidence_band_3yr": [0.0, 0.0],
    "caveat": "string"
  }
}
```
