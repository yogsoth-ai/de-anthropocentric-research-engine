---
name: multiagent-debate
description: "Campaign: Multi-agent structured debate for adversarial validation. Core question: Can this artifact survive structured adversarial debate? Methods: Irving AI Safety via Debate, Du Society of Mind, Liang MAD, Toulmin Argumentation, D3 framework."
type: campaign
produces: DebateVerdict
artifact-types: [gap, hypothesis, research-question, idea, approach, experiment-design, claim]
---

# Multi-Agent Debate Campaign

Core question: **Can this artifact survive structured adversarial debate?**

## Methodology Sources

- Irving et al. (2018) — AI Safety via Debate
- Du et al. (2023) — Society of Mind multi-agent sharing
- Liang et al. (2023) — MAD (Multi-Agent Debate)
- Toulmin (1958) — Argumentation model (claim, ground, warrant, backing, qualifier, rebuttal)
- D3 framework — Deliberate, Debate, Decide

## Strategy Routing

| Artifact Type | Primary Strategy | Fallback Strategy |
|---|---|---|
| hypothesis, claim | critic-defender-judge | adversarial-escalation |
| research-question | multi-perspective-panel | society-of-mind |
| idea, approach | society-of-mind | courtroom-structured |
| experiment-design | courtroom-structured | critic-defender-judge |
| gap | multi-perspective-panel | adversarial-escalation |

## Budget Table

| Parameter | S (Quick) | M (Standard) | L (Deep) |
|---|---|---|---|
| Debate rounds | 4 | 8 | 12 |
| Participating agents | 3 | 5 | 8 |
| Coverage dimensions | 3 | 5 | 7 |
| External evidence searches | 2 | 5 | 10 |

## Tactics

- **dialectical-escalation** — Progressive pressure escalation based on confidence thresholds
- **perspective-rotation** — Sequential perspective evaluation with divergence aggregation
- **evidence-tournament** — Evidence gathering, cross-examination, and quality judgment

## Context Management

Each subagent operates in isolated context. The debate-architect designs structure before execution. Transcripts are passed between rounds via structured markdown. Saturation detection terminates when novelty drops below threshold.

## Output

Produces `DebateVerdict` containing: survival assessment, key vulnerabilities, confidence score, debate transcript summary, and recommended mitigations.
