---
name: gap-keyword-extraction
description: Extract gap-indicating sentences and phrases from papers/reviews. Identifies
  linguistic markers of research gaps (e.g., "remains unclear", "has not been explored",
  "limited understanding").
execution: subagent
prompt: ./prompt.md
input: paper_text (string), extraction_scope (string)
dependencies:
  sops:
  - spawn-agent
---

# Gap Keyword Extraction

Extract gap-indicating sentences and phrases from academic text.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one extraction pass over a paper or review text.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
