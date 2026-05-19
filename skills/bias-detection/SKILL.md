---
name: bias-detection
description: Assess systematic biases in the evidence body — publication bias, reporting bias, and selective outcome reporting. Budget: 40 studies, 40 effect sizes, 40 web searches.
used-by: meta-analysis
---

# Bias Detection Strategy

Design a protocol to systematically assess biases that threaten the validity of meta-analytic conclusions.

## Purpose

Bias in the evidence body (publication bias, outcome reporting bias, citation bias, time-lag bias, language bias) can invalidate pooled estimates. This strategy designs the complete bias detection and adjustment protocol — funnel plots, statistical tests, sensitivity analyses, and GRADE certainty downgrading.

## Budget

| Resource | Floor | Target |
|----------|-------|--------|
| Studies identified | 28 | 40 |
| Effect sizes extracted | 28 | 40 |
| Web searches | 28 | 40 |
| Bias domains assessed | 5 | 8 |
| Quality assessments | 20 | 40 |

Budget gate: cannot exit until 80% of floor met.

## State Ledger

```
<HARD-GATE>
| Metric | Current | Floor | Target | Status |
|--------|---------|-------|--------|--------|
| Studies found | 0 | 28 | 40 | BLOCKED |
| Effect sizes planned | 0 | 28 | 40 | BLOCKED |
| Web searches done | 0 | 28 | 40 | BLOCKED |
| Bias domains assessed | 0 | 5 | 8 | BLOCKED |
| Quality assessed | 0 | 20 | 40 | BLOCKED |
</HARD-GATE>
```

## Available Tactics

| Tactic | When to Use |
|--------|-------------|
| effect-size-extraction | Extract effect sizes with precision (SE, CI) |
| quality-assessment-protocol | Full RoB2 assessment per study |
| evidence-synthesis-planning | Plan bias-adjusted models |

## Available SOPs

| SOP | When to Use |
|-----|-------------|
| pico-formulation | Frame the evidence assessment question |
| inclusion-criteria-design | Include grey literature, preprints |
| effect-size-planning | Ensure precision metrics extracted |
| data-extraction-form | Template capturing reporting completeness |
| risk-of-bias-assessment | Per-study RoB (core of this strategy) |
| publication-bias-assessment | Core SOP — funnel plots, statistical tests |
| sensitivity-analysis-design | Trim-and-fill, selection models |
| heterogeneity-source-analysis | Bias as heterogeneity driver |
| meta-analysis-synthesis | Final bias assessment protocol |

## Execution Guidance

1. **Frame** — Run `pico-formulation` for the evidence reliability question
2. **Scope** — Run `inclusion-criteria-design` maximizing source diversity (grey lit, preprints, registries)
3. **Search** — Search for published AND unpublished studies, trial registries
4. **Extract** — Use `effect-size-extraction` with precision metrics (SE, CI, N)
5. **Assess** — Use `quality-assessment-protocol` for comprehensive RoB2
6. **Detect** — Run `publication-bias-assessment` for statistical detection plan
7. **Investigate** — Run `heterogeneity-source-analysis` for bias-driven heterogeneity
8. **Adjust** — Run `sensitivity-analysis-design` for bias-adjustment methods
9. **Synthesize** — Run `meta-analysis-synthesis` for final protocol

Web searches target: trial registries, grey literature databases, dissertation repositories, conference abstracts.

## Output Format

```yaml
protocol:
  question: [Is the evidence body for X biased?]
  bias_domains:
    publication_bias:
      visual: [funnel plot, contour-enhanced funnel]
      statistical: [Egger's test, Begg's test, Peters' test]
      adjustment: [trim-and-fill, Copas selection model, PET-PEESE]
    outcome_reporting_bias:
      detection: [registry-publication comparison]
      tool: [ROB-ME, ORBIT]
    time_lag_bias:
      detection: [time-to-publication analysis]
    citation_bias:
      detection: [citation network analysis]
    language_bias:
      mitigation: [multi-language search strategy]
    small_study_effects:
      detection: [funnel asymmetry, regression tests]
      adjustment: [limit meta-analysis]
  grey_literature_search: [databases, registries, contacts]
  grade_assessment:
    domain: publication_bias
    downgrading_criteria: [when to downgrade certainty]
  sensitivity_plan: [selection model, 3PSM, p-curve, z-curve]
  reporting: PRISMA-2020 + ROB-ME guidelines
```
