---
name: patent-categorization
description: Classify patents by tech subdomain, application scenario, and value chain
  position
execution: subagent
prompt: ./prompt.md
input: patent_list
dependencies:
  sops:
  - spawn-agent
---

# Patent Categorization

Classifies a list of patents into technology sub-domains, application scenarios, and value chain positions using their titles, abstracts, and IPC codes.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
