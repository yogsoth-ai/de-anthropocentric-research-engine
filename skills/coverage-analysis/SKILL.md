---
name: coverage-analysis
description: Systematic coverage evaluation pipeline — benchmark inventory, method-problem
  crossing, and intersection evaluation to map explored vs unexplored solution space.
execution: tactic
dependencies:
  sops:
  - creative-ideation-benchmark-inventory
  - intersection-evaluation
  - method-problem-crossing
---

# Coverage Analysis

Systematic coverage evaluation: inventory all known methods, cross them against problems, and evaluate which intersections remain unexplored.

## Stages

### Stage 1: Benchmark Inventory

Run benchmark-inventory SOP to catalog all known solutions/methods in the target domain. Output: structured method inventory with performance, applicability, and limitations.

### Stage 2: Method-Problem Crossing

Run method-problem-crossing SOP to build a cross-reference matrix of methods × problems. Output: complete matrix with all cells populated.

### Stage 3: Intersection Evaluation

Run intersection-evaluation SOP to annotate each matrix cell as explored, partial, or unexplored. Output: annotated matrix with exploration status and priority ranking.

## Minimum Yield

| Metric | Floor |
|--------|-------|
| Methods cataloged | ≥80% of known methods in domain |
| Problems enumerated | ≥80% of known problems in domain |
| Matrix cells evaluated | 100% of M×P cells |
| Unexplored intersections identified | ≥5 |
| Priority ranking produced | yes |

## Available SOPs

| SOP | Role |
|-----|------|
| benchmark-inventory | Stage 1 — catalog all known solutions |
| method-problem-crossing | Stage 2 — build cross-reference matrix |
| intersection-evaluation | Stage 3 — annotate exploration status |

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| creative-ideation-benchmark-inventory | Catalog all known solutions/methods in a domain with performance, applicability, and limitations. |
| intersection-evaluation | Evaluate exploration status of each cell in a method×problem matrix, annotating as explored, partial, or unexplored. |
| method-problem-crossing | Build method×problem cross-reference matrix showing which methods have been applied to which problems. |

<!-- END available-tables (generated) -->
