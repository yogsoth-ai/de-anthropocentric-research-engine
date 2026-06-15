---
name: blend-completion
description: Complete blend with background knowledge
execution: subagent
prompt: ./prompt.md
input: initial_blend (object)
dependencies:
  sops:
  - spawn-agent
---

# Blend Completion

Complete blend with background knowledge — recruit additional structure from long-term memory and world knowledge to fill out the blend.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Blend completion requires broad knowledge recruitment — bringing in patterns, frames, and schemas from background knowledge that weren't in either input but are triggered by the blend's emergent structure. Benefits from exploratory breadth.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
