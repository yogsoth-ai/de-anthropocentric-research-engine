# Harness-decoupling triage: `analyze-constraints-readiness`

判定范围：`v4/skills/analyze-constraints-readiness/SKILL.md` 的 **Preserved source criteria ledger**，行 140、145、153、158、162、166。按既有 A/B/C 口径复核；本文件只给 N1 改写依据，不修改 `v4/`。

## Final classification

| Ledger line | Source / criterion (verbatim) | Class | Final action | Basis |
|---:|---|:---:|---|---|
| 140 | `obstacle-analysis` / `propose-mitigations`: `subagent (search required)` | C | Delete the harness qualifier. Keep the scientific requirement to propose evidence-backed mitigations; do not require a named agent, tool, or search mechanism. | `subagent` and mandatory search are dispatch/tooling instructions, not a property of an adequate mitigation analysis. Evidence attachment remains a node-level quality requirement. |
| 145 | `constraint-analysis` / `Subagent calls <=15 per strategy`; `Pause and report partial` | C | Delete the complete ledger row. | Call-count budget is runtime resource control; “pause and report partial” is explicitly excluded agent-exception handling. Neither states a constraint-analysis result. |
| 153 | `resource-constraint` / `Subagent calls <=6` | C | Delete the complete ledger row. | The limit budgets a decomposition plan (three SOPs plus synthesis), not resource-envelope evidence or estimate quality. |
| 158 | `assumption-constraint` / `Subagent calls <=5` | C | Delete the complete ledger row. | The limit budgets two SOPs plus synthesis; it does not constrain the number, fragility, or validation status of assumptions. |
| 162 | `dependency-constraint` / `Subagent calls <=5` | C | Delete the complete ledger row. | The limit budgets two SOPs plus synthesis; dependency identification and critical-chain evidence remain covered by the scientific criteria. |
| 166 | `conflict-resolution` / `Subagent calls <=8` | C | Delete the complete ledger row. | The limit budgets SOP/injection dispatch and validation; conflict criteria remain the conflict model, testable injection, and side-effect bound, independent of harness. |

## Boundary and replacement rule

All six are C because their operative subject is the execution harness (`subagent`, call budget, or pause/report behavior). No line has a standalone scientific threshold worth translating to a relative quantity. Do not replace them with generic “effort” or “coverage” counts: that would preserve a hidden runtime budget under a new name.

When N1 edits the v4 skill, remove only the harness-bearing ledger rows/clauses. Preserve neighboring scientific predicates already present in the body, including evidence-backed mitigation, constraint/removal-path, assumption validation, dependency/critical-chain, and conflict-injection quality gates. No `audit-benchmark-validity` change is implied by this triage; it is outside the six cited entries.

Evidence boundary: runtime ownership is fixed by `12-v4-build-spec.md §3`; agent-exception handling is excluded by the 09-08 ruling; the method/harness separation is fixed by the Pthahnix boundary ruling. This classification does not alter v3 provenance truth; it removes only non-scientific harness obligations from the v4 ledger.
