---
name: excursion-departure
description: Leave the problem entirely and explore an unrelated domain. Produces
  excursion domain discoveries for later force-fitting.
execution: subagent
prompt: ./prompt.md
input: problem (string)
dependencies:
  sops:
  - spawn-agent
---

# Excursion Departure

Leave the problem entirely and explore an unrelated domain.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Excursion departure requires genuine cognitive distance from the problem. Benefits from a fresh context that is not contaminated by problem-solving intent, enabling true discovery in the excursion domain.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
