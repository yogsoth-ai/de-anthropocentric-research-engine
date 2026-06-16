---
name: implementer-dispatch
description: Dispatch execution subagent — select model by complexity, construct prompt
  with full task context
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
input: task specification from executable plan
output: dispatched subagent with constructed prompt and selected model
dependencies:
  sops:
  - spawn-agent
  - "superpowers:subagent-driven-development"
---

# SOP: Implementer Dispatch

为任务选 model、构造执行 prompt、派子代理这件事，**派单逻辑交给
superpowers:subagent-driven-development**（它管 model 选择 / prompt 构造 / 两段
review）。本 SOP 降为"调用 subagent-driven"的路由点；如需 DARE 自有子代理承载，
仍经 spawn-agent。

<!-- BEGIN available-tables (generated) -->
<!-- external rows hand-maintained; do not regenerate this file -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |
| superpowers:subagent-driven-development | Execute the plan via a fresh subagent per task with two-stage review |

<!-- END available-tables (generated) -->
