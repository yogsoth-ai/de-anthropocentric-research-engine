---
name: assumption-surfacing
description: Systematically extract implicit assumptions from methods, frameworks,
  or arguments. Identifies what is taken for granted without explicit justification.
execution: subagent
prompt: ./prompt.md
input: target_text (string), context (string)
dependencies:
  sops:
  - spawn-agent
---

# Assumption Surfacing

Systematically extract implicit assumptions from methods, frameworks, or arguments.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Why Subagent

Assumption detection requires careful line-by-line reading with a skeptical lens — benefits from dedicated context.

## Budget

Quantity target is set by the calling strategy's budget table. This SOP executes one unit = one assumption surfacing pass producing a categorized assumption table.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
