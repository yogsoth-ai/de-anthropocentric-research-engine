---
name: gap-pairwise-judgment
description: "SOP: 对两个 gap 进行逐标准相对优先级判断，输出偏好结果"
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: gap-prioritization
input: "GapRecord A + GapRecord B + 评分标准列表（含权重）"
output: "PairwiseJudgment — 逐标准比较、综合偏好及 Saaty 标度值"
dependencies:
  skills:
    - subagent-spawning
---

# Gap Pairwise Judgment

对两个 gap 进行逐标准相对优先级判断，输出偏好结果。

## HARD-GATE

<HARD-GATE>
- 输入必须包含两个 status: "complete" 的 GapRecord 和至少 1 条评分标准
- preferred_gap 必须为 gap_a_id 或 gap_b_id 之一（不允许 "tie"）
- saaty_value 必须在 [1, 9] 范围内（整数或分数 1/n）
- 每条标准必须有独立的比较结果
</HARD-GATE>

## Pipeline

1. **前置检查**: 验证两个 GapRecord 完整性；确认标准列表非空
2. **逐标准比较**: 对每条标准，独立判断 Gap A 与 Gap B 的相对优势；记录哪个更优及原因
3. **综合偏好判定**: 基于各标准权重加权汇总，确定整体偏好方向
4. **Saaty 标度赋值**: 将偏好强度映射到 Saaty 标度（1=相当 / 3=稍优 / 5=明显优 / 7=强烈优 / 9=极端优）；若 B 优于 A 则取倒数
5. **输出**: 返回 PairwiseJudgment 对象

## Output Format

```json
{
  "gap_a_id": "gap_001",
  "gap_b_id": "gap_002",
  "criteria_comparisons": [
    {
      "criterion": "importance",
      "weight": 0.40,
      "preferred": "gap_001",
      "rationale": "..."
    }
  ],
  "preferred_gap": "gap_001",
  "preference_strength": "moderate",
  "saaty_value": 3,
  "overall_rationale": "综合依据（2-3句）"
}
```
