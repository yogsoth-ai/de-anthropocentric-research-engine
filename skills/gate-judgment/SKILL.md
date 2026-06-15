---
name: gate-judgment
description: Evaluate a candidate against gate criteria and render GO/KILL/RECYCLE
  verdict with evidence.
execution: subagent
prompt: ./prompt.md
input: candidate, gate_criteria
dependencies:
  sops:
  - spawn-agent
---

# Gate Judgment

Evaluate a specific candidate against defined gate criteria and render a verdict: GO (proceed to next stage), KILL (terminate), or RECYCLE (rework and re-evaluate). Every verdict is backed by evidence.

## Execution

Spawns a subagent that:
1. Receives candidate data and gate criteria specification
2. Evaluates candidate against each criterion
3. Applies the pass rule to determine overall verdict
4. Documents evidence for each criterion evaluation
5. Specifies conditions for advancement if verdict is not GO

## Why Subagent

Gate judgment must be rigorous and unbiased. A dedicated subagent applies criteria mechanically without emotional attachment to the candidate, ensuring honest evaluation.

## HARD-GATE

Output MUST include: verdict (GO/KILL/RECYCLE), per-criterion evaluation with evidence, and conditions for advancement. Reject if verdict is not supported by criterion-level evaluation.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
