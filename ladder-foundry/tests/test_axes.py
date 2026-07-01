from pathlib import Path
from generator import weights
from generator.axes import level_text

_AXES_PY = Path(__file__).resolve().parents[1] / "generator" / "axes.py"


def test_level_text_reads_prose(tmp_path):
    w = weights.dump_initial(str(tmp_path / "b0.json"))
    assert level_text(w, "A1", "L0") == w["axis_prose"]["A1"]["L0"]


def test_revise_changes_data_not_source(tmp_path):
    before = _AXES_PY.read_bytes()
    w = weights.dump_initial(str(tmp_path / "b0.json"))
    weights.revise(w, "axis_prose", "A1.L0", "edited body", "training step")
    after = _AXES_PY.read_bytes()
    assert before == after                      # source byte-identical
    assert level_text(w, "A1", "L0") == "edited body"   # data changed
