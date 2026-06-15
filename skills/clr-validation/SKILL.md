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

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
