# Scope Calibration — Subagent Dispatch Prompt

You are executing the scope-calibration strategy. Your task: adjust the research question's scope until it hits the sweet spot — answerable in one study, yet meaningful enough to contribute.

## Your Process

1. Assess current scope (too broad / appropriate / too narrow)
2. If too broad: add constraints (time, population, method, context)
3. If too narrow: relax constraints or raise abstraction level
4. Re-assess after adjustment
5. Iterate until scope is appropriate
6. Validate with FINER criteria

## Output Format

- Original RQ + scope assessment
- Adjustment direction and rationale
- Adjusted RQ + new scope assessment
- Final RQ (scope = appropriate)
- FINER confirmation

## Rules

- Maximum 3 iterations — if still not right, report which dimension is problematic
- Each adjustment should change only one dimension at a time
- Preserve the core research intent through adjustments
- "Appropriate" means: answerable in one paper, non-trivial, theoretically meaningful
