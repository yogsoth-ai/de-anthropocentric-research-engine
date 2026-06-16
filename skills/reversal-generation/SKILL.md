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

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
