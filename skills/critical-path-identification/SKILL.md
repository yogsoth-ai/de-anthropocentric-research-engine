---
name: critical-path-identification
description: Identify which input uncertainties contribute most to output uncertainty
  and compute EVPI for research prioritization.
execution: subagent
prompt: ./prompt.md
input: propagation_results, input_output_relationships
dependencies:
  sops:
  - spawn-agent
---

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one complete critical path analysis (importance ranking, EVPI computation, recommendations).

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
