---
name: assumption-constraint
description: Which assumptions are most fragile? — Vulnerability ranking + impact
  assessment of experiment assumptions
version: 1.0.0
category: experiment-execution
type: strategy
sops:
- assumption-challenging
- resource-quantification
tactics:
- sensitivity-ranking
dependencies:
  sops:
  - assumption-challenging
  - resource-quantification
  tactics:
  - sensitivity-ranking
---

# Strategy: Assumption Constraint

## Methodology

Systematic assumption vulnerability analysis:
- **Extraction**: Surface all implicit and explicit assumptions
- **Scoring**: Quantify vulnerability (confidence × evidence / testability)
- **Impact assessment**: Blast radius × recovery cost
- **Prioritization**: Vulnerability × Impact = Priority
- **Validation planning**: Cheapest test that resolves uncertainty

Assumption categories:
| Category | Examples |
|----------|----------|
| Technical | Method convergence, architecture suitability |
| Data | Availability, quality, representativeness |
| Resource | Sufficiency of compute, time, expertise |
| Environmental | Tool stability, API access, policy |
| Theoretical | Effect existence, measurability, magnitude |

## Execution Flow

1. **Challenge Assumptions** → call `assumption-challenging` SOP
   - Input: experiment plan, hypothesis
   - Output: assumption inventory with validity assessment

2. **Quantify Validation Cost** → call `resource-quantification` SOP
   - Input: validation experiments for top assumptions
   - Output: cost to validate each assumption

3. **Rank Sensitivity** → invoke `sensitivity-ranking` tactic
   - Determine which assumptions are most binding

4. **Report** → synthesize vulnerability assessment
   - Top-5 fragile assumptions with validation paths
   - Binding assumption constraint identification

## Budget Gate

| Resource | Budget | Notes |
|----------|--------|-------|
| Subagent calls | ≤5 | 2 SOPs + synthesis |
| Iterations | ≤2 | Re-rank if new assumptions surface |
| Output size | ≤3000 tokens | Ranked table + validation plan |

<!-- BEGIN available-tables (generated) -->

## Available Tactics

可选,无固定顺序;最终叶子终为 sop。

| Tactic | 何时用 |
| --- | --- |
| sensitivity-ranking | Rank constraints by sensitivity — which ones most impact the outcome if they shift |

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| assumption-challenging | Challenge each assumption's validity — shared cross-repo SOP |
| resource-quantification | Quantify resource demand vs supply vs gap for each resource category |

<!-- END available-tables (generated) -->
