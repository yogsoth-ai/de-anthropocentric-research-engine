---
name: deep-insight-assumption-surfacing
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

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
