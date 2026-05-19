---
name: discrepancy-identification
description: Compare same-method scores across sources, flag significant deviations
execution: subagent
prompt: ./prompt.md
input: score_pairs (source_a, source_b, method, dataset)
used-by: baseline-establishment
---

# Discrepancy Identification


## Purpose

Detect statistically significant discrepancies between scores reported for the same method across different sources. Identifies potential score inflation, implementation bugs, evaluation protocol differences, and unreliable baselines.

## Input Schema

| Field | Type | Description |
|-------|------|-------------|
| score_pairs | object[] | Array of {source_a, source_b, method, dataset, metric, score_a, score_b, conditions_a, conditions_b} |

## Output Schema

```json
{
  "comparisons": [
    {
      "method": "string",
      "dataset": "string",
      "metric": "string",
      "score_a": 0.0,
      "source_a": "string",
      "score_b": 0.0,
      "source_b": "string",
      "absolute_delta": 0.0,
      "relative_delta_pct": 0.0,
      "is_significant": true,
      "likely_cause": "string",
      "confidence": "high|medium|low"
    }
  ],
  "flagged_methods": [
    {
      "method": "string",
      "num_discrepancies": 0,
      "max_delta": 0.0,
      "reliability_assessment": "string"
    }
  ],
  "systematic_patterns": ["string"]
}
```
