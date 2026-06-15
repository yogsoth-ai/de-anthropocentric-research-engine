---
name: consistency-check
description: 'SOP: 检验 pairwise 判断矩阵的传递一致性，识别不一致项并建议修正'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: gap-prioritization
input: n×n pairwise 判断矩阵（Saaty 标度值）+ 维度/gap 标签列表
output: ConsistencyReport — CR 值、不一致项列表及修正建议
dependencies:
  skills:
  - subagent-spawning
---

# Consistency Check

检验 pairwise 判断矩阵的传递一致性，识别不一致项并建议修正。

## HARD-GATE

<HARD-GATE>
- 输入矩阵必须是方阵（n×n），n 在 [2, 9] 范围内
- 矩阵必须满足对角线全为 1 且 a[i][j] = 1/a[j][i]（允许 0.001 浮点误差）
- CR 必须被计算并报告
- 若 CR > 0.1，inconsistent_pairs 列表不得为空
</HARD-GATE>

## Pipeline

1. **前置检查**: 验证矩阵为方阵；检查对角线和倒数性质；若违反则报告具体位置
2. **计算判断矩阵**: 确认输入矩阵有效
3. **计算一致性比率**: 列归一化 → 行均值（权重向量）→ 加权和向量 → λ_max → CI → CR（查 Saaty RI 表）
4. **识别不一致项**: 对每个三元组 (i, j, k)，检验传递性 a[i][k] ≈ a[i][j] × a[j][k]；偏差最大的对即为不一致项
5. **建议修正**: 对每个不一致项，建议将 a[i][j] 调整为使传递性成立的值
6. **输出**: 返回 ConsistencyReport 对象

## Output Format

```json
{
  "labels": ["gap_001", "gap_002", "gap_003"],
  "n": 3,
  "lambda_max": 3.05,
  "ci": 0.025,
  "ri": 0.58,
  "cr": 0.043,
  "cr_acceptable": true,
  "inconsistent_pairs": [],
  "revision_suggestions": [],
  "matrix_issues": []
}
```
