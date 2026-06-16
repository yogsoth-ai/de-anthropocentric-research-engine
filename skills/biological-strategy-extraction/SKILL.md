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

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
