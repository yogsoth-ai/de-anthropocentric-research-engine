---
name: framework-matching
description: "SOP: 根据研究类型匹配最适合的 RQ 框架"
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: research-question
input: "研究类型 + 领域 + 假设特征"
output: "推荐框架 + 理由 + 候选框架对比"
dependencies:
  skills:
    - subagent-spawning
---

# Framework Matching

根据研究类型匹配最适合的 RQ 框架。

## HARD-GATE

<HARD-GATE>
输入必须包含: 研究方向/假设 + 研究类型（或足够信息推断研究类型）。
</HARD-GATE>

## Pipeline

1. **前置检查**: 研究方向和类型是否明确
2. **类型判定**: 确定研究类型（量化干预/定性探索/评估/混合）
3. **框架匹配**: 根据类型匹配候选框架
4. **适用性评估**: 对每个候选框架评估适用性
5. **推荐**: 选择最适合的框架 + 理由
6. **输出**: 推荐框架 + 候选对比表

## Framework Knowledge Base

| 框架 | 适用研究类型 | 核心组件 | 优势 | 局限 |
|------|------------|---------|------|------|
| PICO/PICOTS | 量化/干预 | P-I-C-O(-T-S) | 结构清晰，广泛认可 | 不适合定性研究 |
| SPIDER | 定性 | S-PI-D-E-R | 专为定性设计 | 不适合干预研究 |
| SPICE | 评估 | S-P-I-C-E | 评估导向 | 范围较窄 |
| ECLIPSE | 混合方法 | E-C-L-I-P-S-E | 全面，适合复杂研究 | 组件多，可能过度 |

## Output Format

```
{
  recommended: "PICO",
  rationale: "...",
  candidates: [
    { framework: "PICO", fit_score: 9, reason: "..." },
    { framework: "SPIDER", fit_score: 4, reason: "..." }
  ]
}
```
