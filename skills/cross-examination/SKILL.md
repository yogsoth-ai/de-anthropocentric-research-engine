---
name: cross-examination
description: Probes defender responses for inconsistencies, logical gaps, and unsupported
  claims. Acts as follow-up interrogation after initial defense.
execution: subagent
prompt: ./prompt.md
input: defenses (string), attacks (string), artifact (string)
dependencies:
  sops:
  - spawn-agent
---

# Cross-Examination

Probes defender responses for inconsistencies and logical gaps.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Why Subagent

Cross-examination requires fresh analytical perspective on the defense — isolated context prevents anchoring to either attack or defense framing.

## Input

- **defenses**: Structured defenses from debate-defender
- **attacks**: Original attacks that prompted the defenses
- **artifact**: The artifact being debated (for reference)

## Output

- **probes**: List of follow-up questions targeting defense weaknesses
- **inconsistencies**: Contradictions found within or between defenses
- **unsupported_claims**: Defense claims lacking evidence
- **verdict_suggestion**: Whether defense held up under examination

## Budget

One unit = one cross-examination pass per round.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
