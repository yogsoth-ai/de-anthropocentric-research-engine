---
name: benchmark-inventory
description: Identify and catalog all relevant benchmarks in target domain
execution: subagent
prompt: ./prompt.md
input: research_domain, capability_focus
used-by: benchmark-archaeology
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
