---
name: evaluation-protocol-comparison
description: Compare implementation differences of same benchmark across papers
execution: tactic
used-by: benchmark-archaeology
---

# Evaluation Protocol Comparison Tactic

Compare how different papers implement the same benchmark to expose hidden protocol variance that undermines cross-paper score comparability.

## Stages

### Stage 1: Paper Collection (Same Benchmark)

Collect 10-15 papers that report results on the target benchmark:
- Prioritize diversity: different labs, years, model families
- Include the original benchmark paper as reference protocol
- Include papers from different venues (top conferences, workshops, preprints)
- Search via dare-ss (ss_relevance_search) and dare-scholar (paper_searching)

**Search queries**: "[benchmark name] evaluation", "[benchmark name] results", "[benchmark name] state-of-the-art"

### Stage 2: Protocol Element Extraction

For each paper, run protocol-element-extraction SOP to extract:

| Element Category | Specific Parameters |
|-----------------|-------------------|
| **Data** | Split version, subset selection, preprocessing, filtering |
| **Prompting** | Template format, few-shot examples (count, selection), instruction wording |
| **Generation** | Decoding strategy, temperature, top-p/top-k, max tokens, stop criteria |
| **Evaluation** | Metric implementation, postprocessing, normalization, scoring script version |
| **Infrastructure** | Framework, precision (fp16/bf16/fp32), batch size, hardware |

### Stage 3: Difference Matrix Construction

Build a comparison matrix:
- Rows = protocol elements
- Columns = papers
- Cells = specific value used
- Highlight deviations from original protocol

Compute per-element variance:
- **None**: All papers use identical value
- **Low**: Minor variations (e.g., different random seeds)
- **Medium**: Substantive differences (e.g., different few-shot examples)
- **High**: Fundamental disagreements (e.g., different splits, different metrics)
- **Extreme**: Papers appear to evaluate different things under same name

### Stage 4: Impact Assessment

For each high-variance element:
- Search for ablation studies showing impact of that element
- Estimate score range attributable to protocol choice vs model quality
- Identify which protocol choices systematically favor certain model families
- Flag "protocol p-hacking" — suspicious correlation between protocol choice and reported improvement

## Output

```yaml
protocol_comparison:
  benchmark: string
  papers_compared: int
  reference_protocol: string  # original benchmark paper
  difference_matrix:
    - element: string
      category: data|prompting|generation|evaluation|infrastructure
      variance_level: none|low|medium|high|extreme
      values: list[{paper, value}]
      impact_estimate: string
  highest_variance_elements:
    - element: string
      score_impact: string
      favors: string  # which model family benefits
  protocol_p_hacking_flags:
    - paper: string
      suspicious_choice: string
      benefit: string
  cross_paper_comparability: high|moderate|low|unreliable
  standardization_recommendations:
    - element: string
      recommended_value: string
      rationale: string
```

## Yield Report

| Metric | Minimum |
|--------|---------|
| Papers compared | 8 |
| Protocol elements extracted per paper | 10 |
| High-variance elements identified | 2 |
| Impact estimates produced | 3 |
