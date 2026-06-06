import json
from pathlib import Path

CHECK_TOKENS = ["r13", "r14", "r16", "check fired", "32-check", "primitive", "p1 ", "p2 "]


class Weights:
    """Three trainable weight types: (1) axis_prose (2) interp_params (3) assembler_params.
    No gradient; revise() is the sole entry for the optimizer's coordinate descent and enforces W5."""

    def __init__(self, axis_prose, interp_params, assembler_params, revision_log=None):
        self.axis_prose = axis_prose
        self.interp_params = interp_params
        self.assembler_params = assembler_params
        self.revision_log = revision_log or []

    @classmethod
    def default(cls):
        return cls(axis_prose={"A1.L4": "never asks about mechanism"},
                   interp_params={"step": 1, "collapse_bump": 1},
                   assembler_params={"pressure_turns": 10, "closing_turns": 2})

    def revise(self, target, key, new_value, reason):
        if any(t in reason.lower() for t in CHECK_TOKENS):
            raise ValueError("W5 violation: revision reason references a check/primitive")
        getattr(self, target)[key] = new_value
        self.revision_log.append({"target": target, "key": key,
                                  "new_value": new_value, "reason": reason})

    def save(self, path):
        Path(path).write_text(json.dumps({
            "axis_prose": self.axis_prose, "interp_params": self.interp_params,
            "assembler_params": self.assembler_params, "revision_log": self.revision_log,
        }, ensure_ascii=False, indent=2), encoding="utf-8")

    @classmethod
    def load(cls, path):
        d = json.loads(Path(path).read_text(encoding="utf-8"))
        return cls(d["axis_prose"], d["interp_params"], d["assembler_params"], d.get("revision_log"))
