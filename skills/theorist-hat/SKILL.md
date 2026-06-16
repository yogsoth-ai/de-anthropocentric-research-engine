---
name: theorist-hat
description: Theorist perspective — assess theoretical foundations, formal rigor,
  and formalization opportunities.
execution: subagent
prompt: ./prompt.md
input: solution (string)
dependencies:
  sops:
  - spawn-agent
---

# Theorist Hat

Theorist perspective: assess theoretical foundations.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Theoretical analysis requires deep formal reasoning and literature awareness that benefits from dedicated context.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
