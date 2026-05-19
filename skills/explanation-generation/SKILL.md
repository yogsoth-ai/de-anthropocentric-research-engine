---
name: explanation-generation
description: "SOP: 为异常现象生成候选解释列表"
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: hypothesis-formulation
input: "结构化异常描述（来自 anomaly-characterization 输出）"
output: "候选解释列表 + 各自的可观察预测"
dependencies:
  skills:
    - subagent-spawning
---

# Explanation Generation
通过发散思维为异常现象生成多个候选解释，并为每个解释推导可观察预测。

## HARD-GATE
<HARD-GATE>
前置条件（全部满足才能开始）:
1. 已有结构化异常描述（含 phenomenon + deviation + excluded_explanations）
2. 异常已被确认为非平凡（severity ≠ trivial）

不满足 → 停止，返回错误：需要先完成 anomaly-characterization。
</HARD-GATE>

## Pipeline
1. 前置检查：验证异常描述完整性
2. 发散思维：生成 ≥3 个机制上不同的候选解释（不是同一解释的变体）
3. 预测推导：对每个解释推导 1-2 个可观察预测（如果解释正确，应该观察到什么）
4. 证据一致性检查：检查每个解释与已知证据的一致性（consistent/inconsistent/neutral）
5. 去重：合并机制相同的解释
6. 输出候选解释列表

## Output Format
```json
[
  {
    "explanation_id": "E1",
    "statement": "Candidate explanation in one sentence",
    "mechanism": "How this explanation accounts for the anomaly",
    "predictions": [
      "Observable prediction 1 if this explanation is correct",
      "Observable prediction 2"
    ],
    "evidence_consistency": "consistent | inconsistent | neutral",
    "evidence_notes": "What existing evidence supports or contradicts this",
    "novelty": "known | extension | novel"
  }
]
```
最少 3 个机制上不同的候选解释。
