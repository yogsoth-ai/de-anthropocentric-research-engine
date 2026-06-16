---
name: coverage-gap-detection
description: Detect uncovered regions in the solution space, producing a prioritized
  gap list.
execution: subagent
prompt: ./prompt.md
input: coverage_analysis (object)
dependencies:
  sops:
  - spawn-agent
---

# Coverage Gap Detection

Detect uncovered regions in the solution space and prioritize them for targeted generation.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Gap detection requires comparing actual coverage against theoretical completeness. Benefits from focused context to systematically scan all dimensions without missing regions.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
