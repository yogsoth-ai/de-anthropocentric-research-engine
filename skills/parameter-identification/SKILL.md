---
name: parameter-identification
description: Identify the key parameters/dimensions of a problem space. Produces a
  structured parameter list with value ranges for morphological analysis.
execution: subagent
prompt: ./prompt.md
input: system_description (string)
dependencies:
  sops:
  - spawn-agent
---

# Parameter Identification

Identify the key parameters/dimensions of a problem space.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Parameter identification requires systematic decomposition of a system into orthogonal dimensions. Benefits from focused analytical attention to ensure completeness and independence of parameters.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
