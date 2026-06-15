---
name: trend-analysis
description: Patent filing volume time-series, technology lifecycle stage, and S-curve
  analysis
execution: subagent
prompt: ./prompt.md
input: patent_filing_data
dependencies:
  sops:
  - spawn-agent
---

# Trend Analysis

Analyzes patent filing volume over time, identifies technology lifecycle stages, and fits S-curve models to predict maturity and future filing activity.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
