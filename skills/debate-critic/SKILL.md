---
name: debate-critic
description: Generates structured criticism from attack stance using Toulmin model.
  Produces claims, grounds, warrants, and rebuttals targeting artifact weaknesses.
execution: subagent
prompt: ./prompt.md
input: artifact (string), escalation_level (string), attack_vectors (string)
dependencies:
  sops:
  - spawn-agent
---

# Debate Critic

Generates structured adversarial criticism targeting artifact weaknesses.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Why Subagent

Attack generation requires dedicated adversarial stance without contamination from defensive reasoning. Isolated context ensures pure opposition.

## Input

- **artifact**: The artifact being debated (full text)
- **escalation_level**: Current level (L1-surface, L2-structural, L3-foundational)
- **attack_vectors**: Specific angles to attack (from debate-architect)

## Output

- **attacks**: List of structured attacks (claim + ground + warrant + rebuttal anticipation)
- **confidence**: How confident the critic is in each attack (0.0–1.0)
- **escalation_suggestion**: Whether to escalate, maintain, or de-escalate

## Budget

One unit = one set of attacks for one round.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
