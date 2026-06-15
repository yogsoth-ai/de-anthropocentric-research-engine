---
name: novelty-scoring
description: 'SOP: 评估研究 gap 的新颖性潜力，识别差异化方向并输出评分'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: gap-prioritization
input: GapRecord — 单条标准化 gap 记录
output: NoveltyScore — 含维度分、综合分（1-5）、差异化方向列表及依据
dependencies:
  sops:
  - hypothesis-formation-paper-research
  - hypothesis-formation-paper-search
  - hypothesis-formation-web-research
  - hypothesis-formation-web-search
---

# Novelty Scoring

评估研究 gap 的新颖性潜力，识别差异化方向并输出评分。

## HARD-GATE

<HARD-GATE>
- 输入必须是 status: "complete" 的 GapRecord
- 输出综合分必须在 [1, 5] 区间内
- differentiation_directions 列表不得为空（至少 1 条）
- 每个子维度必须附带至少 1 句文字依据
</HARD-GATE>

## Pipeline

1. **前置检查**: 验证输入 GapRecord 完整性；提取关键词用于文献扫描
2. **现有工作扫描**: 利用 literature-engine 和 web-browsing 检索与该 gap 直接相关的近期工作（近 3 年）；记录已有解法和部分解法
3. **差异化空间识别**: 对比现有工作与该 gap 的完整需求，识别尚未被覆盖的角度（方法、数据、问题设定、评估维度等）
4. **创新潜力评估**: 判断在差异化空间内产出真正新颖贡献的可能性（1-5）；参考：空白区域大小、竞争密度
5. **先进性评估**: 判断该 gap 是否处于领域前沿而非已被充分研究（1-5）
6. **综合评分**: 两维度等权平均，保留一位小数；列出具体差异化方向
7. **输出**: 返回 NoveltyScore 对象

## Output Format

```json
{
  "gap_id": "gap_001",
  "existing_work_summary": "现有工作简述（2-3句）",
  "dimension_scores": {
    "innovation_potential": { "score": 4, "rationale": "..." },
    "frontier_position": { "score": 4, "rationale": "..." }
  },
  "composite_score": 4.0,
  "differentiation_directions": [
    "方向1：...",
    "方向2：..."
  ],
  "overall_rationale": "综合依据（2-4句）"
}
```

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| hypothesis-formation-paper-research | Import SOP: 深度文献研究，原始全文 + PDF 问答（来自 literature-engine） |
| hypothesis-formation-paper-search | Import SOP: 中深度文献搜索，AI 摘要报告（来自 literature-engine） |
| hypothesis-formation-web-research | Import SOP: 深度 web 研究，全文抓取分析（来自 web-browsing） |
| hypothesis-formation-web-search | Import SOP: 快速 web 扫描，发现 URL 和 snippet（来自 web-browsing） |

<!-- END available-tables (generated) -->
