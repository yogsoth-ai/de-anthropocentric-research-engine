---
name: ladder-quality-order
description: loss-2 评判 — 对同一 topic 内 n 档样本做成对质量比较，判定单调性与端点分离。check-blind，只用 D1–D5。
---

# ladder-quality-order (loss-2)

你拿到：同一个 topic 下的 n 条样本，每条含 (research_graph, research_result)，
外加它们的 intended_order（插值器给的 id 序，id0 应最好 → idN-1 应最差）。

## 任务（成对排序，不打绝对分）
1. 枚举所有 i<j 对，对每对问：**在 D1–D5 意义上哪个研究设计更实在？**
   （D1 更有意义 / D2 更有 skill-research 价值 / D3 更可用于 DARE /
    D4 更守 4 层 / D5 前置更扎实）。输出 winner + 一句理由。
2. 聚合成诱导序，算与 intended_order 的 Kendall τ。
3. 端点：直接比 id0 vs idN-1，跨 K 次重复看 id0 是否稳定胜出。

## 输出（JSON）
{"tau": float, "monotonicity_pass": bool,   // τ≥0.7 且端点无倒挂
 "endpoint_separation_pass": bool,          // K 次中 id0 胜 ≥ K-allowance
 "rigor_floor_flag": bool,                  // 若 id0≈idN-1 端点塌（喂回风险册）
 "pairwise_log": [{i,j,winner,reason}]}

## check-blind 契约（硬约束）
- judge prompt **只准** D1–D5 措辞。
- **禁用**：32-check 词汇、6-primitive、"pseudo-good/novel-good" 分类、任何检测特征。
- z⊥C：在 B1 混淆三元组（同实质、异文风）上你的序**必须不变**；若随文风变 →
  你被混淆带跑了，需收紧到 D1–D5 实质。
