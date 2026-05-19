---
name: combination-mapping
description: Systematically enumerate parameter dimensions and generate viable combinations. Orchestrates parameter extraction → value enumeration → compatibility assessment → synthesis.
execution: tactic
used-by: morphological-exploration, combinatorial-creativity, structural-deconstruction, systematic-enumeration
---

# Combination Mapping

Systematically enumerate parameter dimensions and generate viable combinations.

## Stages

### Stage 1: Parameter Extraction

Identify independent parameters of the problem space using parameter-identification SOP. Verify orthogonality.

### Stage 2: Value Enumeration

For each parameter, enumerate 3-5 meaningful values including boundary and extreme values. Use value-enumeration SOP or direct generation.

### Stage 3: Compatibility Assessment

Evaluate pairwise compatibility of value combinations. Flag logically/empirically/normatively inconsistent pairs. Use consistency-pair-evaluation SOP if available.

### Stage 4: Path Generation

Generate viable combination paths through the consistent solution space. Prioritize unexplored regions (white space). Use path-generation or recombination-generation SOP.

### Stage 5: Synthesis

Evaluate generated combinations for novelty and feasibility. Synthesize into structured ideas.

## Minimum Yield

| Metric | Floor |
|--------|-------|
| Parameters identified | ≥4 |
| Values per parameter | ≥3 |
| Combinations evaluated | ≥10 |
| Viable novel combinations | ≥5 |

## Available SOPs

| SOP | Role |
|-----|------|
| parameter-identification | Stage 1 — decompose problem into parameters |
| value-enumeration | Stage 2 — enumerate parameter values |
| consistency-pair-evaluation | Stage 3 — check pairwise compatibility |
| path-generation | Stage 4 — generate combination paths |
| recombination-generation | Stage 4 — alternative combination approach |
| constraint-injection | Stage 3 — inject constraints to reduce space |
| novelty-scoring | Stage 5 — score combinations |
| idea-synthesis | Stage 5 — synthesize into concepts |
| saturation-detection | Post — check if space is exhausted |
