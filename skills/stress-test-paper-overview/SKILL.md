---
name: paper-overview
description: Paper landscape scan returning abstracts and metadata. Import of literature-engine/paper-overview
  skill. Abstracts only — no conclusions from abstracts.
execution: import
source: skills/literature-overview/SKILL.md
dependencies:
  sops:
  - literature-overview
  - stress-test-paper-research
  - stress-test-paper-search
---

# Paper Overview

Paper landscape scan — abstracts and metadata only.

## Execution

Import — strictly follow `literature-engine/paper-overview` skill protocol.

## Quality Gate

Returns abstracts only. Do NOT draw conclusions about methodology, results, or contributions from abstracts. Use paper-search or paper-research for substantive claims.

## Budget

Quantity target is set by the calling strategy's budget table. This SOP executes one unit = one discover_papers or relevanceSearch call.

## Import Source

`literature-engine` repo → `skills/paper-overview/SKILL.md`
