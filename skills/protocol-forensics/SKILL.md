---
name: protocol-forensics
description: Analyze evaluation protocol differences across papers for same benchmark — 5 benchmarks, 60 papers, 30 web searches
used-by: benchmark-archaeology
---

# Protocol Forensics Strategy

Forensic analysis of how the same benchmark is implemented differently across papers. Reveals hidden variance in evaluation protocols that makes cross-paper score comparisons unreliable.

## Purpose

Expose the "reproducibility gap" in benchmark evaluation by documenting how papers differ in their implementation of supposedly standardized evaluation protocols. Quantify the score variance attributable to protocol differences rather than model improvements.

## Budget

| Resource | Floor | Target |
|----------|-------|--------|
| Benchmarks forensically analyzed | 3 | 5 |
| Papers read | 45 | 60 |
| Web searches | 20 | 30 |

## State Ledger

```
<HARD-GATE>
| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| Benchmarks analyzed | 0 | 5 | PENDING |
| Papers fetched | 0 | 60 | PENDING |
| Papers read | 0 | 45 | PENDING |
| Web searches | 0 | 30 | PENDING |
| Protocol extractions complete | 0 | 60 | PENDING |
| Difference matrices built | 0 | 5 | PENDING |
| Variance attributions done | 0 | 5 | PENDING |
| Impact assessments complete | 0 | 5 | PENDING |
</HARD-GATE>
```

Cannot exit until 80% of all targets met.

## Available Tactics

- **evaluation-protocol-comparison** — Core tactic: compare protocol implementations across papers

## Available SOPs

- **benchmark-inventory** — Identify target benchmarks
- **protocol-element-extraction** — Extract protocol parameters from individual papers
- **benchmark-synthesis** — Produce forensics report

## Execution Guidance

1. **Target Selection**: Choose 5 benchmarks with known reproducibility issues or high paper volume
2. **Paper Collection** (per benchmark):
   a. Collect 10-15 papers that report results on the same benchmark
   b. Prioritize papers from different labs, time periods, and model families
3. **Protocol Extraction** (per paper):
   a. Run protocol-element-extraction on each paper
   b. Extract: prompt format, few-shot examples, decoding parameters, evaluation script version, data split, preprocessing
4. **Comparison** (per benchmark):
   a. Run evaluation-protocol-comparison tactic to build difference matrix
   b. Identify which protocol elements vary most across papers
   c. Estimate score impact of each protocol difference
5. **Variance Attribution**: Decompose reported score improvements into:
   - Genuine model improvement
   - Protocol optimization (prompt engineering, example selection)
   - Implementation differences (tokenization, postprocessing)
6. **Synthesis**: Produce per-benchmark forensics report with reproducibility recommendations

## Output Format

```yaml
protocol_forensics:
  benchmark_name: string
  papers_analyzed: int
  protocol_elements:
    - element: string  # e.g., "few-shot examples", "decoding temperature"
      variation_level: none|low|medium|high|extreme
      values_observed: list[string]
      score_impact_estimate: string
  variance_attribution:
    genuine_improvement: float  # proportion of score gains
    protocol_optimization: float
    implementation_differences: float
    unexplained: float
  most_impactful_differences:
    - element: string
      score_range: string  # e.g., "+3.2 to +7.8 points"
      evidence: string
  reproducibility_grade: A|B|C|D|F
  recommendations:
    - recommendation: string
      priority: high|medium|low
```
