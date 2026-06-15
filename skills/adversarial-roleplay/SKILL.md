---
name: adversarial-roleplay
description: 'Tactic: Construct detailed hostile persona, attack artifact from that
  persona''s perspective, record successful attack paths for aggregation.'
type: tactic
strategies:
- adversarial-persona
- groupthink-mitigation
- alternative-analysis
dependencies:
  sops:
  - attack-vector-generation
  - finding-aggregation
  - persona-construction
  - probe-execution
---

# Adversarial Roleplay Tactic

Deploy constructed hostile personas to attack the artifact from distinct motivational frames.

## Orchestration

1. **persona-construction** builds detailed adversary profile:
   - Background and expertise domain
   - Motivation for attacking (career incentive, resource competition, ideological)
   - Known blind spots and biases of this persona type
   - Preferred attack patterns
2. **attack-vector-generation** generates vectors specific to persona's expertise and motivation
3. **probe-execution** executes attacks while maintaining persona consistency
4. Successful attack paths recorded with persona attribution
5. Process repeats for each persona (budget-limited)
6. **finding-aggregation** cross-references findings across personas for convergent vulnerabilities

## Subagents Dispatched

- persona-construction (1 call per persona)
- attack-vector-generation (1 call per persona)
- probe-execution (N calls per persona, budget-limited)
- finding-aggregation (1 call at end, cross-persona)

## Termination Conditions

- All budgeted personas deployed and exhausted
- Convergent vulnerability found by 2+ personas (high-confidence finding)
- Single persona finds critical vulnerability (early report)
- Budget exhausted (report per-persona findings separately)

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| attack-vector-generation | Generate specific attack strategies for a given threat surface, producing concrete probes that can be executed. |
| finding-aggregation | Aggregate, deduplicate, and classify findings from multiple probes into a coherent vulnerability report. |
| persona-construction | Build a detailed adversarial persona with background, motivation, expertise, blind spots, and preferred attack patterns. |
| probe-execution | Execute a single attack probe against an artifact, record the result with evidence and severity classification. |

<!-- END available-tables (generated) -->
