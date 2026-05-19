---
name: parameter-space-construction
description: "Orchestrates driver identification and parameter enumeration to build the complete morphological field"
version: 1.0.0
category: experiment-execution
type: tactic
used-by: scenario-planning
orchestrates:
  - scenario-driver-identification
  - parameter-enumeration
---

# Tactic: Parameter Space Construction

## Orchestration Pattern

1. **Spawn driver identification** → `scenario-driver-identification`
   - Pass: research context, planning horizon, domain constraints
   - Receive: ranked list of 5-8 uncertainty drivers with descriptions

2. **Validate driver set**
   - Check: Are drivers independent? (no redundancy)
   - Check: Do drivers span PESTEL categories? (no blind spots)
   - Check: Are drivers at the right abstraction level? (not too broad, not too narrow)
   - If validation fails: re-spawn with refined instructions

3. **Spawn parameter enumeration** → `parameter-enumeration`
   - Pass: validated driver list, MECE requirement, value count guidance (2-4 per driver)
   - Receive: complete Zwicky Box (driver × value matrix)

4. **Validate parameter space**
   - Check: Are values mutually exclusive within each driver?
   - Check: Are values collectively exhaustive within each driver?
   - Check: Is the total configuration space manageable? (< 500 combinations)
   - If validation fails: re-spawn enumeration with tighter constraints

5. **Compute space metrics**
   - Total configurations: product of all value counts
   - Expected surviving configs after CCA: ~10-20% of total
   - Estimated downstream budget: configs × per-scenario cost

## Quality Checks

- [ ] All drivers are genuinely uncertain (not predetermined)
- [ ] No driver is a subset or consequence of another
- [ ] Values within each driver are truly MECE
- [ ] Total space is computationally tractable for CCA
- [ ] Parameter space covers the planning horizon adequately
