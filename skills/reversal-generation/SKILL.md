---
name: reversal-generation
description: Systematically reverse positive statements to generate creative inversions.
  Produces reversed statements with initial associations.
execution: subagent
prompt: ./prompt.md
input: statement_list (array), reversal_depth (string)
dependencies:
  sops:
  - spawn-agent
---

# Reversal Generation

Systematically reverse positive statements.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Reversal generation requires creative linguistic and conceptual inversion across multiple dimensions. Benefits from dedicated attention to produce both obvious negations and surprising creative reversals.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
