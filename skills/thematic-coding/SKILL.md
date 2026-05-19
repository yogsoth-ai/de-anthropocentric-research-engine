---
name: thematic-coding
description: Identify recurring themes across papers using qualitative coding methodology. Produces a codebook with theme definitions, supporting evidence, and frequency counts. Used by narrative-review.
execution: subagent
prompt: ./prompt.md
input: paper_notes (string)
used-by: literature-survey
---

# Thematic Coding

Identify recurring themes across papers using qualitative coding methodology.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Thematic coding requires iterative comparison across all papers simultaneously — reading, coding, comparing, refining codes. Dedicated context for this qualitative analysis.
