---
name: practitioner-hat
description: Engineer perspective — assess buildability, cost, timeline, and integration
  challenges.
execution: subagent
prompt: ./prompt.md
input: solution (string)
dependencies:
  sops:
  - spawn-agent
---

# Practitioner Hat

Engineer perspective: assess buildability.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Engineering assessment requires systematic evaluation of implementation details that benefits from focused, uninterrupted analysis.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
