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

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
