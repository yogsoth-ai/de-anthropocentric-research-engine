---
name: condition-cataloging
description: Record evaluation conditions (data splits, hyperparams, hardware, seeds) from a paper
execution: subagent
prompt: ./prompt.md
input: paper_content, method_name
used-by: baseline-establishment
---

# Condition Cataloging


## Purpose

Extract the complete set of experimental conditions under which a method was evaluated. This metadata is essential for determining whether two scores are directly comparable or require normalization.

## Input Schema

| Field | Type | Description |
|-------|------|-------------|
| paper_content | string | Full paper text (markdown format) |
| method_name | string | The specific method to catalog conditions for |

## Output Schema

```json
{
  "method": "string",
  "conditions": {
    "data": {
      "dataset_version": "string",
      "split": "string",
      "preprocessing": "string",
      "augmentation": "string",
      "training_size": "string",
      "external_data_used": false
    },
    "compute": {
      "hardware": "string",
      "gpu_count": null,
      "training_time": "string",
      "flops_estimate": "string"
    },
    "hyperparameters": {
      "learning_rate": "string",
      "batch_size": null,
      "epochs": null,
      "optimizer": "string",
      "scheduler": "string",
      "key_hyperparams": {}
    },
    "evaluation": {
      "num_seeds": null,
      "seed_values": [],
      "ensemble": false,
      "post_processing": "string",
      "evaluation_protocol": "string"
    },
    "reproducibility": {
      "code_available": false,
      "code_url": "string",
      "pretrained_model_available": false,
      "full_config_provided": false
    }
  },
  "missing_information": ["string"],
  "completeness_score": 0.0
}
```
