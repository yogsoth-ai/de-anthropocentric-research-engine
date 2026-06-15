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

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
