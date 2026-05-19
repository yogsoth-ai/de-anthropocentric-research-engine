---
name: patent-family-tracing
description: Forward/backward patent citation and priority tracing until saturation
execution: tactic
used-by: patent-mining
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
