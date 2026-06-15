---
name: falsifiability-check
description: 'SOP: 检验假设是否满足可证伪性标准'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: hypothesis-formulation
input: 假设陈述（含 statement + variables + mechanism）
output: 可证伪性判定 + falsification scenario + 修改建议（如不可证伪）
dependencies:
  skills:
  - subagent-spawning
---

# Falsifiability Check
依据 Popper 可证伪性标准检验假设，确保每个假设都有明确的否定条件。

## HARD-GATE
<HARD-GATE>
前置条件（全部满足才能开始）:
1. 已有至少 1 个假设陈述（含 statement）
2. 假设涉及可观察的变量或现象

不满足 → 停止，返回错误：假设陈述不完整。
</HARD-GATE>

## Pipeline
1. 前置检查：验证假设陈述完整性
2. 可观察预测推导：从假设推导出 ≥2 个具体可观察预测
3. 否定预测构建：构建"如果假设错误，应该观察到什么"
4. 可行性评估：否定预测在技术和伦理上是否可检验？
5. 判定：可证伪 / 不可证伪 / 需修改
6. 若不可证伪：提供具体修改建议使其可证伪
7. 输出判定结果

## Output Format
```json
{
  "hypothesis_id": "H1",
  "statement": "...",
  "positive_predictions": [
    "If H1 is true, we should observe X in condition Y"
  ],
  "falsification_scenario": "Specific observation that would conclusively refute H1",
  "testability": "high | medium | low",
  "verdict": "falsifiable | not_falsifiable | needs_revision",
  "revision_suggestion": "How to make it falsifiable (null if already falsifiable)",
  "notes": "Additional considerations"
}
```
