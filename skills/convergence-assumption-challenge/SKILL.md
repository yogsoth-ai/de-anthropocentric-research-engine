---
name: assumption-challenge
description: Construct the strongest counter-argument against a specific assumption
  and propose alternatives.
execution: subagent
prompt: ./prompt.md
input: assumption
dependencies:
  sops:
  - spawn-agent
---

# Assumption Challenge

Attacks a specific assumption adversarially — constructing the strongest argument for why it might be wrong, proposing an alternative assumption, and assessing the impact on the overall decision if the assumption fails.

## Execution

Spawns a subagent that takes a single assumption and builds the strongest possible case against it.

## Why Subagent

- Challenge requires adversarial mindset isolated from the assumption-maker
- Each assumption deserves focused, dedicated attack
- Isolation prevents the challenger from being "too kind" to assumptions

## HARD-GATE

Output must include:
- Challenge argument with evidence or reasoning
- At least 1 alternative assumption (what if the opposite is true?)
- Impact assessment if the assumption is wrong
- Confidence in the challenge itself (is this a real threat or theoretical?)

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
