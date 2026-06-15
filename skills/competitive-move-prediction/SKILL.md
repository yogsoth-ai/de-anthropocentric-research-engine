---
name: competitive-move-prediction
description: Predict competitor progress, publications, and strategic moves
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
input: competitor profile, publication history, resource level, research field context
output: predicted actions, timelines, preemption risk assessment
dependencies:
  sops:
  - spawn-agent
---

# SOP: Competitive Move Prediction

Predict what key competitors will do next based on their publication patterns, resource levels, hiring signals, and strategic positioning. Assess preemption risk and time windows.

Subagent — spawned via subagent-spawning/spawn-agent skill.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
