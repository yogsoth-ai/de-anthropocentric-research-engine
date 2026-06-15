---
name: patent-family-tracing
description: Forward/backward patent citation and priority tracing until saturation
execution: tactic
dependencies:
  sops:
  - citation-network-analysis
  - knowledge-acquisition-saturation-detection
  - legal-status-assessment
  - patent-query-formulation
---

# Patent Family Tracing

Traces patent citation networks and priority chains in both directions (forward citations, backward citations, priority links) until the search space saturates.

## Stages

### 1. Seed Identification
- Accept seed patents from calling strategy
- Validate patent numbers and retrieve basic metadata
- Establish initial frontier set

### 2. Priority Chain Tracing
- For each seed, trace priority/continuation chain to find all family members
- Identify provisional applications, continuations, divisionals, CIPs
- Record priority dates and filing jurisdictions

### 3. Citation Expansion (Forward)
- Find all patents that cite the seed/family patents
- Assess relevance of citing patents to the target technology
- Add relevant citations to the frontier

### 4. Citation Expansion (Backward)
- Find all patents cited by the seed/family patents
- Trace backward to foundational prior art
- Add relevant references to the frontier

### 5. Saturation Check
- Use `saturation-detection` SOP to determine if expansion has converged
- Convergence criteria: <5% new relevant patents per iteration
- If not saturated, return to Stage 3 with expanded frontier

## Available SOPs

| SOP | Role |
|-----|------|
| patent-query-formulation | Generate queries for citation lookup |
| citation-network-analysis | Analyze the citation graph structure |
| legal-status-assessment | Check status of discovered family members |
| saturation-detection | Determine when expansion has converged |

## Execution Guidance

- Run priority chain tracing first — this gives complete family coverage before citation expansion
- Forward citations are more likely to reveal recent developments
- Backward citations reveal foundational prior art
- Limit citation depth to 3 generations unless strategy requires more
- Deduplicate by patent family (same priority) not by individual publication

## Yield Report

Report to calling strategy after each execution:
- New patent families discovered this iteration
- Total frontier size
- Saturation percentage
- Depth reached (citation generations)

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| citation-network-analysis | Build and analyze patent citation networks — main path analysis, PageRank, cluster detection |
| knowledge-acquisition-saturation-detection | Determine when additional searching yields diminishing returns. Analyzes the latest expansion batch against existing corpus to judge continue/near-saturation/saturated. Used by snowball and systematic-survey. |
| legal-status-assessment | Determine patent legal status — active, expired, pending, lapsed, or revoked |
| patent-query-formulation | Construct keyword + IPC/CPC + assignee combination search strategies for patent databases |

<!-- END available-tables (generated) -->
