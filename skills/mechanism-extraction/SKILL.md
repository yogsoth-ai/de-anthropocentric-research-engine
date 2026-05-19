---
name: mechanism-extraction
description: "SOP: 从理论中提取因果机制链"
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: hypothesis-formulation
input: "理论描述（来自 theory-identification 输出）"
output: "因果机制链列表 (X → mediator → Y) + 机制图"
dependencies:
  skills:
    - subagent-spawning
---

# Mechanism Extraction
从理论描述中提取结构化因果机制，为变量识别和假设构建提供骨架。

## HARD-GATE
<HARD-GATE>
前置条件（全部满足才能开始）:
1. 至少 1 个理论描述已提供（含 core_claim）
2. 理论描述足够具体，能够识别出至少 2 个变量

不满足 → 停止，返回错误：理论描述过于模糊，无法提取机制。
</HARD-GATE>

## Pipeline
1. 前置检查：验证理论描述完整性
2. 因果链识别：从理论文本中识别 X → Y 的因果关系陈述
3. 中介变量提取：识别 X 与 Y 之间的中间变量（mediator）
4. 机制命名：为每条机制链赋予简短描述性名称
5. 机制图构建：以有向图形式表示（文本 ASCII 或 JSON 节点/边）
6. 输出结构化机制列表

## Output Format
```json
[
  {
    "name": "Mechanism name",
    "chain": "X → mediator → Y",
    "variables": {
      "cause": "X description",
      "mediator": "mediator description (null if direct)",
      "effect": "Y description"
    },
    "source_theory": "Theory name this was extracted from",
    "direction": "positive | negative | conditional",
    "notes": "Any caveats or conditions"
  }
]
```
每个理论至少提取 1 条机制链；总计至少 2 条。
