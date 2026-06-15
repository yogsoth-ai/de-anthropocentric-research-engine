---
name: network-comparison
description: 'Compare N methods simultaneously including indirect evidence — network
  meta-analysis protocol design. Budget: 50 studies, 80 effect sizes, 60 web searches.'
dependencies:
  tactics:
  - effect-size-extraction
  - evidence-synthesis-planning
  - quality-assessment-protocol
  sops:
  - data-extraction-form
  - effect-size-planning
  - evidence-network-construction
  - heterogeneity-source-analysis
  - inclusion-criteria-design
  - meta-analysis-synthesis
  - pico-formulation
  - publication-bias-assessment
  - risk-of-bias-assessment
  - sensitivity-analysis-design
---

# Network Comparison Strategy

Design a network meta-analysis (NMA) protocol comparing N>=3 methods simultaneously, leveraging both direct and indirect evidence.

## Purpose

When multiple methods have been compared in various head-to-head studies but no single study compares all methods, network meta-analysis synthesizes direct and indirect evidence to rank all methods simultaneously. This strategy produces the complete NMA protocol.

## Budget

| Resource | Floor | Target |
|----------|-------|--------|
| Studies identified | 35 | 50 |
| Effect sizes extracted | 55 | 80 |
| Web searches | 40 | 60 |
| Network nodes (methods) | 3 | N |
| Quality assessments | 25 | 50 |

Budget gate: cannot exit until 80% of floor met.

## State Ledger

```
<HARD-GATE>
| Metric | Current | Floor | Target | Status |
|--------|---------|-------|--------|--------|
| Studies found | 0 | 35 | 50 | BLOCKED |
| Effect sizes planned | 0 | 55 | 80 | BLOCKED |
| Web searches done | 0 | 40 | 60 | BLOCKED |
| Network nodes | 0 | 3 | N | BLOCKED |
| Quality assessed | 0 | 25 | 50 | BLOCKED |
</HARD-GATE>
```

## Available Tactics

| Tactic | When to Use |
|--------|-------------|
| effect-size-extraction | Extract effect sizes from each study arm |
| quality-assessment-protocol | Assess RoB + CINeMA framework for NMA |
| evidence-synthesis-planning | Plan NMA model (consistency, ranking) |

## Available SOPs

| SOP | When to Use |
|-----|-------------|
| pico-formulation | Frame the multi-method comparison |
| inclusion-criteria-design | Define eligibility across all comparisons |
| effect-size-planning | Standardize effect sizes across study designs |
| data-extraction-form | Multi-arm extraction template |
| risk-of-bias-assessment | Per-study + network-level bias |
| evidence-network-construction | Build the network geometry graph |
| heterogeneity-source-analysis | Assess transitivity assumption |
| sensitivity-analysis-design | Node-splitting, exclusion sensitivity |
| publication-bias-assessment | Comparison-adjusted funnel plots |
| meta-analysis-synthesis | Final NMA protocol assembly |

## Execution Guidance

1. **Frame** — Run `pico-formulation` for the multi-method question
2. **Scope** — Run `inclusion-criteria-design` covering all treatment nodes
3. **Search** — Systematic search for all pairwise comparisons
4. **Network** — Run `evidence-network-construction` to map the geometry
5. **Extract** — Use `effect-size-extraction` tactic per study arm
6. **Assess** — Use `quality-assessment-protocol` (RoB2 + CINeMA)
7. **Transitivity** — Run `heterogeneity-source-analysis` to verify transitivity
8. **Plan** — Use `evidence-synthesis-planning` for NMA model selection
9. **Synthesize** — Run `meta-analysis-synthesis` for final protocol

Iterate steps 3-6 until budget floor met. Verify network connectivity after each batch.

## Output Format

```yaml
protocol:
  question: [PICO with multiple interventions]
  network_geometry:
    nodes: [list of methods/interventions]
    edges: [direct comparisons available]
    connected: [yes/no]
  inclusion_criteria: [eligibility rules]
  studies_included: [list with arm-level metadata]
  effect_size_type: [standardized across network]
  model: [consistency/inconsistency NMA model]
  transitivity_assessment: [effect modifiers balanced?]
  ranking_method: [SUCRA/P-score/mean ranks]
  heterogeneity_plan: [global I2, tau2, between-design heterogeneity]
  inconsistency_plan: [node-splitting, design-by-treatment interaction]
  sensitivity_plan: [network reduction, node exclusion]
  bias_assessment_plan: [comparison-adjusted funnel, small-study effects]
  reporting: PRISMA-NMA extension
```

<!-- BEGIN available-tables (generated) -->

## Available Tactics

可选,无固定顺序;最终叶子终为 sop。

| Tactic | 何时用 |
| --- | --- |
| effect-size-extraction | Systematically extract effect sizes and conditions from papers for meta-analytic synthesis |
| evidence-synthesis-planning | Plan the statistical synthesis approach — model selection, heterogeneity strategy, and reporting |
| quality-assessment-protocol | Methodological quality and bias risk assessment of included studies using validated tools |

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| data-extraction-form | Design structured data extraction form for systematic meta-analysis data collection |
| effect-size-planning | Determine effect size types and calculation methods for meta-analytic synthesis |
| evidence-network-construction | Build evidence network graph for network meta-analysis — nodes, edges, geometry assessment |
| heterogeneity-source-analysis | Identify and classify sources of between-study heterogeneity (clinical, methodological, statistical) |
| inclusion-criteria-design | Define inclusion/exclusion criteria for systematic study selection in meta-analysis |
| meta-analysis-synthesis | Produce final meta-analysis protocol document assembling all planning outputs into PRISMA-compliant protocol |
| pico-formulation | Construct PICO/PECO framework for the meta-analysis research question |
| publication-bias-assessment | Plan funnel plots, Egger's test, trim-and-fill, p-curve, and selection model analyses for publication bias |
| risk-of-bias-assessment | Assess methodological bias using RoB2, PROBAST, or QUADAS-2 validated tools |
| sensitivity-analysis-design | Design leave-one-out, influence diagnostics, subgroup analyses, and robustness checks |

<!-- END available-tables (generated) -->
