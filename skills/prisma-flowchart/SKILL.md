---
name: prisma-flowchart
description: Generate PRISMA-compliant flow data documenting the screening funnel — counts at each stage (identification, screening, eligibility, inclusion) with exclusion reasons. Used by systematic-survey via prisma-screening tactic.
execution: subagent
prompt: ./prompt.md
input: screening_data (string)
used-by: literature-survey
---

# PRISMA Flowchart

Generate PRISMA-compliant flow data from screening process.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Flow documentation requires aggregating data from multiple screening stages and producing a precise, standards-compliant document. Dedicated context for accuracy.
