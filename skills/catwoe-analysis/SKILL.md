---
name: catwoe-analysis
description: Apply Checkland's CATWOE analysis from a specific stakeholder perspective
  to reveal how the problem looks from that viewpoint.
execution: subagent
prompt: ./prompt.md
input: system_description, stakeholder_perspective
dependencies:
  sops:
  - spawn-agent
---

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one CATWOE analysis from one stakeholder perspective.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
