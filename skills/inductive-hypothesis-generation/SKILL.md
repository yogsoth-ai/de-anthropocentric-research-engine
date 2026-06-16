---
name: inductive-hypothesis-generation
description: 'Strategy: induce and distill hypotheses from data/observations'
version: 1.0.0
category: hypothesis-formation
type: strategy
campaign: hypothesis-formulation
tactics:
- anomaly-driven-abduction
- falsifiability-audit
sops:
- anomaly-characterization
- explanation-generation
- variable-identification
- relationship-specification
- falsifiability-check
dependencies:
  tactics:
  - anomaly-driven-abduction
  - falsifiability-audit
  sops:
  - hypothesis-formation-variable-identification
  - relationship-specification
---

# Inductive Hypothesis Generation

Induce and distill hypotheses from data/observations: in domains with theoretical gaps or insufficient theory, distill regularities from empirical patterns and cautiously generalize them into testable propositions.

## When to Use

- The domain lacks mature theory but has accumulated abundant empirical observations or data patterns
- The research gap appears as "a recurring phenomenon with no systematic explanation yet"
- The goal is to distill regularities from data, laying a foundation for subsequent theory construction
- An exploratory research stage where it is not yet clear which variables matter

Not applicable: domains that already have a clear theoretical framework → use deductive-hypothesis-generation instead.

## Thinking Framework

**Observe patterns → Extract regularity → Generalize cautiously → Formulate testable claim**

The core logic of induction:

1. **Observe patterns**: systematically organize patterns that recur across existing observations, data, and cases (not single anomalies)
2. **Extract regularity**: identify the regularity behind the patterns — under what conditions it appears, under what conditions it does not
3. **Generalize cautiously**: cautiously generalize the regularity from the specific samples — make the boundary of generalization explicit, do not over-extrapolate
4. **Formulate testable claim**: turn the generalized regularity into a proposition that can be tested on new samples

**The core risk of induction**: over-generalization (jumping from a limited sample to a universal law). Each inductive hypothesis must make explicit:
- Which samples the observations come from (sample characteristics, source, time range)
- Which population it generalizes to (the boundary of generalization scope)
- What evidence would limit or refute the generalization

## Budget Gate

| Tier | Pattern coverage | Regularity extraction | Hypothesis yield | Generalization boundary |
|------|---------|---------|---------|---------|
| S | ≥3 independent observation patterns | ≥2 regularities | ≥2 structured hypotheses | Each hypothesis specifies its sample source |
| M | ≥5 independent observation patterns | ≥3 regularities | ≥3 structured hypotheses | Generalization boundary + falsification scenario |
| L | ≥8 independent observation patterns | ≥5 regularities | ≥4 structured hypotheses | Complete generalization boundary + comparison of competing regularities |

## Default Reference Flow

1. Invoke the `anomaly-characterization` SOP: systematically organize the patterns in existing observations/data (including frequency, conditions, exceptions)
2. Invoke the `explanation-generation` SOP (via the `anomaly-driven-abduction` tactic): generate candidate regularity explanations for each pattern
3. Invoke the `variable-identification` SOP: turn the constructs in the regularities into operationalizable variables
4. Invoke the `relationship-specification` SOP: specify the directional relationships between variables (including moderating conditions)
5. Invoke the `falsifiability-check` SOP (via the `falsifiability-audit` tactic): generate a falsification scenario + generalization boundary for each hypothesis

## context-checkpoint

Record after each round:
- The list of organized observation patterns (pattern description, source, frequency of occurrence)
- The list of extracted regularities (regularity statement, supporting patterns, exceptions)
- The current draft hypothesis set (including generalization-boundary statements)
- Falsifiability status + over-generalization risk assessment

<!-- BEGIN available-tables (generated) -->

## Available Tactics

可选,无固定顺序;最终叶子终为 sop。

| Tactic | 何时用 |
| --- | --- |
| anomaly-driven-abduction | Tactic: 归纳/溯因路径——描述异常现象，生成候选解释，按可信度排序 |
| falsifiability-audit | Tactic: 假设质量保证——检验可证伪性，修复不合格假设，完成操作化与边界条件规范 |

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| hypothesis-formation-variable-identification | SOP: 识别变量及其在假设中的角色 |
| relationship-specification | SOP: 指定变量间关系的方向与形式 |

<!-- END available-tables (generated) -->
