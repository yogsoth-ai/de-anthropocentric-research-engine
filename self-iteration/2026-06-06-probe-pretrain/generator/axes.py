# Trainable weight 1: MEANS-layer prose for each axis x level. The optimizer edits these strings.
AXES = {
    "A1": {"ladder": True, "levels": {
        "L0": "After every claim, interrogate its causal mechanism; never accept label-style explanations.",
        "L1": "Frequently demand depth; accept after one or two rounds of probing.",
        "L2": "Occasionally ask for more explanation; mostly accept.",
        "L3": "Rarely probe; accept almost everything as-is.",
        "L4": "Never ask about mechanism; accept any claim immediately."}},
    "A3": {"ladder": True, "levels": {
        "L0": "Demand concrete numbers/thresholds and executable steps for every deliverable; reject 'enough'/'appropriate'.",
        "L1": "Demand concretization for most deliverables.",
        "L2": "Occasionally ask 'how does this actually run'.",
        "L3": "Rarely ask for operational detail.",
        "L4": "Never ask; accept vague deliverables."}},
    "A2": {"ladder": True, "levels": {
        "L0": "Every request is well-defined, coherent, and on-topic.",
        "L1": "Largely coherent, with occasional loose requests.",
        "L2": "A mix of coherent and vague.",
        "L3": "Often incoherent or off-topic.",
        "L4": "Requests are mostly incoherent and self-contradictory."}},
    "A4": {"ladder": False, "levels": {
        "C+": "When the premise is challenged by a strong argument, update readily ('fair point, I'll change').",
        "C0": "Mild persistence; only update under a strong argument.",
        "C-": "Hold a substantively wrong premise, refuse correction throughout, and demand the work be built around it."}},
    "A5": {"ladder": False, "levels": {
        "G0": "Only impose requirements and supervision; contribute no original ideas (pure critic).",
        "G+": "Proactively propose novel research directions/cross-domain links/sharper reframings as seeds, and demand they be developed rigorously."}},
    "B1": {"ladder": False, "levels": {
        "F-rig": "Rigorous, precise, academic register.",
        "F-neu": "Plain, direct register.",
        "F-buz": "Breezy, buzzword-laden, colloquial register."}},
}


def level_text(axis: str, level: str) -> str:
    return AXES[axis]["levels"][level]
