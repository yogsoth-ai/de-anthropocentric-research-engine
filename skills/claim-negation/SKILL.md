---
name: claim-negation
description: Formally negate the core claim, producing the logical complement for
  reductio testing.
execution: subagent
prompt: ./prompt.md
dependencies:
  sops:
  - spawn-agent
---

# Claim Negation

Subagent that takes a claim P and produces its formal negation ~P, ensuring the negation is logically precise and preserves scope.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
