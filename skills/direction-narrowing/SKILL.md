---
name: direction-narrowing
description: Focus within the user's chosen field(s). Identify specific sub-directions
  through deep paper and web research, then present ranked candidates. Use after landscape-reconnaissance
  has identified fields of interest.
dependencies:
  sops:
  - deep-web-search
  - north-star-crystallization-broad-paper-search
  - present-candidates
---

# Direction Narrowing

Focus within chosen field(s). Identify specific sub-directions and present ranked candidates.

## Available SOPs

| SOP | Purpose | Execution |
|-----|---------|-----------|
| broad-paper-search | Scan papers in the chosen field(s) | import: literature-overview |
| deep-web-search | Deep reading of web resources in the field | subagent |
| present-candidates | Present ranked sub-directions to user | dialogue |

## Methodology Guidance

- hot-start may only need partial SOP execution (a few searches for context)
- You decide search depth based on information sufficiency
- `present-candidates` depth scales by start mode:
  - cold-start: broad sub-directions available to pursue
  - warm-start: specific sub-problems and research tracks
  - hot-start: granular knowledge points, technical details

## Hard Constraints

- `broad-paper-search`: at least 80 papers scanned
- `deep-web-search`: at least 30 web pages read in full

## Output (Tactic-Level Aggregation)

`RankedCandidates[] + user's selection`

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| deep-web-search | Full-page web reading for non-academic perspectives — blogs, tech reports, product pages, industry analysis. Spawns a subagent to read pages in isolated context. Hard constraint: at least 30 web pages read in full. |
| north-star-crystallization-broad-paper-search | Paper landscape scan within selected field(s). Strict import of literature-engine/literature-overview skill. Hard constraint: at least 80 papers scanned. |
| present-candidates | Analyze sub-directions within the user's chosen field and present ranked candidates. Combines sub-direction identification, skill-gap matching, and presentation into a single SOP. Depth scales by start mode: cold-start shows broad sub-directions, warm-start shows specific sub-problems, hot-start shows granular technical details. |

<!-- END available-tables (generated) -->
