---
name: subagent-execution-loop
description: Orchestrate task execution via fresh subagents with dispatch, monitoring,
  and result collection
version: 1.0.0
category: experiment-execution
type: tactic
orchestrates:
- implementer-dispatch
- execution-monitoring
- result-collection
dependencies:
  sops:
  - execution-monitoring
  - implementer-dispatch
  - result-collection
  - "ponytail:ponytail"
  - "ponytail:ponytail-review"
  - "superpowers:receiving-code-review"
  - "superpowers:requesting-code-review"
  - "superpowers:subagent-driven-development"
  - "superpowers:test-driven-development"
---

# Tactic: Subagent Execution Loop

## Orchestration Pattern

执行循环**直接 load superpowers:subagent-driven-development 当引擎**，不再自写循环伪码。
每个任务在引擎内部按以下贯穿规则执行：

1. `Skill` load **ponytail:ponytail** —— 任务开始即开启精简反射。
2. `Skill` load **superpowers:test-driven-development** —— 每任务 RED → GREEN → REFACTOR。
3. `Skill` load **superpowers:requesting-code-review** —— 任务 diff 出来后派 reviewer 子代理。
4. `Skill` load **ponytail:ponytail-review** —— code-review 之后，对 diff 再过一道
   过度工程审（delete/stdlib/native/yagni/shrink）。
5. `Skill` load **superpowers:receiving-code-review** —— 核验 review 反馈再落地，反馈错就反驳。

DARE 原生的 implementer-dispatch / execution-monitoring / result-collection 作为
引擎内每任务的派单、盯状态、收结果三步保留。

## Decision Criteria

| Condition | Action |
|-----------|--------|
| model 选择 / retry / 超时 / 死锁 | 交给 superpowers:subagent-driven-development 引擎处理 |
| code-review 后 | 先 ponytail:ponytail-review 查过度工程，再 receiving-code-review 落地 |
| Budget < 10% remaining | 停，报告 partial（DARE 预算治理） |
| >50% 关键路径 BLOCKED | 中止执行（DARE 排程判据） |

## Error Recovery

- Timeout: Restore from checkpoint, mark task BLOCKED
- Validation failure: Provide failure reason in retry prompt
- Deadlock: Analyze dependency graph for unresolvable cycles
- Budget exhaustion: Produce partial report with remaining task list

<!-- BEGIN available-tables (generated) -->
<!-- external rows hand-maintained; do not regenerate this file -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| execution-monitoring | Monitor execution progress, detect anomalies, and report status |
| implementer-dispatch | Dispatch execution subagent — select model by complexity, construct prompt with full task context |
| ponytail:ponytail | Lazy-senior reflex: simplest thing that holds; mark every deliberate shortcut |
| ponytail:ponytail-review | Audit the diff for over-engineering (delete/stdlib/native/yagni/shrink) |
| result-collection | Collect experiment outputs — metrics, logs, artifacts — into structured result set |
| superpowers:receiving-code-review | Verify review feedback before applying; push back when wrong |
| superpowers:requesting-code-review | Dispatch a code-reviewer subagent after each task |
| superpowers:subagent-driven-development | Execute the plan via a fresh subagent per task with two-stage review |
| superpowers:test-driven-development | RED -> GREEN -> REFACTOR per task |

<!-- END available-tables (generated) -->
