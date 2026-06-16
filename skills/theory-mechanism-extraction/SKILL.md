---
name: theory-mechanism-extraction
description: 'Tactic: Core of the deductive path — start from theory to extract mechanisms,
  variables, and relationships, generating hypothesis candidates'
version: 1.0.0
category: hypothesis-formation
type: tactic
campaign: hypothesis-formulation
sops:
- theory-identification
- mechanism-extraction
- variable-identification
- relationship-specification
dependencies:
  sops:
  - hypothesis-formation-variable-identification
  - mechanism-extraction
  - relationship-specification
  - theory-identification
---

# Theory Mechanism Extraction

Core of the deductive path — starting from existing theory, systematically extract mechanisms, identify variables, and specify relationships, providing a structured basis for deductive hypothesis generation.

## Orchestration Intent

The starting point of deductive reasoning is theory, not data. This tactic forces the CC to first identify relevant theories in the domain, then unpack layer by layer: theory → mechanism → variable → variable-to-variable relationship. Each layer is the prerequisite for the next; skipping steps is not allowed.

The final output is not the hypotheses themselves, but the "raw material" for hypotheses — each mechanism corresponds to at least one hypothesis candidate (with variables and direction), for the upstream strategy to further formalize.

## Available SOPs

| SOP | Responsibility | When to call |
|-----|------|---------|
| theory-identification | Identify existing theories relevant to the gap/insight (including theory name, core claim, scope of applicability) | Required in all modes, executed first |
| mechanism-extraction | Extract operationalizable causal mechanisms from each theory (mechanism = the process linking cause and effect) | Required in all modes, after theory-identification |
| variable-identification | Identify independent, dependent, moderating, and control variables from each mechanism | Required in all modes, after mechanism-extraction |
| relationship-specification | Specify the directional relationships between variables (positive/negative/nonlinear/moderation/mediation), generating hypothesis candidates | Required in all modes, executed last |

## Orchestration Pattern

**Simplified (S tier, 1 theory)**
- Sequential execution: theory-identification → mechanism-extraction → variable-identification → relationship-specification
- Coverage: 1 theory, ≥1 mechanism, ≥1 hypothesis candidate
- Suitable when: the gap background is clear and theoretical support is singular

**Standard (M tier, 2-3 theories)**
- Execute all 4 SOPs sequentially, repeating mechanism-extraction + variable-identification + relationship-specification for each identified theory
- Coverage: ≥2 theories, ≥3 mechanisms, ≥1 hypothesis candidate per mechanism
- Suitable when: the gap spans multiple theoretical frameworks and deductive paths must be compared

**Deep (L tier, ≥3 theories)**
- Execute all 4 SOPs; mechanism-extraction is run independently for each theory; relationship-specification additionally outputs a cross-theory variable-overlap analysis
- Coverage: ≥3 theories, ≥5 mechanisms, cross-theory variable mapping, ≥5 hypothesis candidates
- Suitable when: the domain is theory-rich and systematic deductive coverage is needed

## Minimum Yield

- ≥2 theories identified and described (including core claim and scope of applicability)
- ≥3 mechanisms extracted from the theories (each with a causal-chain description)
- Each mechanism corresponds to at least 1 hypothesis candidate, including:
  - Independent and dependent variables (named)
  - Relationship direction (positive/negative/nonlinear)
  - Source mechanism (traceable to which mechanism of which theory)

## Yield Report

After execution, report to the calling strategy:
- Number of theories identified / mechanisms extracted / hypothesis candidates generated
- Theory coverage (which theories were included, which were excluded and why)
- Variable overlap (variables shared by multiple mechanisms, possibly key moderating variables)
- Hypothesis candidate quality assessment: which candidate variables are highly operationalizable, which need further operationalization

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| hypothesis-formation-variable-identification | SOP: identify variables and their roles within a hypothesis |
| mechanism-extraction | SOP: extract causal mechanism chains from a theory |
| relationship-specification | SOP: specify the direction and form of relationships between variables |
| theory-identification | SOP: Identify theoretical frameworks relevant to a research gap |

<!-- END available-tables (generated) -->
