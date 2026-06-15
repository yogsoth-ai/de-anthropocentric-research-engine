---
name: quality-gate-check
description: 'Shared SOP: verify quality gate criteria are met before proceeding'
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
input: Current deliverable + quality gate criteria
output: Gate verdict (PASS/FAIL) + gap list if FAIL
dependencies:
  sops:
  - spawn-agent
---

# Quality Gate Check

Verify quality gate criteria are met before proceeding to the next phase.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Quality gate verification requires independent assessment against criteria, free from sunk-cost bias of the producing agent.

## Gate Types

| Gate | Checks |
|------|--------|
| Budget Gate | Quantitative floor met (factor count, matrix rows, etc.) |
| Minimum Yield | Required deliverables present and non-trivial |
| HARD-GATE | Preconditions satisfied before starting |
| Completeness | All required sections/fields populated |
| Consistency | No internal contradictions |

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
