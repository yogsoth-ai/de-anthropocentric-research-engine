---
name: theory-identification
description: 'SOP: 识别与研究gap相关的理论框架'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: hypothesis-formulation
input: 研究 gap 描述 + 领域标签
output: 相关理论框架列表 [{name, source, core_claim, relevance, applicability}]
dependencies:
  sops:
  - hypothesis-formation-paper-overview
  - hypothesis-formation-paper-search
  - hypothesis-formation-web-search
---

# Theory Identification
识别与研究 gap 相关的理论框架，为机制提取提供理论基础。

## HARD-GATE
<HARD-GATE>
前置条件（全部满足才能开始）:
1. 已有明确的研究 gap 描述（包含领域、现象、未解答的问题）
2. 领域标签已提供（用于文献扫描方向）

不满足 → 停止，返回错误：缺少 gap 描述或领域标签。
</HARD-GATE>

## Pipeline
1. 前置检查：验证 gap 描述与领域标签完整性
2. 文献扫描：搜索与 gap 相关的理论文献（literature-engine + web-browsing）
3. 理论筛选：保留与 gap 直接或间接相关的理论（≥3 个，去除纯方法论文献）
4. 核心主张提取：对每个理论提炼 1-2 句 core_claim
5. 适用性评估：评估每个理论对当前 gap 的解释力（high/medium/low）
6. 输出结构化理论列表

## Output Format
```json
[
  {
    "name": "Theory Name",
    "source": "Author (Year) or canonical reference",
    "core_claim": "One-sentence summary of what the theory claims",
    "relevance": "Why this theory relates to the gap",
    "applicability": "high | medium | low"
  }
]
```
最少 3 条，最多 8 条（按 applicability 降序排列）。

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| hypothesis-formation-paper-overview | Import SOP: 论文快速扫描，返回 abstract 和 metadata（来自 literature-engine） |
| hypothesis-formation-paper-search | Import SOP: 中深度文献搜索，AI 摘要报告（来自 literature-engine） |
| hypothesis-formation-web-search | Import SOP: 快速 web 扫描，发现 URL 和 snippet（来自 web-browsing） |

<!-- END available-tables (generated) -->
