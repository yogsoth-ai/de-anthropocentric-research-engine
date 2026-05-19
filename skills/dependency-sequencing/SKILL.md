---
name: dependency-sequencing
description: "Determine task dependencies and execution order"
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
used-by:
  - critical-path-planning
  - task-decomposition
input: list of implementation activities
output: dependency graph with predecessor/successor relationships
---

# SOP: Dependency Sequencing

Determine predecessor/successor relationships between activities and produce a valid execution order.

Subagent — spawned via subagent-spawning/spawn-agent skill.
