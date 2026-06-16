---
name: evidence-synthesis
description: Synthesize multi-source evidence into structured argumentation. Weaves
  findings from literature, web, and analysis into coherent evidence maps with explicit
  strength ratings.
execution: subagent
prompt: ./prompt.md
input: evidence_sources (string), synthesis_goal (string), quality_requirements (string)
dependencies:
  sops:
  - spawn-agent
---

# Evidence Synthesis

Weave multi-source evidence into structured argumentation.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Why Subagent

Synthesis requires processing large accumulated evidence corpus in dedicated context.

## Budget

Quantity target is set by the calling strategy's budget table. This SOP executes one unit = one evidence synthesis pass producing a structured evidence map.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
