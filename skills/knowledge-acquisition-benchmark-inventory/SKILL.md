---
name: benchmark-inventory
description: Identify and catalog all relevant benchmarks in target domain
execution: subagent
prompt: ./prompt.md
input: research_domain, capability_focus
dependencies:
  sops:
  - spawn-agent
---

# Benchmark Inventory SOP

Identify, catalog, and characterize all relevant benchmarks for a given research domain and capability focus area.

## Input

- **research_domain**: The broad research area (e.g., "natural language understanding", "code generation", "multimodal reasoning")
- **capability_focus**: Specific capability of interest (e.g., "commonsense reasoning", "mathematical problem solving")

## Procedure

1. Search Papers With Code for benchmarks tagged with the domain
2. Search Semantic Scholar for benchmark papers in the domain
3. Search web for leaderboards and evaluation suites
4. For each benchmark found, collect: name, year, paper, size, primary metric, current SOTA, status
5. Classify by: capability tested, modality, difficulty level, maintenance status

## Output

Structured catalog of benchmarks with metadata sufficient for downstream analysis selection.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
