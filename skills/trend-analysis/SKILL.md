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

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
