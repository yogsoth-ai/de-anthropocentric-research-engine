---
name: personal-identification
description: First-person empathic identification with a system or component. Produces
  experience description and design insights from embodiment.
execution: subagent
prompt: ./prompt.md
input: system_or_component (string)
dependencies:
  sops:
  - spawn-agent
---

# Personal Identification

First-person empathic identification with a system or component.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Personal identification requires deep imaginative immersion in a single perspective. Benefits from uninterrupted focus on embodiment without analytical interference.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
