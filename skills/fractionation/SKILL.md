---
name: fractionation
description: Split concepts into smaller units and recombine them differently to produce
  novel structures.
execution: subagent
prompt: ./prompt.md
input: concept (string)
dependencies:
  sops:
  - spawn-agent
---

# Fractionation

Split concepts into smaller units, recombine differently.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Fractionation requires holding a concept's fragments in mind while exploring all possible recombinations. Benefits from dedicated context that can systematically enumerate fragment combinations without losing track.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
