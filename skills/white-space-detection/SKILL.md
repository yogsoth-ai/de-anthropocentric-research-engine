---
name: white-space-detection
description: Identify matrix regions not covered by existing methods
execution: subagent
prompt: ./prompt.md
input: matrix (object), known_methods_mapping (object)
dependencies:
  sops:
  - spawn-agent
---

# White Space Detection

Identify regions of the morphological matrix not covered by any existing method or solution.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

White space detection requires mapping known solutions onto the matrix, identifying gaps, and reasoning about why those gaps exist (overlooked vs infeasible vs unexplored).

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
