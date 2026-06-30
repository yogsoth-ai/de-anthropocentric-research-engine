import json, subprocess, sys

COMMON = {"ts", "run_id", "event", "batch_id", "topic_id", "rung_id", "seq"}


def emit(trace, **kw):
    args = [sys.executable, "scripts/trace_emit.py", "--trace", str(trace)]
    for k, v in kw.items():
        args += [f"--{k}", str(v)]
    subprocess.check_call(args)


def test_header_seq_and_nested_body(tmp_path):
    tr = tmp_path / "trace.jsonl"
    emit(tr, run_id="2026-06-07-00-00-00", event="run_start", batch_id="batch-0",
         topic_id="topic-00", rung_id="0")
    emit(tr, run_id="2026-06-07-00-00-00", event="rung_start", batch_id="batch-0",
         topic_id="topic-00", rung_id="0", axis_levels='{"A1":"L4","A3":"L4"}')
    rows = [json.loads(l) for l in tr.read_text(encoding="utf-8").splitlines()]
    assert COMMON <= set(rows[0])                       # 7 header fields present
    assert all(rows[0][k] is not None for k in COMMON)  # test-hole: none slip through as None
    assert rows[0]["seq"] == 1 and rows[1]["seq"] == 2  # seq strictly increments
    assert rows[1]["axis_levels"] == {"A1": "L4", "A3": "L4"}  # micro-fix A: parsed object


def test_malformed_body_falls_back_to_raw_string(tmp_path):
    tr = tmp_path / "trace.jsonl"
    emit(tr, run_id="r", event="e", batch_id="b", topic_id="t", rung_id="0",
         note="{bad json not closed")
    row = json.loads(tr.read_text(encoding="utf-8").splitlines()[-1])
    assert row["note"] == "{bad json not closed"        # micro-fix A: graceful raw fallback


def test_truncated_last_line_recovery(tmp_path):
    tr = tmp_path / "trace.jsonl"
    emit(tr, run_id="r", event="e", batch_id="b", topic_id="t", rung_id="0")  # seq 1
    with open(tr, "a", encoding="utf-8") as f:          # simulate a crash mid-write
        f.write('{"seq": 2, "event": "rung_done", trunc')
    emit(tr, run_id="r", event="e2", batch_id="b", topic_id="t", rung_id="0")
    rows = [l for l in tr.read_text(encoding="utf-8").splitlines() if l.strip()]
    assert json.loads(rows[-1])["seq"] == 2             # micro-fix B: scan past corrupt line
