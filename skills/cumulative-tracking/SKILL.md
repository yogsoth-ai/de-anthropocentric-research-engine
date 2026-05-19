---
name: cumulative-tracking
description: Track evidence accumulation over time — cumulative meta-analysis protocol design. Budget: 40 studies, 40 effect sizes, 30 web searches.
used-by: meta-analysis
---

# Cumulative Tracking Strategy

Design a cumulative meta-analysis protocol tracking how evidence evolves over time as new studies are published.

## Purpose

Cumulative meta-analysis adds studies one-by-one in chronological order, showing when the evidence became conclusive, whether early studies were misleading, and how the pooled estimate stabilized. This strategy produces the protocol for temporal evidence tracking.

## Budget

| Resource | Floor | Target |
|----------|-------|--------|
| Studies identified | 28 | 40 |
| Effect sizes extracted | 28 | 40 |
| Web searches | 20 | 30 |
| Temporal coverage (years) | 5 | 10+ |
| Quality assessments | 20 | 40 |

Budget gate: cannot exit until 80% of floor met.

## State Ledger

```
<HARD-GATE>
| Metric | Current | Floor | Target | Status |
|--------|---------|-------|--------|--------|
| Studies found | 0 | 28 | 40 | BLOCKED |
| Effect sizes planned | 0 | 28 | 40 | BLOCKED |
| Web searches done | 0 | 20 | 30 | BLOCKED |
| Year range covered | 0 | 5 | 10+ | BLOCKED |
| Quality assessed | 0 | 20 | 40 | BLOCKED |
</HARD-GATE>
```

## Available Tactics

| Tactic | When to Use |
|--------|-------------|
| effect-size-extraction | Extract effect sizes with publication dates |
| quality-assessment-protocol | Assess quality evolution over time |
| evidence-synthesis-planning | Plan cumulative pooling approach |

## Available SOPs

| SOP | When to Use |
|-----|-------------|
| pico-formulation | Frame the temporal evidence question |
| inclusion-criteria-design | Define eligibility with temporal scope |
| effect-size-planning | Standardize effect sizes for temporal pooling |
| data-extraction-form | Template with mandatory date fields |
| risk-of-bias-assessment | Per-study assessment (track quality trends) |
| heterogeneity-source-analysis | Time-varying heterogeneity |
| sensitivity-analysis-design | First-study effect, vintage analysis |
| publication-bias-assessment | Time-lag bias assessment |
| meta-analysis-synthesis | Final cumulative protocol assembly |

## Execution Guidance

1. **Frame** — Run `pico-formulation` with temporal dimension explicit
2. **Scope** — Run `inclusion-criteria-design` with date range requirements
3. **Search** — Systematic search emphasizing complete temporal coverage
4. **Order** — Sort studies chronologically by publication date
5. **Extract** — Use `effect-size-extraction` tactic with date metadata
6. **Assess** — Use `quality-assessment-protocol` noting temporal trends
7. **Plan** — Use `evidence-synthesis-planning` for cumulative model
8. **Synthesize** — Run `meta-analysis-synthesis` for final protocol

Ensure no temporal gaps. Flag periods with no publications.

## Output Format

```yaml
protocol:
  question: [PICO with temporal dimension]
  temporal_scope: [start_year - end_year]
  inclusion_criteria: [eligibility with date requirements]
  studies_included:
    - [study, year, effect_size, cumulative_n]
  chronological_order: [sorted study list]
  effect_size_type: [consistent metric across time]
  model: [random-effects with cumulative pooling]
  temporal_analyses:
    - cumulative_forest_plot
    - first_study_effect_test
    - evidence_stabilization_point
    - vintage_regression
  time_lag_bias: [assessment plan]
  quality_trend: [RoB evolution over time]
  reporting: PRISMA-2020 + temporal extension
```
