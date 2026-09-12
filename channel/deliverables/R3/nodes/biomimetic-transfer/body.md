# biomimetic-transfer
## Purpose
Translate a target problem into biological functions, find analogous living systems, extract causal strategies, and transfer them back.
## Input contract
```yaml
required: [target_problem, target_function]
optional: [biological_search_space, compatibility_constraints]
constraints: [function must be stated independently of the target implementation]
```
## Execution protocol
1. Biologize the problem (`biologize-problem`).
2. Discover biological analogs (`discover-biological-analog`).
3. Extract the causal strategy (`extract-biological-strategy`).
4. Instantiate the target transfer (`instantiate-transfer`).
5. Check compatibility (`evaluate-compatibility`).
Deviation: BioTRIZ mode may branch during strategy extraction, but all five checks remain required.
## Mode branches
- `biologize-and-discover`: translate function, search biological analogs, then extract mechanism.
- `BioTRIZ`: use biological contradiction/principle framing during strategy extraction before transfer.
## Output contract
```yaml
produces: [biological_analogs, strategy_extract, transfer_candidate, compatibility_report]
delta_fields: [findings, hypothesis_updates, uncertainties, decisions, open_questions]
```
## Thresholds and quality gates
- B: analogs solve the same function; strategy includes mechanism and conditions; target compatibility is explicit.
## Failure and counterexamples
Reject organism-by-appearance analogies, transfers without mechanism, and proposals violating target constraints.
## Provenance map
- `creative-ideation/biomimicry`, `biologize-and-discover`, `biotriz`, `biological-analogy`: resolved/concept only when exact v3 node is found.
- Status: `creative-ideation/biomimicry`, `biologize-and-discover` resolved; `biotriz`, `biological-analogy` concept.
## Preserved source criteria ledger
- Preserve biologize → discover → extract strategy → transfer workflow and BioTRIZ branching.
## Context checkpoint / Delta notes
Append function translation, analog evidence, mechanism, transfer assumptions, and compatibility failures.
