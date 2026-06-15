---
name: dependency-graph-construction
description: Build task dependency graph with predecessor/successor relationships
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
input: task list with descriptions, resource assignments, duration estimates
output: dependency graph (adjacency list) with critical path candidates
shared: true
dependencies:
  sops:
  - spawn-agent
---

# SOP: Dependency Graph Construction

Build a task dependency graph from a work breakdown structure. Identify all predecessor/successor relationships, parallel opportunities, and convergence points.

Subagent — spawned via subagent-spawning/spawn-agent skill.

Shared: Used by dependency-constraint strategy and deep-insight campaign.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
