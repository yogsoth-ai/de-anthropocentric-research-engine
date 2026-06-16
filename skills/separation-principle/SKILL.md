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

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
