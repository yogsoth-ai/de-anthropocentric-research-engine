---
name: dependency-sequencing
description: Determine task dependencies and execution order
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
input: list of implementation activities
output: dependency graph with predecessor/successor relationships
dependencies:
  sops:
  - spawn-agent
---

# SOP: Dependency Sequencing

Determine predecessor/successor relationships between activities and produce a valid execution order.

Subagent — spawned via subagent-spawning/spawn-agent skill.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
