# ladder-foundry/demo.py
"""STAGE 1 health report. Run: python demo.py
Prints batch-0 anatomy + attack tests in plain language; a human verifies
STAGE 1 is correct without reading code.
"""
import tempfile
from pathlib import Path
from generator import weights
from generator.axes import level_text

_AXES_PY = Path(__file__).resolve().parent / "generator" / "axes.py"


def _expect_reject(label, fn):
    try:
        fn()
        print(f"  [FAIL] {label}: was ACCEPTED (should reject)")
    except ValueError:
        print(f"  [ok]   {label}: rejected")


def main():
    tmp = Path(tempfile.mkdtemp()) / "batch-0.json"
    w = weights.dump_initial(str(tmp))

    print("== batch-0 anatomy ==")
    print(f"  4 segments present: {set(w) == {'axis_prose','interp_params','assembler_params','frozen_label'}}")
    print(f"  interp_params 3-key-locked: {set(w['interp_params']) == weights.INTERP_KEYS}")
    print(f"  contains a coord under interp_params? {'coord' in str(w['interp_params'])}")
    print(f"  coord_table empty: {w['frozen_label']['coord_table'] == {}}")
    print(f"  rank direction locked: {w['frozen_label']['rank_order']['direction'] == [0,1,2,3,4,5]}")

    print("== attack tests (all must be rejected) ==")
    _expect_reject("revise frozen_label", lambda: weights.revise(w, "frozen_label", "x", 1, "atk"))
    _expect_reject("set collision=A2", lambda: weights.revise(w, "interp_params", "collision_offset_axis", "A2", "atk"))
    _expect_reject("unknown target", lambda: weights.revise(w, "bogus", "x", 1, "atk"))
    w["interp_params"]["sneaky"] = 1
    _expect_reject("inject extra interp_params key", lambda: weights.revise(w, "assembler_params", "turn_budget", 13, "atk"))
    del w["interp_params"]["sneaky"]

    print("== legal revise (must be accepted, source unchanged) ==")
    before = _AXES_PY.read_bytes()
    weights.revise(w, "axis_prose", "A1.L0", "edited", "legal training step")
    after = _AXES_PY.read_bytes()
    print(f"  revise axis_prose A1.L0: {'ok' if level_text(w,'A1','L0')=='edited' else 'FAIL'}")
    print(f"  axes.py source byte-identical: {before == after}")

    print("== contract reconciliation (field -> schema -> consumer) ==")
    rows = [
        ("axis_prose", "L1 schema seg (1)", "L3 axes.level_text"),
        ("interp_params", "L1 schema seg (2) (3-key lock)", "L4 interpolator.ladder_levels"),
        ("assembler_params", "L1 schema seg (3)", "L5 assembler.build_batch"),
        ("frozen_label.rank_order", "L1 locked (dump_initial only)", "L4 reads direction"),
        ("frozen_label.coord_table", "L1 locked, empty in batch-0", "L4/L5 read coords"),
    ]
    for field, schema, consumer in rows:
        print(f"  {field:28} | {schema:32} | {consumer}")


if __name__ == "__main__":
    main()
