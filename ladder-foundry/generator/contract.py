"""D1 — PolicyCard semantic contract + validator.

Field -> axis map (one-to-one for the label axes A1-A5; F0/F6/F7/F8/F9 are
composed or off-axis):

  F0  persona identity / role header   composite rung + B1 tone
  F1  substance demand                 <- A1
  F2  request legitimacy / coherence   <- A2
  F3  operationalization insistence    <- A3
  F4  premise corrigibility            <- A4
  F5  generativity                     <- A5
  F6  acceptance rule (from F1/F3/F2)   assembler_params.f6_derivation
  F7  prerequisite facts                topic + A4 overlay
  F8  turn budget (constant per batch)  assembler_params.turn_budget
  F9  framing / tone directive         <- B1

A4/A5 are OFF-SPINE overlays: NOT part of primary_sort {A1,A3,A2}, they do not
participate in the composite ladder ordering. axis_prose stays L0..L4-indexed
for ALL 5 axes (STAGE 1 schema lock); the human-meaningful A4/A5 tag is a FIXED
level<->tag convention recorded in axis_levels, defined here as a constant:

  A4: L0<->C-, L2<->C0, L4<->C+   (L1/L3 unused seed slots, accepted)
  A5: L0<->G0, L4<->G+            (L1/L2/L3 unused seed slots, accepted)

B1 has ONE source of truth: axis_levels["B1"]. F9 carries the B1 framing
directive; F0's role header is merely written in a tone CONSISTENT with B1 (F0
does not encode a second, independent B1 value).
"""

A4_TAGS = {"L0": "C-", "L2": "C0", "L4": "C+"}
A5_TAGS = {"L0": "G0", "L4": "G+"}
AXIS_LEVEL_KEYS = {"A1", "A2", "A3", "A4", "A5", "B1"}

_LABEL_LEVELS = {"L0", "L1", "L2", "L3", "L4"}
_A4_VALUES = set(A4_TAGS.values())   # {"C-","C0","C+"}
_A5_VALUES = set(A5_TAGS.values())   # {"G0","G+"}
_F_FIELDS = ["F0", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9"]


def validate_card(card):
    al = card.axis_levels
    if set(al.keys()) != AXIS_LEVEL_KEYS:
        raise ValueError(f"axis_levels keys must be {AXIS_LEVEL_KEYS}, got {set(al.keys())}")
    for ax in ("A1", "A2", "A3"):
        if al[ax] not in _LABEL_LEVELS:
            raise ValueError(f"{ax} level out of enum: {al[ax]!r}")
    if al["A4"] not in _A4_VALUES:
        raise ValueError(f"A4 tag out of enum: {al['A4']!r}")
    if al["A5"] not in _A5_VALUES:
        raise ValueError(f"A5 tag out of enum: {al['A5']!r}")
    if not isinstance(al["B1"], str) or not al["B1"]:
        raise ValueError(f"B1 must be a non-empty str, got {al['B1']!r}")
    for f in _F_FIELDS:
        v = getattr(card, f)
        if not isinstance(v, str) or not v:
            raise ValueError(f"{f} must be a non-empty str, got {v!r}")
    return None
