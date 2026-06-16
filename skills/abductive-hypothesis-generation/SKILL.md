---
name: abductive-hypothesis-generation
description: 'Strategy: Inference to the best explanation in the face of anomalies'
version: 1.0.0
category: hypothesis-formation
type: strategy
campaign: hypothesis-formulation
tactics:
- anomaly-driven-abduction
sops:
- anomaly-characterization
- explanation-generation
- plausibility-ranking
- falsifiability-check
dependencies:
  tactics:
  - anomaly-driven-abduction
  sops:
  - falsifiability-check
---

# Abductive Hypothesis Generation

Inference to the best explanation in the face of anomalies: when an anomalous phenomenon that existing theory cannot explain is observed, systematically generate candidate explanations and select the most plausible one as the hypothesis.

## When to Use

- A clear anomalous phenomenon is observed (a result inconsistent with existing theoretical predictions)
- Existing theory cannot adequately explain a known phenomenon
- One of several competing explanations must be selected as the most worth testing
- The research starting point is "this result is strange, why?"

Not applicable: no clear anomaly, just wanting to explore a new field → use inductive-hypothesis-generation instead.

## Thinking Framework

**Anomaly → Generate candidate explanations → Rank by plausibility → Best explanation = hypothesis**

The core logic of abductive reasoning:

1. **Anomaly**: precisely describe the anomaly — what phenomenon, inconsistent with what expectation, how large the deviation
2. **Generate candidate explanations**: systematically generate all candidate explanations that can account for the anomaly (no premature filtering)
3. **Rank by plausibility**: rank by plausibility — which explanation is most parsimonious, most consistent with known facts, most testable
4. **Best explanation = hypothesis**: select the most plausible explanation as the working hypothesis, retaining the rest as competing hypotheses

**Core principles of abduction**:
- **Occam's razor**: when explanatory power is comparable, prefer the explanation with fewer assumptions
- **Consistency**: the best explanation should not contradict other known facts
- **Testability**: the best explanation must be able to produce observable predictions (otherwise it cannot be verified)
- **Generation completeness**: candidate explanations must be exhausted before ranking, to avoid premature convergence

## Budget Gate

| Tier | Anomaly description | Candidate explanations | Hypothesis output | Competing hypotheses |
|------|---------|---------|---------|---------|
| S | 1 precisely described anomaly | ≥2 candidate explanations | 1 best-explanation hypothesis | ≥1 competing hypothesis retained |
| M | 1–2 anomalies | ≥3 candidate explanations | ≥2 structured hypotheses | complete plausibility ranking |
| L | ≥2 related anomalies | ≥5 candidate explanations | ≥3 structured hypotheses | complete ranking + discriminating prediction design |

## Default Reference Flow

1. Call the `anomaly-characterization` SOP: precisely describe the anomaly (phenomenon, expectation, deviation, excluded trivial explanations)
2. Call the `explanation-generation` SOP (via the `anomaly-driven-abduction` tactic): systematically generate candidate explanations (no premature filtering)
3. Call the `plausibility-ranking` SOP: rank candidate explanations by parsimony, consistency, and testability
4. Call the `falsifiability-check` SOP: generate a falsification scenario for the best explanation, confirming its testability

## context-checkpoint

Record after each round:
- Anomaly description (precise version, with deviation quantification)
- Candidate explanation list (including excluded trivial explanations and exclusion reasons)
- Plausibility ranking result (including ranking basis)
- Best-explanation hypothesis + competing hypothesis list
- Discriminating predictions (what experiment can distinguish the best explanation from competing explanations)

<!-- BEGIN available-tables (generated) -->

## Available Tactics

可选,无固定顺序;最终叶子终为 sop。

| Tactic | 何时用 |
| --- | --- |
| anomaly-driven-abduction | Tactic: 归纳/溯因路径——描述异常现象，生成候选解释，按可信度排序 |

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| falsifiability-check | SOP: 检验假设是否满足可证伪性标准 |

<!-- END available-tables (generated) -->
