---
name: removal-path
description: Design concrete removal steps for a constraint with timeline and resource
  needs.
execution: subagent
prompt: ./prompt.md
input: constraint, removability_data
dependencies:
  sops:
  - spawn-agent
---

# Removal Path

Design a concrete, actionable path to remove or mitigate a constraint. Produces sequenced steps with timeline, resource requirements, and success criteria for each step.

## Execution

Spawns a subagent that:
1. Receives constraint details and removability assessment
2. Selects the best removal approach from those identified
3. Decomposes into concrete, sequenced steps
4. Estimates timeline and resources for each step
5. Defines success criteria and checkpoints

## Why Subagent

Removal path design requires creative problem-solving and detailed planning that benefits from focused attention without distraction from other assessment tasks.

## HARD-GATE

Output MUST include: at least 3 sequenced steps, timeline estimate, resource requirements, and success criteria for each step. Reject if steps are vague or unactionable.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
