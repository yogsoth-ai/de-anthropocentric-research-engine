---
name: clr-validation
description: Apply Goldratt's 8 Categories of Legitimate Reservation to validate causal
  claims. Tests clarity, existence, sufficiency, and logical integrity.
execution: subagent
prompt: ./prompt.md
input: causal_claim (string), context (string)
dependencies:
  sops:
  - spawn-agent
---

# CLR Validation

Validate causal logic via Categories of Legitimate Reservation.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one CLR validation pass.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
