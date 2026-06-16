---
name: debate-defender
description: Responds to attacks with counter-evidence and counter-arguments. Defends
  artifact using evidence, clarification, and rebuttal while acknowledging valid criticisms.
execution: subagent
prompt: ./prompt.md
input: artifact (string), attacks (string), previous_defenses (string)
dependencies:
  sops:
  - spawn-agent
---

# Debate Defender

Responds to structured attacks with counter-evidence and rebuttals.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Why Subagent

Defense requires dedicated advocacy stance. Isolated context prevents premature concession from exposure to attack reasoning.

## Input

- **artifact**: The artifact being defended
- **attacks**: Structured attacks from debate-critic (current round)
- **previous_defenses**: Defenses from prior rounds (for consistency)

## Output

- **defenses**: List of responses (concede, rebut, or clarify per attack)
- **confidence**: Defender's confidence in artifact survival (0.0–1.0)
- **concessions**: Any points conceded as valid weaknesses

## Budget

One unit = one set of defenses for one round of attacks.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
