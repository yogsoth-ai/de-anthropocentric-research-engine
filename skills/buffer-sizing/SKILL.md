---
name: buffer-sizing
description: "Calculate project, feeding, and resource buffers — shared with implementation-planning"
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
used-by: resource-constraint
input: critical chain with task durations (optimistic/likely/pessimistic)
output: buffer sizes and placement recommendations
shared: true
---

# SOP: Buffer Sizing

Calculate appropriate project buffer, feeding buffers, and resource buffers for the critical chain using Goldratt's method.

Subagent — spawned via subagent-spawning/spawn-agent skill.

Shared: This SOP is used by resource-constraint and implementation-planning campaigns.
