---
name: po-provocation
description: Generate PO (Provocative Operation) statements per de Bono's lateral thinking. Creates deliberately illogical provocations to escape dominant thinking patterns.
execution: subagent
prompt: ./prompt.md
input: target_statement (string), provocation_types (string)
used-by: assumption-destruction, lateral-thinking, perspective-forcing
---

# PO Provocation

Generate PO (Provocative Operation) statements.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

PO provocation requires deliberately illogical thinking — suspending judgment and generating statements that are intentionally wrong or impossible. Benefits from a dedicated context that won't self-censor.
