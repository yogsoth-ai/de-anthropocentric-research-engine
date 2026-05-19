---
name: ablation-design
description: "Design ablation studies to isolate component contributions in ML systems"
version: 1.0.0
category: experiment-execution
type: strategy
used-by: experiment-design
sops:
  - ablation-component-mapping
  - baseline-selection
  - metric-specification
  - sample-size-estimation
tactics:
  - statistical-method-selection
---

# Strategy: Ablation Design

**Question**: What does each component contribute?

## Methodology

- **Systematic Ablation** (Newell 1974): Remove one component at a time, measure degradation.
- **Replacement Ablation**: Replace component with simpler alternative to isolate contribution.
- **Combinatorial Ablation** (ABLATOR): Test component subsets to detect interaction effects.
- **Conditional Ablation**: Ablate components under specific data conditions to find context-dependent contributions.

## Execution Flow

1. **ablation-component-mapping** → Map system architecture to ablatable units
2. **baseline-selection** → Select full-system and minimal-system anchors
3. **metric-specification** → Define metrics that capture component contribution
4. **sample-size-estimation** → Determine runs needed for reliable delta estimation
5. **statistical-method-selection** (tactic) → Choose appropriate significance tests for deltas

## Budget Gate

| Ablation Type | Components (N) | Min Runs | When to Use |
|---------------|---------------|----------|-------------|
| Systematic (leave-one-out) | 3-8 | N + 2 | Standard component analysis |
| Replacement | 3-8 | 2N + 2 | Need to distinguish "removal" vs "simplification" |
| Combinatorial (selected) | 4-6 | ~2N | Suspected interactions between components |
| Combinatorial (full) | 3-4 | 2^N | Small systems, need complete picture |
| Conditional | 3-6 | N * conditions | Context-dependent contributions |
