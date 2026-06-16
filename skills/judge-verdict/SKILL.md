---
name: judge-verdict
description: Render an impartial verdict on advocate case vs critic attacks with explicit
  reasoning.
execution: subagent
prompt: ./prompt.md
input: advocate_case, critic_attacks
dependencies:
  sops:
  - spawn-agent
---

# Judge Verdict

Renders an impartial verdict after weighing the advocate's case against the critic's attacks. The judge must address every argument explicitly and produce a clear ACCEPT/REJECT/REVISE decision with conditions.

## Execution

Spawns a subagent with the judge role. The subagent receives both the advocate case and critic attacks, then renders a verdict with full reasoning.

## Why Subagent

- Impartiality requires isolation from both advocate and critic roles
- Judge must weigh evidence without prior commitment to either side
- Separation ensures the verdict is based on argument quality, not role loyalty

## HARD-GATE

Output must include:
- Explicit verdict: ACCEPT, REJECT, or REVISE
- Point-by-point response to every critic attack
- Assessment of advocate case strength post-attack
- Conditions for acceptance (if ACCEPT or REVISE)
- Clear reasoning chain from evidence to verdict

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
