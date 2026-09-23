# Threshold operator compatibility

N1's target rendering is ASCII (`>=`, `<=`, `+/-`). The validator now canonicalizes these alongside Unicode (`≥`, `≤`, `±`) and LaTeX (`\\ge`, `\\geq`, `\\le`, `\\leq`, `\\pm`) before matching ledger rows.

The verification was run against the actual pilot bodies and v3 source ledger, not synthetic fixtures: all five pilot source checks report `missing=0`; total matched source criteria is 541 after the existing narrow structural exclusions; process exit code is 0. The run also reports the real current inventory warning `full-node-coverage=266/267` for the pre-existing `structured-consensus` path artifact.
