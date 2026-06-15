---
name: propose-mitigations
description: Propose concrete mitigation strategies for severe obstacles. MUST use
  search tools to validate that proposed mitigations are realistic — no armchair theorizing.
  Each mitigation must have evidence of feasibility.
execution: subagent
prompt: ./prompt.md
input: obstacles_with_severity (string), actor_profile (string)
dependencies:
  sops:
  - spawn-agent
---

# Propose Mitigations

Concrete, search-validated mitigation strategies for severe obstacles.

## Execution

Subagent — spawned via `subagent-spawning/spawn-agent` skill.

## Input

- Obstacles with severity assessments
- ActorProfile

## Search

**Required** — must use imported skills to validate feasibility:
- web-search (web-browsing): Quick discovery of tools, frameworks, courses
- web-research (web-browsing): Deep reading of mitigation resources
- literature-overview (literature-engine): Find papers that solved similar obstacles
- literature-search (literature-engine): Medium-depth search for methodological alternatives
- literature-research (literature-engine): Deep reading for specific evidence

## Output

For each severe obstacle: mitigation strategy + evidence of feasibility + estimated effort.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
