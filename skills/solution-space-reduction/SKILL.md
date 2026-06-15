---
name: solution-space-reduction
description: Apply CCA to remove inconsistent combinations
execution: subagent
prompt: ./prompt.md
input: matrix (object), consistency_judgments (array)
dependencies:
  sops:
  - spawn-agent
---

# Solution Space Reduction

Apply cross-consistency analysis to remove all configurations containing inconsistent pairs, producing a reduced solution space.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Space reduction requires systematic application of consistency constraints across the full matrix, computing which complete configurations survive filtering, and reporting reduction statistics.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
