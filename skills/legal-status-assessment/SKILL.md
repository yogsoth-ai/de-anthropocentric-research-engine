---
name: legal-status-assessment
description: Determine patent legal status — active, expired, pending, lapsed, or
  revoked
execution: subagent
prompt: ./prompt.md
input: patent_identifiers
dependencies:
  sops:
  - spawn-agent
---

# Legal Status Assessment

Determines the current legal status of patents (active/granted, pending/application, expired, lapsed, revoked) based on available metadata and filing information.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
