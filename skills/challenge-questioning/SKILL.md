---
name: challenge-questioning
description: Non-threatening 'Why?' questioning of current practices to reveal historical
  accidents vs. genuine constraints.
execution: subagent
prompt: ./prompt.md
input: current_practices (string)
dependencies:
  sops:
  - spawn-agent
---

# Challenge Questioning

Non-threatening 'Why?' questioning of current practices.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Challenge questioning requires maintaining a non-judgmental stance while systematically probing every aspect of current practice. Benefits from dedicated context that can track which practices have been challenged and which remain.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
