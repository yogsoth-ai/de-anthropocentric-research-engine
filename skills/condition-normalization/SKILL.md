---
name: condition-normalization
description: Compare and standardize experimental conditions across papers
execution: tactic
used-by: baseline-establishment
---

# Condition Normalization


## Purpose

Build a structured understanding of how experimental conditions vary across papers, then define normalization schemes that enable fair method-to-method comparison. Addresses the fundamental problem that papers evaluate under different settings, making raw score comparison misleading.

## Stages

### Stage 1: Condition Extraction

For each method-paper pair, extract all evaluation conditions:
- Training data: size, version, preprocessing, augmentation
- Hardware: GPU type, memory, training time
- Hyperparameters: learning rate schedule, batch size, epochs
- Evaluation protocol: data split version, ensembling, post-processing
- Random seeds: number of runs, seed selection, variance reported

**Yield**: Condition vectors per method-paper pair.

### Stage 2: Difference Matrix

Build a matrix showing which conditions differ across methods:
- Identify dimensions with high variance across papers
- Identify dimensions that are controlled (same across all)
- Quantify the impact of each dimension on reported scores (if literature exists)

**Yield**: Condition difference matrix with impact annotations.

### Stage 3: Normalization Scheme

Define rules for adjusting scores to common conditions:
- Compute-normalized comparison (score per FLOP)
- Data-normalized comparison (score per training example)
- Time-normalized comparison (score per GPU-hour)
- Identify which normalizations are valid vs. speculative

**Yield**: Normalization rule set with validity bounds.

### Stage 4: Fair Comparison Baseline

Apply normalization to produce fair comparison subsets:
- Controlled comparison: methods evaluated under identical conditions
- Adjusted comparison: methods with score adjustments applied
- Pareto frontier: compute-vs-performance optimal set

**Yield**: Fair comparison tables with methodology notes.

## Minimum Yield

| Metric | Floor |
|--------|-------|
| Condition dimensions cataloged | 5 |
| Methods with full condition vectors | 10 |
| Normalization rules defined | 3 |
| Fair comparison sets produced | 2 |

## SOPs Used

- condition-cataloging (for Stage 1)
- compute-normalization (for Stage 3)
- performance-table-assembly (for Stage 4)
