---
name: experiment-running
description: Execute the plan by dispatching fresh subagents per task, monitoring
  status, and collecting results
version: 1.0.0
category: experiment-execution
type: strategy
sops:
- implementer-dispatch
- execution-monitoring
- result-collection
tactics:
- subagent-execution-loop
- checkpoint-and-recover
dependencies:
  sops:
  - execution-monitoring
  - implementer-dispatch
  - result-collection
  - "ponytail:ponytail"
  - "ponytail:ponytail-debt"
  - "superpowers:executing-plans"
  - "superpowers:finishing-a-development-branch"
  - "superpowers:subagent-driven-development"
  - "superpowers:using-git-worktrees"
  - "superpowers:verification-before-completion"
  tactics:
  - checkpoint-and-recover
  - subagent-execution-loop
---

# Strategy: Experiment Running

**Key Question**: How to execute?

## Methodology

实现的执行**直接交给 superpowers 现成链路**，不再自写 fresh-subagent / 三段 review。
plan（上游 plan-writing 产出）就绪后，本策略是一串决策节点：

1. `Skill` load **superpowers:using-git-worktrees** —— 建隔离工作区 + 跑 baseline 测试。
2. `Skill` load **ponytail:ponytail** —— 进入写代码前开启精简反射（边写边 lean）。
3. 二选一执行引擎：
   - **superpowers:executing-plans**（本 session 批量执行，带 checkpoint），或
   - **superpowers:subagent-driven-development**（每任务 fresh 子代理 + 两段 review）。
   多数实验实现用前者；任务高度独立、需强隔离时用后者（详见 subagent-execution-loop）。
4. `Skill` load **superpowers:verification-before-completion** —— claim 完成前先跑证明命令。
5. `Skill` load **ponytail:ponytail-debt** —— 收尾前收集 `ponytail:` 欠债标记。
6. `Skill` load **superpowers:finishing-a-development-branch** —— 验证测试 → merge/PR/branch。

DARE 原生的 checkpoint-and-recover（高风险操作前存档）与 subagent-execution-loop
（执行循环细节）作为 tactic 仍在编排内保留。

## Execution Flow

```
[plan from plan-writing]
    → superpowers:using-git-worktrees   (隔离区 + baseline)
    → ponytail:ponytail                 (精简反射开启)
    → superpowers:executing-plans  或  superpowers:subagent-driven-development
    → superpowers:verification-before-completion  (claim 前验证)
    → ponytail:ponytail-debt            (收欠债)
    → superpowers:finishing-a-development-branch  (收尾)
```

## Budget Gate

| Step | Max Budget | Output |
|------|-----------|--------|
| Per-task execution | 50% of execution budget / N tasks | Task result |
| Monitoring overhead | 5% of execution budget | Status log |
| Retry budget | 10% of execution budget | Unblocked tasks |

## Key Decisions

- **执行引擎二选一**：批量 → executing-plans；强隔离/逐任务审查 → subagent-driven-development
- **model 选择 / retry / 并行**：交给所选 superpowers 引擎，不在本策略重定义
- **Abort**：>50% 关键路径 BLOCKED 时中止并报告（DARE 排程层判据）

<!-- BEGIN available-tables (generated) -->
<!-- external rows hand-maintained; do not regenerate this file -->

## Available Tactics

Optional, no fixed order; the final leaf is always a sop.

| Tactic | When to use |
| --- | --- |
| checkpoint-and-recover | Checkpoint state before risky operations, detect anomalies, and recover gracefully |
| subagent-execution-loop | Orchestrate task execution via fresh subagents with dispatch, monitoring, and result collection |

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| execution-monitoring | Monitor execution progress, detect anomalies, and report status |
| implementer-dispatch | Dispatch execution subagent — select model by complexity, construct prompt with full task context |
| ponytail:ponytail | Lazy-senior reflex: simplest thing that holds; mark every deliberate shortcut |
| ponytail:ponytail-debt | Harvest ponytail debt markers before finishing |
| result-collection | Collect experiment outputs — metrics, logs, artifacts — into structured result set |
| superpowers:executing-plans | Execute the plan task-by-task in the current session with checkpoints |
| superpowers:finishing-a-development-branch | Verify tests -> merge / PR / branch cleanup |
| superpowers:subagent-driven-development | Execute the plan via a fresh subagent per task with two-stage review |
| superpowers:using-git-worktrees | Create an isolated worktree + run baseline tests before implementing |
| superpowers:verification-before-completion | Run the proving command and confirm output before claiming done |

<!-- END available-tables (generated) -->
