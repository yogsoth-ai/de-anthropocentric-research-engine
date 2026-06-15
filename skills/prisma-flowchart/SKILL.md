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

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
