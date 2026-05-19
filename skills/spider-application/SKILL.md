---
name: spider-application
description: "SOP: 应用 SPIDER 框架结构化定性研究问题"
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: research-question
input: "研究意图（定性研究方向）"
output: "完整 SPIDER 填充 + RQ 表述"
dependencies:
  skills:
    - subagent-spawning
---

# SPIDER Application

应用 SPIDER 框架 — 适用于定性研究。

## HARD-GATE

<HARD-GATE>
输入必须包含: 明确的定性研究意图（探索性、理解性、解释性）。
</HARD-GATE>

## Pipeline

1. **前置检查**: 确认研究适合 SPIDER 框架
2. **S (Sample)**: 定义样本/研究对象
3. **PI (Phenomenon of Interest)**: 定义关注的现象
4. **D (Design)**: 定义研究设计（访谈/观察/案例等）
5. **E (Evaluation)**: 定义评估方式（主题分析/扎根理论等）
6. **R (Research type)**: 定义研究类型（探索/描述/解释）
7. **组装**: 将各组件组装为完整 RQ 句子
8. **输出**: SPIDER 填充表 + RQ 表述

## Output Format

```
S: [样本描述]
PI: [关注现象]
D: [研究设计]
E: [评估方式]
R: [研究类型]

RQ: "How do [S] experience [PI], as explored through [D] and evaluated via [E]?"
```
