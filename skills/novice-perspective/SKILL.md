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

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
