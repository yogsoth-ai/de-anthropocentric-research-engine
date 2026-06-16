---
name: sensitivity-synthesis
description: Synthesize all sensitivity analysis results into a coherent report with
  prioritized recommendations.
execution: subagent
prompt: ./prompt.md
input: screening_results, decomposition_results, assumption_criticality, propagation_results,
  decision_sensitivity
dependencies:
  sops:
  - spawn-agent
---

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one complete synthesis report across all sensitivity analysis components.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
