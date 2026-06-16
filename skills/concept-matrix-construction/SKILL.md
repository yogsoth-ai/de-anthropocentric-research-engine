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

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
