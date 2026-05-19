---
name: competing-hypothesis-construction
description: "Strategy: 为同一现象构建多个竞争假设"
version: 1.0.0
category: hypothesis-formation
type: strategy
campaign: hypothesis-formulation
tactics:
  - competing-hypothesis-matrix
sops:
  - competing-hypothesis-generation
  - discriminating-prediction-design
  - hypothesis-comparison-matrix
  - falsifiability-check
dependencies:
  skills:
    - context-management
    - subagent-spawning
    - literature-engine
---

# Competing Hypothesis Construction

为同一现象构建多个竞争假设：主动对抗 confirmation bias，通过并行构建真正不同的解释来保持认识论开放性，并设计能区分它们的判决性预测。

## 适用场景

- 研究者已有一个"偏好假设"，需要主动挑战它
- 现象有多种合理解释，过早收敛会导致错误方向
- 需要向审稿人或资助方展示已考虑替代解释
- 设计实验时需要确定哪个变量最能区分竞争解释

不适用：现象已有压倒性证据支持单一解释 → 直接用 deductive-hypothesis-generation 精化该解释。

## 思维框架

**Avoid confirmation bias by generating genuinely different explanations, then find discriminating predictions**

竞争假设构建的核心逻辑：

1. **强制多样性**：竞争假设必须在机制层面真正不同，而非同一机制的变体
2. **对称对待**：每个假设都以同等严肃性对待，不允许偏好假设获得特殊待遇
3. **区分性预测**：找到能区分假设的判决性预测——什么结果支持 H1 但反对 H2，反之亦然
4. **矩阵化比较**：通过系统矩阵揭示假设间的结构性差异

**竞争假设的质量标准**：
- **真正竞争**：两个假设对同一现象给出不同的因果解释（不是同一解释的强弱版本）
- **互斥性**：至少存在一个观察结果，能支持其中一个而反对另一个
- **可比较性**：两个假设都有明确的可测试预测

## Budget Gate

| Tier | 竞争假设数 | 区分性预测 | 比较矩阵 | 可证伪性 |
|------|---------|---------|---------|---------|
| S | ≥2 个真正竞争的假设 | ≥1 个区分性预测 | 简化版（2×2） | 每个假设 1 个 falsification scenario |
| M | ≥3 个竞争假设 | ≥2 个区分性预测 | 完整矩阵（假设×预测） | 每个假设完整 falsification |
| L | ≥4 个竞争假设 | ≥3 个区分性预测 | 完整矩阵 + 实验设计建议 | 完整 falsifiability audit |

## 默认参考流

1. 调用 `competing-hypothesis-generation` SOP（via `competing-hypothesis-matrix` tactic）：强制生成机制层面真正不同的竞争假设
2. 调用 `discriminating-prediction-design` SOP：为每对竞争假设设计区分性预测
3. 调用 `hypothesis-comparison-matrix` SOP：构建假设×预测比较矩阵，揭示结构性差异
4. 调用 `falsifiability-check` SOP：为每个假设生成 falsification scenario

## context-checkpoint

每轮结束后记录：
- 竞争假设清单（每个假设的核心机制声明）
- 机制差异分析（假设间在哪个层面真正不同）
- 区分性预测列表（每个预测能区分哪对假设）
- 比较矩阵（假设×预测，标注支持/反对/中性）
- 推荐的判决性实验方向
