---
name: actor-profiling
description: Understand who the user is — background, resources, constraints, and
  deep motivations. Produces an ActorProfile that informs all downstream decisions.
  Use this tactic at the start of any crystallization process to build a model of
  the user's capabilities, limitations, and intent.
dependencies:
  sops:
  - ask-constraints
  - ask-intentionality
  - clarify-resources
  - explore-resume
---

# Actor Profiling

Build a comprehensive model of the user as a research actor — who they are, what they have, what constrains them, and why they're doing this.

## Available SOPs

| SOP | Purpose | Execution |
|-----|---------|-----------|
| explore-resume | Background, skills, projects, publications, research experience | dialogue (once only) |
| clarify-resources | Compute, timeline, collaboration, data, environment | dialogue |
| ask-constraints | Venue targets, methodology preferences, avoidance areas, advisor requirements | dialogue |
| ask-intentionality | Deep WHY probing — motivation, risk tolerance, innovation preference, etc. | dialogue |

## Methodology Guidance

The goal is to construct an ActorProfile with enough information to inform field exploration and goal decomposition. How you get there is your decision.

**Typical flow:**
1. `explore-resume` first (one-time, never re-run)
2. `clarify-resources` → `ask-constraints` → `ask-intentionality`

**But you may:**
- Return to `ask-intentionality` at any point when you discover a deeper WHY to probe
- Interleave `clarify-resources` when intentionality probing reveals resource-related gaps
- Skip or abbreviate SOPs when the user's initial message already provides the information

**End condition:** You judge that you have enough information to construct a meaningful ActorProfile. In cold-start scenarios, "enough" may mean just establishing boundaries (what the user won't do) rather than specifics.

## Cold-Start Special Case

When the user doesn't know what they want or can do, the ActorProfile captures boundaries rather than commitments:
- "User has experience in NLP and GNN, won't jump to physics/chemistry"
- "Timeline is flexible, no hard deadline"
- "Motivated by interest, not graduation pressure"

This is sufficient — later tactics will help narrow within these boundaries.

## Output (Tactic-Level Aggregation)

After running the SOPs you deem necessary, synthesize an ActorProfile:

```
ActorProfile {
  background: { skills, projects, publications, researchExp }
  resources: { compute, timeline, collaboration, data, environment }
  constraints: { venue, methodology, avoidance, advisor }
  intentionality: {
    motivation, successDefinition,
    riskTolerance, innovationPreference,
    independencePreference, timeUrgency, learningWillingness
  }
  boundary: "..."  // what the user definitely won't do
}
```

This is a conceptual schema, not a JSON requirement. Express it in whatever format serves the downstream context best.
