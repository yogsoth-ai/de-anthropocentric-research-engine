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

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
