---
name: premortem-to-fmea-pipeline
description: 'Tactic: Pre-mortem rapid screening feeds high-risk items into full FMEA
  analysis. Bridges fast intuitive generation with systematic structured analysis.'
type: tactic
strategies:
- prospective-hindsight
- risk-prioritization
dependencies:
  sops:
  - action-priority-matrix
  - detection-scoring
  - failure-chain-construction
  - failure-mode-extraction
  - function-analysis
  - occurrence-scoring
  - premortem-facilitation
  - severity-scoring
---

# Pre-Mortem to FMEA Pipeline Tactic

Rapid pre-mortem screening identifies candidate failures; high-severity items trigger full FMEA deep-dive.

## Orchestration

1. **premortem-facilitation** generates failure scenarios (fast, intuitive)
2. **failure-mode-extraction** structures scenarios into failure mode list
3. **severity-scoring** performs rapid severity screen (1-10)
4. Items scoring >= threshold pass to FMEA pipeline:
   - **function-analysis** → **failure-chain-construction**
   - **occurrence-scoring** + **detection-scoring**
   - **action-priority-matrix** classifies H/M/L
5. Low-severity items documented but not analyzed further

## Threshold Logic

- Budget S: threshold = 7 (only critical items get FMEA)
- Budget M: threshold = 5 (moderate and above)
- Budget L: threshold = 3 (comprehensive coverage)

## Subagents Dispatched

- premortem-facilitation (scenario generation)
- failure-mode-extraction (structuring)
- severity-scoring (screening gate)
- function-analysis, failure-chain-construction (FMEA deep-dive)
- occurrence-scoring, detection-scoring (full scoring)
- action-priority-matrix (classification)

## Termination Conditions

- All generated scenarios have been screened
- High-severity items have completed full FMEA cycle
- Action priority assigned to all items above threshold

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| action-priority-matrix | Compute Risk Priority Number (RPN = S x O x D), classify failure modes into H/M/L action priority per AIAG-VDA tables. |
| detection-scoring | Rate detectability 1-10 (inverted: 10 = hardest to detect). Estimates how likely current controls would catch the failure before impact. |
| failure-chain-construction | Build cause-mode-effect chains tracing upstream root causes and downstream cascading effects for each failure mode. |
| failure-mode-extraction | Extract structured failure mode list from raw scenarios or artifact analysis. Produces standardized failure mode records. |
| function-analysis | FMEA Step 3: Decompose artifact into function tree — identify what each component is supposed to do before analyzing how it can fail. |
| occurrence-scoring | Rate failure mode occurrence probability 1-10. Estimates how likely each failure mode is to manifest during research execution. |
| premortem-facilitation | Execute Klein pre-mortem protocol — assume failure has occurred, generate plausible failure scenarios through prospective hindsight. |
| severity-scoring | Rate failure mode severity 1-10 based on end-effect impact. Follows AIAG-VDA severity scale calibrated for research artifacts. |

<!-- END available-tables (generated) -->
