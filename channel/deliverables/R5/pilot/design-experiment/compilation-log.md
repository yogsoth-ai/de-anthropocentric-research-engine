# Compilation log

- Sources manually reviewed: `experiment-design`, `ablation-design`, `comparison-design`, `scaling-design`, `robustness-design`, `statistical-method-selection`, `reproducibility-protocol`, and `budget-constrained-design` (8 resolvable source directories).
- Unresolved source: `factor-level-design` is named by architecture but its directory is absent; no criteria were inferred for it.
- Kept: five design modes, factor/control logic, pre-registration, statistical-method selection, reproducibility and resource gates.
- Rework: copied numeric budget tables from experiment-design, ablation, comparison, scaling, robustness, and budget-constrained-design into body.
- Compressed: repeated strategy introductions and executor/provider instructions.
- Manual textual-gate review found HARD-GATE/minimum-yield requirements, same-compute and same-tuning fair-comparison conditions, pre-registration and power/stopping predicates, and seed/environment/verification reproducibility predicates. Source HARD-GATE text is partly XML-like and partly Markdown; normalized to one gate while preserving requirement.
- Contract: body fixed section, per R1 2026-09-03 ruling; registry is generated index only.
