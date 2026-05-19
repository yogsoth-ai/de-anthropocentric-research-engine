---
name: baseline-synthesis
description: Produce final structured baseline report integrating all analysis results
execution: subagent
prompt: ./prompt.md
input: all_analysis_results
used-by: baseline-establishment
---

# Baseline Synthesis


## Purpose

Synthesize all outputs from the baseline establishment campaign into a single coherent report. Integrates method inventory, performance tables, condition analysis, discrepancy findings, and progress curves into an actionable baseline document.

## Input Schema

| Field | Type | Description |
|-------|------|-------------|
| all_analysis_results | object | Combined outputs from all prior strategies and SOPs |

## Output Schema

```json
{
  "report": {
    "title": "string",
    "task": "string",
    "domain": "string",
    "date_generated": "string",
    "summary": "string"
  },
  "method_landscape": {
    "total_methods": 0,
    "method_families": [{"name": "string", "count": 0, "era": "string"}],
    "active_methods": 0,
    "deprecated_methods": 0
  },
  "performance_summary": {
    "primary_table": {},
    "sota": {"method": "string", "score": 0.0, "date": "string"},
    "fair_sota": {"method": "string", "score": 0.0, "conditions": "string"},
    "pareto_optimal": []
  },
  "reliability_assessment": {
    "high_confidence_baselines": ["string"],
    "questionable_baselines": ["string"],
    "known_discrepancies": []
  },
  "progress_assessment": {
    "current_status": "saturating|active_progress|early_stage",
    "annual_rate": 0.0,
    "headroom_remaining": 0.0,
    "next_breakthrough_needed": "string"
  },
  "actionable_insights": [
    {
      "finding": "string",
      "implication": "string",
      "recommendation": "string"
    }
  ]
}
```
