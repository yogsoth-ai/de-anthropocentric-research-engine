---
name: score-extraction
description: Extract (Task, Dataset, Metric, Score, Conditions) tuples from a paper
execution: subagent
prompt: ./prompt.md
input: paper_content, target_tasks
used-by: baseline-establishment
---

# Score Extraction


## Purpose

Parse a paper's results sections, tables, and figures to extract all reported performance scores as structured tuples. Each tuple captures the full context needed for fair comparison: what was measured, on what data, under what conditions.

## Input Schema

| Field | Type | Description |
|-------|------|-------------|
| paper_content | string | Full paper text (markdown format) |
| target_tasks | string[] | Tasks to focus extraction on (empty = extract all) |

## Output Schema

```json
{
  "paper_title": "string",
  "scores": [
    {
      "method": "string",
      "task": "string",
      "dataset": "string",
      "split": "test|val|dev|train",
      "metric": "string",
      "score": 0.0,
      "score_std": null,
      "num_runs": null,
      "is_primary_result": true,
      "is_ablation": false,
      "table_reference": "string",
      "notes": "string"
    }
  ],
  "baselines_reported": ["string"],
  "extraction_confidence": "high|medium|low"
}
```
