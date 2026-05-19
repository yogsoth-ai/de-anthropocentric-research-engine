---
name: critic-attack
description: Attack an advocate's case with multiple arguments rated by severity.
execution: subagent
prompt: ./prompt.md
input: winner, advocate_case
used-by: [steel-manning, validation]
---

# Critic Attack

Attacks an advocate's case from multiple angles, producing rated arguments that expose weaknesses, logical gaps, and unsupported claims. The critic's job is to find every legitimate vulnerability.

## Execution

Spawns a subagent with the critic role. The subagent receives the winner context and the advocate's case, then attacks the case systematically.

## Why Subagent

- Role isolation prevents sympathy with the advocate's position
- Critic must attack without mercy or compromise
- Separation ensures the attack is genuine, not performative

## HARD-GATE

Output must include:
- >= 3 distinct attack arguments
- Severity rating for each (HIGH/MEDIUM/LOW)
- Evidence or reasoning for each attack
- At least 1 attack targeting the advocate's strongest point
