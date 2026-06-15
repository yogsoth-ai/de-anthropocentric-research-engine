---
name: anomaly-characterization
description: 'SOP: 描述和分类无法被现有理论解释的异常现象'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: hypothesis-formulation
input: 异常观察描述（数据、实验结果、文献矛盾）
output: 结构化异常描述（现象 + 偏差量化 + 分类 + 排除已知解释）
dependencies:
  skills:
  - subagent-spawning
---

# Anomaly Characterization
系统描述和分类异常现象，为溯因推理（abductive reasoning）提供精确的起点。

## HARD-GATE
<HARD-GATE>
前置条件（全部满足才能开始）:
1. 已有具体的异常观察描述（不能是模糊的"结果很奇怪"）
2. 有参照基准（预期结果或理论预测）用于量化偏差

不满足 → 停止，返回错误：异常描述不足，需要具体观察和参照基准。
</HARD-GATE>

## Pipeline
1. 前置检查：验证异常描述和参照基准完整性
2. 现象描述：用精确语言重述异常（what was observed vs. what was expected）
3. 与预期偏差量化：量化或定性描述偏差程度（magnitude, direction, frequency）
4. 排除已知解释：列举并逐一排除可能的平凡解释（测量误差、采样偏差、已知效应）
5. 异常分类：将异常归类（unexpected absence / unexpected presence / unexpected magnitude / unexpected pattern / unexpected timing）
6. 输出结构化异常描述

## Output Format
```json
{
  "anomaly_id": "A1",
  "phenomenon": "Precise description of what was observed",
  "expected": "What theory or prior evidence predicted",
  "deviation": {
    "direction": "higher | lower | absent | present | different_pattern",
    "magnitude": "Quantitative or qualitative estimate",
    "frequency": "Isolated | recurring | systematic"
  },
  "excluded_explanations": [
    {"explanation": "...", "reason_excluded": "..."}
  ],
  "anomaly_type": "unexpected_absence | unexpected_presence | unexpected_magnitude | unexpected_pattern | unexpected_timing",
  "severity": "minor | moderate | major",
  "notes": "Additional context"
}
```
