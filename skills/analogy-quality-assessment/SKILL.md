---
name: analogy-quality-assessment
description: Assess analogy depth (surface/structural/systemic). Determines whether an analogy warrants transfer investment.
execution: subagent
prompt: ./prompt.md
input: analogy_mapping (string)
used-by: cross-domain-discovery, bridge-validation, analogical-transfer, design-by-analogy, domain-divergence
---

# Analogy Quality Assessment

Assess analogy depth (surface/structural/systemic).

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Quality assessment requires rigorous, unbiased evaluation of analogy depth. Benefits from a dedicated evaluator role that is not invested in the analogy's success and can apply strict classification criteria without creative bias.
