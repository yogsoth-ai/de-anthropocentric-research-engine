---
name: finding-aggregation
description: Aggregate, deduplicate, and classify findings from multiple probes into
  a coherent vulnerability report.
execution: subagent
prompt: ./prompt.md
input: findings (string), attack_metadata (string)
dependencies:
  sops:
  - spawn-agent
---

# Finding Aggregation

Synthesizes findings from multiple attack probes into a coherent, deduplicated report.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Why Subagent

Aggregation requires neutral analytical stance — neither inflating nor minimizing findings. The aggregator must see patterns across individual probe results.

## Input

- **findings**: All probe results from the campaign
- **attack_metadata**: Metadata about attack coverage (surfaces hit, vectors used, personas deployed)

## Output

- **vulnerabilities**: Deduplicated list classified by severity and type
- **patterns**: Cross-cutting patterns observed across multiple probes
- **coverage_gaps**: Surfaces or dimensions not adequately tested
- **recommendations**: Prioritized hardening actions

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
