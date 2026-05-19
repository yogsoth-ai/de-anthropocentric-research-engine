---
name: critical-path-calculation
description: "CPM forward/backward pass with float calculation to identify the critical path"
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
used-by: critical-path-planning
input: activity list with dependencies and PERT duration estimates
output: critical path, float table, earliest/latest start-finish times
---

# SOP: Critical Path Calculation

Perform CPM forward and backward pass to identify the critical path and calculate float for all activities.

Subagent — spawned via subagent-spawning/spawn-agent skill.
