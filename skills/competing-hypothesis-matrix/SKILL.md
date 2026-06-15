---
name: competing-hypothesis-matrix
description: 'Tactic: 多假设管理——生成竞争假设，设计区分性预测，构建结构化比较矩阵'
version: 1.0.0
category: hypothesis-formation
type: tactic
campaign: hypothesis-formulation
sops:
- competing-hypothesis-generation
- discriminating-prediction-design
- hypothesis-comparison-matrix
dependencies:
  sops:
  - competing-hypothesis-generation
  - discriminating-prediction-design
  - hypothesis-comparison-matrix
---

# Competing Hypothesis Matrix

多假设管理——系统生成与主假设竞争的替代解释，设计能区分它们的关键预测，并构建结构化比较矩阵，避免 confirmation bias。

## 编排意图

科学推理中最危险的偏差是只持有一个假设。本 tactic 强制 CC 在确定"最优"假设之前，先系统构建竞争假设，再设计能将它们区分开来的预测。

三步不可颠倒：先生成竞争假设（不允许跳过），再设计区分性预测（不允许只比较，不测试），最后构建比较矩阵（不允许只列举，不量化）。最终产出不是"哪个假设是对的"，而是"用什么实验能区分它们"。

## 可用 SOPs

| SOP | 职责 | 何时调用 |
|-----|------|---------|
| competing-hypothesis-generation | 基于主假设，生成 ≥3 个与之竞争的替代假设（不同机制，相同或相似的现象预测范围） | 所有模式必选，首先执行 |
| discriminating-prediction-design | 为每对竞争假设设计区分性预测——找到一个观察结果，使两个假设预测不同 | 所有模式必选，在 competing-hypothesis-generation 之后 |
| hypothesis-comparison-matrix | 将所有假设和区分性预测组装为结构化比较矩阵，标注各假设对每个预测的预期结果 | 所有模式必选，最后执行 |

## 编排模式

**Simplified（S tier，1 个主假设）**
- 顺序执行全部 3 个 SOP；生成 ≥3 个竞争假设；设计 ≥2 个区分性预测；构建比较矩阵
- 适用：单一主假设，需要竞争性思维检验

**Standard（M tier，2-3 个主假设）**
- competing-hypothesis-generation 为每个主假设独立生成竞争假设；discriminating-prediction-design 跨主假设和竞争假设设计区分性预测；hypothesis-comparison-matrix 包含所有假设（主 + 竞争）
- 适用：已有多个候选假设，需要统一管理和比较

**Deep（L tier，复杂假设集）**
- 全部 3 个 SOP 执行；competing-hypothesis-generation 额外要求：至少 1 个竞争假设来自完全不同的理论框架；discriminating-prediction-design 额外要求：每个区分性预测标注所需实验规模和难度；hypothesis-comparison-matrix 额外输出：推荐的实验优先级（最有区分力的预测排前）
- 适用：假设空间复杂，需要为实验设计提供直接输入

## Minimum Yield

- ≥3 个竞争假设（与主假设解释相同现象但机制不同）
- ≥2 个区分性预测（每个预测对至少 2 个假设产生不同的预期结果）
- 结构化比较矩阵：假设 × 预测，每格标注预期结果方向（支持/反对/无关）

## Yield Report

执行结束后向调用方 strategy 报告：
- 竞争假设数 / 区分性预测数
- 最有区分力的预测（能同时区分最多假设对）
- 最难区分的假设对（预测几乎相同，需要极精细的实验设计）
- 推荐优先测试的假设（最易被证伪 + 区分性最强）

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| competing-hypothesis-generation | SOP: 为同一现象生成机制上不同的竞争假设 |
| discriminating-prediction-design | SOP: 设计能区分竞争假设的关键预测和观察方案 |
| hypothesis-comparison-matrix | SOP: 构建竞争假设的多维度对比矩阵 |

<!-- END available-tables (generated) -->
