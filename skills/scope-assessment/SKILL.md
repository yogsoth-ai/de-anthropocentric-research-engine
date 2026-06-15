---
name: scope-assessment
description: 'SOP: 评估研究问题的范围是否合适（太宽/合适/太窄）'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: research-question
input: 研究问题（RQ）
output: 范围判定 + 调整建议
dependencies:
  skills:
  - subagent-spawning
---

# Scope Assessment

评估研究问题的范围 — 判断太宽、合适、还是太窄，并给出调整建议。

## HARD-GATE

<HARD-GATE>
输入必须包含: 至少 1 个完整表述的研究问题。
</HARD-GATE>

## Pipeline

1. **前置检查**: RQ 是否为完整句子
2. **维度分析**: 识别 RQ 中的限定维度（时间/地点/人群/方法/现象）
3. **可回答性判断**: 这个问题需要多大规模的研究来回答？
4. **范围判定**: 太宽 / 合适 / 太窄
5. **调整建议**: 如果不合适，建议具体调整方向
6. **输出**: 判定结果 + 理由 + 调整建议

## Judgment Criteria

- **太宽**: 需要一本书 / 多篇论文 / 无法设计单一实验
- **合适**: 一篇论文可以回答 / 可以设计明确的研究方案
- **太窄**: 答案显而易见 / 缺乏理论贡献 / trivial

## Output Format

```
Scope: TOO_BROAD / APPROPRIATE / TOO_NARROW
Rationale: [一句话理由]
Dimensions: [当前限定维度列表]
Suggestion: [调整方向] (only if not APPROPRIATE)
```
