---
name: patent-synthesis
description: Produce final structured patent intelligence report from all analysis
  results
execution: subagent
prompt: ./prompt.md
input: all_analysis_results
dependencies:
  sops:
  - spawn-agent
---

# Patent Synthesis

Produces the final structured patent intelligence report by synthesizing results from all upstream analysis SOPs into a coherent, actionable deliverable.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
