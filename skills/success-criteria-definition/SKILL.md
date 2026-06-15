---
name: success-criteria-definition
description: 'SOP: 为研究问题定义可测量的成功标准'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: research-question
input: 研究问题（RQ）
output: 可测量的成功标准 + 阈值
dependencies:
  skills:
  - subagent-spawning
---

# Success Criteria Definition

为研究问题定义可测量的成功标准 — 什么算"回答了这个问题"。

## HARD-GATE

<HARD-GATE>
输入必须包含: 1 个通过 FINER 检验的研究问题。
</HARD-GATE>

## Pipeline

1. **前置检查**: RQ 是否已通过 FINER
2. **结果类型识别**: 定量结果 / 定性结果 / 混合
3. **指标定义**: 用什么指标衡量"回答了问题"
4. **阈值设定**: 什么程度算"成功回答"
5. **部分成功定义**: 什么算"部分回答"
6. **失败定义**: 什么结果意味着"问题无法回答"
7. **输出**: 成功标准 + 阈值 + 部分成功 + 失败条件

## Output Format

```
RQ: [研究问题]
Success criteria:
  - Full success: [具体条件 + 阈值]
  - Partial success: [具体条件]
  - Failure/inconclusive: [具体条件]
Measurement: [如何测量]
Timeline: [预期需要多长时间]
```
