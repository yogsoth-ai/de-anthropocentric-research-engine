---
name: intermediate-objective-design
description: Design intermediate objectives to overcome each identified obstacle
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
input: categorized obstacle list
output: intermediate objectives with verification criteria and dependency sequence
dependencies:
  sops:
  - spawn-agent
---

# SOP: Intermediate Objective Design

Design concrete, verifiable intermediate objectives (IOs) that overcome each identified obstacle.

Subagent — spawned via subagent-spawning/spawn-agent skill.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
