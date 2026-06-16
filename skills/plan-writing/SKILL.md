---
name: plan-writing
description: Format critical path and prerequisites into bite-sized executable plan
  following superpowers:writing-plans conventions
version: 1.0.0
category: experiment-execution
type: strategy
sops:
- plan-formatting
tactics:
- task-decomposition
dependencies:
  sops:
  - plan-formatting
  - "superpowers:brainstorming"
  - "superpowers:writing-plans"
  tactics:
  - task-decomposition
---

# Strategy: Plan Writing

**Key Question**: How to write it as an executable plan?

## Methodology

实现 spec 与 plan 的产出**直接交给 superpowers 现成链路**，不再自造 bite-sized 规则。

排程层（critical-path-planning / prerequisite-planning / task-decomposition）产出
任务 DAG、关键路径、工期后，本策略：

1. `Skill` load **superpowers:brainstorming** —— 把 ③ experiment-design 的科学实验设计
   当输入，完整跑一趟（clarify → approaches → 实现 spec → self-review → 用户 gate），
   产出**实现 spec**。
2. brainstorming 终态自动转 **superpowers:writing-plans** —— 产出 bite-sized、
   TDD 结构的可执行 plan。

排程层的任务 DAG 作为 brainstorming/writing-plans 的输入上下文传入。

## Execution Flow

```
[排程层: 关键路径 + IO 序列]
    → Skill load superpowers:brainstorming  (科学设计 → 实现 spec, 自带用户 gate)
        → 终态自动 → superpowers:writing-plans  (出 bite-sized plan)
```

## Budget Gate

| Step | Max Budget | Output |
|------|-----------|--------|
| Plan formatting | 5% | Complete task plan |
| Validation pass | 2% | Confirmed no placeholders |

## Quality Criteria

A valid plan has:
- [ ] Every task has: ID, description, inputs, expected output, success criterion
- [ ] Every file path is absolute
- [ ] Every task is independently executable (no hidden dependencies)
- [ ] Critical path tasks are marked
- [ ] Buffer tasks (non-critical) are identified with float values
- [ ] No TBD/TODO/placeholder text anywhere
- [ ] Estimated duration per task (from PERT)

<!-- BEGIN available-tables (generated) -->
<!-- external rows hand-maintained; do not regenerate this file -->

## Available Tactics

Optional, no fixed order; the final leaf is always a sop.

| Tactic | When to use |
| --- | --- |
| task-decomposition | Orchestrate the breakdown of experiment design into sequenced, estimated, and formatted task plan |

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| plan-formatting | Format task plan as bite-sized executable tasks following superpowers:writing-plans conventions |
| superpowers:brainstorming | Turn the experiment design into an implementation spec (clarify -> approaches -> spec -> self-review -> user gate) |
| superpowers:writing-plans | Produce a bite-sized, TDD-structured implementation plan from the spec |

<!-- END available-tables (generated) -->
