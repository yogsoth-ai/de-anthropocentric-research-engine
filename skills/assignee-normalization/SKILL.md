---
name: assignee-normalization
description: Standardize assignee names and identify corporate group affiliations
  across patent offices
execution: subagent
prompt: ./prompt.md
input: raw_assignee_list
dependencies:
  sops:
  - spawn-agent
---

# Assignee Normalization

Standardizes patent assignee names across different patent offices and identifies corporate group affiliations (parent companies, subsidiaries, acquired entities).

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
