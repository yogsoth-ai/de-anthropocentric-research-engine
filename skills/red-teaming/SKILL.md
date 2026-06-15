---
name: red-teaming
description: 'Campaign: Systematic adversarial attack from military/intelligence/AI-safety
  traditions. Core question: Can systematic adversarial attacks find fatal flaws?
  Methods: UFMCS Red Team Handbook v9.0, CIA SAT, Anthropic Red Teaming, NIST AI RMF,
  Inie et al. 12-strategy taxonomy.'
type: campaign
produces: RedTeamReport
artifact-types:
- gap
- hypothesis
- research-question
- idea
- approach
- experiment-design
- claim
dependencies:
  strategies:
  - adversarial-persona
  - alternative-analysis
  - groupthink-mitigation
  - stress-test-assumption-challenge
  - systematic-probing
  tactics:
  - adversarial-roleplay
  - assumption-cascade
  - structured-attack-campaign
  sops:
  - context-checkpoint
  - context-init
  - mitigation-proposal
  - stress-test-saturation-detection
  - verdict-synthesis
  - weakness-classification
---

# Red Teaming Campaign

Core question: **Can systematic adversarial attacks find fatal flaws in this artifact?**

## Methodology Sources

- UFMCS Red Team Handbook v9.0 — Military structured analytic techniques
- CIA Structured Analytic Techniques (SAT) — Key Assumptions Check, Devil's Advocacy
- Anthropic Red Teaming (2022) — AI-safety systematic probing methodology
- NIST AI Risk Management Framework — Threat surface enumeration
- Inie et al. (2024) — 12-strategy taxonomy of adversarial attacks

## Strategy Routing

| Artifact Type | Primary Strategy | Fallback Strategy |
|---|---|---|
| hypothesis, claim | assumption-challenge | adversarial-persona |
| research-question | alternative-analysis | groupthink-mitigation |
| idea, approach | systematic-probing | assumption-challenge |
| experiment-design | systematic-probing | alternative-analysis |
| gap | adversarial-persona | groupthink-mitigation |

## Budget Table

| Parameter | S (Quick) | M (Standard) | L (Deep) |
|---|---|---|---|
| Attack vectors | 5 | 12 | 20 |
| Probing rounds | 3 | 6 | 10 |
| Personas | 2 | 4 | 6 |
| Assumption checks | 5 | 10 | 20 |

## Tactics

- **structured-attack-campaign** — Threat surface enumeration, vector generation, systematic probing, aggregation
- **assumption-cascade** — Surface assumptions, dependency sort, root attack, cascade trace
- **adversarial-roleplay** — Construct hostile persona, attack from persona perspective, record paths

## Context Management

Each subagent operates in isolated adversarial context. Persona contamination is prevented by spawning separate agents per attack role. Findings are aggregated only after all probing rounds complete. Attack vectors are deduplicated before scoring.

## Output

Produces `RedTeamReport` containing: threat surface map, attack results by vector, assumption cascade analysis, resilience score (0.0-1.0), critical vulnerabilities, and recommended hardening actions.
