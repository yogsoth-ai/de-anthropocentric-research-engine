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
