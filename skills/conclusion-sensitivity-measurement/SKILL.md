---
name: conclusion-sensitivity-measurement
description: Quantify how much conclusions change across all assumption negations
  and produce a sensitivity ranking.
execution: subagent
prompt: ./prompt.md
input: original_conclusion, re_derived_conclusions
dependencies:
  sops:
  - spawn-agent
---

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one complete sensitivity measurement and ranking across all tested assumptions.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
