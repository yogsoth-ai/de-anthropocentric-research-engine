---
name: quality-scoring
description: Multi-dimensional patent quality assessment — forward citations, family
  size, claim count, geographic breadth
execution: subagent
prompt: ./prompt.md
input: patent_metadata
dependencies:
  sops:
  - spawn-agent
---

# Quality Scoring

Performs multi-dimensional quality assessment of patents using quantitative indicators: forward citation count, family size, claim count, geographic breadth, and prosecution history.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
