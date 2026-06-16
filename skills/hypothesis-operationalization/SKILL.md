---
name: hypothesis-operationalization
description: 'Strategy: refine a working hypothesis into a precise, testable form'
version: 1.0.0
category: hypothesis-formation
type: strategy
campaign: hypothesis-formulation
tactics:
- falsifiability-audit
sops:
- operationalization
- falsifiability-check
- boundary-condition-specification
- variable-identification
dependencies:
  tactics:
  - falsifiability-audit
  sops:
  - hypothesis-formation-variable-identification
---

# Hypothesis Operationalization

Refine a working hypothesis into a testable form: transform a vague directional idea or conceptual hypothesis into a precise, testable proposition in which every term has an operational definition and every variable has a measurement method.

## When to Use

- A directional hypothesis already exists ("I think X may influence Y"), but it has not been made precise
- The hypothesis contains abstract constructs that need to be concretized into observable indicators
- Preparing to enter the research-design stage and needing a directly operationalizable version of the hypothesis
- A reviewer or collaborator gives feedback that "the hypothesis is too vague"

Not applicable: there is not yet any hypothesis direction → first use one of the other three strategies to generate a hypothesis, then return to this strategy to refine it.

## Thinking Framework

**Abstract → Concrete**

Every term gets an operational definition, every variable gets a measurement method.

The five levels of operationalization:

1. **Construct clarification**: what does each term in the hypothesis mean? (conceptual level)
2. **Variable identification**: which are the operationalizable variables? (analytical level)
3. **Operational definition**: how is each variable measured/manipulated? (methodological level)
4. **Boundary conditions**: within what scope does the hypothesis hold? (applicability level)
5. **Falsifiability criteria**: what observation would refute this hypothesis? (judgment level)

**Common operationalization failure modes**:
- Circular definition (defining X in terms of X) → an operational definition must reference observable behavior or measurement
- Mismatch between measurement and construct (operationalism gap) → must argue that the measurement instrument actually captures the construct
- Overly broad boundary conditions ("in all contexts") → must be specific about sample, context, and time range

## Budget Gate

| Tier | Operationalization completeness | Variable measurement | Boundary conditions | Falsifiability |
|------|---------|---------|---------|---------|
| S | All abstract terms have operational definitions | All variables have draft measurement methods | Main boundary conditions specified | 1 falsification scenario |
| M | Above + justification of operationalization validity | Variable measurement includes reliability/validity considerations | Complete boundary conditions | ≥2 falsification scenarios |
| L | Above + comparison of competing operationalization schemes | Main variables include multiple operationalization schemes | Boundary conditions + external-validity statement | Complete falsifiability audit |

## Default Reference Flow

1. Invoke the `variable-identification` SOP: identify all constructs in the hypothesis, classify them as IV/DV/moderator/mediator
2. Invoke the `operationalization` SOP: provide an operational definition for each construct (including measurement method/instrument/indicator)
3. Invoke the `boundary-condition-specification` SOP: specify the scope of the hypothesis (population, context, time, culture)
4. Invoke the `falsifiability-check` SOP (via the `falsifiability-audit` tactic): generate falsification scenarios, confirm the hypothesis's falsifiability

## context-checkpoint

Record after each round:
- The original version of the hypothesis before operationalization
- The operational definition of each construct (including measurement method)
- The precise hypothesis after operationalization (If [operationalized X], then [operationalized Y])
- Boundary-condition list
- Falsification scenarios
- Operationalization quality self-assessment (any circular definitions, measurement-construct match)

<!-- BEGIN available-tables (generated) -->

## Available Tactics

可选,无固定顺序;最终叶子终为 sop。

| Tactic | 何时用 |
| --- | --- |
| falsifiability-audit | Tactic: 假设质量保证——检验可证伪性，修复不合格假设，完成操作化与边界条件规范 |

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| hypothesis-formation-variable-identification | SOP: 识别变量及其在假设中的角色 |

<!-- END available-tables (generated) -->
