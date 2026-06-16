---
name: white-space-mapping
description: Feature cross-matrix construction and blank area identification for patent
  opportunity mapping
execution: subagent
prompt: ./prompt.md
input: feature_dimensions, existing_patents
dependencies:
  sops:
  - spawn-agent
---

# White Space Mapping

Constructs multi-dimensional feature cross-matrices from patent data and identifies blank areas representing unprotected technology combinations.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
