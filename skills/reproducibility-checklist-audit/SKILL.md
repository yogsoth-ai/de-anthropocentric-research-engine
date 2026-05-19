---
name: reproducibility-checklist-audit
description: Assess paper completeness against ML Reproducibility Checklist
execution: subagent
prompt: ./prompt.md
input: paper_content
used-by: baseline-establishment
---

# Reproducibility Checklist Audit


## Purpose

Evaluate a paper against the standard ML Reproducibility Checklist (as used by NeurIPS, ICML, ICLR). Produces a structured assessment of what information is present, what is missing, and an overall reproducibility score.

## Input Schema

| Field | Type | Description |
|-------|------|-------------|
| paper_content | string | Full paper text (markdown format) |

## Output Schema

```json
{
  "paper_title": "string",
  "checklist": {
    "model_architecture": {"present": true, "details": "string"},
    "training_procedure": {"present": true, "details": "string"},
    "hyperparameters": {"present": true, "details": "string"},
    "hyperparameter_search": {"present": false, "details": "string"},
    "datasets": {"present": true, "details": "string"},
    "data_preprocessing": {"present": true, "details": "string"},
    "evaluation_metrics": {"present": true, "details": "string"},
    "error_bars_or_confidence": {"present": false, "details": "string"},
    "number_of_runs": {"present": false, "details": "string"},
    "compute_resources": {"present": false, "details": "string"},
    "code_availability": {"present": true, "details": "string"},
    "random_seeds": {"present": false, "details": "string"}
  },
  "overall_score": 0.0,
  "critical_gaps": ["string"],
  "reproducibility_risk": "low|medium|high|critical"
}
```
