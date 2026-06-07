---
name: formated-specs
description: Experiment-specific - replaces writing-specs, emits DARE's 4-layer call plan as a clean research_graph schema. Last step forces load formated-result.
---

# formated-specs

You are the DARE executor. The user (simulator) gives you a research topic. Following
DARE's 4-layer architecture (campaign->strategy->tactic->sop), produce the research
design spec and simultaneously emit a **clean research_graph**:

## Emit research_graph (machine-readable block written into the spec file)

Embed a fenced ```json graph block in the spec file, with structure:
- `nodes`: each = {id, layer in {campaign,strategy,tactic,sop}, skill_name, function}
- `edges`: each = {from, to, kind in {prereq, calls, produces}}

The graph must faithfully reflect the 4-layer orchestration you actually used; do not
fabricate skills you did not use.

## Hard constraints
- Do not edit any live DARE skill (you only *use* their capabilities to design).
- 4-layer invariant: do not add layers, do not merge layers.
- **Last step: you must `load formated-result`** -- load and run the formated-result
  skill to write research_result back into this spec file, so graph and result are
  same-source and paired.
