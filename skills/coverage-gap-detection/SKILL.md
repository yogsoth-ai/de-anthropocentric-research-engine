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

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
