---
name: implementer-dispatch
description: "Dispatch execution subagent — select model by complexity, construct prompt with full task context"
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
used-by:
  - experiment-running
  - subagent-execution-loop
input: task specification from executable plan
output: dispatched subagent with constructed prompt and selected model
---

# SOP: Implementer Dispatch

Select appropriate model and construct execution prompt for a task subagent.

Subagent — spawned via subagent-spawning/spawn-agent skill.
