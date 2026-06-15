---
name: citation-network-analysis
description: Build and analyze patent citation networks — main path analysis, PageRank,
  cluster detection
execution: subagent
prompt: ./prompt.md
input: patent_citation_pairs
dependencies:
  sops:
  - spawn-agent
---

# Citation Network Analysis

Builds patent citation networks from citation pair data and performs structural analysis including main path identification, PageRank computation, and cluster detection.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
