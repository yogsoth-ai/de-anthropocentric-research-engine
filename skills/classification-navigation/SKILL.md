---
name: classification-navigation
description: IPC/CPC hierarchy drill-down and lateral expansion for patent discovery
execution: tactic
used-by: patent-mining
---

# Classification Navigation

Navigates the IPC/CPC patent classification hierarchy to discover patents through structured taxonomy traversal — drilling down into subclasses and expanding laterally to related classes.

## Stages

### 1. Top-Level Classification Identification
- Determine relevant IPC/CPC sections and classes from seed patents or technology description
- Map the technology domain to classification entry points
- Identify primary and secondary classification codes

### 2. Subclass Drill-Down
- For each identified class, drill into subclass, main group, and subgroup levels
- Assess patent density at each level
- Identify the most specific relevant classification codes

### 3. Lateral Expansion to Related Classes
- From identified subclasses, explore sibling and cousin classes
- Follow "see also" and "related" cross-references in classification schemes
- Identify adjacent technology areas that may contain relevant patents

### 4. Cross-Reference Validation
- Verify that lateral expansion yields relevant results
- Check that discovered classes actually contain patents related to the target technology
- Prune irrelevant branches and confirm final classification scope

## Available SOPs

| SOP | Role |
|-----|------|
| patent-query-formulation | Generate IPC/CPC-based search queries |
| patent-categorization | Validate classification relevance of found patents |
| saturation-detection | Determine when classification space is fully explored |

## Execution Guidance

- Start broad (section/class level) and narrow down based on relevance
- IPC and CPC diverge at subgroup level — check both schemes
- Pay attention to classification reform dates — codes may have changed
- Cross-references in CPC scheme definitions reveal non-obvious connections
- A single invention often spans 3-5 classification codes — always check secondary classifications

## Yield Report

Report to calling strategy after each execution:
- Classification codes explored (with depth level)
- New relevant codes discovered
- Patent count per classification code
- Coverage assessment (% of relevant classification space explored)
