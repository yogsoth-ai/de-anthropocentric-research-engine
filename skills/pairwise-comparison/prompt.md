# Pairwise Comparison — Subagent Dispatch Prompt

You are executing the pairwise-comparison tactic for gap prioritization.

Your job is to rank gaps through systematic pairwise judgments rather than absolute scoring, using AHP-style comparison and consistency verification.

## Your Process

1. **Receive inputs**: Accept the list of gaps (with descriptions). Count N gaps. If N > 15, halt and instruct the calling strategy to first run scoring-matrix-construction to reduce the gap list to ≤15 before proceeding.

2. **Build comparison pairs**: Enumerate all N×(N-1)/2 unique pairs. Present each pair to the gap-pairwise-judgment SOP for relative importance judgment using the Saaty 1-9 scale:
   - 1 = equally important
   - 3 = moderately more important
   - 5 = strongly more important
   - 7 = very strongly more important
   - 9 = extremely more important
   - 2, 4, 6, 8 = intermediate values

3. **Invoke gap-pairwise-judgment SOP**: For each pair (Gap A, Gap B), obtain a judgment score (1-9 from A's perspective, reciprocal from B's perspective) plus a 1-sentence rationale.

4. **Construct the N×N pairwise matrix**: Fill in all judgments. Diagonal = 1. Lower triangle = reciprocals of upper triangle.

5. **Invoke consistency-check SOP**: Compute the consistency ratio CR using the principal eigenvalue method. If CR ≥ 0.1:
   - Identify the judgment pairs contributing most to inconsistency
   - Request revised judgments only for those pairs (max 3 revision rounds)
   - Recompute CR after each revision
   - If CR remains ≥ 0.1 after 3 rounds, report the situation and proceed with best-achieved matrix, flagging the result as INCONSISTENT

6. **Invoke priority-synthesis SOP**: Once CR < 0.1 (or after exhausting revision rounds), compute normalized priority weights for each gap via eigenvector method. Produce the final ranked list.

7. **Emit Yield Report** as the final block.

## Your Output

- The complete N×N pairwise comparison matrix in Markdown table format
- Consistency check result: final CR value and pass/fail status
- Revision history (if any): which pairs were revised and why
- Final priority ranking table: rank | gap ID | gap name | normalized weight
- Yield Report block:
  ```
  YIELD REPORT
  Gaps compared: N | Comparison pairs: N*(N-1)/2
  Revision rounds: R | Final CR: X.XX
  Top 3: <gap IDs and weights>
  Unstable rankings (weight gap < 0.05): <list or "none">
  ```

## Rules

- Never skip a comparison pair. All N×(N-1)/2 pairs must be judged.
- CR < 0.1 is a hard floor. Do not present a final ranking as authoritative if CR ≥ 0.1; instead mark the output INCONSISTENT and explain which judgments caused the problem.
- Judgment rationales must reference specific properties of the gaps (scope, evidence quality, novelty, etc.) — not generic phrases.
- Do not convert pairwise output directly to a 0-10 score; use normalized eigenvector weights.
- If two gaps have weights within 0.02 of each other, note them as effectively tied in rank.
- Minimum yield hard floor: complete matrix + CR < 0.1 + final ranking must all be present before reporting done.
