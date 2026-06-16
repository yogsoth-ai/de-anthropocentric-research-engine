---
name: deductive-hypothesis-generation
description: 'Strategy: deduce hypotheses from existing theory'
version: 1.0.0
category: hypothesis-formation
type: strategy
campaign: hypothesis-formulation
tactics:
- theory-mechanism-extraction
- falsifiability-audit
sops:
- theory-identification
- mechanism-extraction
- variable-identification
- relationship-specification
- boundary-condition-specification
- falsifiability-check
- operationalization
dependencies:
  tactics:
  - falsifiability-audit
  - theory-mechanism-extraction
---

# Deductive Hypothesis Generation

Deduce hypotheses from existing theory: in domains with mature theory, transform theoretical propositions into specific testable predictions through an explicit reasoning chain.

## When to Use

- The domain has mature foundational theory (named theories, formal models, or accepted mechanisms)
- The research gap manifests as "a discrepancy between theoretical prediction and real-world observation"
- The goal is to test, extend, or delimit the scope of an existing theory
- Highly defensible hypotheses are needed (reviewers will press for theoretical justification)

Not applicable: emerging domains rich in data but lacking theory → use inductive-hypothesis-generation instead.

## Thinking Framework

**Theory → Mechanism → Variable Relationship → Testable Prediction**

The core logic of deduction:

1. **Theory**: identify the foundational theory underpinning the research question (named theory, formal model)
2. **Mechanism**: extract the causal mechanism from the theory (the intermediate process by which "X affects Y through Z")
3. **Variable Relationship**: translate the mechanism into directional relationships among variables (positive/negative/moderating/mediating)
4. **Testable Prediction**: concretize the variable relationship into an observable prediction under specific conditions

Every step must be traceable: each prediction traces back to a mechanism, each mechanism traces back to a theory. This is what distinguishes a deductive hypothesis from a guess.

**Common pitfalls**:
- Theory citation that stays superficial (naming only, no specific propositions) → you must cite the theory's core propositions
- Skipping the mechanism and jumping straight from theory to prediction → the mechanism is the key node of the deductive chain and cannot be omitted
- Hypothesis scope too broad ("in all contexts") → deduction must state boundary conditions

## Budget Gate

| Tier | Theory coverage | Mechanism extraction | Hypothesis output | Falsifiability |
|------|---------|---------|---------|---------|
| S | ≥2 named theories | ≥3 causal mechanisms | ≥2 structured hypotheses | 1 falsification scenario per hypothesis |
| M | ≥3 named theories | ≥5 causal mechanisms | ≥3 structured hypotheses | ≥1 scenario + boundary conditions per hypothesis |
| L | ≥5 named theories | ≥8 causal mechanisms | ≥5 structured hypotheses | full falsifiability audit + competing-theory comparison |

## Default Reference Flow

1. Call the `theory-identification` SOP: scan the domain literature and list the named theories relevant to the gap and their core propositions
2. Call the `mechanism-extraction` SOP (via the `theory-mechanism-extraction` tactic): extract causal mechanism chains from each theory
3. Call the `variable-identification` SOP: translate the constructs in the mechanisms into operational variables
4. Call the `relationship-specification` SOP: specify directional relationships among variables (including moderating/mediating structures)
5. Call the `boundary-condition-specification` SOP: identify the preconditions under which the theory applies (population, context, time range, etc.)
6. Call the `falsifiability-check` SOP (via the `falsifiability-audit` tactic): generate a falsification scenario for each hypothesis
7. Call the `operationalization` SOP: provide draft measurement methods for the key variables

## context-checkpoint

After each round, record:
- The list of identified theories (name, core proposition, source)
- The list of extracted mechanisms (each tagged with its source theory)
- The current set of hypothesis drafts (including variable relationships + boundary conditions)
- Falsifiability status (passed / pending review / unfalsifiable, needs revision)

<!-- BEGIN available-tables (generated) -->

## Available Tactics

可选,无固定顺序;最终叶子终为 sop。

| Tactic | 何时用 |
| --- | --- |
| falsifiability-audit | Tactic: 假设质量保证——检验可证伪性，修复不合格假设，完成操作化与边界条件规范 |
| theory-mechanism-extraction | Tactic: 演绎路径核心——从理论出发提取机制、变量与关系，生成假设候选 |

<!-- END available-tables (generated) -->
