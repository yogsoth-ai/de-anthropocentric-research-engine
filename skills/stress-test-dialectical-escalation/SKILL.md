---
name: dialectical-escalation
description: 'Tactic: Progressive debate escalation based on confidence thresholds.
  Each round increases attack sophistication until defender collapses or proves resilient.'
type: tactic
strategies:
- critic-defender-judge
- adversarial-escalation
dependencies:
  sops:
  - confidence-calibration
  - debate-critic
  - debate-defender
  - debate-judge
---

# Dialectical Escalation Tactic

Progressive pressure escalation — attack sophistication increases each round based on defender confidence.

## Orchestration

1. **debate-critic** generates attack at current escalation level
2. **debate-defender** responds with counter-arguments
3. **debate-judge** evaluates exchange, scores defender confidence (0.0–1.0)
4. **confidence-calibration** determines next action:
   - confidence > 0.7 → escalate to next level
   - confidence 0.3–0.7 → repeat at same level with different angle
   - confidence < 0.3 → defender collapsed, record vulnerability
5. Repeat until max rounds reached or saturation detected

## Escalation Levels

- **L1 Surface**: Factual accuracy, evidence quality, citation validity
- **L2 Structural**: Logical coherence, argument dependencies, internal consistency
- **L3 Foundational**: Core assumptions, paradigm fit, alternative explanations

## Subagents Dispatched

- debate-critic (attack generation per level)
- debate-defender (response generation)
- debate-judge (round scoring)
- confidence-calibration (escalation decision)

## Termination Conditions

- Max rounds exhausted (budget-dependent: 4/8/12)
- Defender confidence drops below 0.3 (collapsed)
- Saturation detected (no new attack vectors found)
- All escalation levels completed with confidence > 0.7 (survived)
