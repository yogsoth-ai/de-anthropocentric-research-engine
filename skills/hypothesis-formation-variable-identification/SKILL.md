---
name: variable-identification
description: 'SOP: 识别变量及其在假设中的角色'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: hypothesis-formulation
input: 机制描述（来自 mechanism-extraction 输出）
output: 变量清单 + 角色标注 (IV/DV/mediator/moderator/control) + 操作化可能性评估
dependencies:
  skills:
  - subagent-spawning
---

# Variable Identification
从机制描述中识别所有变量并标注其在假设结构中的角色。

## HARD-GATE
<HARD-GATE>
前置条件（全部满足才能开始）:
1. 至少 1 条因果机制链已提供
2. 机制链包含可识别的变量名称

不满足 → 停止，返回错误：机制描述不足以识别变量。
</HARD-GATE>

## Pipeline
1. 前置检查：验证机制链完整性
2. 变量提取：从所有机制链中枚举全部变量（含隐含变量）
3. 角色分类：为每个变量分配角色（IV/DV/mediator/moderator/control/confound）
4. 去重合并：同一变量在不同机制中出现时合并，标注多重角色
5. 操作化可能性评估：评估每个变量是否可被测量（high/medium/low/unclear）
6. 输出结构化变量清单

## Output Format
```json
[
  {
    "name": "Variable name",
    "role": "IV | DV | mediator | moderator | control | confound",
    "description": "What this variable represents",
    "source_mechanism": ["mechanism name(s) where this variable appears"],
    "operationalizable": "high | medium | low | unclear",
    "operationalization_notes": "How it might be measured or manipulated"
  }
]
```
至少识别 2 个变量（1 个 IV + 1 个 DV）。
