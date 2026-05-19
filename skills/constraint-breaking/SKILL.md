---
name: constraint-breaking
description: "Orchestrate the full constraint-breaking cycle: extract conflict, challenge assumptions, project resolution"
version: 1.0.0
category: experiment-execution
type: tactic
used-by: constraint-analysis
orchestrates:
  - core-conflict-extraction
  - assumption-challenging
  - future-reality-projection
---

# Tactic: Constraint Breaking

## Orchestration Pattern

1. **Extract Core Conflict** → spawn `core-conflict-extraction`
   - Input: the binding constraint expressed as a dilemma
   - Output: Evaporating Cloud (A-B-C-D-D') with assumptions on each arrow
   - If constraint is not a dilemma, reframe: "We need X" vs "We cannot have X because Y"

2. **Challenge Assumptions** → spawn `assumption-challenging`
   - Input: all assumptions from the EC (typically 8-15 assumptions across 4 arrows)
   - Output: validity assessment for each assumption
   - Focus on: assumptions rated "Weak" or "No evidence"

3. **Generate Injections** → synthesize (no SOP needed)
   - For each invalid assumption, propose a concrete action that makes it irrelevant
   - Injection must be: specific, actionable, within our control, and testable
   - Generate 2-3 candidate injections

4. **Project Future Reality** → spawn `future-reality-projection`
   - Input: best injection candidate(s)
   - Output: Future Reality Tree showing:
     - Does the injection resolve the original conflict?
     - Does it create new Undesirable Effects (negative branches)?
     - What conditions (prerequisites) must hold?

5. **Validate or Iterate**
   - If injection resolves conflict without new UDEs → DONE
   - If new UDEs appear → trim negative branches (add caveats/conditions)
   - If no injection works → escalate to parent strategy with "unresolvable" flag

## Decision Criteria

- **When to use**: A binding constraint has been identified and needs resolution
- **When to skip**: Constraint is a simple resource gap (just acquire more) — no conflict to break
- **Success criterion**: At least one injection that resolves the conflict with ≤2 manageable side effects
- **Failure criterion**: After 3 injection attempts, none resolve cleanly → flag as hard constraint
- **Escalation**: If the constraint is a paradigm constraint (belief system), flag for human decision
