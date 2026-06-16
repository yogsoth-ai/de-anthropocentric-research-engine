---
name: deep-insight-provocation-generation
description: Generate de Bono lateral thinking provocations to challenge dominant
  ideas using escape, reversal, exaggeration, and distortion.
execution: subagent
prompt: ./prompt.md
input: dominant_idea
dependencies:
  sops:
  - spawn-agent
---

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one complete provocation set (4+ provocations) for one dominant idea.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
