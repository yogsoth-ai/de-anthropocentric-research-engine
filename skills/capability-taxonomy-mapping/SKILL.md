---
name: capability-taxonomy-mapping
description: Build capability taxonomy, map existing benchmark coverage
execution: subagent
prompt: ./prompt.md
input: domain, existing_benchmarks
used-by: benchmark-archaeology
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
