---
name: landscape-reconnaissance
description: Broad, shallow exploration of candidate research fields. Understand what's
  out there before narrowing. Use when the user needs to discover which fields are
  available to them — especially in cold-start and warm-start scenarios.
dependencies:
  sops:
  - generate-candidate-fields
  - landscape-synthesis
  - north-star-crystallization-broad-web-search
  - present-and-ask
---

# Landscape Reconnaissance

Broad, shallow field exploration. Understand the landscape of possibilities before narrowing.

## Available SOPs

| SOP | Purpose | Execution |
|-----|---------|-----------|
| generate-candidate-fields | Generate candidate fields from ActorProfile | subagent |
| broad-web-search | Scan web for each candidate field | import: web-search |
| landscape-synthesis | Synthesize search results into FieldPanorama | subagent |
| present-and-ask | Present panorama to user, get field selection | dialogue |

## Methodology Guidance

- If iteration is needed, expand breadth (more fields, more searches), never depth
- Depth is direction-narrowing's job
- You decide when enough information exists to synthesize

## Hard Constraints

- `broad-web-search`: brave_web_search count=10 per call, at least 150 total results before synthesis
- `landscape-synthesis`: Don't only chase niche/novel combinations. Must also consider direct frontal competition in hot fields. The ambition to tackle hard problems head-on must be present.

## Output (Tactic-Level Aggregation)

`FieldPanorama[] + user's selected 1-2 fields of interest`

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| generate-candidate-fields | Propose 3-8 candidate research fields based on the full ActorProfile. When user wants to explore beyond their current stack, use other ActorProfile signals (intentionality, boundary) to determine exploration space. Free exploration within the boundary. |
| landscape-synthesis | Evaluate each candidate research field on maturity, competition, entry barrier, and publication opportunity. Synthesizes broad-web-search results into a structured FieldPanorama. Must consider both niche approaches AND direct frontal competition in hot fields. |
| north-star-crystallization-broad-web-search | Quick web scanning for field landscape understanding. Strict import of web-browsing/web-search skill. Hard constraint: brave_web_search count=10 per call, at least 150 total search results before completing. |
| present-and-ask | Present the field panorama to the user and gather their preferences — which fields interest them, which they reject, and why. A dialogue SOP that bridges landscape-synthesis output to user decision. |

<!-- END available-tables (generated) -->
