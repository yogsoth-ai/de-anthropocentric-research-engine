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

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
