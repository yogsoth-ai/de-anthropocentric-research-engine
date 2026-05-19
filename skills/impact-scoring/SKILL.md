---
name: impact-scoring
description: "SOP: 评估研究 gap 的潜在影响力，识别受益方并输出影响力评分"
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: gap-prioritization
input: "GapRecord — 单条标准化 gap 记录"
output: "ImpactScore — 含维度分、综合分（1-5）、受益方分析及依据"
dependencies:
  skills:
    - subagent-spawning
---

# Impact Scoring

评估研究 gap 的潜在影响力，识别受益方并输出影响力评分。

## HARD-GATE

<HARD-GATE>
- 输入必须是 status: "complete" 的 GapRecord
- 输出综合分必须在 [1, 5] 区间内
- beneficiaries 列表不得为空（至少 1 条受益方）
- 每个子维度必须附带至少 1 句文字依据
</HARD-GATE>

## Pipeline

1. **前置检查**: 验证输入 GapRecord 完整性
2. **受益方识别**: 枚举填补该 gap 后的直接和间接受益方（研究者、从业者、患者、政策制定者、社会等）
3. **影响范围评估**: 受益方的广度——受影响人群/机构的规模（1-5）
4. **影响深度评估**: 对受益方的改变程度——是边际改善还是根本性变革（1-5）
5. **综合评分**: 两维度等权平均，保留一位小数
6. **输出**: 返回 ImpactScore 对象

## Output Format

```json
{
  "gap_id": "gap_001",
  "beneficiaries": [
    { "group": "受益方名称", "type": "direct | indirect", "description": "如何受益" }
  ],
  "dimension_scores": {
    "breadth": { "score": 4, "rationale": "..." },
    "depth": { "score": 3, "rationale": "..." }
  },
  "composite_score": 3.5,
  "overall_rationale": "综合依据（2-4句）"
}
```
