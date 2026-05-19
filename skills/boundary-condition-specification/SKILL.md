---
name: boundary-condition-specification
description: "SOP: 指定假设成立的边界条件"
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: hypothesis-formulation
input: "假设草案（含 statement + variables + mechanism）"
output: "边界条件列表（时间/空间/人群/条件/排除）"
dependencies:
  skills:
    - subagent-spawning
---

# Boundary Condition Specification
系统地识别假设成立所需的前提条件，防止过度泛化。

## HARD-GATE
<HARD-GATE>
前置条件（全部满足才能开始）:
1. 已有至少 1 个假设草案（含 statement 和 mechanism）
2. 假设涉及可识别的实体、时间或情境

不满足 → 停止，返回错误：假设草案不完整，无法确定边界条件。
</HARD-GATE>

## Pipeline
1. 前置检查：验证假设草案完整性
2. 时间边界：假设在什么时间段/历史时期成立？是否有时效性？
3. 空间边界：假设在什么地理/文化/组织范围内成立？
4. 人群边界：假设适用于哪类主体（人群、物种、系统类型）？
5. 条件边界：假设成立需要哪些前提条件（技术、制度、环境）？
6. 排除条件：明确列出假设不适用的情境
7. 输出结构化边界条件列表

## Output Format
```json
{
  "hypothesis_id": "H1 (or hypothesis statement snippet)",
  "boundary_conditions": {
    "temporal": "Time period or duration constraints",
    "spatial": "Geographic, cultural, or organizational scope",
    "population": "Subject type, sample characteristics",
    "conditional": ["Prerequisite condition 1", "Prerequisite condition 2"],
    "exclusions": ["Situation where hypothesis does NOT apply"]
  },
  "generalizability": "narrow | moderate | broad",
  "notes": "Any additional caveats"
}
```
每个假设草案产出 1 个边界条件对象。
