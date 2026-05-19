---
name: duration-estimation
description: "Three-point PERT estimation for implementation activities"
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
used-by: critical-path-planning
input: sequenced activity list with dependency information
output: PERT estimates (optimistic, most likely, pessimistic, expected, variance) per activity
---

# SOP: Duration Estimation

Estimate activity durations using three-point PERT methodology.

Subagent — spawned via subagent-spawning/spawn-agent skill.
