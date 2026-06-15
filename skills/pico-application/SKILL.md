---
name: pico-application
description: 'SOP: 应用 PICO/PICOTS 框架结构化研究问题'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: research-question
input: 研究意图 + 假设
output: 完整 PICO 填充 + RQ 表述
dependencies:
  skills:
  - subagent-spawning
---

# PICO Application

应用 PICO/PICOTS 框架 — 适用于量化/干预研究。

## HARD-GATE

<HARD-GATE>
输入必须包含: 明确的研究意图（涉及干预或量化比较）。
</HARD-GATE>

## Pipeline

1. **前置检查**: 确认研究适合 PICO 框架
2. **P (Population)**: 定义目标人群/对象（具体特征）
3. **I (Intervention)**: 定义干预/暴露/方法
4. **C (Comparison)**: 定义对照组/替代方案
5. **O (Outcome)**: 定义预期结果/测量指标
6. **T (Timeframe)**: 可选 — 定义时间范围
7. **S (Setting)**: 可选 — 定义研究场景
8. **组装**: 将各组件组装为完整 RQ 句子
9. **输出**: PICO 填充表 + RQ 表述

## Output Format

```
P: [具体人群描述]
I: [具体干预描述]
C: [具体对照描述]
O: [具体结果指标]
T: [时间范围] (optional)
S: [研究场景] (optional)

RQ: "In [P], does [I] compared to [C] improve [O] (within [T], in [S])?"
```
