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

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
