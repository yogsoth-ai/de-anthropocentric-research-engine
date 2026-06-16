---
name: symbolic-compression
description: Compress problem contradiction into 2-3 word oxymoron. Produces oxymorons
  with interpretation directions for each.
execution: subagent
prompt: ./prompt.md
input: problem_contradiction (string)
dependencies:
  sops:
  - spawn-agent
---

# Symbolic Compression

Compress problem contradiction into 2-3 word oxymoron.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Symbolic compression requires poetic/linguistic sensitivity and the ability to hold contradictions in tension without resolving them prematurely. Benefits from focused creative-linguistic processing.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
