---
name: pairwise-synthesis
description: Compare two methods across multiple studies — paired meta-analysis protocol design. Budget: 30 studies, 30 effect sizes, 40 web searches.
used-by: meta-analysis
---

# Pairwise Synthesis Strategy

Design a pairwise meta-analysis protocol comparing method A vs method B across multiple independent studies.

## Purpose

When two methods (interventions, algorithms, approaches) have been compared across multiple studies, synthesize the evidence into a single quantitative estimate of relative performance. This strategy produces the complete protocol — stopping before computation.

## Budget

| Resource | Floor | Target |
|----------|-------|--------|
| Studies identified | 20 | 30 |
| Effect sizes extracted | 20 | 30 |
| Web searches | 25 | 40 |
| Quality assessments | 15 | 30 |

Budget gate: cannot exit until 80% of floor met.

## State Ledger

```
<HARD-GATE>
| Metric | Current | Floor | Target | Status |
|--------|---------|-------|--------|--------|
| Studies found | 0 | 20 | 30 | BLOCKED |
| Effect sizes planned | 0 | 20 | 30 | BLOCKED |
| Web searches done | 0 | 25 | 40 | BLOCKED |
| Quality assessed | 0 | 15 | 30 | BLOCKED |
</HARD-GATE>
```

## Available Tactics

| Tactic | When to Use |
|--------|-------------|
| effect-size-extraction | After study identification, extract paired effect sizes |
| quality-assessment-protocol | Assess RoB for each included study |
| evidence-synthesis-planning | After extraction, plan the statistical model |

## Available SOPs

| SOP | When to Use |
|-----|-------------|
| pico-formulation | First — frame the comparison question |
| inclusion-criteria-design | After PICO — define what studies qualify |
| effect-size-planning | Determine which effect size metric to use |
| data-extraction-form | Design the extraction template |
| risk-of-bias-assessment | Per-study quality assessment |
| sensitivity-analysis-design | Plan robustness checks |
| publication-bias-assessment | Assess reporting bias |
| meta-analysis-synthesis | Final protocol assembly |

## Execution Guidance

1. **Frame** — Run `pico-formulation` to structure the comparison
2. **Scope** — Run `inclusion-criteria-design` to define eligibility
3. **Search** — Use dare-scholar and dare-ss to find candidate studies
4. **Extract** — Use `effect-size-extraction` tactic for each study
5. **Assess** — Use `quality-assessment-protocol` tactic for bias risk
6. **Plan** — Use `evidence-synthesis-planning` tactic for model selection
7. **Synthesize** — Run `meta-analysis-synthesis` to produce protocol

Iterate steps 3-5 until budget floor is met. Check state ledger before each iteration.

## Output Format

```yaml
protocol:
  question: [PICO-structured question]
  inclusion_criteria: [eligibility rules]
  studies_included: [list with metadata]
  effect_size_type: [SMD/OR/RR/MD]
  model: [fixed-effect/random-effects]
  heterogeneity_plan: [I2, tau2, subgroup, meta-regression]
  sensitivity_plan: [leave-one-out, influence diagnostics]
  bias_assessment_plan: [funnel plot, Egger's, trim-and-fill]
  reporting: PRISMA-2020
```
