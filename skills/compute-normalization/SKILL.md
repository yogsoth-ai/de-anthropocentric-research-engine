---
name: compute-normalization
description: Normalize results by compute budget (Pareto analysis)
execution: subagent
prompt: ./prompt.md
input: method_scores, compute_costs
used-by: baseline-establishment
---

# Compute Normalization


## Purpose

Analyze the performance-compute tradeoff across methods. Identify Pareto-optimal methods (best performance for a given compute budget), compute-normalized rankings, and efficiency frontiers. Essential for practical method selection under resource constraints.

## Input Schema

| Field | Type | Description |
|-------|------|-------------|
| method_scores | object[] | Array of {method, dataset, metric, score} |
| compute_costs | object[] | Array of {method, flops, gpu_hours, params, training_cost_usd} |

## Output Schema

```json
{
  "pareto_frontier": [
    {
      "method": "string",
      "score": 0.0,
      "compute_metric": "string",
      "compute_value": 0.0,
      "is_pareto_optimal": true
    }
  ],
  "efficiency_rankings": [
    {
      "method": "string",
      "score_per_flop": 0.0,
      "score_per_gpu_hour": 0.0,
      "score_per_param": 0.0
    }
  ],
  "compute_normalized_scores": [
    {
      "method": "string",
      "raw_score": 0.0,
      "normalized_score": 0.0,
      "normalization_method": "string"
    }
  ],
  "practical_recommendations": {
    "budget_low": {"method": "string", "score": 0.0, "cost": "string"},
    "budget_medium": {"method": "string", "score": 0.0, "cost": "string"},
    "budget_high": {"method": "string", "score": 0.0, "cost": "string"}
  }
}
```
