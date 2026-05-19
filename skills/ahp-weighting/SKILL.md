---
name: ahp-weighting
description: "SOP: 使用 AHP 层次分析法确定评分维度权重，输出权重向量"
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: gap-prioritization
input: "维度列表（字符串数组）+ 可选的两两比较偏好矩阵"
output: "AHPWeights — 权重向量、一致性比率（CR）及判断矩阵"
dependencies:
  skills:
    - subagent-spawning
---

# AHP Weighting

使用 AHP 层次分析法确定评分维度权重，输出权重向量。

## HARD-GATE

<HARD-GATE>
- 输入维度数量必须在 [2, 9] 范围内（AHP 适用范围）
- 输出权重向量各元素之和必须等于 1.0（允许 ±0.001 误差）
- 一致性比率 CR 必须被计算并报告；若 CR > 0.1 必须标记警告
</HARD-GATE>

## Pipeline

1. **前置检查**: 验证维度列表非空且数量在 [2, 9] 范围内
2. **维度列表确认**: 输出维度列表供调用方确认；若已提供比较矩阵则跳至步骤 4
3. **两两比较矩阵构建**: 对每对维度 (i, j) 赋予 Saaty 标度值（1-9）；矩阵满足 a[j][i] = 1/a[i][j]
4. **特征向量计算**: 对每列归一化后取行均值，得到优先级向量（权重）
5. **一致性比率检验**: 计算最大特征值 λ_max → 一致性指数 CI = (λ_max - n)/(n-1) → CR = CI/RI（查 Saaty RI 表）；CR < 0.1 为可接受
6. **输出**: 返回 AHPWeights 对象；若 CR > 0.1 附加修正建议

## Output Format

```json
{
  "dimensions": ["importance", "feasibility", "novelty", "impact"],
  "comparison_matrix": [[1, 3, 2, 2], [0.33, 1, 0.5, 0.5], [0.5, 2, 1, 1], [0.5, 2, 1, 1]],
  "weights": { "importance": 0.40, "feasibility": 0.15, "novelty": 0.23, "impact": 0.22 },
  "lambda_max": 4.02,
  "ci": 0.007,
  "ri": 0.90,
  "cr": 0.008,
  "cr_acceptable": true,
  "warnings": [],
  "revision_suggestions": []
}
```
