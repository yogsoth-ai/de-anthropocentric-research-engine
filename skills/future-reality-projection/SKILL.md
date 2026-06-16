---
name: future-reality-projection
description: Project solution effects using Future Reality Tree logic
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
input: proposed injection/solution, current reality context, desired effects
output: Future Reality Tree with positive effects, negative branches, and prerequisites
dependencies:
  sops:
  - spawn-agent
---

# SOP: Future Reality Projection

Predict the effects of a proposed solution using Goldratt's Future Reality Tree. Verify that the injection resolves the original problem without creating unacceptable new problems.

Subagent — spawned via subagent-spawning/spawn-agent skill.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
