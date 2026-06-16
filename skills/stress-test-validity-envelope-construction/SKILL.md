---
name: stress-test-validity-envelope-construction
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

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
