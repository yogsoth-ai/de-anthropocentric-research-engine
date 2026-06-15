---
name: argument-mapping
description: Campaign for mapping argument structures — extract claims, link evidence,
  assess strength, synthesize positions. Produces argument graphs in the wiki vault.
execution: campaign
dependencies:
  strategies:
  - argument-synthesis
  - claim-extraction
  - evidence-linking-arg
  tactics:
  - knowledge-compilation
  sops:
  - context-checkpoint
  - context-init
---

# Argument Mapping

Map argument structures for research domains. Extracts claims from sources, links supporting and opposing evidence, assesses argument strength, and synthesizes coherent positions from complex debates.

## Manifest

| Level | Count | Skills |
|-------|-------|--------|
| Strategy | 3 | claim-extraction, evidence-linking-arg, argument-synthesis |
| Tactic | 2 | claim-decomposition, strength-assessment |
| SOP | 6 | claim-page-creation, rebuttal-documentation, evidence-attachment, strength-scoring, argument-visualization, synthesis-report |

## Budget Table

| Metric | Small | Medium | Large |
|--------|-------|--------|-------|
| Claims extracted | 10 | 25 | 50 |
| Evidence links created | 15 | 40 | 80 |
| Rebuttals documented | 3 | 10 | 20 |
| Strength scores assigned | 10 | 25 | 50 |
| Synthesis reports | 1 | 3 | 5 |

## Strategy Sequence (Reference, Not Prescription)

1. **claim-extraction** — identify and extract claims from source material
2. **evidence-linking-arg** — link evidence to claims (supporting, contradicting, qualifying)
3. **argument-synthesis** — synthesize positions from the argument graph

## MCP Tools Used

- `vault_search` — find existing claims and evidence
- `vault_add_edge` — create argument edges (supported_by, contradicts, derived_from)
- `vault_query_graph` — trace argument chains
- `vault_graph_stats` — assess argument coverage
- `vault_lint` — validate structural integrity

## Context-Management

<HARD-GATE>
- Call `context-init` at campaign start
- Call `context-checkpoint` after each strategy completes
- Call `knowledge-compilation` after each strategy
</HARD-GATE>

## Guiding Principles

- **Claims are atomic.** Each claim page states exactly one proposition. Compound claims must be decomposed.
- **Evidence is typed.** Every evidence link specifies its relationship: supports, contradicts, qualifies, or is irrelevant.
- **Strength is earned.** A claim's strength comes from the weight and diversity of its evidence, not from authority or repetition.
- **Steel-man first.** Before documenting rebuttals, ensure the strongest version of each claim is represented.
- **Synthesis is not averaging.** The synthesis report identifies which claims survive scrutiny, not a compromise between all positions.
