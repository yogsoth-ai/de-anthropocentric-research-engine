---
name: premortem-to-fmea-pipeline
description: "Tactic: Pre-mortem rapid screening feeds high-risk items into full FMEA analysis. Bridges fast intuitive generation with systematic structured analysis."
type: tactic
used-by: [failure-anticipation]
strategies: [prospective-hindsight, risk-prioritization]
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
