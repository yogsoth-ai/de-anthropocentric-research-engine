---
name: answering-sequence-design
description: 'SOP: 设计子问题的最优回答顺序'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: research-question
input: 子问题列表 + 依赖图
output: 执行序列 + 理由 + 并行机会
dependencies:
  skills:
  - subagent-spawning
---

# Answering Sequence Design

设计子问题的最优回答顺序 — 基于依赖关系和资源效率。

## HARD-GATE

<HARD-GATE>
输入必须包含: 子问题列表 + 依赖图（来自 dependency-mapping）。
</HARD-GATE>

## Pipeline

1. **前置检查**: 依赖图是否无循环
2. **拓扑排序**: 基于依赖关系确定基本顺序
3. **并行分组**: 识别可同时进行的子问题
4. **资源优化**: 考虑资源约束调整顺序
5. **风险排序**: 高风险/高不确定性的优先（fail fast）
6. **最终序列**: 综合以上因素确定最优序列
7. **输出**: 执行序列 + 分阶段计划 + 并行机会

## Output Format

```
Phase 1 (parallel): [SQ1, SQ3] — no mutual dependencies
Phase 2 (sequential): [SQ2] — depends on SQ1
Phase 3 (parallel): [SQ4, SQ5] — depend on SQ2
Rationale: [为什么这个顺序最优]
Risk note: [哪些子问题如果失败会影响后续]
```
