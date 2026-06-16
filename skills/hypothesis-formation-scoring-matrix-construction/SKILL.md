---
name: hypothesis-formation-scoring-matrix-construction
description: 'Tactic: orchestrate multi-dimensional scoring SOPs to build a comprehensive
  assessment matrix for all gaps'
version: 1.0.0
category: hypothesis-formation
type: tactic
campaign: gap-prioritization
sops:
- importance-scoring
- feasibility-scoring
- novelty-scoring
- impact-scoring
- ahrq-picme-assessment
dependencies:
  sops:
  - ahrq-picme-assessment
  - feasibility-scoring
  - hypothesis-formation-novelty-scoring
  - impact-scoring
  - importance-scoring
---

# Scoring Matrix Construction

Orchestrate multiple scoring-dimension SOPs to build a multi-dimensional comprehensive assessment matrix for each gap, serving as the quantitative basis for ranking decisions.

## Orchestration Intent

Single-dimension scoring is prone to bias (e.g., ranking purely by "importance" ignores feasibility). This tactic invokes each scoring SOP in parallel or serial, comparing the multiple dimension scores of all gaps within a single matrix, so that priority judgments rest on systematic evidence rather than intuition.

CC selects the number of dimensions to cover based on topic tier; each dimension's scoring is handled by a dedicated SOP; once scoring is complete, CC consolidates the SOP outputs into a single matrix format.

## Available SOPs

| SOP | Responsibility | When to invoke |
|-----|------|---------|
| importance-scoring | Assess a gap's strategic importance to the field (0-10) | Required for all tiers |
| feasibility-scoring | Assess the feasibility of attacking a gap with currently available resources/methods (0-10) | Required for all tiers |
| novelty-scoring | Assess the research novelty and original-contribution potential of a gap (0-10) | Required for all tiers |
| impact-scoring | Assess the potential citation/application impact of the research output (0-10) | Added at M/L tier |
| ahrq-picme-assessment | Use the AHRQ PiCMe framework for a structured assessment of clinical/applied gaps | At L tier or when the biomedical/health domain is involved |

## Orchestration Pattern

**Simplified (S tier, 3 dims)**
- Invoke: importance-scoring, feasibility-scoring, novelty-scoring
- Matrix: gaps × 3 dimensions
- Execute all SOPs in parallel, consolidate results

**Default (M tier, 4 dims)**
- Invoke: importance-scoring, feasibility-scoring, novelty-scoring, impact-scoring
- Matrix: gaps × 4 dimensions
- Execute the first 4 SOPs in parallel, consolidate results

**Deep (L tier, 5 dims + PiCMe)**
- Invoke: all 5 SOPs
- Matrix: gaps × 5 dimensions + PiCMe structured-assessment appendix
- Execute the first 4 SOPs in parallel first, PiCMe serially after (depends on domain confirmation)

## Minimum Yield

- Complete matrix: every gap × every dimension has a score filled in (no blanks)
- Each scoring cell carries a 1-2 sentence scoring rationale
- The matrix includes a weighted-total column (equal weights by default, unless weights are provided upstream)
- Output format: Markdown table + a scoring-summary paragraph for each gap

## Yield Report

After execution, report to the calling strategy:
- Number of gaps covered / number of scoring dimensions
- Score distribution (highest/lowest/median)
- The dimension with the largest scoring variance (for sensitivity-testing to perturb first)
- Scoring confidence: which gaps have sufficient evidence and which need supplementary literature

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| ahrq-picme-assessment | SOP: Use the AHRQ PiCMe framework to systematically assess a research gap across 6 dimensions |
| feasibility-scoring | SOP: assess the attackability of a research gap, identify bottlenecks, and output a feasibility score |
| hypothesis-formation-novelty-scoring | SOP: Assess the novelty potential of a research gap, identify differentiation directions, and output a score |
| impact-scoring | SOP: assess the potential impact of a research gap, identify beneficiaries and output an impact score |
| importance-scoring | SOP: assess the academic and practical importance of a research gap, output a 1-5 score with rationale |

<!-- END available-tables (generated) -->
