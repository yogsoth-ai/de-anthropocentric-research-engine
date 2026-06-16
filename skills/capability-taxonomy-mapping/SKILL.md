---
name: capability-taxonomy-mapping
description: Build capability taxonomy, map existing benchmark coverage
execution: subagent
prompt: ./prompt.md
input: domain, existing_benchmarks
dependencies:
  sops:
  - spawn-agent
---

# Capability Taxonomy Mapping SOP

Build a hierarchical capability taxonomy for a domain and map existing benchmark coverage onto it to identify gaps and redundancies.

## Input

- **domain**: The capability domain to taxonomize (e.g., "language understanding", "visual reasoning")
- **existing_benchmarks**: List of known benchmarks in the domain with brief descriptions

## Procedure

1. Construct hierarchical capability taxonomy from literature
2. Map each benchmark to taxonomy nodes it covers
3. Compute coverage density per node
4. Identify white spaces (uncovered capabilities)
5. Identify redundancy clusters (over-covered capabilities)

## Output

Annotated taxonomy tree with coverage statistics and prioritized gaps.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
