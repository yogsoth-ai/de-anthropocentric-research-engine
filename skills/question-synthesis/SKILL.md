---
name: question-synthesis
description: 'SOP: 综合所有中间产物产出最终研究问题集'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: research-question
input: 所有中间产物（框架应用、FINER 结果、子问题等）
output: 最终 RQ 文档（完整结构化）
dependencies:
  skills:
  - subagent-spawning
---

# Question Synthesis

综合所有中间产物产出最终研究问题集 — campaign 的最终输出步骤。

## HARD-GATE

<HARD-GATE>
输入必须包含: 至少 1 个通过 FINER 检验的 RQ + 对应的框架应用结果。
</HARD-GATE>

## Pipeline

1. **前置检查**: 所有 RQ 是否通过 FINER
2. **收集中间产物**: 框架应用、scope 评估、FINER 结果、子问题、依赖图
3. **一致性检查**: 各产物之间是否一致
4. **格式化**: 按标准格式组装最终文档
5. **完整性检查**: 每个 RQ 是否包含全部 6 个必要组件
6. **输出**: 最终 RQ 文档

## Required Components (per RQ)

每个 RQ 必须包含:
1. Main question（一句话精确表述）
2. Framework（使用的框架及各组件填充）
3. Scope（明确的边界）
4. Success criteria（可测量的成功标准）
5. Sub-questions（如有）
6. FINER assessment（5/5 通过）

## Output Format

```
# Research Question Set

## RQ1: [主问题]
- Framework: [框架名] — [各组件]
- Scope: In scope: [...] / Out of scope: [...]
- Success criteria: [可测量标准]
- Sub-questions: [如有]
- FINER: F✓ I✓ N✓ E✓ R✓

## RQ2: [主问题]
...
```
