---
name: survey-synthesis
description: Final synthesis step — weave all gathered evidence (reading notes, extracted
  data, categorizations) into a coherent structured output appropriate to the strategy
  type. Used by all 5 strategies as the final step.
execution: subagent
prompt: ./prompt.md
input: strategy_type (string), accumulated_notes (string), extracted_data (string)
dependencies:
  sops:
  - spawn-agent
---

# Survey Synthesis

Produce the final structured survey output from all accumulated evidence.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill. The subagent receives all accumulated materials and produces a single coherent document.

## Why Subagent

Synthesis requires processing the entire accumulated corpus (potentially 50+ papers worth of notes). Running in a subagent provides dedicated context for weaving a coherent narrative without polluting the main session.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
