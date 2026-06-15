---
name: plausibility-ranking
description: 'SOP: 对候选解释按合理性进行多维度加权排序'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: hypothesis-formulation
input: 候选解释列表 + 相关证据（来自 explanation-generation 输出）
output: 合理性排序列表 + 各维度评分 + 排序理由
dependencies:
  skills:
  - subagent-spawning
---

# Plausibility Ranking
对候选解释从证据一致性、简约性、解释范围三个维度评分，加权排序，产出优先级列表。

## HARD-GATE
<HARD-GATE>
前置条件（全部满足才能开始）:
1. 已有 ≥2 个候选解释（来自 explanation-generation）
2. 每个解释有 mechanism 和 predictions 字段

不满足 → 停止，返回错误：需要至少 2 个候选解释才能排序。
</HARD-GATE>

## Pipeline
1. 前置检查：验证候选解释列表完整性
2. 证据一致性评分（0-10）：与已知证据的符合程度
3. 简约性评分（0-10）：解释所需假设数量（越少越高分）
4. 解释范围评分（0-10）：能解释多少相关现象（不仅仅是当前异常）
5. 加权排序：默认权重 0.5/0.3/0.2（证据/简约/范围），可调整
6. 输出排序列表 + 理由

## Output Format
```json
{
  "weights": {"evidence": 0.5, "parsimony": 0.3, "scope": 0.2},
  "rankings": [
    {
      "rank": 1,
      "explanation_id": "E1",
      "statement": "...",
      "scores": {
        "evidence_consistency": 8,
        "parsimony": 7,
        "explanatory_scope": 6
      },
      "weighted_score": 7.4,
      "rationale": "Why this ranks here",
      "key_weakness": "Main reason it might be wrong"
    }
  ]
}
```
