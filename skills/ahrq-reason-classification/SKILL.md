---
name: ahrq-reason-classification
description: Classify gap root causes using AHRQ 4-reason framework (insufficient
  info, biased info, inconsistent info, not yet integrated).
execution: subagent
prompt: ./prompt.md
input: gap_description (string), surrounding_evidence (string)
dependencies:
  sops:
  - spawn-agent
---

# AHRQ Reason Classification

Classify why a research gap exists using the AHRQ framework.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one AHRQ reason classification pass.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
