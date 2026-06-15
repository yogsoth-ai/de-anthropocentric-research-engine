---
name: systematic-probing
description: 'Strategy: AI-safety systematic probing — enumerate all threat surfaces,
  generate attack vectors per surface, execute probes, and aggregate findings across
  the full attack space.'
type: strategy
tactics:
- structured-attack-campaign
- assumption-cascade
dependencies:
  tactics:
  - assumption-cascade
  - structured-attack-campaign
  sops:
  - attack-resilience-scoring
  - attack-vector-generation
  - finding-aggregation
  - probe-execution
  - threat-surface-mapping
---

# Systematic Probing Strategy

Anthropic-style systematic probing: exhaustive coverage of all threat surfaces with structured attack generation and execution.

## Method

1. **threat-surface-mapping** enumerates all attackable surfaces of the artifact
2. **attack-vector-generation** produces specific attacks per surface
3. Vectors prioritized by expected severity and likelihood
4. **probe-execution** executes each attack, records success/failure/partial
5. Failed probes trigger deeper investigation via follow-up vectors
6. **attack-resilience-scoring** computes coverage and resilience metrics

## Budget Table

| Parameter | S | M | L |
|---|---|---|---|
| Attack vectors | 5 | 12 | 20 |
| Probing rounds | 3 | 6 | 10 |
| Personas | 2 | 4 | 6 |
| Assumption checks | 5 | 10 | 20 |

## Orchestration

```
threat-surface-mapping → [enumerate surfaces]
→ [for each surface]:
    attack-vector-generation (generate vectors)
    → [for each vector]:
        probe-execution (execute attack)
        → (if partial success: generate follow-up vectors)
→ finding-aggregation → attack-resilience-scoring
```

## Subagents

- threat-surface-mapping (surface enumeration)
- attack-vector-generation (vector design)
- probe-execution (attack execution)
- finding-aggregation (result synthesis)
- attack-resilience-scoring (metric computation)

<!-- BEGIN available-tables (generated) -->

## Available Tactics

可选,无固定顺序;最终叶子终为 sop。

| Tactic | 何时用 |
| --- | --- |
| assumption-cascade | Tactic: Surface assumptions, sort by dependency, attack root assumptions first, then trace cascade failures through the dependency graph. |
| structured-attack-campaign | Tactic: Full attack lifecycle — threat surface enumeration, attack vector generation, systematic probing, and finding aggregation across all surfaces. |

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| attack-resilience-scoring | Compute overall resilience score (0.0-1.0) based on attack results, coverage, and vulnerability severity distribution. |
| attack-vector-generation | Generate specific attack strategies for a given threat surface, producing concrete probes that can be executed. |
| finding-aggregation | Aggregate, deduplicate, and classify findings from multiple probes into a coherent vulnerability report. |
| probe-execution | Execute a single attack probe against an artifact, record the result with evidence and severity classification. |
| threat-surface-mapping | Enumerate all attackable surfaces of an artifact — logical, empirical, methodological, social, and practical dimensions. |

<!-- END available-tables (generated) -->
