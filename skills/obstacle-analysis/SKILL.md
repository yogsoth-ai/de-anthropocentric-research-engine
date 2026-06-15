---
name: obstacle-analysis
description: Identify what blocks the user from pursuing their chosen direction, assess
  severity, propose mitigations with search-validated evidence, and get user acceptance.
  Use after direction-narrowing has identified a specific direction.
dependencies:
  sops:
  - ask-obstacle-acceptance
  - assess-obstacle-severity
  - identify-obstacles
  - propose-mitigations
---

# Obstacle Analysis

Identify barriers, assess severity, propose mitigations, get acceptance.

## Available SOPs

| SOP | Purpose | Execution |
|-----|---------|-----------|
| identify-obstacles | Identify obstacles from ActorProfile + chosen direction | subagent (search optional) |
| assess-obstacle-severity | Rate severity of each obstacle | subagent (search optional) |
| propose-mitigations | Propose evidence-backed mitigations | subagent (search **required**) |
| ask-obstacle-acceptance | Present obstacles + mitigations, get user decision | dialogue (search optional) |

## Search Tools Available (for all SOPs)

- web-search (web-browsing): Quick web scanning, snippets
- web-research (web-browsing): Full page reading + analysis
- literature-overview (literature-engine): Paper landscape scan
- literature-search (literature-engine): Medium-depth paper search (AI summaries)
- literature-research (literature-engine): Deep paper reading (raw full text + PDF queries)

## Methodology Guidance

- SOPs can iterate within this tactic (re-assess after new information)
- You decide whether additional search is needed to evaluate obstacles

## Hard Constraint

- Maximum 2 rounds of the full identify → assess → propose → ask cycle
- After 2 rounds of `ask-obstacle-acceptance` with unresolved obstacles: return to `present-candidates` (direction-narrowing tactic)

## Output (Tactic-Level Aggregation)

`ObstacleReport { obstacles[], mitigations[], accepted: bool }`

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| ask-obstacle-acceptance | Present obstacles with their severity assessments and proposed mitigations to the user. Ask whether they can accept these obstacles. If unacceptable after 2 rounds, return to present-candidates. |
| assess-obstacle-severity | Rate each identified obstacle's difficulty — overcomability, time cost, workaround existence. May optionally use search tools to validate assessments. |
| identify-obstacles | Enumerate barriers to pursuing the chosen research direction — knowledge barriers, resource barriers, capability barriers, competition barriers. May optionally use search tools to discover obstacles the user hasn't mentioned. |
| propose-mitigations | Propose concrete mitigation strategies for severe obstacles. MUST use search tools to validate that proposed mitigations are realistic — no armchair theorizing. Each mitigation must have evidence of feasibility. |

<!-- END available-tables (generated) -->
