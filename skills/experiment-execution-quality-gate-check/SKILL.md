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

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
