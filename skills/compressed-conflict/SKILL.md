---
name: compressed-conflict
description: Generate compressed conflicts (oxymorons) from problem contradictions
  and extract concrete idea directions from the symbolic tension.
execution: tactic
dependencies:
  sops:
  - analogy-chain
  - springboard-launch
  - symbolic-compression
---

# Compressed Conflict

Generate compressed conflicts (oxymorons) from problem contradictions and extract concrete idea directions.

## Stages

### Stage 1: Symbolic Compression

Identify the core contradiction in the problem and compress it into 2-3 word oxymorons using symbolic-compression SOP. Generate multiple oxymorons capturing different facets of the tension.

### Stage 2: Analogy Chain

Take the most evocative oxymorons and deepen them through analogy chaining using analogy-chain SOP. Each layer reveals new aspects of the contradiction and potential resolution paths.

### Stage 3: Idea Extraction

Extract concrete idea directions from the symbolic tensions. Each oxymoron should suggest at least one mechanism that resolves the contradiction it embodies.

## Minimum Yield

| Metric | Floor |
|--------|-------|
| Contradictions identified | ≥2 |
| Oxymorons generated | ≥4 |
| Oxymorons with concrete idea directions | ≥2 |
| Analogy chain depth | ≥3 layers |

## Available SOPs

| SOP | Role |
|-----|------|
| symbolic-compression | Stage 1 — compress contradictions into oxymorons |
| analogy-chain | Stage 2 — deepen oxymorons through layers |
| springboard-launch | Stage 3 — convert symbolic insights to solutions |
| synectics-synthesis | Post — synthesize compressed conflict outputs |

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| analogy-chain | Chain analogies to deeper levels (3-5 layers). Each layer reveals new aspects and insights not visible at the surface. |
| springboard-launch | Convert analogy insights into concrete feasible solutions. Transform abstract connections into actionable mechanisms. |
| symbolic-compression | Compress problem contradiction into 2-3 word oxymoron. Produces oxymorons with interpretation directions for each. |

<!-- END available-tables (generated) -->
