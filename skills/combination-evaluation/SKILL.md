---
name: combination-evaluation
description: Evaluate new combinations for feasibility and novelty
execution: subagent
prompt: ./prompt.md
input: combination_proposals (array)
dependencies:
  sops:
  - spawn-agent
---

# Combination Evaluation

Evaluate proposed combinations for feasibility, novelty, and implementation difficulty.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Combination evaluation requires multi-criteria assessment of each proposed configuration, weighing technical feasibility against novelty and estimating implementation barriers.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
