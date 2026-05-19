---
name: operationalization
description: "SOP: 将抽象概念操作化为可测量的指标和方法"
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: hypothesis-formulation
input: "抽象变量描述（来自 variable-identification 输出）"
output: "操作定义 + 测量方法 + 效度论证（内容/构念/标准）"
dependencies:
  skills:
    - subagent-spawning
---

# Operationalization
将假设中的抽象概念转化为具体可测量的指标，并论证测量有效性。

## HARD-GATE
<HARD-GATE>
前置条件（全部满足才能开始）:
1. 已有至少 1 个需要操作化的变量（operationalizable ≠ "high" 时尤其需要）
2. 变量的理论定义已提供（来自 variable-identification 的 description 字段）

不满足 → 停止，返回错误：需要先完成 variable-identification。
</HARD-GATE>

## Pipeline
1. 前置检查：验证变量描述完整性
2. 概念分析：分解变量的核心属性（概念维度）
3. 指标选择：为每个维度选择 1-2 个可测量指标
4. 测量方法确定：指定数据收集方式（survey/experiment/observation/archival/computational）
5. 效度论证：
   - 内容效度：指标是否覆盖概念的全部关键维度？
   - 构念效度：指标是否与相关构念收敛、与不相关构念区分？
   - 标准效度：指标是否与已验证的标准测量相关？
6. 输出操作定义

## Output Format
```json
[
  {
    "variable": "Variable name",
    "theoretical_definition": "Abstract definition",
    "dimensions": ["Dimension 1", "Dimension 2"],
    "indicators": [
      {
        "indicator": "Indicator name",
        "measurement_method": "How to collect/measure",
        "scale": "nominal | ordinal | interval | ratio",
        "validity": {
          "content": "Justification",
          "construct": "Justification",
          "criterion": "Justification or null if not applicable"
        }
      }
    ],
    "operationalization_notes": "Any remaining challenges or alternatives"
  }
]
```
