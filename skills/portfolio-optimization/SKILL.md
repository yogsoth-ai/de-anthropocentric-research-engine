---
name: portfolio-optimization
description: "Strategy: gap 组合视为投资组合——用风险/收益/多样性优化选出最优 gap 组合"
version: 1.0.0
category: hypothesis-formation
type: strategy
campaign: gap-prioritization
tactics:
  - scoring-matrix-construction
  - priority-sensitivity-testing
sops:
  - importance-scoring
  - feasibility-scoring
  - novelty-scoring
  - impact-scoring
  - ahp-weighting
  - priority-synthesis
dependencies:
  skills:
    - context-management
    - subagent-spawning
---

# Portfolio Optimization

将研究 gap 组合视为投资组合：不仅评估单个 gap 的价值，还分析 gap 之间的相关性和互补性，选出整体收益最大、风险最分散的 gap 组合。

## 适用场景

- gap 数量较大（20+），无法全部攻击
- 研究团队有多条并行线（可同时推进多个 gap）
- 需要在"高风险高回报"和"稳健可交付"之间平衡
- 资源有限，需要最大化整体研究产出

## 思维框架

**核心原则**：单个 gap 的价值不等于它在组合中的边际贡献。

将 gap 组合优化类比为 Markowitz 投资组合理论：

**收益（Return）**：gap 的预期学术/应用价值（重要性 × 影响力）

**风险（Risk）**：gap 的不确定性（可行性的倒数 + 技术成熟度的倒数）

**相关性（Correlation）**：两个 gap 是否依赖相同的方法、数据或前置工作？高相关 gap 同时失败的概率更高，应降低组合权重。

**多样性（Diversity）**：组合应覆盖不同子领域、不同方法论、不同时间跨度（短期可交付 + 长期突破）。

**有效前沿（Efficient Frontier）**：在给定风险水平下，找到收益最大的 gap 组合；或在给定收益目标下，找到风险最小的组合。

**关键洞察**：一个中等价值但与其他 gap 低相关的 gap，可能比一个高价值但高相关的 gap 更值得纳入组合——因为它提供了真正的多样化。

## Budget Gate

| Tier | Gap 数量 | 相关性分析 | 组合规模 | 最终产出 |
|------|---------|-----------|---------|---------|
| S | 20–30 | 定性（高/中/低） | 选 3–5 个 | 推荐组合 + 理由 |
| M | 31–50 | 半定量（相关矩阵） | 选 5–8 个 | 推荐组合 + 有效前沿图 + 备选组合 |
| L | 50+ | 定量（方法/数据重叠度） | 选 8–12 个 | 完整组合分析 + 有效前沿 + 风险分解 |

## 默认参考流

1. 调用 `gap-normalization` SOP：统一 gap 格式，提取方法论标签和数据依赖
2. 并行调用四维度评分 SOP（`importance-scoring`、`feasibility-scoring`、`novelty-scoring`、`impact-scoring`）
3. 调用 `scoring-matrix-construction` tactic：构建评分矩阵
4. 构建相关性矩阵：分析 gap 对之间的方法/数据/前置依赖重叠度
5. 计算每个 gap 的收益（重要性 × 影响力）和风险（1/可行性）
6. 枚举候选组合，计算组合收益和组合风险（考虑相关性）
7. 调用 `priority-sensitivity-testing` tactic：检验组合在不同风险偏好下的稳健性
8. 调用 `priority-synthesis` SOP：输出推荐组合 + 有效前沿分析

## context-checkpoint

每轮结束后记录：
- 各 gap 的收益/风险得分
- 相关性矩阵（gap 对 × 重叠度）
- 候选组合列表及其组合得分
- 推荐组合（含选择理由）
- 有效前沿描述（文字或表格）
