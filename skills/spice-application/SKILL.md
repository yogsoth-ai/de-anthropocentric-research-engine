---
name: spice-application
description: "SOP: 应用 SPICE 框架结构化评估研究问题"
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: research-question
input: "研究意图（评估研究方向）"
output: "完整 SPICE 填充 + RQ 表述"
dependencies:
  skills:
    - subagent-spawning
---

# SPICE Application

应用 SPICE 框架 — 适用于评估研究。

## HARD-GATE

<HARD-GATE>
输入必须包含: 明确的评估研究意图（评估某干预/项目/服务的效果）。
</HARD-GATE>

## Pipeline

1. **前置检查**: 确认研究适合 SPICE 框架
2. **S (Setting)**: 定义研究场景
3. **P (Perspective)**: 定义评估视角（谁的视角？）
4. **I (Intervention)**: 定义被评估的干预/项目
5. **C (Comparison)**: 定义比较对象
6. **E (Evaluation)**: 定义评估指标和方法
7. **组装**: 将各组件组装为完整 RQ 句子
8. **输出**: SPICE 填充表 + RQ 表述

## Output Format

```
S: [研究场景]
P: [评估视角]
I: [被评估的干预]
C: [比较对象]
E: [评估指标和方法]

RQ: "In [S], from [P]'s perspective, how does [I] compare to [C] in terms of [E]?"
```
