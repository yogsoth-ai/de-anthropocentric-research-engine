---
name: evidence-based-prioritization
description: 'Strategy: evidence-strength-based AHRQ PiCMe assessment — drive gap
  prioritization with the quality of literature evidence'
version: 1.0.0
category: hypothesis-formation
type: strategy
campaign: gap-prioritization
tactics:
- scoring-matrix-construction
sops:
- ahrq-picme-assessment
- importance-scoring
- priority-synthesis
dependencies:
  tactics:
  - hypothesis-formation-scoring-matrix-construction
  sops:
  - gap-normalization
  - priority-synthesis
---

# Evidence-Based Prioritization

Evidence-strength-based prioritization: use the six dimensions of the AHRQ PiCMe framework to systematically assess the quality of the literature evidence behind each gap, surfacing the gaps where evidence is weakest and impact is greatest.

## When to Use

- Gaps come from rigorous literature review (with explicit citation support)
- You need to explain prioritization decisions to academic peers or funding agencies
- The research domain has a mature evidence-grading system (medicine, biology, some CS subfields)
- You want to prioritize attacking the gaps with the "largest evidence void" rather than the "most popular" ones

## Thinking Framework

**Core principle**: a gap's priority depends not only on how important it is, but also on how weak the existing evidence is. The weaker the evidence and the higher the importance, the higher the priority.

The AHRQ PiCMe six-dimension assessment framework:

1. **Population (P)**: how well-defined is the population/system this gap affects? How broad is the coverage?
2. **Intervention (I)**: what is the evidence quality of existing interventions/methods? (RCT > observational > expert opinion)
3. **Comparator (C)**: is there a reasonable control baseline? Is the lack of a control itself a gap?
4. **Metrics (Me)**: are the outcome metrics standardized? Is the absence of metrics part of the gap?
5. **Evidence Strength (E)**: consistency, sample size, and methodological rigor of existing evidence
6. **Evidence Gap (G)**: among the five dimensions above, which has the scarcest evidence?

Final score = importance score × (1 − evidence sufficiency). Gaps with more sufficient evidence get lower priority (because others are already working on them).

**Key insight**: this framework naturally favors "neglected important problems" over "popular but already crowded problems."

## Budget Gate

| Tier | Number of gaps | PiCMe dimensions | Literature check | Final output |
|------|---------|-----------|---------|---------|
| S | 3–8 | all 6 dimensions | ≥2 supporting references per gap | ranking table + evidence-void report |
| M | 9–15 | all 6 dimensions | ≥3 supporting references per gap | ranking table + evidence-void report + attack suggestions for top 3 gaps |
| L | 16–20 | all 6 dimensions | ≥5 supporting references per gap | ranking table + detailed evidence map + attack suggestions for top 5 gaps |

## Default Reference Flow

1. Call the `gap-normalization` SOP: standardize the gap format and extract the list of supporting references for each gap
2. Call the `ahrq-picme-assessment` SOP: run the six-dimension assessment on each gap
3. Call the `importance-scoring` SOP: assess importance independently (not influenced by evidence strength)
4. Call the `scoring-matrix-construction` tactic: build a gap × PiCMe-dimension matrix
5. Compute the composite score: importance × (1 − mean evidence sufficiency)
6. Call the `priority-synthesis` SOP: produce the final ranking + evidence-void summary

## context-checkpoint

After each round, record:
- The PiCMe assessment matrix (gap × 6-dimension scores)
- The supporting-reference list for each gap (with evidence grade)
- The composite evidence-sufficiency scores
- The final priority ranking (with scoring formula)

<!-- BEGIN available-tables (generated) -->

## Available Tactics

Optional, no fixed order; the final leaf is always a sop.

| Tactic | When to use |
| --- | --- |
| hypothesis-formation-scoring-matrix-construction | Tactic: orchestrate multi-dimensional scoring SOPs to build a comprehensive assessment matrix for all gaps |

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| gap-normalization | SOP: Unify gaps from different sources into the standard GapRecord format |
| priority-synthesis | SOP: synthesize all scoring data into a final gap priority list and attack-path suggestions |

<!-- END available-tables (generated) -->
