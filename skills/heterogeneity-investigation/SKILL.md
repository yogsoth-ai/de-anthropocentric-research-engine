---
name: heterogeneity-investigation
description: Explain why different studies reach different conclusions — heterogeneity investigation protocol. Budget: 30 studies, 30 effect sizes, 50 web searches.
used-by: meta-analysis
---

# Heterogeneity Investigation Strategy

Design a protocol to investigate and explain between-study heterogeneity — why studies of the same question reach different conclusions.

## Purpose

When a meta-analysis reveals substantial heterogeneity (I2 > 50%, significant Q-test, large tau2), this strategy designs the investigation protocol: subgroup analyses, meta-regression, moderator identification, and outlier diagnostics. Produces the investigation plan, not the computation.

## Budget

| Resource | Floor | Target |
|----------|-------|--------|
| Studies identified | 20 | 30 |
| Effect sizes extracted | 20 | 30 |
| Web searches | 35 | 50 |
| Moderator candidates | 5 | 10+ |
| Quality assessments | 15 | 30 |

Budget gate: cannot exit until 80% of floor met.

## State Ledger

```
<HARD-GATE>
| Metric | Current | Floor | Target | Status |
|--------|---------|-------|--------|--------|
| Studies found | 0 | 20 | 30 | BLOCKED |
| Effect sizes planned | 0 | 20 | 30 | BLOCKED |
| Web searches done | 0 | 35 | 50 | BLOCKED |
| Moderators identified | 0 | 5 | 10+ | BLOCKED |
| Quality assessed | 0 | 15 | 30 | BLOCKED |
</HARD-GATE>
```

## Available Tactics

| Tactic | When to Use |
|--------|-------------|
| effect-size-extraction | Extract effect sizes with full study characteristics |
| quality-assessment-protocol | Assess whether quality explains heterogeneity |
| evidence-synthesis-planning | Plan subgroup and meta-regression models |

## Available SOPs

| SOP | When to Use |
|-----|-------------|
| pico-formulation | Frame the heterogeneity question |
| inclusion-criteria-design | Broad inclusion to capture variation |
| effect-size-planning | Standardize for comparability |
| data-extraction-form | Rich moderator variable extraction |
| risk-of-bias-assessment | RoB as potential moderator |
| heterogeneity-source-analysis | Core SOP — classify heterogeneity sources |
| sensitivity-analysis-design | Outlier removal, influence diagnostics |
| publication-bias-assessment | Bias as heterogeneity source |
| meta-analysis-synthesis | Final investigation protocol |

## Execution Guidance

1. **Frame** — Run `pico-formulation` emphasizing variation in P/I/C/O
2. **Scope** — Run `inclusion-criteria-design` with broad criteria (capture variation)
3. **Search** — Systematic search + web research on known moderators
4. **Extract** — Use `effect-size-extraction` with rich study-level covariates
5. **Hypothesize** — Run `heterogeneity-source-analysis` to generate moderator hypotheses
6. **Assess** — Use `quality-assessment-protocol` (RoB as moderator)
7. **Plan** — Use `evidence-synthesis-planning` for subgroup + meta-regression
8. **Synthesize** — Run `meta-analysis-synthesis` for investigation protocol

Web searches focus on domain knowledge about why results might differ (methodological, clinical, statistical heterogeneity).

## Output Format

```yaml
protocol:
  question: [Why do studies of X reach different conclusions?]
  heterogeneity_metrics: [I2, tau2, Q-test, prediction interval]
  moderator_candidates:
    clinical: [population, intervention details, outcome timing]
    methodological: [study design, RoB, measurement tools]
    statistical: [effect size type, analysis method, sample size]
  investigation_plan:
    subgroup_analyses: [categorical moderators]
    meta_regression: [continuous moderators]
    outlier_diagnostics: [influence analysis, Baujat plot]
    sensitivity: [leave-one-out, cumulative by quality]
  a_priori_hypotheses: [pre-specified moderator hypotheses]
  multiple_testing: [correction strategy]
  reporting: PRISMA-2020 + heterogeneity reporting guidelines
```
