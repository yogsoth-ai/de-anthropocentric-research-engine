---
name: concept-fan-expansion
description: Expand concept fan from purpose through concepts to directions to ideas
  (de Bono Concept Fan).
execution: subagent
prompt: ./prompt.md
input: purpose_statement (string)
dependencies:
  sops:
  - spawn-agent
---

# Concept Fan Expansion

Expand concept fan from purpose through concepts to ideas.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Concept fan expansion requires maintaining multiple abstraction levels simultaneously and generating ideas at each level. Benefits from dedicated context that can hold the full fan structure while exploring each branch.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
