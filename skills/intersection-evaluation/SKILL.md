---
name: intersection-evaluation
description: Evaluate exploration status of each cell in a method×problem matrix,
  annotating as explored, partial, or unexplored.
execution: subagent
prompt: ./prompt.md
input: cross_matrix (object)
dependencies:
  sops:
  - spawn-agent
---

# Intersection Evaluation

Evaluate the exploration status of each cell in a method×problem matrix and prioritize unexplored intersections.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Evaluation requires careful assessment of each intersection's exploration depth, consulting literature and benchmarks. Benefits from focused context to maintain consistent evaluation criteria.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
