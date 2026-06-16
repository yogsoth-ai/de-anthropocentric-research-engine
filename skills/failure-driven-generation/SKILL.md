---
name: failure-driven-generation
description: Generate targeted solutions for each identified failure mode, ensuring
  every failure has at least one proposed mitigation.
execution: subagent
prompt: ./prompt.md
input: failure_modes (array)
dependencies:
  sops:
  - spawn-agent
---

# Failure-Driven Generation

Generate solutions that specifically target identified failure modes.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Solution generation for failures requires creative thinking constrained by specific failure characteristics. Benefits from dedicated context that can deeply engage with each failure mode's mechanics.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
