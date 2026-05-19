---
name: sub-question-generation
description: "SOP: 将主研究问题分解为可独立回答的子问题"
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: research-question
input: "主研究问题（RQ）"
output: "子问题列表 + 独立性论证"
dependencies:
  skills:
    - subagent-spawning
---

# Sub-Question Generation

将主研究问题分解为可独立回答的子问题。

## HARD-GATE

<HARD-GATE>
输入必须包含: 1 个已确认范围合适但复杂度高的主研究问题。
</HARD-GATE>

## Pipeline

1. **前置检查**: 主 RQ 是否确实需要分解（复杂度判断）
2. **维度识别**: 识别主 RQ 中的独立维度
3. **分解策略选择**: 按因果/变量/条件/层级/时序
4. **子问题生成**: 为每个维度生成子问题
5. **MECE 检验**: 互斥且穷尽
6. **独立性论证**: 每个子问题可独立研究
7. **覆盖性检验**: 子问题答案组合 = 主问题答案
8. **输出**: 子问题列表 + 独立性论证 + 覆盖性论证

## Output Format

```
Main RQ: [主问题]
Decomposition strategy: [选择的分解策略]
Sub-questions:
  1. [子问题1] — Independence: [论证]
  2. [子问题2] — Independence: [论证]
  ...
MECE check: PASS/FAIL
Coverage check: PASS/FAIL
```
