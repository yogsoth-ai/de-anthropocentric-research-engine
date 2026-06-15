---
name: adversarial-persona
description: 'Strategy: Role-play attacks from hostile personas — competing lab researcher,
  hostile reviewer, funding skeptic, domain outsider — each with distinct attack motivations
  and blind spots.'
type: strategy
tactics:
- adversarial-roleplay
- structured-attack-campaign
dependencies:
  tactics:
  - adversarial-roleplay
  - structured-attack-campaign
  sops:
  - attack-resilience-scoring
  - attack-vector-generation
  - finding-aggregation
  - persona-construction
  - probe-execution
---

# Adversarial Persona Strategy

Construct and deploy hostile personas that attack from distinct motivational frames. Each persona has unique expertise, biases, and attack patterns.

## Method

1. **persona-construction** builds detailed adversary profiles (background, motivation, expertise, blind spots)
2. Each persona attacks from their specific frame:
   - Hostile Reviewer: methodological rigor, statistical validity, novelty claims
   - Competing Lab: priority disputes, alternative approaches, resource efficiency
   - Funding Skeptic: impact claims, feasibility, timeline realism
   - Domain Outsider: jargon opacity, unstated assumptions, accessibility
3. **probe-execution** executes persona-specific attacks
4. Cross-persona findings compared to identify convergent vulnerabilities
5. **finding-aggregation** synthesizes across all persona perspectives

## Budget Table

| Parameter | S | M | L |
|---|---|---|---|
| Attack vectors | 5 | 12 | 20 |
| Probing rounds | 3 | 6 | 10 |
| Personas | 2 | 4 | 6 |
| Assumption checks | 5 | 10 | 20 |

## Orchestration

```
persona-construction → [build N personas per budget]
→ [for each persona]:
    attack-vector-generation (persona-specific vectors)
    → probe-execution (execute persona attacks)
→ finding-aggregation (cross-persona synthesis)
→ attack-resilience-scoring
```

## Subagents

- persona-construction (adversary profile building)
- attack-vector-generation (persona-specific attack design)
- probe-execution (persona attack execution)
- finding-aggregation (cross-persona synthesis)
- attack-resilience-scoring (convergent vulnerability scoring)

<!-- BEGIN available-tables (generated) -->

## Available Tactics

可选,无固定顺序;最终叶子终为 sop。

| Tactic | 何时用 |
| --- | --- |
| adversarial-roleplay | Tactic: Construct detailed hostile persona, attack artifact from that persona's perspective, record successful attack paths for aggregation. |
| structured-attack-campaign | Tactic: Full attack lifecycle — threat surface enumeration, attack vector generation, systematic probing, and finding aggregation across all surfaces. |

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| attack-resilience-scoring | Compute overall resilience score (0.0-1.0) based on attack results, coverage, and vulnerability severity distribution. |
| attack-vector-generation | Generate specific attack strategies for a given threat surface, producing concrete probes that can be executed. |
| finding-aggregation | Aggregate, deduplicate, and classify findings from multiple probes into a coherent vulnerability report. |
| persona-construction | Build a detailed adversarial persona with background, motivation, expertise, blind spots, and preferred attack patterns. |
| probe-execution | Execute a single attack probe against an artifact, record the result with evidence and severity classification. |

<!-- END available-tables (generated) -->
