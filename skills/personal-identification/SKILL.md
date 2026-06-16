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

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
