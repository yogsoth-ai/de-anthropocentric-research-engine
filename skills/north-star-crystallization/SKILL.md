---
name: north-star-crystallization
description: Goal-Driven Requirement Refinement Engine for Research. Crystallize a
  user's fuzzy research intent into a North Star statement and structured ResearchBrief
  through adaptive dialogue and on-demand investigation.
execution: campaign
dependencies:
  strategies:
  - cold-start
  - hot-start
  - warm-start
  sops:
  - context-checkpoint
  - context-init
---

# North Star Crystallization

## Strategy Routing

| Signal | Route to |
|--------|----------|
| No direction at all ("I want to publish but don't know what") | cold-start |
| Has a general direction but not specific ("I'm interested in LLM reasoning") | warm-start |
| Has a specific topic/problem ("I want to improve CoT faithfulness") | hot-start |

## Manifest

### Strategies (3)

| Strategy | Purpose |
|----------|---------|
| cold-start | Full crystallization from zero — actor profiling through synthesis |
| warm-start | Simplified flow for users with a general direction |
| hot-start | Rapid crystallization for users with a specific topic |

### Tactics (6)

| Tactic | Purpose |
|--------|---------|
| actor-profiling | Understand user's background, expertise, resources |
| landscape-reconnaissance | Broad survey of potential research areas |
| direction-narrowing | Focus from broad area to specific problem |
| obstacle-analysis | Identify and assess obstacles to research goals |
| goal-decomposition | Break down research goals into sub-goals |
| north-star-synthesis | Converge into North Star + ResearchBrief |

### SOPs (23)

Dialogue + investigation operations. See individual SOP directories for details.

## Context Management

- Output: North Star Statement + ResearchBrief
- Downstream: knowledge-acquisition campaigns consume the ResearchBrief
