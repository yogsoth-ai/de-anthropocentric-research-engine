---
name: feasibility-scoring
description: 'SOP: 评估研究 gap 的可攻击性，识别瓶颈并输出可行性评分'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: gap-prioritization
input: GapRecord — 单条标准化 gap 记录
output: FeasibilityScore — 含维度分、综合分（1-5）、瓶颈列表及依据
dependencies:
  skills:
  - subagent-spawning
---

# Feasibility Scoring

评估研究 gap 的可攻击性，识别瓶颈并输出可行性评分。

## HARD-GATE

<HARD-GATE>
- 输入必须是 status: "complete" 的 GapRecord
- 输出综合分必须在 [1, 5] 区间内
- 瓶颈列表（bottlenecks）必须存在，若无瓶颈则为空数组 []
- 每个子维度必须附带至少 1 句文字依据
</HARD-GATE>

## Pipeline

1. **前置检查**: 验证输入 GapRecord 完整性
2. **方法可用性评估**: 现有方法论工具箱是否足以攻击该 gap（1-5）；参考：是否有成熟算法/框架可复用
3. **数据可获取性评估**: 所需数据集/语料库是否公开可得（1-5）；参考：公开数据集存在性、数据规模需求
4. **资源需求评估**: 计算/实验资源需求是否在合理范围（1-5）；参考：GPU 需求、实验室设备、经费
5. **时间框架评估**: 在典型博士/项目周期内是否可完成（1-5）；参考：预期工作量、依赖链长度
6. **综合评分**: 四维度等权平均，保留一位小数；提取主要瓶颈（score ≤ 2 的维度）
7. **输出**: 返回 FeasibilityScore 对象

## Output Format

```json
{
  "gap_id": "gap_001",
  "dimension_scores": {
    "method_availability": { "score": 4, "rationale": "..." },
    "data_accessibility": { "score": 2, "rationale": "..." },
    "resource_requirements": { "score": 3, "rationale": "..." },
    "time_horizon": { "score": 3, "rationale": "..." }
  },
  "composite_score": 3.0,
  "bottlenecks": ["data_accessibility"],
  "overall_rationale": "综合依据（2-4句）"
}
```
