---
name: ahrq-picme-assessment
description: 'SOP: 使用 AHRQ PiCMe 框架对研究 gap 进行 6 维度系统评估'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: gap-prioritization
input: GapRecord — 单条标准化 gap 记录
output: PiCMeAssessment — 6 维度独立评分、综合判定及研究问题草稿
dependencies:
  skills:
  - subagent-spawning
---

# AHRQ PiCMe Assessment

使用 AHRQ PiCMe 框架对研究 gap 进行 6 维度系统评估。

## HARD-GATE

<HARD-GATE>
- 输入必须是 status: "complete" 的 GapRecord
- 6 个维度（P/I/C/M/E + 综合判定）必须全部完成，不得跳过
- 每个维度必须有独立评分（1-5）和文字说明
- overall_verdict 必须为 "strong" | "moderate" | "weak" 之一
</HARD-GATE>

## Pipeline

1. **前置检查**: 验证输入 GapRecord 完整性；确认 domain 字段有效
2. **Population (P)**: 明确该 gap 涉及的目标人群/系统/数据集；评估定义清晰度（1-5）
3. **Intervention (I)**: 明确拟议的干预/方法/解决方案；评估可操作性（1-5）
4. **Comparator (C)**: 明确对比基线（现有 SOTA、无干预、替代方案）；评估基线合理性（1-5）
5. **Metrics (M)**: 明确评估指标；评估指标的可测量性和相关性（1-5）
6. **Evidence (E)**: 评估现有证据对该 gap 存在性的支持强度（1-5）
7. **综合判定**: 基于 5 维度均值判定整体质量（strong ≥ 3.5 / moderate 2.5-3.4 / weak < 2.5）；生成研究问题草稿
8. **输出**: 返回 PiCMeAssessment 对象

## Output Format

```json
{
  "gap_id": "gap_001",
  "dimensions": {
    "population": { "score": 4, "description": "目标人群描述", "rationale": "..." },
    "intervention": { "score": 3, "description": "干预/方法描述", "rationale": "..." },
    "comparator": { "score": 3, "description": "对比基线描述", "rationale": "..." },
    "metrics": { "score": 4, "description": "评估指标描述", "rationale": "..." },
    "evidence": { "score": 4, "description": "证据强度描述", "rationale": "..." }
  },
  "mean_score": 3.6,
  "overall_verdict": "strong",
  "research_question_draft": "研究问题草稿（1句）",
  "improvement_suggestions": ["建议1", "建议2"]
}
```
