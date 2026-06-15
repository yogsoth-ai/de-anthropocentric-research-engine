---
name: priority-synthesis
description: 'SOP: 综合所有评分数据产出最终 gap 优先级列表及攻击路径建议'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: gap-prioritization
input: 全部评分数据（ImportanceScore[] + FeasibilityScore[] + NoveltyScore[] + ImpactScore[]）+
  AHP 权重向量
output: PriorityList — 有序 gap 列表、加权综合分、前 N 个攻击路径建议
dependencies:
  skills:
  - subagent-spawning
---

# Priority Synthesis

综合所有评分数据产出最终 gap 优先级列表及攻击路径建议。

## HARD-GATE

<HARD-GATE>
- 输入必须包含所有 gap 的全部评分维度（importance / feasibility / novelty / impact）
- 权重向量必须归一化（和为 1.0，允许 ±0.001 误差）
- 输出 priority_list 按综合分降序排列，不得有并列（若分数相同则按 feasibility 子分排序）
- 前 N 个 gap（N = min(3, total_gaps)）必须附带攻击路径建议
</HARD-GATE>

## Pipeline

1. **前置检查**: 验证所有 gap 的评分数据完整性；验证权重向量归一化
2. **加权汇总**: 对每个 gap，用 AHP 权重对四维评分加权求和得到综合分
3. **排序**: 按综合分降序排列；同分则按 feasibility 子分排序
4. **前 N 名攻击路径建议**: 对排名前 N 的 gap，结合其优势维度和 novelty 的 differentiation_directions，生成具体攻击路径建议（方法选择、数据来源、预期突破点）
5. **整体分析**: 输出分数分布统计、维度贡献分析
6. **输出**: 返回 PriorityList 对象

## Output Format

```json
{
  "priority_list": [
    {
      "rank": 1,
      "gap_id": "gap_003",
      "gap_title": "...",
      "composite_score": 4.2,
      "dimension_scores": {
        "importance": 4.5,
        "feasibility": 3.8,
        "novelty": 4.0,
        "impact": 4.2
      },
      "attack_path": {
        "recommended_approach": "方法建议（1-2句）",
        "data_sources": ["数据来源1", "数据来源2"],
        "expected_breakthrough": "预期突破点（1句）",
        "estimated_timeline": "预估时间框架"
      }
    }
  ],
  "statistics": {
    "total_gaps": 5,
    "score_range": [2.1, 4.2],
    "mean_score": 3.3,
    "top_dimension": "importance"
  },
  "synthesis_notes": "综合分析说明（3-5句）"
}
```
