---
name: hypothesis-comparison-matrix
description: "SOP: 构建竞争假设的多维度对比矩阵"
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: hypothesis-formulation
input: "竞争假设集 + 区分性预测（来自上游输出）"
output: "结构化对比矩阵（表格 + 综合评估）"
dependencies:
  skills:
    - subagent-spawning
---

# Hypothesis Comparison Matrix
构建竞争假设的多维度对比矩阵，高亮关键差异，支持知情选择。

## HARD-GATE
<HARD-GATE>
前置条件（全部满足才能开始）:
1. 已有 ≥2 个假设（含主假设 + ≥1 个竞争假设）
2. 假设包含 mechanism、predictions 等基本组件

不满足 → 停止，返回错误：需要至少 2 个假设才能构建对比矩阵。
</HARD-GATE>

## Pipeline
1. 前置检查：验证假设集完整性
2. 维度确定：选择对比维度（默认：机制类型/证据支持/可测试性/简约性/解释范围/理论依据）
3. 逐假设逐维度填充：为每个假设在每个维度上赋值
4. 差异高亮：标记假设间差异最大的维度
5. 综合评估：基于矩阵给出综合推荐
6. 输出结构化对比表

## Output Format
```json
{
  "dimensions": ["mechanism_type", "evidence_support", "testability", "parsimony", "scope", "theoretical_basis"],
  "matrix": [
    {
      "hypothesis_id": "H1",
      "label": "Primary Hypothesis",
      "statement": "...",
      "mechanism_type": "...",
      "evidence_support": "strong | moderate | weak | none",
      "testability": "high | medium | low",
      "parsimony": "high | medium | low",
      "scope": "broad | moderate | narrow",
      "theoretical_basis": "Theory name(s)"
    }
  ],
  "key_differentiators": ["Dimension where hypotheses differ most"],
  "recommendation": "Which hypothesis to prioritize and why",
  "caveats": "Important limitations of the comparison"
}
```
