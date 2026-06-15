---
name: adversarial-debate-protocol
description: Structured debate protocol that constructs an advocate, deploys critic
  attacks, and renders a judge verdict through iterative rounds.
execution: tactic
dependencies:
  sops:
  - advocate-construction
  - critic-attack
  - judge-verdict
---

# Adversarial Debate Protocol

A formal three-role debate structure ensuring decisions survive rigorous adversarial challenge. The protocol assigns distinct roles (advocate, critic, judge) to prevent confirmation bias and ensure intellectual honesty.

## Stages

1. **Advocate Construction** — Build the strongest possible case for the position under debate
2. **Critic Attack** — Attack the advocate's case from multiple angles with severity ratings
3. **Judge Verdict** — Impartial assessment of advocate case vs critic attacks, rendering ACCEPT/REJECT/REVISE
4. **Iteration** (if REVISE) — Advocate revises case, critic re-attacks, judge re-evaluates

## Available SOPs

| SOP | Role | Purpose |
|-----|------|---------|
| advocate-construction | Advocate | Build strongest case for position |
| critic-attack | Critic | Attack the case with rated arguments |
| judge-verdict | Judge | Render impartial verdict |

## Execution Guidance

- Minimum 2 rounds before accepting ACCEPT verdict
- Critic must produce >= 3 distinct attack arguments per round
- Judge must address every critic argument explicitly
- If judge verdict is REVISE, advocate must address specific weaknesses identified
- Maximum 4 rounds before escalating to strategy level

## Minimum Yield

- Advocate case with explicit evidence and reasoning
- Critic attacks with severity ratings (HIGH/MEDIUM/LOW)
- Judge verdict (ACCEPT/REJECT/REVISE) with point-by-point reasoning
- Conditions for acceptance (if ACCEPT)
- Required modifications (if REVISE)

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| advocate-construction | Construct the strongest possible case for a rejected candidate or counter-position. |
| critic-attack | Attack an advocate's case with multiple arguments rated by severity. |
| judge-verdict | Render an impartial verdict on advocate case vs critic attacks with explicit reasoning. |

<!-- END available-tables (generated) -->
