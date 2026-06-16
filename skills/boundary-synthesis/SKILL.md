---
name: boundary-synthesis
description: Compile all boundary analysis products into a coherent report — validity
  envelopes, robustness results, failure catalogs, scaling maps, safe operating conditions.
execution: subagent
prompt: ./prompt.md
input: intermediate_products (string), synthesis_scope (string)
dependencies:
  sops:
  - spawn-agent
---

# Boundary Synthesis

Compile boundary analysis into a final report.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one synthesis report generation.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
