---
name: multi-perspective-attack
description: Assign distinct perspectives to attack a decision from multiple angles,
  then synthesize findings into a unified assessment.
execution: tactic
dependencies:
  sops:
  - perspective-assignment
  - perspective-attack
  - steel-manning-synthesis
---

# Multi-Perspective Attack

A structured approach to attacking a decision from multiple distinct viewpoints simultaneously. Each perspective brings different values, concerns, and failure modes — ensuring blind spots from any single viewpoint are exposed.

## Stages

1. **Perspective Assignment** — Define distinct perspectives with their values, concerns, and evaluation criteria
2. **Perspective Attack** — Each perspective independently attacks the decision and proposes alternatives
3. **Steel-Manning Synthesis** — Synthesize all attacks into a unified assessment with final verdict

## Available SOPs

| SOP | Phase | Purpose |
|-----|-------|---------|
| perspective-assignment | Assign | Define perspective briefs |
| perspective-attack | Attack | Execute attack from each perspective |
| steel-manning-synthesis | Synthesize | Unify findings into verdict |

## Execution Guidance

- Minimum 3 distinct perspectives (more for high-stakes decisions)
- Perspectives must be genuinely different (not variations of same viewpoint)
- Each perspective attacks independently before synthesis
- Synthesis must address every attack, not just convenient ones
- Final verdict must account for all perspectives, with explicit trade-off reasoning

## Minimum Yield

- >= 3 perspective briefs with distinct values and concerns
- Independent attack from each perspective with constructive alternatives
- Synthesis across all attacks
- Final verdict (ACCEPT/REJECT/REVISE) with surviving concerns
- Recommended modifications addressing highest-severity cross-perspective concerns

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| perspective-assignment | Define distinct stakeholder or analytical perspectives with their values, concerns, and evaluation criteria. |
| perspective-attack | Attack a decision from a specific assigned perspective, producing rated arguments and constructive alternatives. |
| steel-manning-synthesis | Synthesize all attacks and verdicts into a final unified assessment with surviving concerns and recommended modifications. |

<!-- END available-tables (generated) -->
