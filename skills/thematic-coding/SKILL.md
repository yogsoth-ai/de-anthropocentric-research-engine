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

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
