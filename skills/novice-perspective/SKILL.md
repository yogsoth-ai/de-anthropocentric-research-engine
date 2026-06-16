---
name: novice-perspective
description: Novice perspective — question the 'obvious' by adopting deliberate ignorance
  to reveal hidden complexity.
execution: subagent
prompt: ./prompt.md
input: solution (string)
dependencies:
  sops:
  - spawn-agent
---

# Novice Perspective

Novice perspective: question the 'obvious'.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Deliberate novice thinking requires suppressing expert knowledge, which benefits from a clean context without accumulated domain assumptions.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
