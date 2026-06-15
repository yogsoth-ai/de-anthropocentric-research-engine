---
name: buffer-sizing
description: Calculate project, feeding, and resource buffers — shared with implementation-planning
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
input: critical chain with task durations (optimistic/likely/pessimistic)
output: buffer sizes and placement recommendations
shared: true
dependencies:
  sops:
  - spawn-agent
---

# SOP: Buffer Sizing

Calculate appropriate project buffer, feeding buffers, and resource buffers for the critical chain using Goldratt's method.

Subagent — spawned via subagent-spawning/spawn-agent skill.

Shared: This SOP is used by resource-constraint and implementation-planning campaigns.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
