import json, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from generator.weights import dump_initial


def test_f2_revise_writes_next_batch_and_log(tmp_path):
    wd = tmp_path / "weights"; wd.mkdir()
    dump_initial(wd / "batch-0.json")
    subprocess.check_call([sys.executable, "scripts/apply_weight_update.py",
        "--weights-dir", str(wd), "--batch-id", "batch-0",
        "--target", "axis_prose", "--key", "A1.L0", "--new", "stronger pressure prose",
        "--reason", "loss-1 failed"])
    nxt = json.loads((wd / "batch-1.json").read_text(encoding="utf-8"))
    assert nxt["axis_prose"]["A1"]["L0"] == "stronger pressure prose"   # exactly one cell changed
    rec = json.loads((wd.parent / "revision_log.jsonl").read_text(encoding="utf-8").splitlines()[-1])
    assert rec["target"] == "axis_prose" and rec["key"] == "A1.L0"      # logged


def test_f1_copy_byte_identical_no_log(tmp_path):
    wd = tmp_path / "weights"; wd.mkdir()
    dump_initial(wd / "batch-0.json")
    subprocess.check_call([sys.executable, "scripts/apply_weight_update.py",
        "--weights-dir", str(wd), "--batch-id", "batch-0", "--copy"])
    nxt_path = wd / "batch-1.json"
    assert nxt_path.stat().st_size > 0                                  # test-hole: not empty
    assert json.loads(nxt_path.read_text(encoding="utf-8")) == \
           json.loads((wd / "batch-0.json").read_text(encoding="utf-8"))  # byte-equal content
    assert not (wd.parent / "revision_log.jsonl").exists()              # copy writes NO log
