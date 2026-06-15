---
name: contradiction-detection
description: Evaluate whether a derivation chain has reached a genuine contradiction,
  absurdity, or inconclusive state.
execution: subagent
prompt: ./prompt.md
dependencies:
  sops:
  - spawn-agent
---

# Contradiction Detection

Subagent that evaluates derivation chains to determine if a genuine logical contradiction has been reached.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
