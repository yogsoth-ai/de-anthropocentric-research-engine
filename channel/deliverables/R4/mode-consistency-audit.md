# R4 Mode Consistency Audit

Source of truth: `refactory/2026-08-23-22-16-dare-v4-architecture.json` (the requested `file-transfer/...` path is absent; channel roster identifies this refactory copy as the read-only source). No graph or body files were modified.

| Node | Authoritative architecture `modes` | Body state | Determination | Owner |
|---|---|---|---|---|
| `rank-candidates` | `gap-prioritization`, `direction-selection`, `mcda-best-choice`, `full-ranking`, `category-sorting`, `non-compensatory-screening`, `rapid-triage`, `stakeholder-weighted` | No `## Mode branches` | Body missing section; write the eight exact modes from architecture. | N1 |
| `analyze-constraints-readiness` | `obstacle-triage`, `readiness-assessment`, `resource-envelope`, `causal-constraint-analysis`, `maturation-path` | No `## Mode branches` | Body missing section; write the five exact modes from architecture. | N1 |
| `map-stakeholder-system` | `critical-systems-heuristics`, `jobs-to-be-done`, `stakeholder-salience` | No `## Mode branches` | Body missing section; write the three exact modes from architecture. | N1 |
| `resolve-inventive-contradiction` | `technical-contradiction`, `physical-contradiction`, `separation` | No `## Mode branches` | Body missing section; write the three exact modes from architecture. | N1 |
| `synthesize-meta-analytic-evidence` | field absent (`modes` not present) | Body lists `pairwise`, `network`, `cumulative`, `heterogeneity`, `bias`; description also names them | Body overstates graph schema. Do not add `modes` to graph from description; remove/route the body mode branch for N1 adjudication. | N1 |
| `problem-reframing` | `dominant-frame-escape`, `perspective-shift`, `stakeholder/worldview`, `polarity`, `abstraction-scope` | Same five; slash form preserved | Consistent. Architecture literal is `stakeholder/worldview`; no rename. | None |
| `biomimetic-transfer` | `biologize-and-discover`, `BioTRIZ` | Same two; `BioTRIZ` capitalization preserved | Consistent. Architecture literal is `BioTRIZ`; no rename. | None |

## Mechanical conclusion

- Graph additions required: none identified. The four graph entries already carry the authoritative mode arrays.
- Body repairs required: four missing sections above; `synthesize-meta-analytic-evidence` requires body correction because architecture has no `modes` field.
- Naming exceptions are not mismatches: `stakeholder/worldview` (slash) and `BioTRIZ` (capitalization) exactly match the authoritative architecture.
- Counts: 4 body-missing, 1 body-overstated, 2 consistent naming forms; graph-missing additions 0.
