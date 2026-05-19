---
name: experiment-design
description: "Transform validated hypotheses into rigorous, executable experiment designs"
version: 1.0.0
category: experiment-execution
type: campaign
strategies:
  - factor-level-design
  - ablation-design
  - comparison-design
  - scaling-design
  - robustness-design
tactics:
  - statistical-method-selection
  - reproducibility-protocol
  - budget-constrained-design
---

# Campaign: Experiment Design

**Positioning**: What experiment to run — transform a validated hypothesis into a rigorous experiment design that maximizes information yield per compute dollar.

## HARD-GATE

Before entering this campaign, the following must be satisfied:

| Gate | Requirement |
|------|-------------|
| Hypothesis | A falsifiable hypothesis with clearly stated IV/DV exists |
| Scope | Research question is bounded (not open-ended exploration) |
| Resources | Preliminary compute/time budget is stated |
| Prior Work | Relevant baselines and datasets have been identified |

If any gate fails, route back to hypothesis-generation or research-question refinement.

## Campaign Goal

Produce a complete experiment design document that specifies:
1. What factors to vary and at what levels
2. What to measure and how to determine significance
3. What baselines to compare against
4. How to ensure reproducibility
5. An executable configuration ready for implementation

## Strategy Selection

| Signal in Hypothesis | Strategy | When to Use |
|---------------------|----------|-------------|
| "Factor X affects Y" | factor-level-design | Testing effects of specific variables |
| "Component C contributes to performance" | ablation-design | Understanding component contributions |
| "Method M outperforms baseline B" | comparison-design | Claiming superiority over existing work |
| "Performance scales with resource R" | scaling-design | Understanding scaling behavior |
| "Method works under condition C" | robustness-design | Testing failure boundaries |

Multiple strategies may be composed for complex hypotheses.

## Budget Gate

| Tier | GPU-hours | Max Factors | Max Runs | Strategy Constraint |
|------|-----------|-------------|----------|-------------------|
| Micro | < 10 | 3 | 20 | Fractional factorial or single ablation |
| Small | 10-100 | 5 | 50 | Full factorial on key factors |
| Medium | 100-1000 | 8 | 200 | Multi-strategy composition |
| Large | > 1000 | Unlimited | Unlimited | Full design space exploration |

## Context Management

- Each SOP runs as a subagent to preserve main-thread context
- Strategy orchestrators pass structured JSON between SOPs
- Final design-synthesis SOP compiles all outputs into a single document
- Intermediate artifacts are stored as structured data, not prose

## Minimum Yield

Every campaign invocation must produce at minimum:
- A design matrix (even if single-factor)
- Metric specification with significance threshold
- Seed protocol
- Estimated total compute cost
