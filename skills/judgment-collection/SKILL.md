---
name: judgment-collection
description: Collect independent judgments from all perspectives on a given question.
execution: subagent
prompt: ./prompt.md
input: question, perspectives[]
dependencies:
  sops:
  - spawn-agent
---

# Judgment Collection

Collect independent judgments from each perspective on the focal question. Each perspective provides its rating/estimate and supporting reasoning without seeing others' responses.

## Execution

Spawn a subagent that takes the question and list of perspectives, then generates an independent judgment from each perspective's viewpoint. Judgments include both a structured response (rating, probability, or position) and free-text reasoning.

## Why Subagent

- Each perspective must be generated independently without cross-contamination
- The collection task is well-bounded and parallelizable
- Keeps the parent context clean for orchestration logic

## HARD-GATE

Output MUST contain: one judgment object per perspective, each with `perspective_id`, `response`, and `reasoning` fields. Missing any perspective fails the gate.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
