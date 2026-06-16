---
name: plan-formatting
description: Format task plan as bite-sized executable tasks following superpowers:writing-plans
  conventions
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
input: estimated and sequenced activity list with IOs
output: executable plan document with no TBD/TODO (HARD-GATE)
dependencies:
  sops:
  - spawn-agent
---

# SOP: Plan Formatting

Format the complete task information into a bite-sized executable plan. HARD-GATE: output must contain zero TBD/TODO/placeholder text.

Subagent — spawned via subagent-spawning/spawn-agent skill.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
