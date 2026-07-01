import re, subprocess, sys


def test_run_id_format_and_skeleton(tmp_path):
    out = subprocess.check_output([sys.executable, "scripts/new_run_id.py",
        "--runs-root", str(tmp_path)], text=True).strip()
    assert re.fullmatch(r"\d{4}-\d{2}-\d{2}-\d{2}-\d{2}-\d{2}", out)  # run_id format
    base = tmp_path / out
    for sub in ("configs", "transcripts", "triples", "loss", "weights"):
        assert (base / sub).is_dir()                                  # 5 subdirs built
