---
name: claim-parsing
description: Patent claim syntax parsing — independent/dependent relationships and
  element extraction
execution: subagent
prompt: ./prompt.md
input: claim_text
dependencies:
  sops:
  - spawn-agent
---

# Claim Parsing

Parses patent claim text into structured components: identifies independent vs. dependent claims, extracts individual elements (limitations), and maps claim hierarchy.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
