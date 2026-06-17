---
name: ara-rigor-review
description: 'SOP: Run the external ARA rigor-reviewer (Seal Level 2, six-dimension semantic review) over ../ara/ and pass its level2_report.json to the user'
version: 1.0.0
category: ara-from-context
type: sop
campaign: ara-from-context
input: A populated ara/ directory (Level 1 passed)
output: ara/level2_report.json (grade + D1–D6 + findings)
dependencies:
  skills:
  - rigor-reviewer
---

# SOP: ARA Rigor Review

**Key question**: 这份 ARA 的认识论严谨度如何?逻辑弧在结构上闭合了吗?

## Preflight

先确认外部 `rigor-reviewer` skill 可 load。不可用则提示安装并**停下**。

## Procedure

1. **跑 Level 2**:`Skill` load **rigor-reviewer**,传 `<artifact_dir>` = `../ara/`。
   它对 ARA 跑六维语义审查(全是要读懂 + 推理的语义检查,不是结构校验):
   - D1 Evidence Relevance — 证据是否在**实质**上支撑每条 claim;
   - D2 Falsifiability Quality — 证伪标准是否有意义、可操作、范围合适;
   - D3 Scope Calibration — claim 是否恰好断言其证据所支撑的,不多不少;
   - D4 Argument Coherence — 是否从 problem→solution→evidence 逻辑闭合;
   - D5 Exploration Integrity — exploration tree 是否记录了真实研究过程(含失败);
   - D6 Methodological Rigor — 实验设计/baseline/ablation/报告是否到位。

2. **产物**:`rigor-reviewer` 在 artifact 根目录写 `level2_report.json`
   (每维 1–5 分 + strengths/weaknesses/suggestions + severity 排序 findings +
   overall grade + 给作者的问题)。

3. **D5 低分不是错误,是"探索素材不足"信号。** 透传给用户,由用户决定是否回
   `context-exploring` 补打捞过程线。**本 SOP 不自动循环。**

> 注意:`rigor-reviewer` 的 D1–D6 是 **ARA 自己的**维度,与 DARE 的 D1–D5 评判
> 标准是两套东西,不要混。本 SOP 只透传 ARA 的报告,不施加 DARE 的 D1–D5。

## Output

`ara/level2_report.json` + 一句话总结(grade + 最该关注的 finding),交付用户。
