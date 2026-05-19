---
name: failure-anticipation
description: "Campaign: Forward-looking failure analysis combining pre-mortem rapid screening with systematic FMEA deep-dive. Core question: If this artifact fails, how will it fail? Methods: Klein Pre-Mortem 2007, AIAG-VDA FMEA 2019, IEC 60812."
type: campaign
produces: FailureAnticipationReport
artifact-types: [gap, hypothesis, research-question, idea, approach, experiment-design, claim]
---

# Failure Anticipation Campaign

Core question: **If this artifact fails, how will it fail?**

## Methodology Sources

- Klein (2007) — Pre-Mortem technique: assume failure, retrospect causes
- AIAG-VDA FMEA Handbook (2019) — 7-step FMEA with Action Priority
- IEC 60812 — Failure modes and effects analysis standard

## Strategy Routing

| Artifact Type | Primary Strategy | Fallback Strategy |
|---|---|---|
| hypothesis, claim | prospective-hindsight | design-fmea |
| research-question | design-fmea | process-fmea |
| idea, approach | design-fmea | prospective-hindsight |
| experiment-design | process-fmea | design-fmea |
| gap | risk-prioritization | prospective-hindsight |

## Budget Table

| Parameter | S (Quick) | M (Standard) | L (Deep) |
|---|---|---|---|
| Failure modes | 8 | 20 | 40 |
| Failure chain depth | 2 | 4 | 6 |
| Mitigation measures | 3 | 8 | 15 |
| Re-scoring rounds | 1 | 2 | 3 |

## Tactics

- **premortem-to-fmea-pipeline** — Pre-mortem screens, high-risk items trigger full FMEA
- **failure-chain-tracing** — Trace upstream causes and downstream effects
- **mitigation-validation** — Mini-FMEA on proposed mitigations to verify no new risks

## Context Management

Each subagent operates in isolated context. Pre-mortem facilitation runs first to generate rapid failure scenarios. High-severity items are passed to FMEA subagents for structured analysis. Severity/Occurrence/Detection scores flow through action-priority-matrix for classification. Mitigations are validated via re-scoring loop.

## Output

Produces `FailureAnticipationReport` containing: failure mode catalog, cause-effect chains, S/O/D scores, action priority classification (H/M/L), mitigation measures, and post-mitigation re-scores.
