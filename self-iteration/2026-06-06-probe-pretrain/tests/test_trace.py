import json
from optimizer.trace import TraceEmitter


def test_emit_appends_jsonl_with_common_header(tmp_path):
    em = TraceEmitter(run_id="run-x", run_dir=str(tmp_path))
    em.emit("rung_start", batch_id="batch0", topic_id="topic-01", rung_id=0,
            sample_id="batch0-topic-01-id0", config_full={"f0_persona": "研究监督者"})
    lines = (tmp_path / "trace.jsonl").read_text(encoding="utf-8").splitlines()
    rec = json.loads(lines[0])
    assert rec["event"] == "rung_start" and rec["run_id"] == "run-x"
    assert rec["seq"] == 0 and rec["rung_id"] == 0
    assert rec["config_full"]["f0_persona"] == "研究监督者"
    assert "ts" in rec


def test_seq_is_monotonic(tmp_path):
    em = TraceEmitter(run_id="r", run_dir=str(tmp_path))
    em.emit("batch_start", batch_id="b0")
    em.emit("batch_done", batch_id="b0", pass_ratio=1.0)
    seqs = [json.loads(l)["seq"]
            for l in (tmp_path / "trace.jsonl").read_text(encoding="utf-8").splitlines()]
    assert seqs == [0, 1]


def test_save_transcript_returns_relative_path_no_log_dir(tmp_path):
    em = TraceEmitter(run_id="r", run_dir=str(tmp_path))
    rel = em.save_transcript("batch0-topic-01-id0", "user: 为什么?\nassistant: 因为X")
    # 隐私红线：返回相对路径，不含绝对 log 路径
    assert rel == "transcripts/batch0-topic-01-id0.md"
    assert "\\" not in rel and not rel.startswith("/")
    body = (tmp_path / "transcripts" / "batch0-topic-01-id0.md").read_text(encoding="utf-8")
    assert "因为X" in body
