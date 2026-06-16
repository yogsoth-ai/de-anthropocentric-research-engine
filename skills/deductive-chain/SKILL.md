---
name: deductive-chain
description: Derive logical consequences step by step from a given premise, building
  a traceable derivation chain.
execution: subagent
prompt: ./prompt.md
dependencies:
  sops:
  - spawn-agent
---

# Deductive Chain

Subagent that takes a premise and derives logical consequences through valid inference steps, producing a traceable chain.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
