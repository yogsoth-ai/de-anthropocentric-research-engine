---
name: categorize-papers
description: Cluster papers by theme, method, or timeline. Produces natural groupings
  from a paper collection. Used by scoping-survey and narrative-review.
execution: subagent
prompt: ./prompt.md
input: paper_list (string)
dependencies:
  sops:
  - spawn-agent
---

# Categorize Papers

Cluster papers by theme/method/timeline into natural groupings.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Categorization requires holding the entire paper collection in context simultaneously to identify patterns and groupings. Subagent provides dedicated space for this comparative analysis.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
