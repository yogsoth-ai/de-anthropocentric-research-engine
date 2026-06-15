---
name: separation-principle
description: Apply time/space/condition/scale separation to resolve physical contradictions
  where the same parameter must satisfy opposing requirements.
execution: subagent
prompt: ./prompt.md
input: physical_contradiction (string)
dependencies:
  sops:
  - spawn-agent
---

# Separation Principle

Resolve physical contradictions through separation in time, space, condition, or scale.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Separation requires exploring four distinct dimensions of resolution, each with its own logic. Benefits from dedicated context that can systematically work through all four separation types without conflation.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
