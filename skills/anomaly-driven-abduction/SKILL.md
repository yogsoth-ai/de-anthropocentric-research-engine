---
name: anomaly-driven-abduction
description: 'Tactic: 归纳/溯因路径——描述异常现象，生成候选解释，按可信度排序'
version: 1.0.0
category: hypothesis-formation
type: tactic
campaign: hypothesis-formulation
sops:
- anomaly-characterization
- explanation-generation
- plausibility-ranking
dependencies:
  sops:
  - anomaly-characterization
  - explanation-generation
  - plausibility-ranking
---

# Anomaly Driven Abduction

归纳/溯因路径——精确描述无法被现有理论解释的异常现象，生成多个候选解释，按可信度排序，为溯因假设提供结构化基础。

## 编排意图

溯因推理（abduction）的起点是"意外"——观察到的现象与现有理论预测不符。本 tactic 强制 CC 先精确描述异常（不允许模糊），再系统生成解释（不允许只想到一个），最后按可信度排序（不允许主观偏好）。

三步缺一不可：描述不精确则解释无法聚焦；解释不充分则排序无意义；排序无依据则假设选择变成猜测。

## 可用 SOPs

| SOP | 职责 | 何时调用 |
|-----|------|---------|
| anomaly-characterization | 精确描述异常现象：观察到什么、与预期的偏差、发生条件、已排除的平凡解释 | 所有模式必选，首先执行 |
| explanation-generation | 生成多个候选解释（溯因假设），每个解释必须能够完整解释异常 | 所有模式必选，在 anomaly-characterization 之后 |
| plausibility-ranking | 按可信度标准（先验概率、解释力、简洁性、可测试性）对候选解释排序 | 所有模式必选，最后执行 |

## 编排模式

**Simplified（S tier，单一异常）**
- 顺序执行：anomaly-characterization → explanation-generation（≥3 个解释）→ plausibility-ranking
- 适用：单一明确的异常现象，背景信息充分

**Standard（M tier，1-3 个相关异常）**
- anomaly-characterization 对每个异常独立执行；explanation-generation 生成 ≥3 个解释（可跨异常共享解释）；plausibility-ranking 对所有解释统一排序
- 适用：多个相关异常可能有共同解释，需要跨异常整合

**Deep（L tier，复杂异常集群）**
- 全部 3 个 SOP 执行；explanation-generation 额外要求：每个解释必须说明为何现有理论无法解释该异常；plausibility-ranking 额外输出：哪些解释可以被单一实验区分
- 适用：异常现象复杂、相互关联，需要系统性溯因分析

## Minimum Yield

- 结构化异常描述：含观察内容、与预期的偏差、发生条件、已排除的平凡解释
- ≥3 个候选解释，每个解释：
  - 完整解释异常的机制
  - 与现有理论的关系（扩展/修正/替代）
- 排序列表：含每个解释的可信度评分和排序依据

## Yield Report

执行结束后向调用方 strategy 报告：
- 异常描述完整度（是否满足 HARD-GATE 要求）
- 生成候选解释数 / 排序完成数
- 最高可信度解释（供 strategy 优先 formalize）
- 可区分性：哪些解释可以通过单一实验区分（供后续实验设计参考）
