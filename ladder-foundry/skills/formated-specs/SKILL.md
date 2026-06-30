---
name: formated-specs
description: Spec-slot skill for the research-executor. Emit the 4-layer DARE orchestration of the assigned topic as one research-graph JSON fenced block in your reply. Replaces the generic spec-writing step.
---

# formated-specs

You occupy the spec step of the research executor. Instead of writing a spec
file, you emit the orchestration you are about to (notionally) run as a single
JSON object inside one fenced block, directly in your reply.

## Hard contract

1. Emit exactly one fenced block opened with ` ```research-graph ` (that exact
   info-string, hyphen, NOT ` ```json `) and closed with ` ``` `.
2. The block body is a single valid JSON object, the schema below.
3. Emit it **into your reply (the dialogue)** — do NOT write it to a file. The
   block lands in this session's transcript; the harness cuts it from there.
4. Atomicity: produce the whole block within one assistant turn.
5. If you revise after pushback, emit a new full `research-graph` block; the
   harness keeps the LAST one. Never emit a half block.
6. Mandatory final step: after the graph block, load and run `formated-results`.

## research-graph schema

```json
{
  "nodes":        [ {"id": "n1", "skill": "<skill-name>", "layer": "campaign|strategy|tactic|sop"} ],
  "edges":        [ {"from": "n1", "to": "n2", "kind": "calls|sequences"} ],
  "layer_labels": { "n1": "campaign|strategy|tactic|sop" },
  "manifest":     [ "<skill actually orchestrated>" ],
  "prereq_dag":   [ {"node": "n2", "requires": ["n1"]} ]
}
```

Populate `manifest` only with skills you actually orchestrated; do not
fabricate. `layer` and `layer_labels` must respect the 4-layer architecture
(campaign → strategy → tactic → sop). Judge nothing against academic
standards; this is a structural record of orchestration only.
