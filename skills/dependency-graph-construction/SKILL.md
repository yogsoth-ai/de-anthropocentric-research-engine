---
name: dependency-graph-construction
description: "Build task dependency graph with predecessor/successor relationships"
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
used-by: dependency-constraint
input: task list with descriptions, resource assignments, duration estimates
output: dependency graph (adjacency list) with critical path candidates
shared: true
---

# SOP: Dependency Graph Construction

Build a task dependency graph from a work breakdown structure. Identify all predecessor/successor relationships, parallel opportunities, and convergence points.

Subagent — spawned via subagent-spawning/spawn-agent skill.

Shared: Used by dependency-constraint strategy and deep-insight campaign.
