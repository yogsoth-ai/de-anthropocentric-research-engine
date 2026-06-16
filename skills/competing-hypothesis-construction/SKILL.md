---
name: competing-hypothesis-construction
description: 'Strategy: Construct multiple competing hypotheses for the same phenomenon'
version: 1.0.0
category: hypothesis-formation
type: strategy
campaign: hypothesis-formulation
tactics:
- competing-hypothesis-matrix
sops:
- competing-hypothesis-generation
- discriminating-prediction-design
- hypothesis-comparison-matrix
- falsifiability-check
dependencies:
  tactics:
  - competing-hypothesis-matrix
  sops:
  - falsifiability-check
---

# Competing Hypothesis Construction

Construct multiple competing hypotheses for the same phenomenon: actively counter confirmation bias, maintain epistemic openness by building genuinely different explanations in parallel, and design decisive predictions that can distinguish them.

## When to Use

- The researcher already has a "preferred hypothesis" and needs to actively challenge it
- The phenomenon has multiple plausible explanations, and premature convergence would lead in the wrong direction
- You need to show reviewers or funders that alternative explanations have been considered
- When designing experiments, you need to determine which variable best discriminates between competing explanations

Not applicable: the phenomenon has overwhelming evidence supporting a single explanation → directly use deductive-hypothesis-generation to refine that explanation.

## Thinking Framework

**Avoid confirmation bias by generating genuinely different explanations, then find discriminating predictions**

The core logic of competing hypothesis construction:

1. **Force diversity**: competing hypotheses must be genuinely different at the mechanism level, not variants of the same mechanism
2. **Symmetric treatment**: each hypothesis is treated with equal seriousness; the preferred hypothesis is not allowed special treatment
3. **Discriminating predictions**: find decisive predictions that distinguish the hypotheses — what result supports H1 but contradicts H2, and vice versa
4. **Matrix comparison**: reveal structural differences between hypotheses through a systematic matrix

**Quality criteria for competing hypotheses**:
- **Genuinely competing**: two hypotheses give different causal explanations for the same phenomenon (not weaker/stronger versions of the same explanation)
- **Mutual exclusivity**: there exists at least one observable result that can support one while contradicting the other
- **Comparability**: both hypotheses have clear testable predictions

## Budget Gate

| Tier | Competing hypotheses | Discriminating predictions | Comparison matrix | Falsifiability |
|------|---------|---------|---------|---------|
| S | ≥2 genuinely competing hypotheses | ≥1 discriminating prediction | simplified version (2×2) | 1 falsification scenario per hypothesis |
| M | ≥3 competing hypotheses | ≥2 discriminating predictions | full matrix (hypotheses × predictions) | full falsification per hypothesis |
| L | ≥4 competing hypotheses | ≥3 discriminating predictions | full matrix + experiment design suggestions | full falsifiability audit |

## Default Reference Flow

1. Call the `competing-hypothesis-generation` SOP (via the `competing-hypothesis-matrix` tactic): force generation of hypotheses that are genuinely different at the mechanism level
2. Call the `discriminating-prediction-design` SOP: design discriminating predictions for each pair of competing hypotheses
3. Call the `hypothesis-comparison-matrix` SOP: build a hypotheses × predictions comparison matrix to reveal structural differences
4. Call the `falsifiability-check` SOP: generate a falsification scenario for each hypothesis

## context-checkpoint

Record after each round:
- Competing hypothesis list (core mechanism statement for each hypothesis)
- Mechanism difference analysis (at what level the hypotheses are genuinely different)
- Discriminating prediction list (which pair of hypotheses each prediction can distinguish)
- Comparison matrix (hypotheses × predictions, annotated support/contradict/neutral)
- Recommended decisive experiment directions

<!-- BEGIN available-tables (generated) -->

## Available Tactics

可选,无固定顺序;最终叶子终为 sop。

| Tactic | 何时用 |
| --- | --- |
| competing-hypothesis-matrix | Tactic: 多假设管理——生成竞争假设，设计区分性预测，构建结构化比较矩阵 |

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| falsifiability-check | SOP: 检验假设是否满足可证伪性标准 |

<!-- END available-tables (generated) -->
