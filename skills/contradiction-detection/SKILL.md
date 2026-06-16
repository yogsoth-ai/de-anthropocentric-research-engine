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

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
