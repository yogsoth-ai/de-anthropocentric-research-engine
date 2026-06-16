---
name: egm-construction
description: Build structured Evidence Gap Maps — define axes (intervention × outcome
  or method × domain), place gaps in cells, annotate with evidence density and quality.
execution: subagent
prompt: ./prompt.md
input: classified_gaps (string), axis_definitions (string)
dependencies:
  sops:
  - spawn-agent
---

# EGM Construction

Build structured Evidence Gap Maps for visual gap representation.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one EGM construction from classified gaps.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
