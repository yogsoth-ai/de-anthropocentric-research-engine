---
name: implementer-dispatch
description: Dispatch execution subagent — select model by complexity, construct prompt
  with full task context
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
input: task specification from executable plan
output: dispatched subagent with constructed prompt and selected model
dependencies:
  sops:
  - spawn-agent
---

# SOP: Implementer Dispatch

Select appropriate model and construct execution prompt for a task subagent.

Subagent — spawned via subagent-spawning/spawn-agent skill.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
