---
name: conflict-resolution
description: "How do constraints conflict with each other? — Evaporating Cloud + assumption challenging + injection to resolve constraint conflicts"
version: 1.0.0
category: experiment-execution
type: strategy
used-by: constraint-analysis
sops:
  - core-conflict-extraction
  - assumption-challenging
  - future-reality-projection
tactics:
  - constraint-breaking
---

# Strategy: Conflict Resolution

## Methodology

Based on Goldratt's Evaporating Cloud (EC) and injection methodology:
- **Surface the conflict**: Express opposing demands in EC format
- **Challenge assumptions**: Each EC arrow rests on assumptions — find the invalid one
- **Inject**: Propose an action that invalidates the false assumption
- **Project future**: Use Future Reality Tree to verify injection resolves the conflict without creating new UDEs

Evaporating Cloud structure:
```
        B ←── D
       ↗         ↘ (conflict)
  A                    
       ↘         ↗ (conflict)
        C ←── D'
```
- A: Common objective both sides want
- B: Need that leads to wanting D
- C: Need that leads to wanting D'
- D and D': Mutually exclusive wants

## Execution Flow

1. **Extract Core Conflict** → call `core-conflict-extraction` SOP
   - Input: identified constraints that oppose each other
   - Output: Evaporating Cloud (A-B-C-D-D') with assumptions on each arrow

2. **Challenge Assumptions** → call `assumption-challenging` SOP
   - Input: assumptions underlying each EC arrow
   - Output: validity assessment, weakest assumptions identified

3. **Generate Injections** → synthesize from challenged assumptions
   - For each invalid assumption, propose an injection (action that makes the conflict disappear)

4. **Project Future Reality** → call `future-reality-projection` SOP
   - Input: proposed injections
   - Output: Future Reality Tree showing resolved conflict + any new UDEs

5. **Validate Resolution** → invoke `constraint-breaking` tactic
   - Orchestrate full resolution cycle

## Budget Gate

| Resource | Budget | Notes |
|----------|--------|-------|
| Subagent calls | ≤8 | 3 SOPs + injection generation + validation |
| Iterations | ≤3 | May need multiple injection attempts |
| Output size | ≤3000 tokens | EC + injection + FRT summary |
