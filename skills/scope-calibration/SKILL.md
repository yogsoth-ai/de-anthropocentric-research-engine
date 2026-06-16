---
name: scope-calibration
description: 'Strategy: Adjust research question scope — zoom in/out until the scope is appropriate'
version: 1.0.0
category: hypothesis-formation
type: strategy
campaign: research-question
tactics:
- question-refinement-loop
sops:
- scope-assessment
- finer-criteria-check
- success-criteria-definition
dependencies:
  tactics:
  - question-refinement-loop
---

# Scope Calibration

Adjust research question scope — when a question is too broad or too narrow, find the right granularity through systematic zoom in/out.

## When to Use

- The initial RQ is too broad (cannot be answered within a reasonable time)
- The initial RQ is too narrow (the answer is trivial or lacks significance)
- A balance between ambition and feasibility is needed

## Thinking Framework

Core logic: a good research question has "Goldilocks" characteristics — not too broad, not too narrow, just right.

### Zoom In (when the question is too broad)

Add constraints to narrow the scope:
- Time constraint: "within the past 5 years..."
- Place constraint: "among Chinese universities..."
- Population constraint: "for beginners..."
- Method constraint: "using a transformer architecture..."
- Phenomenon constraint: "especially under scenario X..."

### Zoom Out (when the question is too narrow)

Relax constraints to widen the scope:
- Raise the level of abstraction: from concrete instance to general principle
- Remove unnecessary qualifiers
- Extend the scope of applicability

### Judgment Criteria

- Too broad: requires a book to answer / cannot be answered by a single experiment
- Appropriate: answerable by one paper / a clear study design can be specified
- Too narrow: answer is self-evident / lacks theoretical contribution

## Budget Gate

| Tier | Iteration rounds | Output |
|------|---------|------|
| S | ≥1 round of scope adjustment | Appropriately scoped RQ |
| M | ≥2 rounds of scope adjustment + comparison | Before/after comparison + final RQ |
| L | ≥3 rounds + multi-direction exploration | Multiple granularity versions + rationale for the optimal choice |

## Default Reference Flow

1. Run scope-assessment on the current RQ
2. Choose the zoom direction based on the verdict (too broad / too narrow)
3. Apply constraint adjustments
4. Re-assess scope
5. Iterate until "appropriate"
6. Confirm with the FINER check

## context-checkpoint

After the strategy completes, context-checkpoint must be called, recording:
- The original RQ and its scope verdict
- The adjustment direction and concrete operations
- The final RQ and its scope verdict
- The adjustment rationale

<!-- BEGIN available-tables (generated) -->

## Available Tactics

可选,无固定顺序;最终叶子终为 sop。

| Tactic | 何时用 |
| --- | --- |
| question-refinement-loop | Tactic: 迭代精化研究问题直到通过 FINER 5 项标准 |

<!-- END available-tables (generated) -->
