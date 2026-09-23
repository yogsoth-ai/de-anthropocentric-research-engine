# DARE v4 Architecture

## Two executable layers

v4 contains exactly two executable node types: `tactic` and `sop`. A tactic is a compositional entry point; an SOP is an atomic scientific operation. `shared-basis`, `specialized`, `family`, and `scope` are inspection metadata only, never execution layers.

The authoritative graph is `v4/registry/graph.json`, derived from the read-only architecture source. It contains 267 nodes, 317 `calls` edges, 157 `jump` edges, and 474 total edges.

### Edge semantics

- `calls`: tactic → SOP vocabulary. It is not a mandatory linear execution order.
- `jump`: tactic → tactic or SOP → SOP handoff. Cross-type jumps are invalid.
- Provider/tool edges do not belong in the scientific graph.

## State handoff

Each node consumes a relevant state slice and returns a `ResearchStateDelta`. The delta is limited to these fields:

```yaml
findings: []
evidence_updates: []
hypothesis_updates: []
assumption_updates: []
uncertainties: []
decisions: []
open_questions: []
recommended_jumps: []
```

`delta_fields` in a node's output contract must be a subset of the fixed eight fields and must correspond to `produces`. Nodes do not prescribe provider-specific storage, checkpoint formats, scheduling, retries, or monitoring; those belong to the host runtime boundary.

## Contracts and catalog

`v4/registry/capabilities.json` is the 146-row v3 → v4 capability regression matrix. It is a catalog/index, not a second graph source. Node contracts remain authoritative in each `skills/<id>/SKILL.md` document.

Run `python v4/scripts/validate_graph.py` after changing registry or skill files. The validator reports file and line locations for actionable corrections and invokes the existing R5 threshold-fidelity gate.
