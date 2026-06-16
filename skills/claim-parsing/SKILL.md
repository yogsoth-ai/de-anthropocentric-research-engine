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

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
