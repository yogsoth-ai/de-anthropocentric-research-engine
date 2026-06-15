---
name: abductive-hypothesis-generation
description: 'Strategy: 面对异常的最佳解释推理'
version: 1.0.0
category: hypothesis-formation
type: strategy
campaign: hypothesis-formulation
tactics:
- anomaly-driven-abduction
sops:
- anomaly-characterization
- explanation-generation
- plausibility-ranking
- falsifiability-check
dependencies:
  tactics:
  - anomaly-driven-abduction
  sops:
  - falsifiability-check
---

# Abductive Hypothesis Generation

面对异常的最佳解释推理：当观察到现有理论无法解释的异常现象时，系统生成候选解释并选出最合理者作为假设。

## 适用场景

- 观察到明确的异常现象（与现有理论预测不符的结果）
- 现有理论无法充分解释某个已知现象
- 需要在多个竞争解释中选出最值得检验的一个
- 研究起点是"这个结果很奇怪，为什么？"

不适用：没有明确异常、只是想探索一个新领域 → 改用 inductive-hypothesis-generation。

## 思维框架

**Anomaly → Generate candidate explanations → Rank by plausibility → Best explanation = hypothesis**

溯因推理的核心逻辑：

1. **Anomaly**：精确描述异常——什么现象、与什么预期不符、偏差有多大
2. **Generate candidate explanations**：系统生成所有能解释该异常的候选解释（不过早筛选）
3. **Rank by plausibility**：按可信度排序——哪个解释最简洁、最与已知事实一致、最可检验
4. **Best explanation = hypothesis**：选出最合理的解释作为工作假设，其余作为竞争假设保留

**溯因的核心原则**：
- **奥卡姆剃刀**：在解释力相当时，优先选择假设更少的解释
- **一致性**：最佳解释不应与其他已知事实矛盾
- **可检验性**：最佳解释必须能产生可观测的预测（否则无法验证）
- **生成完整性**：在排序前必须穷举候选解释，避免过早收敛

## Budget Gate

| Tier | 异常描述 | 候选解释 | 假设产出 | 竞争假设 |
|------|---------|---------|---------|---------|
| S | 1 个精确描述的异常 | ≥2 个候选解释 | 1 个最佳解释假设 | ≥1 个竞争假设保留 |
| M | 1–2 个异常 | ≥3 个候选解释 | ≥2 个结构化假设 | 完整可信度排序 |
| L | ≥2 个相关异常 | ≥5 个候选解释 | ≥3 个结构化假设 | 完整排序 + 区分性预测设计 |

## 默认参考流

1. 调用 `anomaly-characterization` SOP：精确描述异常（现象、预期、偏差、已排除的平凡解释）
2. 调用 `explanation-generation` SOP（via `anomaly-driven-abduction` tactic）：系统生成候选解释（不过早筛选）
3. 调用 `plausibility-ranking` SOP：按简洁性、一致性、可检验性对候选解释排序
4. 调用 `falsifiability-check` SOP：为最佳解释生成 falsification scenario，确认其可检验性

## context-checkpoint

每轮结束后记录：
- 异常描述（精确版本，含偏差量化）
- 候选解释清单（含已排除的平凡解释及排除理由）
- 可信度排序结果（含排序依据）
- 最佳解释假设 + 竞争假设列表
- 区分性预测（什么实验能区分最佳解释与竞争解释）
