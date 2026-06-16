---
name: governing-variable-surfacing
description: Apply Argyris framework to identify governing variables — the unstated
  rules driving behavior in a research field.
execution: subagent
prompt: ./prompt.md
input: observed_behavior_patterns
dependencies:
  sops:
  - spawn-agent
---

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one complete governing variable analysis for a field/domain.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
