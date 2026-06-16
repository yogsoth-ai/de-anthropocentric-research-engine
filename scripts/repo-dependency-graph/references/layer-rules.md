# Layer & edge rules — the use-dependency model

The graph reconstructs a DARE skill repo's **true `use`-dependency** relations.
There is exactly **one edge type (`use`)** and **5 vertex types**. These rules are
the judgement calls that keep reconstruction consistent across repos.

## The 5 vertex types

| layer | color | meaning |
| --- | --- | --- |
| `campaign` | `#ff3864` red | end-to-end pipeline orchestrator |
| `strategy` | `#00f0ff` cyan | orchestrates nested tactics |
| `tactic` | `#f9c80e` yellow | sequences SOPs, aggregates output |
| `sop` | `#9d7bff` purple | leaf that calls tools directly |
| `references` | `#5a6988` gray (dashed) | small `.py`/`.md` helper a skill points to |

## How to infer a skill's layer

Read each `skills/*/SKILL.md` **frontmatter first**. The declaration field is
**`type:` and/or `layer:`** — NOT `execution:` (a separate, often-absent field).
Many infra skills declare `type: sop` AND `layer: sop` redundantly; trust it.

If no layer field exists, infer from the body + README: does the skill
orchestrate other skills (higher layer) or call tools directly (sop)? State the
inference reasoning in the graph JSON's per-node `desc` or in your summary.

`references` vertices are not skills — they are helper files (`timestamp.py`,
`RULES.md`, a `references/foo.md`) that a skill actually points to in its body.
Only add one if a skill's text genuinely references it (a broken/never-used
pointer in a README does NOT justify a vertex — verify the live reference).

## The single edge type: `use`

`A -->|use| B` means **A invokes/orchestrates/calls B** at runtime. Direction is
**caller → callee** (the orchestrator points at what it drives).

## Edge legality (orchestration direction)

A higher layer may `use` any lower layer or a reference:

- `campaign` → {strategy, tactic, sop, references}
- `strategy` → {tactic, sop, references}
- `tactic`   → {sop, references}
- `sop`      → {references}
- **any layer** → `references`

## The escalation judgement (locked decision)

Sibling SOPs sometimes say "escalate to X" / "for deeper analysis use X" /
"import X". **All of these are drawn as `use` edges.** When both ends are the
same layer (the common `sop` → `sop` case), this is an **escalation handoff** and
is **explicitly allowed** — do NOT promote one skill to a higher layer just to
make the edge "legal". Same-layer `sop → sop` is a first-class edge here.

Rationale: forcing a layer bump to satisfy a hierarchy rule distorts the repo's
real declared structure. The edge records a true runtime handoff; the layers stay
as declared. `check_edges()` in `render_graph.py` treats `sop → sop` as valid and
only warns on other lower/equal-rank directions.

## What is NOT an edge

- A human-facing routing hint that is contradicted by an explicit "never calls
  other SOPs" rule in the same file — unless your project decides to treat all
  escalations as edges (this project does: see above).
- A pointer to an external MCP tool/server (e.g. `alphaxiv`, `brave`) — those are
  tools, not skill or reference vertices.
- A `dependencies:` entry that names a separate repo (cross-repo edge the
  single-repo parse cannot resolve) — note it as a dangling/cross-repo reference,
  do not invent a vertex for it unless you are building the combined graph.
