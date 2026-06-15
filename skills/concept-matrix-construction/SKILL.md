---
name: concept-matrix-construction
description: Build articles × concepts coverage matrix to visualize research landscape
  and identify empty cells as gap candidates.
execution: subagent
prompt: ./prompt.md
input: paper_collection (string), concept_list (string)
dependencies:
  sops:
  - spawn-agent
---

# Concept Matrix Construction

Build coverage matrices to visualize where research is dense vs absent.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one concept matrix construction from a paper collection.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
