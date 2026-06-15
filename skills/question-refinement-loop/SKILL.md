---
name: question-refinement-loop
description: 'Tactic: 迭代精化研究问题直到通过 FINER 5 项标准'
version: 1.0.0
category: hypothesis-formation
type: tactic
campaign: research-question
sops:
- finer-criteria-check
- scope-assessment
- success-criteria-definition
dependencies:
  sops:
  - finer-criteria-check
  - scope-assessment
  - success-criteria-definition
---

# Question Refinement Loop

迭代精化研究问题 — 反复打磨直到通过 FINER 5 项标准。

## 编排意图

将"精化问题"结构化为：检验 → 识别问题 → 修正 → 重新检验的循环。每轮聚焦于未通过的标准项。

## 可用 SOPs

| SOP | 职责 | 何时调用 |
|-----|------|---------|
| finer-criteria-check | FINER 5 项标准逐项检验 | 每轮循环的检验步骤 |
| scope-assessment | 评估问题范围是否合适 | 当 F(Feasible) 不通过时 |
| success-criteria-definition | 定义可测量的成功标准 | 循环结束后，确认 RQ 可衡量 |

## 编排模式

**标准循环**:
1. finer-criteria-check → 获得 5 项判定
2. 如果全通过 → 调用 success-criteria-definition → 结束
3. 如果有未通过项 → 针对性修正:
   - F 不通过 → scope-assessment → 缩小范围
   - I 不通过 → 增强理论动机
   - N 不通过 → 检查文献确认新颖性
   - E 不通过 → 调整研究设计
   - R 不通过 → 强化实践意义
4. 修正后回到步骤 1

**最大迭代**: 3 轮。超过 3 轮仍不通过 → 报告哪项持续不通过 + 建议根本性调整方向。

## Minimum Yield

- RQ 通过 FINER 5/5
- Success criteria 定义完成（可测量）
- 如果 3 轮未通过：明确报告问题项 + 建议

## Yield Report

执行完成后报告:
- 迭代轮次
- 每轮的 FINER 结果
- 最终 RQ 表述
- Success criteria
