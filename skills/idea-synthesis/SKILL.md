---
name: idea-synthesis
description: Synthesize diverse ideas into coherent solution concepts. Combines fragments
  from multiple ideation passes into structured, actionable ideas with clear mechanism
  descriptions.
execution: subagent
prompt: ./prompt.md
input: raw_ideas (string), campaign_context (string)
dependencies:
  sops:
  - spawn-agent
---

# Idea Synthesis

Synthesize diverse ideas into coherent solution concepts.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Synthesis requires holding all intermediate outputs in context simultaneously and identifying connections, redundancies, and complementary fragments across multiple ideation passes.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
