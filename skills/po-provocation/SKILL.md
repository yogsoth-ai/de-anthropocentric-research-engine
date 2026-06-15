---
name: po-provocation
description: Generate PO (Provocative Operation) statements per de Bono's lateral
  thinking. Creates deliberately illogical provocations to escape dominant thinking
  patterns.
execution: subagent
prompt: ./prompt.md
input: target_statement (string), provocation_types (string)
dependencies:
  sops:
  - spawn-agent
---

# PO Provocation

Generate PO (Provocative Operation) statements.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

PO provocation requires deliberately illogical thinking — suspending judgment and generating statements that are intentionally wrong or impossible. Benefits from a dedicated context that won't self-censor.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
