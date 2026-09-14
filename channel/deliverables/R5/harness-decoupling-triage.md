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

## Whole-ledger follow-up (the previously omitted budget family)

The full ledger block was re-read line by line, not keyword-filtered. The following additional entries are the same C class:

| Ledger line | Source / criterion | Class | Final action | Basis |
|---:|---|:---:|---|---|
| 145 | `constraint-analysis`: `Context tokens <=80k per strategy`; `Summarize and spawn fresh` | C | Delete the complete ledger row. | Token ceiling is provider-specific runtime budget; summarization/spawn is context-management and dispatch behavior. Neither is a scientific constraint-analysis outcome. |
| 144 | `constraint-analysis`: `Wall-clock time <=30 min per strategy`; `Checkpoint and continue` | C | Delete the complete ledger row. | Wall-clock and checkpoint continuation are runtime scheduling/recovery controls. |
| 146 | `constraint-analysis`: `Total campaign <=5 strategies`; `Skip if constraint already resolved` | C | Delete the complete ledger row. | Strategy-count cap and skip routing bound execution orchestration, not the validity or completeness of the constraint model. |
| 151 | `resource-constraint`: `Iterations <=2`; `Re-quantify if estimates change` | C | Delete the budget row/criterion. | The numeric iteration cap is execution budget. The scientific requirement to update estimates when evidence changes remains expressible without a fixed run count. |
| 152 | `resource-constraint`: `Output size <=3000 tokens` | C | Delete the budget row/criterion. | Output-token cap is a harness/provider limit; the gap table and recommendation remain the scientific output. |
| 155 | `assumption-constraint`: `Iterations <=2`; `Re-rank if new assumptions surface` | C | Delete the budget row/criterion. | Iteration cap is orchestration budget. Re-ranking on newly surfaced assumptions is a method behavior and may remain without a numeric cap. |
| 156 | `assumption-constraint`: `Output size <=3000 tokens` | C | Delete the budget row/criterion. | Provider/output budget, not an assumption-quality threshold; preserve the ranked table and validation plan. |
| 158 | `dependency-constraint`: `Iterations <=2`; `Re-build if tasks change` | C | Delete the budget row/criterion. | Iteration cap is orchestration budget. Rebuilding when dependencies change is a correctness behavior independent of a fixed count. |
| 159 | `dependency-constraint`: `Output size <=3000 tokens` | C | Delete the budget row/criterion. | Output-token cap is runtime/provider control; preserve graph summary and critical-chain content. |
| 161 | `conflict-resolution`: `Iterations <=3`; `May need multiple injection attempts` | C | Delete the budget row/criterion. | Attempt count is dispatch budget. The scientific requirement is a testable injection and side-effect assessment, not a maximum number of attempts. |
| 162 | `conflict-resolution`: `Output size <=3000 tokens` | C | Delete the budget row/criterion. | Provider/output budget; preserve EC, injection, and FRT scientific artifacts. |

The following nearby numeric criteria are **not** harness budgets and remain in force: estimate precision `+/-30%` to `+/-10%` through evidence-driven iteration; top-5 fragile assumptions; UDE/constraint counts; candidate injections and side-effect bounds; and the sensitivity rule `>2* median`. They describe the research object or evidence quality rather than agent count, token budget, context compression, pause/recovery, or scheduling.

The current ledger text at line 140 is rendered as “must use imported skills to validate feasibility” after upstream cleanup. Treat that as the same C-class tooling dependency as the earlier `subagent (search required)` wording: remove the mandatory tool/skill mechanism, while retaining the underlying feasibility-validation and evidence requirement.
