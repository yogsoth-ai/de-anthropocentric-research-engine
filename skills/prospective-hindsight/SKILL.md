---
name: prospective-hindsight
description: "Strategy: Klein pre-mortem — assume the artifact has failed, then retrospect plausible causes. Generates rapid failure scenario catalog."
type: strategy
used-by: [failure-anticipation]
tactics: [premortem-to-fmea-pipeline, failure-chain-tracing]
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
