# R4 Mode Consistency Audit

Read-only source: `file-transfer/2026-08-23-22-16-dare-v4-architecture.json` and `refactory/2026-08-23-22-16-dare-v4-architecture.json` both exist, are 256318 bytes, and have identical MD5 `9ea41ed855f1937c7192b6cc59882262`. The earlier absence report was a relative-path error from the repository working directory. No graph or body files were modified.

| Node | Authoritative architecture `modes` | Body state | Determination | Owner |
|---|---|---|---|---|
| `rank-candidates` | `gap-prioritization`, `direction-selection`, `mcda-best-choice`, `full-ranking`, `category-sorting`, `non-compensatory-screening`, `rapid-triage`, `stakeholder-weighted` | No `## Mode branches` | Body missing section; write the eight exact modes from architecture. | N1 |
| `analyze-constraints-readiness` | `obstacle-triage`, `readiness-assessment`, `resource-envelope`, `causal-constraint-analysis`, `maturation-path` | No `## Mode branches` | Body missing section; write the five exact modes from architecture. | N1 |
| `map-stakeholder-system` | `critical-systems-heuristics`, `jobs-to-be-done`, `stakeholder-salience` | No `## Mode branches` | Body missing section; write the three exact modes from architecture. | N1 |
| `resolve-inventive-contradiction` | `technical-contradiction`, `physical-contradiction`, `separation` | No `## Mode branches` | Body missing section; write the three exact modes from architecture. | N1 |
| `synthesize-meta-analytic-evidence` | field absent (`modes` not present) | Body lists `pairwise`, `network`, `cumulative`, `heterogeneity`, `bias`; description also names them | Graph description and body both preserve five declared meta-analysis modes; graph is internally incomplete. Keep the body branches and add the five mode values to graph with description provenance. | N2 |
| `problem-reframing` | `dominant-frame-escape`, `perspective-shift`, `stakeholder/worldview`, `polarity`, `abstraction-scope` | Same five; slash form preserved | Consistent. Architecture literal is `stakeholder/worldview`; no rename. | None |
| `biomimetic-transfer` | `biologize-and-discover`, `BioTRIZ` | Same two; `BioTRIZ` capitalization preserved | Consistent. Architecture literal is `BioTRIZ`; no rename. | None |

## 33 empty-mode tactic scan

The scan used one mechanical rule: only a description that explicitly calls an enumeration a `mode`/`modes` or `execution modes` is a schema contradiction. Generic variants, scenario classes, failure modes, or operation lists are not promoted to graph modes without an explicit declaration.

| Tactic | Authoritative description claim | Determination | Owner |
|---|---|---|---|
| `sensitivity-analysis` | `Morris/Sobol/perturbation/Monte-Carlo as modes` (architecture line 380) | Graph mode field is absent despite an explicit mode declaration; record the four literal values with description provenance. | N2 |
| `synthesize-literature-evidence` | `Scoping, systematic, deep, narrative, and snowball are execution modes` (architecture line 599) | Graph mode field is absent despite five explicit execution modes; record the five literal values with description provenance. | N2 |
| `synthesize-meta-analytic-evidence` | `pairwise/network/cumulative/heterogeneity/bias modes` (architecture line 667) | Graph mode field is absent despite five explicit modes; record the five literal values with description provenance. | N2 |
| `design-experiment` | `Factorial, ablation, comparison, scaling, and robustness designs are modes` (architecture line 756) | Graph mode field is absent despite five explicit design modes; record the five literal values with description provenance. | N2 |

The other 29 empty-mode tactics were checked and have no equivalent explicit mode declaration: `falsifiability-audit`, `formulate-research-question`, `decompose-research-question`, `validate-research-gap`, `drill-root-causes`, `assumption-stress-test`, `robustness-analysis`, `structured-red-team`, `fmea-risk-analysis`, `counterfactual-causal-analysis`, `reductio-counterexample-analysis`, `analogical-discovery`, `structural-transformation`, `coverage-white-space-search`, `pairwise-ranking`, `structured-consensus`, `portfolio-optimization`, `map-research-landscape`, `decompose-research-goal`, `mine-patent-landscape`, `assess-prior-art-and-claims`, `map-patent-white-space`, `audit-benchmark-validity`, `establish-empirical-baseline`, `build-domain-ontology`, `construct-causal-model`, `construct-argument-map`, `analyze-future-scenarios`, `analyze-experiment-results`. The raw token scan also finds `fmea-risk-analysis` because its line 432 says `failure modes`; that is the object being enumerated, not an execution-mode declaration. Likewise, model `variants` in robustness analysis and future/competitive/temporal/stress scenario labels are not execution-mode declarations.

## Mechanical conclusion

- Graph additions required: four description-declared omissions above (one already assigned: `synthesize-meta-analytic-evidence`; three newly found: `sensitivity-analysis`, `synthesize-literature-evidence`, `design-experiment`). N2 should add only the literal values stated in each description and record description provenance. No graph entry is to be inferred from generic variant/scenario wording.
- Body repairs required: the four missing sections above (`rank-candidates`, `analyze-constraints-readiness`, `map-stakeholder-system`, `resolve-inventive-contradiction`) remain N1 work. `synthesize-meta-analytic-evidence` body branches are retained and do not require deletion.
- Naming exceptions are not mismatches: `stakeholder/worldview` (slash) and `BioTRIZ` (capitalization) exactly match the authoritative architecture.
- Counts: 4 body-missing, 4 graph-missing description declarations (3 new in this scan), 2 consistent naming forms; no body-overstated case.
