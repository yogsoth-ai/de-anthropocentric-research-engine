---
name: prisma-flowchart
description: Generate PRISMA-compliant flow data documenting the screening funnel
  — counts at each stage (identification, screening, eligibility, inclusion) with
  exclusion reasons. Used by systematic-survey via prisma-screening tactic.
execution: subagent
prompt: ./prompt.md
input: screening_data (string)
dependencies:
  sops:
  - spawn-agent
---

# PRISMA Flowchart

Generate PRISMA-compliant flow data from screening process.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Flow documentation requires aggregating data from multiple screening stages and producing a precise, standards-compliant document. Dedicated context for accuracy.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
