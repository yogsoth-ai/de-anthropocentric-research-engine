---
name: importance-scoring
description: 'SOP: 评估研究 gap 的学术与实践重要性，输出 1-5 分及依据'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: gap-prioritization
input: GapRecord — 单条标准化 gap 记录
output: ImportanceScore — 含维度分、综合分（1-5）及文字依据
dependencies:
  skills:
  - subagent-spawning
---

# Importance Scoring

评估研究 gap 的学术与实践重要性，输出 1-5 分及依据。

## HARD-GATE

<HARD-GATE>
- 输入必须是 status: "complete" 的 GapRecord（id、title、description、domain 均非空）
- 输出综合分必须在 [1, 5] 区间内（可为小数，保留一位）
- 每个子维度必须附带至少 1 句文字依据
</HARD-GATE>

## Pipeline

1. **前置检查**: 验证输入 GapRecord 完整性；确认 domain 字段有效
2. **领域影响评估**: 判断该 gap 对所在领域的核心问题影响程度（1-5）；参考：是否阻碍领域进展、是否被多篇文献反复提及
3. **理论贡献评估**: 判断填补该 gap 对理论体系的贡献（1-5）；参考：是否挑战现有范式、是否能统一分散理论
4. **实践价值评估**: 判断填补该 gap 的现实应用价值（1-5）；参考：受益人群规模、可落地性、产业/政策影响
5. **综合评分**: 三维度加权平均（领域影响 40%、理论贡献 30%、实践价值 30%），保留一位小数
6. **输出**: 返回 ImportanceScore 对象

## Output Format

```json
{
  "gap_id": "gap_001",
  "dimension_scores": {
    "domain_impact": { "score": 4, "rationale": "..." },
    "theoretical_contribution": { "score": 3, "rationale": "..." },
    "practical_value": { "score": 4, "rationale": "..." }
  },
  "composite_score": 3.7,
  "overall_rationale": "综合依据（2-4句）"
}
```
