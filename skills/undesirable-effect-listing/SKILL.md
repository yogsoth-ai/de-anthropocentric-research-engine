---
name: undesirable-effect-listing
description: List current Undesirable Effects (UDEs) — observable symptoms of system
  underperformance
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
input: system description, observed problems, stakeholder complaints
output: numbered UDE list with evidence and severity ratings
dependencies:
  sops:
  - spawn-agent
---

# SOP: Undesirable Effect Listing

List all observable Undesirable Effects (UDEs) in the system — symptoms that indicate the system is not performing as desired.

Subagent — spawned via subagent-spawning/spawn-agent skill.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
