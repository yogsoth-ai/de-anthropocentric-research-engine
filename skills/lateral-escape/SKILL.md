---
name: lateral-escape
description: de Bono lateral escape sequence — identify dominant idea, generate provocations
  (escape/reversal/exaggeration/distortion), follow consequences to extract new framings.
  Breaks paradigm lock-in.
execution: tactic
dependencies:
  sops:
  - consequence-following
  - deep-insight-provocation-generation
  - deep-insight-web-research
  - dominant-idea-identification
---

# Lateral Escape

Break paradigm lock-in through systematic provocation.

## Operations

dominant-idea-identification → provocation-generation → consequence-following

## Available SOPs

**Subagent:** dominant-idea-identification, provocation-generation, consequence-following
**Import:** web-research

## Execution Guidance

First identify what everyone "knows" (the dominant idea), then systematically challenge it via PO provocations (4 types: escape, reversal, exaggeration, distortion), follow each provocation's consequences to see if viable new framings emerge.

The goal is not to prove the dominant idea wrong — it is to escape its gravitational pull and discover what becomes visible from outside it.

## Minimum Yield

```
<HARD-GATE>
- Dominant ideas identified: >= 2
- Provocations generated: >= 4 (one per type minimum)
- Consequence chains followed: >= 3
- Viable new framings extracted: >= 1
</HARD-GATE>
```

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| consequence-following | Follow a provocation's logical consequences step by step to extract viable insights and new research directions. |
| deep-insight-provocation-generation | Generate de Bono lateral thinking provocations to challenge dominant ideas using escape, reversal, exaggeration, and distortion. |
| deep-insight-web-research | Deep web research with full page fetching via Apify. Import of web-browsing/web-research skill. Must fetch full page — no conclusions from previews. |
| dominant-idea-identification | Identify dominant paradigms and assumptions constraining thinking in a research field. |

<!-- END available-tables (generated) -->
