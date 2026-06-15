---
name: competing-hypothesis-generation
description: 'SOP: 为同一现象生成机制上不同的竞争假设'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: hypothesis-formulation
input: 现象描述 + 主假设（来自上游产出）
output: 竞争假设列表（机制上不同，非主假设的变体）
dependencies:
  skills:
  - subagent-spawning
---

# Competing Hypothesis Generation
为同一现象生成真正不同的竞争假设，防止确认偏误，保持解释开放性。

## HARD-GATE
<HARD-GATE>
前置条件（全部满足才能开始）:
1. 已有至少 1 个主假设（含 statement + mechanism）
2. 现象描述已提供（主假设试图解释的现象）

不满足 → 停止，返回错误：需要主假设和现象描述。
</HARD-GATE>

## Pipeline
1. 前置检查：验证主假设和现象描述完整性
2. 替代机制搜索：寻找能解释同一现象的不同因果机制
3. 替代理论应用：从不同理论框架推导对同一现象的预测
4. 反向推理：考虑因果方向相反的解释
5. 去重：确保每个竞争假设在机制上与主假设和其他竞争假设不同
6. 输出竞争假设列表

## Output Format
```json
[
  {
    "hypothesis_id": "CH1",
    "statement": "Competing hypothesis statement",
    "mechanism": "Different causal mechanism from the primary hypothesis",
    "theoretical_basis": "Theory or reasoning supporting this alternative",
    "key_difference": "How this differs mechanistically from the primary hypothesis",
    "shared_prediction": "Prediction shared with primary hypothesis (makes discrimination hard)",
    "unique_prediction": "Prediction unique to this hypothesis (enables discrimination)"
  }
]
```
最少 2 个竞争假设，每个在机制上与主假设不同。
