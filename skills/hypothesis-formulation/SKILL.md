---
name: hypothesis-formulation
description: 'Campaign: transform insights and gaps into structured testable hypotheses'
version: 1.0.0
category: hypothesis-formation
type: campaign
input: Ranked gaps + insights + tensions (from gap-prioritization or an upstream repo)
output: Structured hypothesis set + falsifiability criteria + boundary conditions
strategies:
- deductive-hypothesis-generation
- inductive-hypothesis-generation
- abductive-hypothesis-generation
- competing-hypothesis-construction
- hypothesis-operationalization
tactics:
- theory-mechanism-extraction
- anomaly-driven-abduction
- falsifiability-audit
- competing-hypothesis-matrix
dependencies:
  campaigns:
  - research-question
  strategies:
  - abductive-hypothesis-generation
  - competing-hypothesis-construction
  - deductive-hypothesis-generation
  - hypothesis-operationalization
  - inductive-hypothesis-generation
  sops:
  - context-checkpoint
  - context-init
  - hypothesis-formation-quality-gate-check
  - hypothesis-formation-saturation-detection
  - hypothesis-synthesis
---

# Hypothesis Formulation

Transform insights and gaps into structured testable hypotheses — answering "how do we turn an insight into a testable hypothesis?"

## HARD-GATE

<HARD-GATE>
Preconditions (all must hold before starting):
1. At least 1 clear research gap or insight has been identified
2. The gap/insight has sufficient context (domain, existing theory, observed phenomenon)
3. The research intent is clear (knowing what is to be explained or predicted)

Not met → stop, recommend completing gap-prioritization or upstream work first.
</HARD-GATE>

## Campaign Goal

Transform a vague "there's a gap here" or "this phenomenon is interesting" into a precise, falsifiable hypothesis with boundary conditions. The output is not a "solution" but a "testable proposition."

## Strategy Selection

| Strategy | When to Use | Reasoning direction |
|----------|---------|---------|
| deductive-hypothesis-generation | The domain has mature theory, and the gap is a deviation between theoretical prediction and reality | Theory → prediction |
| inductive-hypothesis-generation | The domain lacks theory but has abundant empirical observations or data patterns | Data → regularity |
| abductive-hypothesis-generation | An anomalous phenomenon that existing theory cannot explain has been observed | Anomaly → best explanation |
| competing-hypothesis-construction | Need to maintain openness and avoid confirmation bias | Multiple explanations in parallel |
| hypothesis-operationalization | A directional hypothesis exists and needs to be formalized into a testable form | Vague → precise |

CC selects autonomously based on input characteristics (whether there is theoretical support, whether there is anomalous data, hypothesis maturity). Can be combined serially.

## Budget Gate

| Tier | Hypothesis yield | Theory/mechanism | Falsifiability | Competing hypotheses |
|------|---------|----------|---------|---------|
| S | ≥2 structured hypotheses | ≥2 relevant theories | 1 falsification scenario per hypothesis | Optional |
| M | ≥3 structured hypotheses | ≥3 theories + ≥5 mechanisms | ≥1 scenario + boundary conditions per hypothesis | ≥2 competing hypotheses |
| L | ≥5 structured hypotheses | ≥5 theories + ≥8 mechanisms | Complete falsifiability audit | ≥3 competing hypotheses + discriminating predictions |

## Hypothesis Structure (standard output format)

Each hypothesis must contain:
- **Statement**: If X then Y (condition-result form)
- **Variables**: independent, dependent, control, and moderator variables
- **Mechanism**: why X causes Y (causal chain)
- **Boundary conditions**: the preconditions under which the hypothesis holds
- **Falsification**: what observation would refute this hypothesis
- **Measurability**: how to measure it (operational definitions)

## Context Management

- Invoke context-init at campaign start
- Invoke context-checkpoint after each strategy completes (hard constraint)
- All outputs accumulate in a single campaign-scoped context file

## Minimum Yield

Each campaign run must produce:
1. ≥2 complete structured hypotheses (including all 6 components)
2. A falsifiability argument for each hypothesis
3. Relationship notes between hypotheses (complementary/competing/independent)
4. A recommended next direction (which hypothesis is most worth further developing into a research question)

<!-- BEGIN available-tables (generated) -->

## Available Strategies

可选,无固定顺序;最终叶子终为 sop。

| Strategy | 何时用 |
| --- | --- |
| abductive-hypothesis-generation | Strategy: 面对异常的最佳解释推理 |
| competing-hypothesis-construction | Strategy: 为同一现象构建多个竞争假设 |
| deductive-hypothesis-generation | Strategy: 从现有理论演绎推导假设 |
| hypothesis-operationalization | Strategy: 将 working hypothesis 精确化为可测试形式 |
| inductive-hypothesis-generation | Strategy: 从数据/观察归纳提炼假设 |

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| context-checkpoint | Append research process and results to the current Phase's context file. Each append MUST contain >=500 lines of markdown covering both process and results. Use this skill at plan-designated checkpoint points — typically after each strategy completes or at key decision nodes within a research Phase. |
| context-init | Create a new context file for a research Phase. Called once at Phase start to initialize the file that subsequent context-checkpoint calls will append to. Use this skill whenever a new research Phase begins and a fresh context file is needed. |
| hypothesis-formation-quality-gate-check | Shared SOP: 通用质量门检查（格式完整性、逻辑一致性） |
| hypothesis-formation-saturation-detection | Shared SOP: 判断当前活动是否已达信息饱和 |
| hypothesis-synthesis | SOP: 综合所有中间产物，产出最终结构化假设集 |

## Available Campaigns

可选,无固定顺序;最终叶子终为 sop。

| Campaign | 何时用 |
| --- | --- |
| research-question | Campaign: 将假设细化为精确的、框架化的研究问题 |

<!-- END available-tables (generated) -->
