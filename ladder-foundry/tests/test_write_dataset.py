import json, subprocess, sys

WHITELIST = {"sample_id", "label", "research_config", "research_graph",
             "research_result", "loss1_fidelity", "topic_pass", "intended_rank"}


def _triple(extra=None):
    d = {"research_config": {"F0": "x"}, "research_graph": {"nodes": []},
         "research_result": {"title": "t"}}
    if extra:
        d.update(extra)
    return d


def test_rejects_non_whitelist_field(tmp_path):
    rd = tmp_path / "run"; (rd / "triples").mkdir(parents=True)
    # inject a leaked field (e.g. a logs_dir). The VALUE is a synthetic sentinel,
    # NOT a real device path — committed tests must never carry a real CC-log path.
    (rd / "triples" / "s1.json").write_text(json.dumps(
        _triple({"logs_dir": "REDACTED-synthetic-sentinel-not-a-real-path"})), encoding="utf-8")
    r = subprocess.run([sys.executable, "scripts/write_dataset.py",
        "--run-dir", str(rd), "--sample", "s1", "--topic", "topic-00",
        "--rung", "0", "--out-root", str(tmp_path / "dataset")])
    assert r.returncode != 0      # non-whitelist field in triple -> hard-fail abort


def test_writes_whitelisted_sample(tmp_path):
    rd = tmp_path / "run"; (rd / "triples").mkdir(parents=True)
    (rd / "triples" / "batch-0-topic00-id0.json").write_text(
        json.dumps(_triple()), encoding="utf-8")
    subprocess.check_call([sys.executable, "scripts/write_dataset.py",
        "--run-dir", str(rd), "--sample", "batch-0-topic00-id0", "--topic", "topic-00",
        "--rung", "0", "--out-root", str(tmp_path / "dataset"),
        "--axis-levels", '{"A1":"L0"}', "--loss1", "1.0", "--topic-pass", "true"])
    out = json.loads((tmp_path / "dataset" / "topic-00" /
                      "batch-0-topic00-id0.json").read_text(encoding="utf-8"))
    assert set(out) <= WHITELIST            # output keys subset of whitelist
    assert out["label"]["rung_id"] == 0     # label.rung_id correct
    assert out["topic_pass"] is True
