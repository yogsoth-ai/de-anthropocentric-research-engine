---
name: failure-chain-tracing
description: 'Tactic: Trace upstream causes and downstream effects of each failure
  mode. Builds multi-level cause-mode-effect chains for systemic understanding.'
type: tactic
strategies:
- prospective-hindsight
- design-fmea
- process-fmea
dependencies:
  sops:
  - failure-chain-construction
  - severity-scoring
---

# Failure Chain Tracing Tactic

Trace each failure mode both upstream (root causes) and downstream (cascading effects) to build complete causal chains.

## Orchestration

1. Start from identified failure mode
2. **failure-chain-construction** traces upstream:
   - Why could this mode occur? (immediate cause)
   - Why could that cause occur? (root cause)
   - Repeat to budget depth (2/4/6 levels)
3. **failure-chain-construction** traces downstream:
   - What effect does this mode produce? (local effect)
   - What does that effect cause? (system-level effect)
   - What is the end impact? (customer/stakeholder effect)
4. Chain validated for logical consistency
5. Shared causes across multiple modes flagged as systemic risks

## Depth Control

- Budget S: 2 levels (immediate cause → mode → local effect)
- Budget M: 4 levels (root cause → ... → system effect)
- Budget L: 6 levels (full chain with environmental factors)

## Subagents Dispatched

- failure-chain-construction (upstream and downstream tracing)
- severity-scoring (end-effect severity assessment)

## Termination Conditions

- Chain depth exhausted per budget
- Root cause reached (no further upstream cause identifiable)
- End effect reached (stakeholder-level impact identified)
- Circular dependency detected (flag and stop)

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| failure-chain-construction | Build cause-mode-effect chains tracing upstream root causes and downstream cascading effects for each failure mode. |
| severity-scoring | Rate failure mode severity 1-10 based on end-effect impact. Follows AIAG-VDA severity scale calibrated for research artifacts. |

<!-- END available-tables (generated) -->
