---
name: novelty-scoring
description: 'SOP: Assess the novelty potential of a research gap, identify differentiation directions, and output a score'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: gap-prioritization
input: GapRecord — a single standardized gap record
output: NoveltyScore — includes dimension scores, composite score (1-5), list of differentiation directions, and rationale
dependencies:
  sops:
  - hypothesis-formation-paper-research
  - hypothesis-formation-paper-search
  - hypothesis-formation-web-research
  - hypothesis-formation-web-search
---

# Novelty Scoring

Assess the novelty potential of a research gap, identify differentiation directions, and output a score.

## HARD-GATE

<HARD-GATE>
- Input must be a GapRecord with status: "complete"
- The output composite score must be within the interval [1, 5]
- The differentiation_directions list must not be empty (at least 1 entry)
- Each sub-dimension must be accompanied by at least 1 sentence of textual rationale
</HARD-GATE>

## Pipeline

1. **Precondition check**: Verify the completeness of the input GapRecord; extract keywords for literature scanning
2. **Existing-work scan**: Use literature-engine and web-browsing to retrieve recent work (past 3 years) directly related to the gap; record existing solutions and partial solutions
3. **Differentiation-space identification**: Compare existing work against the gap's full requirements to identify angles not yet covered (methods, data, problem setup, evaluation dimensions, etc.)
4. **Innovation-potential assessment**: Judge the likelihood of producing a genuinely novel contribution within the differentiation space (1-5); consider: size of the white space, competition density
5. **Frontier assessment**: Judge whether the gap is at the frontier of the field rather than already well-studied (1-5)
6. **Composite scoring**: Equal-weight average of the two dimensions, keeping one decimal place; list specific differentiation directions
7. **Output**: Return the NoveltyScore object

## Output Format

```json
{
  "gap_id": "gap_001",
  "existing_work_summary": "Brief summary of existing work (2-3 sentences)",
  "dimension_scores": {
    "innovation_potential": { "score": 4, "rationale": "..." },
    "frontier_position": { "score": 4, "rationale": "..." }
  },
  "composite_score": 4.0,
  "differentiation_directions": [
    "Direction 1: ...",
    "Direction 2: ..."
  ],
  "overall_rationale": "Overall basis (2-4 sentences)"
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
