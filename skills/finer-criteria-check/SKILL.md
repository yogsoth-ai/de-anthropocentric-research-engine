---
name: finer-criteria-check
description: 'SOP: FINER 5 项标准逐项检验研究问题质量'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: research-question
input: 研究问题（RQ）
output: 5 项逐项判定 + 未通过项的修正建议
dependencies:
  skills:
  - subagent-spawning
---

# FINER Criteria Check

FINER 5 项标准逐项检验 — 研究问题质量的标准化测试。

## HARD-GATE

<HARD-GATE>
输入必须包含: 至少 1 个完整表述的研究问题。
</HARD-GATE>

## Pipeline

1. **前置检查**: RQ 是否为完整句子
2. **F (Feasible)**: 在可用资源/时间/数据条件下是否可行
3. **I (Interesting)**: 对领域学者和实践者是否有趣
4. **N (Novel)**: 是否提供新知识/新视角/新方法
5. **E (Ethical)**: 是否符合研究伦理
6. **R (Relevant)**: 是否与领域/社会/实践相关
7. **综合判定**: 全通过 / 部分通过
8. **修正建议**: 对未通过项给出具体修正方向
9. **输出**: 5 项判定结果 + 修正建议（如有）

## Output Format

```
F: PASS/FAIL — [理由]
I: PASS/FAIL — [理由]
N: PASS/FAIL — [理由]
E: PASS/FAIL — [理由]
R: PASS/FAIL — [理由]

Overall: PASS (5/5) / PARTIAL (X/5)
Suggestions: [针对 FAIL 项的具体修正建议]
```
