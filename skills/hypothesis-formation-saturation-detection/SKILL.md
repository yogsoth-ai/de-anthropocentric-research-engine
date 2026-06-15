---
name: saturation-detection
description: 'Shared SOP: 判断当前活动是否已达信息饱和'
version: 1.0.0
category: hypothesis-formation
type: sop
shared: true
campaigns:
- gap-prioritization
- hypothesis-formulation
- research-question
input: 当前活动的累积产出 + 最近一轮的增量
output: 饱和/未饱和判定 + 理由
dependencies:
  skills:
  - subagent-spawning
---

# Saturation Detection

判断当前活动是否已达信息饱和 — 决定是否继续迭代。

## HARD-GATE

<HARD-GATE>
输入必须包含: 至少 2 轮迭代的产出（需要对比增量）。
</HARD-GATE>

## Pipeline

1. **前置检查**: 是否有足够的迭代数据供对比
2. **增量分析**: 最近一轮相比前一轮新增了什么
3. **新颖性判断**: 新增内容是否提供了真正新的信息
4. **收敛检测**: 增量是否在递减
5. **饱和判定**: 饱和 / 未饱和
6. **输出**: 判定 + 理由 + 建议

## Saturation Criteria

**饱和（应停止迭代）**:
- 最近一轮没有产出新的实质性信息
- 新增内容主要是已知内容的重述或微调
- 增量对最终产出的贡献 < 5%

**未饱和（应继续迭代）**:
- 最近一轮产出了新的维度/视角/信息
- 增量对最终产出有实质性贡献
- 存在已知但未探索的方向

## Output Format

```
Judgment: SATURATED / NOT_SATURATED
Confidence: HIGH / MEDIUM / LOW
Rationale: [一句话理由]
Last round increment: [最近一轮新增了什么]
Recommendation: STOP / CONTINUE (with direction)
```
