---
name: analogy-extraction
description: Extract transferable structural principles from source domains. Orchestrates source identification → abstraction → structural mapping → transfer validation.
execution: tactic
used-by: cross-domain-discovery, synectics, biomimicry
---

# Analogy Extraction

Extract transferable structural principles from source domains.

## Stages

### Stage 1: Source Identification

Identify candidate source domains using domain-scanning SOP. Evaluate each for structural similarity depth (surface/structural/systemic).

### Stage 2: Abstraction

For each promising source, extract the abstract principle using abstraction-extraction or biological-strategy-extraction SOP. Strip domain-specific details to reveal the transferable mechanism.

### Stage 3: Structural Mapping

Map source structure to target domain. Identify: corresponding elements, missing elements (gaps), extra elements (opportunities). Use structural-mapping SOP.

### Stage 4: Transfer Validation

Assess mapping quality: Is the analogy surface-level (shared labels) or deep (shared relational structure)? Use analogy-quality-assessment SOP. Only deep analogies warrant transfer.

## Minimum Yield

| Metric | Floor |
|--------|-------|
| Source domains scanned | ≥5 |
| Abstractions extracted | ≥3 |
| Structural mappings completed | ≥3 |
| Validated deep analogies | ≥2 |

## Available SOPs

| SOP | Role |
|-----|------|
| domain-scanning | Stage 1 — find candidate source domains |
| web-search | Stage 1 — supplement domain search |
| paper-overview | Stage 1 — find academic analogies |
| abstraction-extraction | Stage 2 — extract abstract principles |
| structural-mapping | Stage 3 — map source→target structure |
| analogy-quality-assessment | Stage 4 — validate mapping depth |
| novelty-scoring | Post — score resulting ideas |
| idea-synthesis | Post — synthesize into coherent concepts |
