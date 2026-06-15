---
name: metric-decomposition
description: Decompose composite metrics into constituent signals, analyze polarity
  and ceiling effects
execution: subagent
prompt: ./prompt.md
input: metric_name, metric_definition, score_distribution
dependencies:
  sops:
  - spawn-agent
---

# Metric Decomposition SOP

Decompose a benchmark's evaluation metric into its constituent signals to understand what is actually being measured, identify ceiling effects, and detect polarity issues.

## Input

- **metric_name**: Name of the metric (e.g., "F1", "BLEU", "Pass@k", "ELO")
- **metric_definition**: Mathematical definition or description of how the metric is computed
- **score_distribution**: Known score distribution data (top scores, median, floor)

## Procedure

1. Parse metric formula into component signals
2. Identify what each component rewards/penalizes
3. Analyze ceiling and floor effects
4. Check for known pathologies (metric gaming, Goodhart's law instances)
5. Assess granularity and discriminative power at current SOTA level

## Output

Structured decomposition showing constituent signals, their weights, ceiling effects, and known pathologies.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
