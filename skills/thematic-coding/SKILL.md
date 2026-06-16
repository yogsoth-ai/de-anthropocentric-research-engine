---
name: thematic-coding
description: Identify recurring themes across papers using qualitative coding methodology.
  Produces a codebook with theme definitions, supporting evidence, and frequency counts.
  Used by narrative-review.
execution: subagent
prompt: ./prompt.md
input: paper_notes (string)
dependencies:
  sops:
  - spawn-agent
---

# Thematic Coding

Identify recurring themes across papers using qualitative coding methodology.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Thematic coding requires iterative comparison across all papers simultaneously — reading, coding, comparing, refining codes. Dedicated context for this qualitative analysis.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
