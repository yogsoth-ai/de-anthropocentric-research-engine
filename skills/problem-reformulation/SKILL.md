---
name: problem-reformulation
description: Problem Reformulation Campaign — question the problem itself. Escape
  dominant ideas, reframe from multiple perspectives, apply dialectical inquiry, assess
  wickedness, discover appreciative alternatives. 5 strategies, 3 tactics, 10 subagent
  SOPs.
execution: campaign
dependencies:
  strategies:
  - appreciative-reframing
  - dialectical-reformulation
  - dominant-idea-escape
  - multi-perspective-reframing
  - wickedness-assessment
  sops:
  - context-checkpoint
  - context-init
---

# Problem Reformulation

Question the problem itself — are we solving the right problem?

## Strategy Routing

| Signal | Strategy |
|--------|----------|
| 主导观念、范式锁定、横向思维、逃逸 | → dominant-idea-escape |
| 多视角、CATWOE、重构矩阵、Rich Pictures | → multi-perspective-reframing |
| 双环学习、支配变量、辩证探究 | → dialectical-reformulation |
| 邪恶问题、Rittel 标准、复杂性、Cynefin | → wickedness-assessment |
| 正向偏差、欣赏式探询、优势视角 | → appreciative-reframing |

## Available Tactics

lateral-escape, multi-worldview-comparison, dialectical-escalation

## Available SOPs

**Import:** web-search, web-research, paper-overview, paper-search, paper-research
**Subagent:** dominant-idea-identification, provocation-generation, consequence-following, catwoe-analysis, reframing-matrix, governing-variable-surfacing, counter-assumption-generation, wickedness-scoring, appreciative-discovery, reformulation-synthesis
**Shared:** assumption-surfacing, multi-stakeholder-simulation

<!-- BEGIN available-tables (generated) -->

## Available Strategies

可选,无固定顺序;最终叶子终为 sop。

| Strategy | 何时用 |
| --- | --- |
| appreciative-reframing | Find positive deviants and reframe the problem from deficit-based to asset-based using Appreciative Inquiry. |
| dialectical-reformulation | Surface Argyris governing variables and test whether the problem dissolves under alternative governing variables (double-loop learning). |
| dominant-idea-escape | Identify dominant paradigms constraining the field and use de Bono lateral thinking provocations to escape them. |
| multi-perspective-reframing | Apply CATWOE from multiple stakeholder viewpoints and reframing matrix to reveal aspects invisible from the dominant perspective. |
| wickedness-assessment | Apply Rittel's 10 criteria to determine if the problem is tame, complex, or wicked, and adjust research strategy accordingly. |

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| context-checkpoint | Append research process and results to the current Phase's context file. Each append MUST contain >=500 lines of markdown covering both process and results. Use this skill at plan-designated checkpoint points — typically after each strategy completes or at key decision nodes within a research Phase. |
| context-init | Create a new context file for a research Phase. Called once at Phase start to initialize the file that subsequent context-checkpoint calls will append to. Use this skill whenever a new research Phase begins and a fresh context file is needed. |

<!-- END available-tables (generated) -->
