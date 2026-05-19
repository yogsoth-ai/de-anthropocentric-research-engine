---
name: critical-chain-identification
description: "Identify the critical chain — longest path considering resource contention"
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
used-by: dependency-constraint
input: dependency graph, resource assignments, duration estimates
output: critical chain with resource conflicts resolved, feeding chains identified
shared: true
---

# SOP: Critical Chain Identification

Identify the critical chain (longest resource-constrained path) using Goldratt's Critical Chain method. Differs from CPM by resolving resource contention and removing task-level safety margins.

Subagent — spawned via subagent-spawning/spawn-agent skill.

Shared: Used by dependency-constraint strategy and implementation-planning campaign.
