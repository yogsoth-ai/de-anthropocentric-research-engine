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

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
