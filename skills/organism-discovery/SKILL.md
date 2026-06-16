---
name: organism-discovery
description: Find organisms solving similar problems. Search across kingdoms for biological
  champions.
execution: subagent
prompt: ./prompt.md
input: biological_function_need (string)
dependencies:
  sops:
  - spawn-agent
---

# Organism Discovery

Find organisms solving similar problems.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Organism discovery requires broad biological knowledge search across multiple kingdoms, phyla, and ecological niches. Benefits from dedicated research attention to find non-obvious biological champions.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
