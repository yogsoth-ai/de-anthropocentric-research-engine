---
name: decomposition-formulation
description: 'Strategy: decompose a complex research question into a hierarchy of independently answerable sub-questions'
version: 1.0.0
category: hypothesis-formation
type: strategy
campaign: research-question
tactics:
- sub-question-decomposition
sops:
- sub-question-generation
- dependency-mapping
- answering-sequence-design
- finer-criteria-check
dependencies:
  tactics:
  - sub-question-decomposition
  sops:
  - finer-criteria-check
---

# Decomposition Formulation

Decompose a complex research question into independently answerable sub-questions — when a single experiment cannot answer the whole question.

## When to Use

- High problem complexity, involving multiple independent dimensions
- A single experiment/study cannot answer it completely
- Research plans that need to proceed in phases
- The question contains multiple causal chains or multiple variable groups

## Thinking Framework

Core logic: a complex problem = a combination of several simpler problems. Find the right decomposition such that each sub-question can be answered independently, and the answers to the sub-questions combine to answer the main question.

### Decomposition Principles

- **MECE**: sub-questions are mutually exclusive and collectively exhaustive
- **Independence**: each sub-question can have its research design developed independently
- **Coverage**: the combined answers of all sub-questions = the answer to the main question
- **Operationalizability**: each sub-question is researchable (not a philosophical question)

### Decomposition Dimensions

- By causal chain: antecedent → mechanism → outcome
- By variable: one sub-question per key variable
- By condition: behavior under different boundary conditions
- By level: macro → meso → micro
- By time: short-term → mid-term → long-term effects

## Budget Gate

| Tier | Sub-questions | Dependency analysis | Sequence design |
|------|---------|---------|---------|
| S | ≥2 sub-questions | basic dependency identification | suggested order |
| M | ≥3 sub-questions | dependency graph + critical path | optimal sequence + parallelization opportunities |
| L | ≥5 sub-questions | full dependency graph + cycle detection | multi-path plan + resource allocation |

## Default Reference Flow

1. Analyze the complexity dimensions of the main RQ
2. Choose a decomposition strategy (by causality/variable/condition/level/time)
3. Generate sub-questions (sub-question-generation SOP)
4. Verify MECE and coverage
5. Map dependencies (dependency-mapping SOP)
6. Design the answering sequence (answering-sequence-design SOP)
7. Run a FINER check on each sub-question

## context-checkpoint

After the Strategy completes, you must call context-checkpoint and record:
- The main RQ and its complexity analysis
- The chosen decomposition strategy
- The list of sub-questions + independence argument
- The dependency graph
- The suggested answering sequence

<!-- BEGIN available-tables (generated) -->

## Available Tactics

可选,无固定顺序;最终叶子终为 sop。

| Tactic | 何时用 |
| --- | --- |
| sub-question-decomposition | Tactic: 将主问题分解为可独立回答的子问题层级 |

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| finer-criteria-check | SOP: FINER 5 项标准逐项检验研究问题质量 |

<!-- END available-tables (generated) -->
