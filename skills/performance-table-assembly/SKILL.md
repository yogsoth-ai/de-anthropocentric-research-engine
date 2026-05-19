---
name: performance-table-assembly
description: Assemble unified comparison table with confidence interval annotations
execution: subagent
prompt: ./prompt.md
input: extracted_scores, condition_metadata
used-by: baseline-establishment
---

# Performance Table Assembly


## Purpose

Combine extracted scores from multiple papers into a single unified comparison table. Handles method name normalization, metric alignment, confidence interval propagation, and fair comparison annotations.

## Input Schema

| Field | Type | Description |
|-------|------|-------------|
| extracted_scores | object[] | Array of score tuples from score-extraction SOP |
| condition_metadata | object[] | Array of condition records from condition-cataloging SOP |

## Output Schema

```json
{
  "tables": [
    {
      "dataset": "string",
      "metric": "string",
      "higher_is_better": true,
      "rows": [
        {
          "method": "string",
          "score": 0.0,
          "confidence_interval": [0.0, 0.0],
          "num_runs": null,
          "conditions_comparable": true,
          "condition_notes": "string",
          "source": "string",
          "year": 2024
        }
      ],
      "sota_method": "string",
      "sota_score": 0.0,
      "fairness_notes": ["string"]
    }
  ],
  "excluded_entries": [
    {
      "method": "string",
      "reason": "string"
    }
  ]
}
```
