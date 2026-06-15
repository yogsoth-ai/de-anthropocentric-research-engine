---
name: escape-technique
description: Identify dominant thinking pattern and escape it via deliberate pattern-breaking.
execution: subagent
prompt: ./prompt.md
input: current_thinking (string)
dependencies:
  sops:
  - spawn-agent
---

# Escape Technique

Identify dominant thinking pattern and escape it.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Escape requires first identifying the dominant pattern (which is invisible to those inside it) and then deliberately breaking free. Benefits from dedicated context that can analyze the thinking pattern from outside.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
