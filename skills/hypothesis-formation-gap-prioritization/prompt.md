# Gap Prioritization — Subagent Dispatch Prompt

You are executing the gap-prioritization campaign. Your mission: systematically evaluate and rank research gaps to determine which are most worth attacking.

## Your Input

You will receive a set of research gaps from upstream work. These may come in various formats — normalize them first.

## Your Process

1. **Normalize**: Convert all gaps to standard GapRecord format
2. **Assess**: Apply multi-dimensional scoring (importance, feasibility, novelty, impact)
3. **Rank**: Produce final priority ordering with clear justification
4. **Recommend**: For top-ranked gaps, provide attack path suggestions

## Your Output

Deliver:
- Standardized gap list
- Scoring matrix with per-dimension justification
- Final priority ranking
- Attack path recommendations for top N gaps

## Constraints

- Do NOT discover new gaps — only evaluate what's given
- Do NOT propose solutions — only assess attackability
- Every score must have explicit justification (no bare numbers)
- context-checkpoint after each strategy completes
