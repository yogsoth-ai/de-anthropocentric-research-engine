---
name: plan-formatting
description: Format task plan as bite-sized executable tasks following superpowers:writing-plans
  conventions
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
input: estimated and sequenced activity list with IOs
output: executable plan document with no TBD/TODO (HARD-GATE)
dependencies:
  sops:
  - spawn-agent
  - "superpowers:writing-plans"
---

# SOP: Plan Formatting

把任务信息格式化为 bite-sized 可执行 plan 这件事，**直接 `Skill` load
superpowers:writing-plans**，不再自造格式规则。writing-plans 自带 HARD-GATE
（零 TBD/TODO/占位符）。本 SOP 仅作为"调用 writing-plans"的路由点；如需子代理
承载，仍经 spawn-agent。

<!-- BEGIN available-tables (generated) -->
<!-- external rows hand-maintained; do not regenerate this file -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |
| superpowers:writing-plans | Produce a bite-sized, TDD-structured implementation plan from the spec |

<!-- END available-tables (generated) -->
