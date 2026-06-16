---
name: green-hat-session
description: Structured creative thinking in Six Hats Green Hat mode — pure creative
  output with judgment suspended.
execution: subagent
prompt: ./prompt.md
input: problem (string)
dependencies:
  sops:
  - spawn-agent
---

# Green Hat Session

Structured creative thinking in Six Hats Green Hat mode.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Green Hat requires complete suspension of judgment (Black Hat) and pure creative generation. Benefits from dedicated context that can maintain the creative-only mindset without contamination from evaluation.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
