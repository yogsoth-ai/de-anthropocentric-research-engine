---
name: validity-envelope-construction
description: Synthesize breakpoints across dimensions into a coherent validity envelope
  for a claim.
execution: subagent
prompt: ./prompt.md
dependencies:
  sops:
  - spawn-agent
---

# Validity Envelope Construction

Subagent that takes breakpoint data from multiple dimensions and constructs a multi-dimensional validity envelope.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
