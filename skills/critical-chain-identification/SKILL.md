---
name: critical-chain-identification
description: Identify the critical chain — longest path considering resource contention
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
input: dependency graph, resource assignments, duration estimates
output: critical chain with resource conflicts resolved, feeding chains identified
shared: true
dependencies:
  sops:
  - spawn-agent
---

# SOP: Critical Chain Identification

Identify the critical chain (longest resource-constrained path) using Goldratt's Critical Chain method. Differs from CPM by resolving resource contention and removing task-level safety margins.

Subagent — spawned via subagent-spawning/spawn-agent skill.

Shared: Used by dependency-constraint strategy and implementation-planning campaign.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
