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

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
