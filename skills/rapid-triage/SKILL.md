---
name: rapid-triage
description: "Strategy: 快速粗筛——两轮过滤将大量 gaps 压缩为可精排的候选集"
version: 1.0.0
category: hypothesis-formation
type: strategy
campaign: gap-prioritization
tactics:
  - scoring-matrix-construction
sops:
  - gap-normalization
  - importance-scoring
  - feasibility-scoring
  - priority-synthesis
dependencies:
  skills:
    - context-management
    - subagent-spawning
---

# Rapid Triage

快速粗筛：当 gap 数量极大（50+）时，先用二元过滤快速淘汰明显不合格的 gap，再对幸存者做轻量评分，将候选集压缩到可精排的规模。

## 适用场景

- gap 数量极大（50+），无法对每个 gap 做完整多维度评分
- 时间或计算资源有限，需要快速得到初步排序
- 作为 multi-criteria-ranking 或 portfolio-optimization 的前置步骤
- 需要向团队快速展示"哪些 gap 不值得考虑"

## 思维框架

**核心原则**：不要对垃圾做精细排序。先淘汰，再精排。

两轮过滤：

**第一轮：二元过滤（Keep / Drop）**
对每个 gap 问三个是非题：
- 这个 gap 在我们的研究范围内吗？（范围过滤）
- 这个 gap 在技术上是否可解决的（非哲学问题、非无限问题）？（可解性过滤）
- 这个 gap 是否已有充分的近期工作在解决？（新颖性过滤）

任一答案为"否"→ Drop。通过三关 → 进入第二轮。

**第二轮：轻量评分（1–3 分，两维度）**
对幸存 gap 只评两个维度：
- 重要性（1–3）：领域影响力的粗略估计
- 可行性（1–3）：以现有资源能否在 6 个月内取得进展

得分 = 重要性 × 可行性（最高 9 分）。取 top-K（K = 目标精排数量）进入下一阶段。

**关键洞察**：第一轮的三个问题必须快速回答（每个 gap 不超过 30 秒），不允许深度分析。速度是这个策略的核心价值。

## Budget Gate

| Tier | 输入 Gap 数量 | 第一轮保留率 | 第二轮输出 | 最终产出 |
|------|------------|------------|---------|---------|
| S | 50–80 | ≤60% | top-15 | 候选集 + 淘汰理由摘要 |
| M | 81–150 | ≤50% | top-20 | 候选集 + 淘汰理由摘要 |
| L | 150+ | ≤40% | top-30 | 候选集 + 淘汰理由摘要 + 分类统计 |

## 默认参考流

1. 调用 `gap-normalization` SOP：统一 gap 格式，为每个 gap 生成一句话摘要
2. 执行第一轮二元过滤：对每个 gap 回答三个是非题，标记 Keep / Drop
3. 记录 Drop 理由（范围外 / 不可解 / 已被充分研究）
4. 对 Keep 集合调用 `importance-scoring` SOP（1–3 分粗评）
5. 对 Keep 集合调用 `feasibility-scoring` SOP（1–3 分粗评）
6. 调用 `scoring-matrix-construction` tactic：构建轻量评分矩阵
7. 按重要性 × 可行性排序，取 top-K
8. 调用 `priority-synthesis` SOP：输出候选集 + 淘汰统计

## context-checkpoint

每轮结束后记录：
- 第一轮过滤结果（Keep/Drop 数量 + Drop 原因分布）
- 第二轮评分矩阵（幸存 gap × 2 维度）
- 最终候选集（top-K gap 列表）
- 建议的下一步策略（multi-criteria-ranking 或 portfolio-optimization）
