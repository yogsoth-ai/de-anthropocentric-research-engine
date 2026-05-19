---
name: headroom-estimation
description: Estimate theoretical/practical ceiling vs current SOTA gap
execution: subagent
prompt: ./prompt.md
input: task_name, current_sota, human_performance, theoretical_bounds
used-by: baseline-establishment
---

# Headroom Estimation


## Purpose

Quantify the remaining improvement potential for a task by estimating various performance ceilings and computing the gap between current SOTA and those ceilings. Distinguishes between theoretical limits (information-theoretic), practical limits (current paradigm), and human performance baselines.

## Input Schema

| Field | Type | Description |
|-------|------|-------------|
| task_name | string | The target task |
| current_sota | object | {method, score, metric, dataset, date} |
| human_performance | object | {score, conditions, source} or null |
| theoretical_bounds | object | {bound_type, value, derivation} or null |

## Output Schema

```json
{
  "task": "string",
  "dataset": "string",
  "metric": "string",
  "ceilings": {
    "theoretical": {
      "value": null,
      "type": "information_theoretic|bayes_optimal|combinatorial",
      "derivation": "string",
      "confidence": "high|medium|low|speculative"
    },
    "human": {
      "value": null,
      "conditions": "string",
      "source": "string",
      "is_expert": true,
      "confidence": "high|medium|low"
    },
    "practical": {
      "value": null,
      "assumptions": "string",
      "based_on": "string",
      "confidence": "medium|low|speculative"
    }
  },
  "headroom": {
    "vs_theoretical": null,
    "vs_human": null,
    "vs_practical": null,
    "interpretation": "string"
  },
  "saturation_assessment": {
    "status": "saturating|active_progress|early_stage|unknown",
    "evidence": "string",
    "years_to_human_parity": null
  }
}
```
