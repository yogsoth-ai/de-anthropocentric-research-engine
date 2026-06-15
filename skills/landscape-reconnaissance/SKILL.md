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
