---
name: biological-strategy-extraction
description: Extract strategy principles from organisms. Identify mechanism-level
  details of how biological systems achieve their function.
execution: subagent
prompt: ./prompt.md
input: organism (string)
dependencies:
  sops:
  - spawn-agent
---

# Biological Strategy Extraction

Extract strategy principles from organisms.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Strategy extraction requires deep dive into biological mechanisms, understanding multi-scale interactions, and identifying the transferable principle beneath species-specific details. Benefits from focused analytical attention.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
