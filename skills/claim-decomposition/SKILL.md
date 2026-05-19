---
name: claim-decomposition
description: Independent/dependent claim parsing, element extraction, and feature mapping to technical domains
execution: tactic
used-by: patent-mining
---

# Claim Decomposition

Parses patent claims into their structural components — identifying independent vs. dependent claims, extracting individual elements, and mapping features to technical domains.

## Stages

### 1. Independent Claim Identification
- Identify all independent claims (method, apparatus, system, composition)
- Determine claim category (process, machine, manufacture, composition of matter)
- Extract the preamble, transitional phrase, and body of each independent claim

### 2. Dependent Claim Tree Construction
- Map dependency relationships (which claims depend on which)
- Build the full claim tree hierarchy
- Identify claim sets (groups of dependents narrowing the same independent)

### 3. Element Extraction
- Parse each claim into individual elements (limitations)
- Identify structural elements vs. functional elements
- Extract means-plus-function limitations and their corresponding structure

### 4. Feature Mapping to Technical Domains
- Map extracted elements to technical feature categories
- Identify which elements correspond to known technology components
- Create feature-to-claim mapping for scope analysis

## Available SOPs

| SOP | Role |
|-----|------|
| claim-parsing | Core parsing of claim text into structured elements |
| patent-categorization | Classify claim elements by technical domain |
| quality-scoring | Assess claim quality based on structure and specificity |

## Execution Guidance

- Always start with independent claims — they define the broadest protection
- Transitional phrases matter: "comprising" (open) vs. "consisting of" (closed)
- Means-plus-function claims (35 USC 112(f)) have narrower scope than they appear
- Method claims and apparatus claims may cover the same invention differently
- Count elements carefully — more elements = narrower claim scope

## Yield Report

Report to calling strategy after each execution:
- Number of claims parsed (independent + dependent)
- Total elements extracted
- Claim tree depth (max dependency chain)
- Feature categories identified
