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

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
