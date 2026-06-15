---
name: fragility-measurement
description: Compute a fragility index from flip-point distances and degradation scores,
  summarizing how robust the conclusion is.
execution: subagent
prompt: ./prompt.md
input: flip_points (list), degradation_scores (list), factor_count (number)
dependencies:
  sops:
  - spawn-agent
---

# Fragility Measurement

Aggregates flip-point distances and degradation scores into a single fragility index.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Why Subagent

Fragility computation requires synthesizing results from multiple ablation and flip-point tests into a coherent assessment.

## Input

- **flip_points**: List of {dimension, distance, confidence}
- **degradation_scores**: List of {factor, score, classification}
- **factor_count**: Total factors examined

## Output

- **fragility_index**: Overall fragility (0.0 = robust, 1.0 = extremely fragile)
- **most_fragile_dimension**: Where the conclusion is most vulnerable
- **robustness_assessment**: Qualitative summary
- **recommendations**: What to investigate further

## Budget

One unit = one aggregation per campaign run.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
