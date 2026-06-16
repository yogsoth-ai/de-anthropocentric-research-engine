---
name: constraint-response
description: Generate creative solutions under extreme constraints — no "impossible"
  allowed, find a way.
execution: subagent
prompt: ./prompt.md
input: constraint (string), problem (string)
dependencies:
  sops:
  - spawn-agent
---

# Constraint Response

Generate creative solutions under extreme constraints.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Constraint-forced creativity requires sustained divergent thinking under pressure, benefiting from dedicated context that fully commits to the constraint.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
