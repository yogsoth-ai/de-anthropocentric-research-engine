---
name: validity-probing
description: Challenge construct validity — does benchmark measure claimed capability? — 3 benchmarks, 40 papers, 30 web searches
used-by: benchmark-archaeology
---

# Validity Probing Strategy

Deep investigation of construct validity for individual benchmarks. Determines whether a benchmark actually measures the capability it claims to measure, or whether high scores can be achieved through shortcuts, artifacts, or unrelated competencies.

## Purpose

Produce a construct validity assessment that identifies the gap between what a benchmark claims to measure and what it actually measures. Expose confounds, shortcuts, and alternative explanations for high performance.

## Budget

| Resource | Floor | Target |
|----------|-------|--------|
| Benchmarks probed | 2 | 3 |
| Papers read | 30 | 40 |
| Web searches | 20 | 30 |

## State Ledger

```
<HARD-GATE>
| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| Benchmarks probed | 0 | 3 | PENDING |
| Papers fetched | 0 | 40 | PENDING |
| Papers read | 0 | 30 | PENDING |
| Web searches | 0 | 30 | PENDING |
| Construct validity assessments | 0 | 3 | PENDING |
| Artifact detection runs | 0 | 3 | PENDING |
| Alternative explanation catalogs | 0 | 3 | PENDING |
| Convergent validity checks | 0 | 3 | PENDING |
</HARD-GATE>
```

Cannot exit until 80% of all targets met.

## Available Tactics

- **artifact-detection** — Detect annotation artifacts and shortcuts
- **evaluation-protocol-comparison** — Compare how different papers implement the benchmark

## Available SOPs

- **construct-validity-assessment** — Core validity evaluation
- **metric-decomposition** — Understand what the metric actually captures
- **contamination-audit** — Rule out data leakage as confound
- **benchmark-synthesis** — Produce validity report

## Execution Guidance

1. **Target Selection**: Choose 3 benchmarks where validity concerns exist (high scores but questionable real-world transfer, known shortcuts, or contested claims)
2. **Per-Benchmark Deep Dive**:
   a. Collect the original benchmark paper + all critique/analysis papers
   b. Run construct-validity-assessment: map claimed capability to actual task requirements
   c. Run artifact-detection tactic: probe for shortcuts and spurious correlations
   d. Run metric-decomposition: identify what signals the metric actually rewards
   e. Check convergent validity: do models that score high also perform well on related tasks?
   f. Check discriminant validity: do models that score high fail on tasks they shouldn't if the capability were real?
3. **Alternative Explanation Catalog**: For each benchmark, enumerate non-target explanations for high scores
4. **Synthesis**: Produce validity verdict with evidence strength ratings

## Output Format

```yaml
validity_report:
  benchmark_name: string
  claimed_capability: string
  actual_measurement: string  # what it really measures
  validity_verdict: valid|partially_valid|questionable|invalid
  evidence_strength: strong|moderate|weak
  confounds_identified:
    - confound: string
      severity: high|medium|low
      evidence: string
  shortcuts_found:
    - shortcut: string
      exploit_method: string
      performance_gain: string
  convergent_validity: pass|partial|fail
  discriminant_validity: pass|partial|fail
  recommendations: list[string]
```
