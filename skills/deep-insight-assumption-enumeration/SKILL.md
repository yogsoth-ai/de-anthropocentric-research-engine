---
name: assumption-enumeration
description: Systematically identify all assumptions in a method/model — structural,
  parametric, distributional, and scope assumptions.
execution: subagent
prompt: ./prompt.md
input: method_description (string), context (string)
dependencies:
  sops:
  - spawn-agent
---

# Assumption Enumeration

Exhaustively list all assumptions in a method.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one assumption enumeration pass.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
