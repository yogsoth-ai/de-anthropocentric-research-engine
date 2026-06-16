---
name: sub-question-decomposition
description: 'Tactic: Decompose a main question into a hierarchy of independently
  answerable sub-questions'
version: 1.0.0
category: hypothesis-formation
type: tactic
campaign: research-question
sops:
- sub-question-generation
- dependency-mapping
- answering-sequence-design
dependencies:
  sops:
  - answering-sequence-design
  - dependency-mapping
  - sub-question-generation
---

# Sub-Question Decomposition

Decompose a main question into a hierarchy of independently answerable sub-questions — when the question is too complex to answer in one pass.

## Orchestration Intent

Structure "decomposing a complex question" as: generate sub-questions → map dependencies → design answering order. The three steps run sequentially, each step's output being the next step's input.

## Available SOPs

| SOP | Responsibility | When to call |
|-----|------|---------|
| sub-question-generation | Decompose the main question into sub-questions | First step, mandatory |
| dependency-mapping | Map dependency relationships among sub-questions | After sub-questions are generated |
| answering-sequence-design | Design the optimal answering order | After the dependency graph is complete |

## Orchestration Pattern

**Serial mode (the only mode)**:
1. sub-question-generation → sub-question list + independence argument
2. dependency-mapping → dependency graph + critical path
3. answering-sequence-design → execution sequence + parallelization opportunities

Each step strictly depends on the previous step's output; no parallelization.

## Minimum Yield

- ≥3 sub-questions (M tier)
- Each sub-question has an independence argument
- Dependency graph (no circular dependencies)
- Suggested answering sequence + parallelization opportunity identification

## Yield Report

After execution, report:
- Number of sub-questions generated
- Number of dependency relationships
- Critical path length
- Groups of sub-questions that can be answered in parallel

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| answering-sequence-design | SOP: Design the optimal answering order for sub-questions |
| dependency-mapping | SOP: map dependency relationships among sub-questions |
| sub-question-generation | SOP: Decompose a main research question into independently answerable sub-questions |

<!-- END available-tables (generated) -->
