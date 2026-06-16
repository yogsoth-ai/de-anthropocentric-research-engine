---
name: prospective-hindsight
description: 'Strategy: Klein pre-mortem — assume the artifact has failed, then retrospect
  plausible causes. Generates rapid failure scenario catalog.'
type: strategy
tactics:
- premortem-to-fmea-pipeline
- failure-chain-tracing
dependencies:
  tactics:
  - failure-chain-tracing
  - premortem-to-fmea-pipeline
  sops:
  - failure-mode-extraction
  - premortem-facilitation
  - severity-scoring
---

# Prospective Hindsight Strategy

Assume the artifact has already failed. Retrospect: what went wrong?

## Method

1. **premortem-facilitation** frames the failure assumption
2. Each participant generates independent failure scenarios
3. **failure-mode-extraction** structures raw scenarios into failure mode list
4. Scenarios are ranked by plausibility and severity
5. High-risk items feed into FMEA pipeline (premortem-to-fmea-pipeline tactic)

## Budget Table

| Parameter | S | M | L |
|---|---|---|---|
| Failure scenarios generated | 8 | 20 | 40 |
| Independent perspectives | 2 | 4 | 6 |
| Screening threshold (severity) | 7 | 5 | 3 |

## Orchestration

```
premortem-facilitation → failure-mode-extraction
  → severity-scoring (rapid screen)
  → [high-severity items] → premortem-to-fmea-pipeline
```

## Subagents

- premortem-facilitation (execute Klein protocol)
- failure-mode-extraction (structure scenarios)
- severity-scoring (rapid severity screen)

<!-- BEGIN available-tables (generated) -->

## Available Tactics

Optional, no fixed order; the final leaf is always a sop.

| Tactic | When to use |
| --- | --- |
| failure-chain-tracing | Tactic: Trace upstream causes and downstream effects of each failure mode. Builds multi-level cause-mode-effect chains for systemic understanding. |
| premortem-to-fmea-pipeline | Tactic: Pre-mortem rapid screening feeds high-risk items into full FMEA analysis. Bridges fast intuitive generation with systematic structured analysis. |

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| failure-mode-extraction | Extract structured failure mode list from raw scenarios or artifact analysis. Produces standardized failure mode records. |
| premortem-facilitation | Execute Klein pre-mortem protocol — assume failure has occurred, generate plausible failure scenarios through prospective hindsight. |
| severity-scoring | Rate failure mode severity 1-10 based on end-effect impact. Follows AIAG-VDA severity scale calibrated for research artifacts. |

<!-- END available-tables (generated) -->
