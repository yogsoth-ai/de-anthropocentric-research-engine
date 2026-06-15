---
name: weight-perturbation
description: 'SOP: 扰动权重检验 gap 排序稳定性，输出稳定性判定'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: gap-prioritization
input: 基准权重向量 + gap 评分矩阵（gap × 维度）
output: PerturbationReport — 扰动方案、排序变化幅度及稳定性判定
dependencies:
  skills:
  - subagent-spawning
---

# Weight Perturbation

扰动权重检验 gap 排序稳定性，输出稳定性判定。

## HARD-GATE

<HARD-GATE>
- 输入权重向量各元素之和必须等于 1.0（允许 ±0.001 误差）
- 评分矩阵行数（gap 数）必须 ≥ 2
- 至少生成 4 个扰动方案（±20% 各维度）
- stability_verdict 必须为 "stable" | "sensitive" | "unstable" 之一
</HARD-GATE>

## Pipeline

1. **前置检查**: 验证权重向量归一化；验证评分矩阵维度与权重向量长度一致
2. **基准排序计算**: 用基准权重对评分矩阵加权求和，得到基准排序
3. **扰动方案生成**: 对每个维度分别施加 +20% 和 -20% 扰动（重新归一化后），生成 2×n 个扰动方案
4. **重新计算排序**: 对每个扰动方案计算新排序
5. **比较变化幅度**: 统计每个方案中排序变化的 gap 数量；计算 Kendall τ 与基准排序的相关性
6. **稳定性判定**: stable（所有方案 τ ≥ 0.8）/ sensitive（任意方案 0.5 ≤ τ < 0.8）/ unstable（任意方案 τ < 0.5）
7. **输出**: 返回 PerturbationReport 对象

## Output Format

```json
{
  "baseline_ranking": ["gap_003", "gap_001", "gap_002"],
  "perturbation_scenarios": [
    {
      "scenario_id": "importance_+20%",
      "perturbed_weights": { "importance": 0.48, "feasibility": 0.18, "novelty": 0.17, "impact": 0.17 },
      "ranking": ["gap_003", "gap_001", "gap_002"],
      "kendall_tau": 1.0,
      "rank_changes": 0
    }
  ],
  "min_kendall_tau": 0.87,
  "stability_verdict": "stable",
  "sensitive_dimensions": [],
  "summary": "稳定性摘要（2-3句）"
}
```
