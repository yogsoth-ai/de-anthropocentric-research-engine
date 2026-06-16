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

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
