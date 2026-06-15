---
name: relationship-specification
description: 'SOP: 指定变量间关系的方向与形式'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: hypothesis-formulation
input: 变量对列表（来自 variable-identification 输出）
output: 关系规格列表：方向 + 函数形式 + 理论依据
dependencies:
  skills:
  - subagent-spawning
---

# Relationship Specification
对每对关键变量，指定关系方向（正/负）和函数形式（线性/非线性/U型/阈值），并引用理论依据。

## HARD-GATE
<HARD-GATE>
前置条件（全部满足才能开始）:
1. 已有至少 1 个 IV + 1 个 DV 的变量对
2. 相关机制或理论信息已提供（用于判断关系形式）

不满足 → 停止，返回错误：无法确定关系，缺少变量对或理论依据。
</HARD-GATE>

## Pipeline
1. 前置检查：验证变量对完整性
2. 方向判定：对每对变量判定关系方向（正向/负向/双向/无方向）
3. 形式判定：判断关系的函数形式（线性/非线性/U型/倒U型/阈值/饱和）
4. 理论依据引用：为每个判定引用支持该关系形式的理论或经验证据
5. 不确定性标注：若方向/形式存在争议，标注竞争预测
6. 输出结构化关系规格列表

## Output Format
```json
[
  {
    "pair": "IV_name → DV_name",
    "direction": "positive | negative | bidirectional | unknown",
    "form": "linear | nonlinear | U-shaped | inverted-U | threshold | saturating | unknown",
    "theoretical_basis": "Theory or evidence supporting this specification",
    "competing_prediction": "Alternative specification if contested (null if uncontested)",
    "confidence": "high | medium | low"
  }
]
```
至少覆盖所有 IV→DV 对；可选包含 IV→mediator 和 mediator→DV。
