---
name: structured-attack-campaign
description: "Tactic: Full attack lifecycle — threat surface enumeration, attack vector generation, systematic probing, and finding aggregation across all surfaces."
type: tactic
used-by: [red-teaming]
strategies: [systematic-probing, assumption-challenge, adversarial-persona, alternative-analysis]
---

# Structured Attack Campaign Tactic

Complete attack lifecycle from surface enumeration through probing to aggregated findings.

## Orchestration

1. **threat-surface-mapping** enumerates all attackable surfaces of the artifact
2. **attack-vector-generation** produces prioritized attack vectors per surface
3. **probe-execution** executes each vector, records outcome (success/failure/partial)
4. Partial successes trigger follow-up vector generation (depth-first on promising attacks)
5. **finding-aggregation** deduplicates, classifies, and ranks all findings
6. **attack-resilience-scoring** computes coverage metrics and overall resilience score

## Subagents Dispatched

- threat-surface-mapping (1 call at start)
- attack-vector-generation (1 call per surface)
- probe-execution (1 call per vector, budget-limited)
- finding-aggregation (1 call at end)
- attack-resilience-scoring (1 call at end)

## Termination Conditions

- All budgeted attack vectors exhausted
- All surfaces probed to at least depth 1
- Critical vulnerability found (early termination with immediate report)
- Diminishing returns: 3 consecutive probes yield no new findings
