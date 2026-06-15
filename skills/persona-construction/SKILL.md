---
name: persona-construction
description: Build a detailed adversarial persona with background, motivation, expertise,
  blind spots, and preferred attack patterns.
execution: subagent
prompt: ./prompt.md
input: persona_type (string), artifact_domain (string)
dependencies:
  sops:
  - spawn-agent
---

# Persona Construction

Builds detailed adversary personas for roleplay-based attacks.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Why Subagent

Persona construction requires creative character building without contamination from the artifact's perspective. The persona must feel authentic and internally consistent.

## Input

- **persona_type**: Category of adversary (hostile-reviewer, competing-lab, funding-skeptic, domain-outsider, or custom)
- **artifact_domain**: The domain of the artifact being attacked (for expertise calibration)

## Output

- **persona**: Complete adversary profile (name, background, motivation, expertise, blind spots)
- **attack_style**: How this persona typically attacks (preferred patterns)
- **trigger_phrases**: What aspects of artifacts particularly provoke this persona

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
