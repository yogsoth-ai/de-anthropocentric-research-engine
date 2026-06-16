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

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
