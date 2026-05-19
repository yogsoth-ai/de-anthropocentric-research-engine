---
name: dependency-mapping
description: "SOP: 映射子问题间的依赖关系"
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: research-question
input: "子问题列表"
output: "依赖图 + 关键路径 + 建议回答顺序"
dependencies:
  skills:
    - subagent-spawning
---

# Dependency Mapping

映射子问题间的依赖关系 — 确定哪些子问题必须先回答。

## HARD-GATE

<HARD-GATE>
输入必须包含: ≥2 个已生成的子问题。
</HARD-GATE>

## Pipeline

1. **前置检查**: 子问题列表是否完整
2. **依赖识别**: 对每对子问题判断是否存在依赖
3. **依赖类型标注**: 强依赖（必须先完成）/ 弱依赖（有帮助但非必须）
4. **循环检测**: 检查是否存在循环依赖
5. **关键路径识别**: 找到最长依赖链
6. **并行机会识别**: 找到可同时进行的子问题组
7. **输出**: 依赖图 + 关键路径 + 并行机会

## Output Format

```
Dependencies:
  SQ1 → SQ2 (strong: SQ2 needs SQ1's result as input)
  SQ1 → SQ3 (weak: SQ3 benefits from SQ1 but can proceed independently)
  SQ2 → SQ4 (strong)

Circular dependencies: NONE / [list]
Critical path: SQ1 → SQ2 → SQ4 (length: 3)
Parallel groups: [SQ1, SQ3] can run simultaneously
```
