---
name: discriminating-prediction-design
description: "SOP: 设计能区分竞争假设的关键预测和观察方案"
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: hypothesis-formulation
input: "竞争假设集（来自 competing-hypothesis-generation 输出）"
output: "区分性预测列表 + 建议观察/实验方法"
dependencies:
  skills:
    - subagent-spawning
---

# Discriminating Prediction Design
设计能在竞争假设之间做出区分的关键预测，为后续实验设计提供方向。

## HARD-GATE
<HARD-GATE>
前置条件（全部满足才能开始）:
1. 已有 ≥2 个竞争假设（含 unique_prediction 字段）
2. 每个假设有明确的 mechanism 描述

不满足 → 停止，返回错误：需要至少 2 个竞争假设才能设计区分性预测。
</HARD-GATE>

## Pipeline
1. 前置检查：验证竞争假设集完整性
2. 逐对比较：对每对假设，找出它们预测不同的情境
3. 分歧点识别：找到预测差异最大的条件或测量维度
4. 区分性观察/实验设计：设计能在分歧点上产生不同结果的观察或实验
5. 可行性评估：技术可行性 + 伦理可行性 + 资源需求
6. 输出区分性预测列表

## Output Format
```json
[
  {
    "comparison": "H1 vs CH1",
    "divergence_point": "The condition or measurement where predictions differ",
    "h1_prediction": "What H1 predicts in this condition",
    "ch1_prediction": "What CH1 predicts in this condition",
    "discriminating_observation": "The observation or experiment that would distinguish them",
    "method": "Suggested research method (experiment/survey/natural experiment/meta-analysis/etc.)",
    "feasibility": "high | medium | low",
    "feasibility_notes": "Why feasible or what barriers exist"
  }
]
```
覆盖所有主要假设对（primary vs. each competing）。
