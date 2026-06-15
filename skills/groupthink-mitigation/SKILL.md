---
name: groupthink-mitigation
description: 'Strategy: 10th Man Rule and Liberating Structures — institutionalized
  dissent to prevent premature consensus and expose suppressed objections.'
type: strategy
tactics:
- adversarial-roleplay
- assumption-cascade
dependencies:
  tactics:
  - adversarial-roleplay
  - assumption-cascade
  sops:
  - devils-advocacy
  - finding-aggregation
  - key-assumptions-check
  - persona-construction
  - probe-execution
---

# Groupthink Mitigation Strategy

Prevent premature consensus by mandating structured dissent. Based on Israeli intelligence 10th Man doctrine and Lipmanowicz Liberating Structures.

## Method

1. **persona-construction** builds mandatory dissenter (10th Man) regardless of consensus
2. 10th Man must argue against the dominant conclusion even if personally agreeing
3. Liberating Structures applied: 1-2-4-All, TRIZ (worst possible outcome), Wicked Questions
4. **devils-advocacy** generates strongest case against current consensus
5. **probe-execution** tests dissenting arguments against evidence
6. Findings recorded even if dissent ultimately fails — the process matters

## Budget Table

| Parameter | S | M | L |
|---|---|---|---|
| Attack vectors | 5 | 12 | 20 |
| Probing rounds | 3 | 6 | 10 |
| Personas | 2 | 4 | 6 |
| Assumption checks | 5 | 10 | 20 |

## Orchestration

```
persona-construction → [build 10th Man dissenter]
→ devils-advocacy (construct dissenting case)
→ [for each dissenting claim]:
    probe-execution (test claim)
    → key-assumptions-check (verify consensus assumptions)
→ finding-aggregation → attack-resilience-scoring
```

## Subagents

- persona-construction (dissenter role creation)
- devils-advocacy (dissent argument generation)
- probe-execution (dissent testing)
- key-assumptions-check (consensus assumption audit)
- finding-aggregation (dissent documentation)

<!-- BEGIN available-tables (generated) -->

## Available Tactics

可选,无固定顺序;最终叶子终为 sop。

| Tactic | 何时用 |
| --- | --- |
| adversarial-roleplay | Tactic: Construct detailed hostile persona, attack artifact from that persona's perspective, record successful attack paths for aggregation. |
| assumption-cascade | Tactic: Surface assumptions, sort by dependency, attack root assumptions first, then trace cascade failures through the dependency graph. |

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| devils-advocacy | Construct the strongest possible counter-argument against a position, steelmanning the opposition before attacking. |
| finding-aggregation | Aggregate, deduplicate, and classify findings from multiple probes into a coherent vulnerability report. |
| key-assumptions-check | Military ACT: systematically enumerate all assumptions, classify by type, and evaluate evidence strength supporting each. |
| persona-construction | Build a detailed adversarial persona with background, motivation, expertise, blind spots, and preferred attack patterns. |
| probe-execution | Execute a single attack probe against an artifact, record the result with evidence and severity classification. |

<!-- END available-tables (generated) -->
