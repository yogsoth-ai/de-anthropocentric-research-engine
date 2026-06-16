---
name: problem-biologization
description: Restate technical problem as biological question. Translate engineering
  challenges into nature's language.
execution: subagent
prompt: ./prompt.md
input: technical_problem (string)
dependencies:
  sops:
  - spawn-agent
---

# Problem Biologization

Restate technical problem as biological question.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Biologization requires creative reframing of technical problems into biological language, searching for functional equivalents across kingdoms of life. Benefits from dedicated attention to find non-obvious biological framings.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
