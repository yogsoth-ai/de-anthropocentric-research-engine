---
name: hypothesis-synthesis
description: "SOP: 综合所有中间产物，产出最终结构化假设集"
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: hypothesis-formulation
input: "所有中间产物（理论、机制、变量、关系、边界条件、可证伪性、竞争假设、对比矩阵）"
output: "最终假设文档（完整 6 组件结构 + 排序 + 关系说明）"
dependencies:
  skills:
    - subagent-spawning
---

# Hypothesis Synthesis
收集并整合所有中间产物，产出完整、去重、排序的最终假设集。

## HARD-GATE
<HARD-GATE>
前置条件（全部满足才能开始）:
1. 已有 ≥2 个假设候选（来自上游任意步骤）
2. 每个假设至少有 statement + mechanism + falsification_scenario

不满足 → 停止，返回错误：假设候选不足或缺少必要组件。
</HARD-GATE>

## Pipeline
1. 前置检查：验证所有中间产物完整性
2. 收集全部假设候选：汇总来自 deductive/inductive/abductive 路径的所有假设
3. 去重合并：识别并合并机制相同的假设（保留最完整版本）
4. 完整性检查：确保每个假设包含全部 6 个组件（statement/variables/mechanism/boundary_conditions/falsification/measurability）
5. 排序：按证据支持度 + 可测试性 + 理论重要性综合排序
6. 关系说明：标注假设间关系（互补/竞争/独立/层级）
7. 格式化输出最终假设文档

## Output Format
```json
{
  "summary": {
    "total_hypotheses": 3,
    "primary_hypothesis": "H1",
    "reasoning_path": "deductive | inductive | abductive | mixed"
  },
  "hypotheses": [
    {
      "hypothesis_id": "H1",
      "priority": 1,
      "statement": "If X then Y under conditions Z",
      "variables": {
        "independent": "X",
        "dependent": "Y",
        "mediators": [],
        "moderators": [],
        "controls": []
      },
      "mechanism": "Causal chain explanation",
      "boundary_conditions": {
        "temporal": "...",
        "spatial": "...",
        "population": "...",
        "conditional": [],
        "exclusions": []
      },
      "falsification": {
        "scenario": "...",
        "testability": "high | medium | low"
      },
      "measurability": {
        "iv_measure": "...",
        "dv_measure": "..."
      },
      "evidence_support": "strong | moderate | weak | none",
      "theoretical_basis": "Theory name(s)"
    }
  ],
  "hypothesis_relationships": [
    {
      "pair": "H1 and H2",
      "relationship": "complementary | competing | independent | hierarchical",
      "notes": "..."
    }
  ],
  "recommended_next_step": "Which hypothesis to develop into a research question first, and why"
}
```
