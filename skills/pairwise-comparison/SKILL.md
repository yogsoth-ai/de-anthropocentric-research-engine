---
name: pairwise-comparison
description: 'Tactic: 通过相对比较而非绝对评分对 gaps 进行排序，适用于难以量化的场景'
version: 1.0.0
category: hypothesis-formation
type: tactic
campaign: gap-prioritization
sops:
- gap-pairwise-judgment
- consistency-check
- priority-synthesis
dependencies:
  sops:
  - consistency-check
  - gap-pairwise-judgment
  - priority-synthesis
  tactics:
  - hypothesis-formation-scoring-matrix-construction
---

# Pairwise Comparison

当绝对评分难以可靠执行时（gap 描述模糊、维度间不可比、评分者偏差大），通过两两相对比较建立 gap 排序，再经一致性检验确保判断无矛盾。

## 编排意图

绝对评分要求评分者对每个 gap 独立赋值，容易受锚定效应影响。相对比较（"A 比 B 更值得优先"）认知负担更低、判断更稳定。本 tactic 实现 AHP（层次分析法）风格的成对比较流程：先收集所有 gap 对的相对判断，再检验判断一致性，最后合成最终排序。

不一致判断（如 A>B、B>C、C>A 的循环）会被 consistency-check SOP 检测并触发修正轮次，直到一致性比率 CR < 0.1。

## 可用 SOPs

| SOP | 职责 | 何时调用 |
|-----|------|---------|
| gap-pairwise-judgment | 对每对 gap 做相对重要性判断（1-9 Saaty 量表） | 必选，第一步 |
| consistency-check | 计算一致性比率（CR），识别矛盾判断对 | 必选，每轮比较后 |
| priority-synthesis | 从成对比较矩阵合成最终优先级权重和排序 | 必选，CR 达标后 |

## 编排模式

**Default（标准流程）**
1. gap-pairwise-judgment：对所有 N×(N-1)/2 对 gap 执行比较，产出比较矩阵
2. consistency-check：计算 CR；若 CR ≥ 0.1，标记矛盾判断对并返回修正建议
3. （如需修正）重新调用 gap-pairwise-judgment 仅针对矛盾对，最多 3 轮
4. priority-synthesis：CR < 0.1 后合成最终排序

**Simplified（gap 数量 ≤ 5）**
- 同 Default，但比较对数少（≤10 对），通常一轮即可通过一致性检验

**Deep（gap 数量 > 15）**
- 先用 scoring-matrix-construction 做初步筛选，将 gap 缩减至 ≤15 个
- 再执行标准 pairwise 流程
- priority-synthesis 额外输出 sensitivity 分析（哪些 gap 排名对单次判断变化最敏感）

## Minimum Yield

- 完整的 N×N 成对比较矩阵（所有 gap 对均已判断，无缺失）
- 最终一致性比率 CR < 0.1（硬性约束，不可跳过）
- 最终优先级排序（含每个 gap 的归一化权重）
- 修正历史记录（若经历过矛盾修正，记录哪些判断被修改及原因）

## Yield Report

执行结束后向调用方 strategy 报告：
- Gap 数量 / 比较对数 / 修正轮次
- 最终 CR 值
- 排名前 3 的 gap 及其权重
- 排名最不稳定的 gap（权重与相邻 gap 差距 < 0.05 的情况）
