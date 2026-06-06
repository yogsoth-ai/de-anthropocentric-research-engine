from dataclasses import dataclass, asdict


@dataclass
class AxisLevels:
    A1: str
    A2: str
    A3: str
    A4: str
    A5: str
    B1: str


@dataclass
class PolicyCard:
    label: str
    ladder_position: float
    axis_levels: AxisLevels
    f0_persona: str
    f1_substance: str
    f2_operationalization: str
    f3_legitimacy: str
    f4_corrigibility: str
    f5_framing: str
    f6_acceptance: str
    f7_wrong_premise: str
    f8_pressure_turns: int
    f8_closing_turns: int
    f9_generativity: str

    def validate(self):
        if self.axis_levels.A4 == "C-" and not self.f7_wrong_premise.strip():
            raise ValueError("F7 wrong_premise required when A4=C-")
        return self

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, d):
        lv = AxisLevels(**d["axis_levels"])
        d = {**d, "axis_levels": lv}
        return cls(**d)
