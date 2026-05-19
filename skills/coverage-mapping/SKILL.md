---
name: coverage-mapping
description: Map evaluation coverage, identify untested capability dimensions — 20 benchmarks, 30 papers, 50 web searches
used-by: benchmark-archaeology
---

# Coverage Mapping Strategy

Map the evaluation landscape for a domain to identify which capabilities are well-tested, which are undertested, and which have no evaluation coverage at all. Produces a capability taxonomy with benchmark coverage annotations.

## Purpose

Build a comprehensive map of "what we can and cannot measure" for a given AI capability domain. Identify white spaces where important capabilities lack rigorous evaluation, and redundancies where multiple benchmarks test the same narrow skill.

## Budget

| Resource | Floor | Target |
|----------|-------|--------|
| Benchmarks mapped | 15 | 20 |
| Papers read | 20 | 30 |
| Web searches | 35 | 50 |

## State Ledger

```
<HARD-GATE>
| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| Benchmarks mapped | 0 | 20 | PENDING |
| Capability taxonomy nodes | 0 | 30 | PENDING |
| Papers fetched | 0 | 30 | PENDING |
| Papers read | 0 | 20 | PENDING |
| Web searches | 0 | 50 | PENDING |
| Coverage annotations complete | 0 | 20 | PENDING |
| White spaces identified | 0 | 5 | PENDING |
| Redundancy clusters found | 0 | 3 | PENDING |
</HARD-GATE>
```

Cannot exit until 80% of all targets met.

## Available Tactics

- **score-trajectory-analysis** — Understand maturity level of each benchmark

## Available SOPs

- **benchmark-inventory** — Catalog all benchmarks in domain
- **capability-taxonomy-mapping** — Build hierarchical capability taxonomy
- **metric-decomposition** — Understand what each benchmark actually measures
- **benchmark-synthesis** — Produce coverage map report

## Execution Guidance

1. **Domain Scoping**: Define the capability domain and its boundaries
2. **Taxonomy Construction**:
   a. Run capability-taxonomy-mapping to build hierarchical capability tree
   b. Use papers and web searches to refine taxonomy with community consensus
3. **Benchmark Inventory**:
   a. Run benchmark-inventory to collect all known benchmarks in domain
   b. For each benchmark, run metric-decomposition to identify tested capabilities
4. **Coverage Annotation**:
   a. Map each benchmark to taxonomy nodes it covers
   b. Identify coverage density per node (over-tested vs under-tested)
   c. Mark white spaces (zero coverage nodes)
5. **Redundancy Analysis**: Cluster benchmarks that test identical capabilities
6. **Maturity Assessment**: Run score-trajectory-analysis on key benchmarks to assess evaluation maturity
7. **Synthesis**: Produce coverage map with gap prioritization

## Output Format

```yaml
coverage_map:
  domain: string
  taxonomy:
    - node: string
      level: int
      children: list
      coverage_status: well-covered|partial|minimal|none
      benchmarks: list[string]
  white_spaces:
    - capability: string
      importance: high|medium|low
      reason_untested: string
      proposed_evaluation: string
  redundancy_clusters:
    - capability: string
      benchmarks: list[string]
      differentiation: string
  coverage_statistics:
    total_capabilities: int
    well_covered: int
    partial: int
    minimal: int
    none: int
    coverage_ratio: float
```
