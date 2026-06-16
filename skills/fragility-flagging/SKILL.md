---
name: fragility-flagging
description: Identify which specific assumption changes cause conclusion divergence.
  Rates fragility severity and plausibility of alternatives.
execution: subagent
prompt: ./prompt.md
input: convergence_results (string), context (string)
dependencies:
  sops:
  - spawn-agent
---

# Fragility Flagging

Flag conclusions that are fragile to assumption changes.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one fragility assessment pass.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
