---
name: excursion-departure
description: Leave the problem entirely and explore an unrelated domain. Produces
  excursion domain discoveries for later force-fitting.
execution: subagent
prompt: ./prompt.md
input: problem (string)
dependencies:
  sops:
  - spawn-agent
---

# Excursion Departure

Leave the problem entirely and explore an unrelated domain.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Excursion departure requires genuine cognitive distance from the problem. Benefits from a fresh context that is not contaminated by problem-solving intent, enabling true discovery in the excursion domain.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
