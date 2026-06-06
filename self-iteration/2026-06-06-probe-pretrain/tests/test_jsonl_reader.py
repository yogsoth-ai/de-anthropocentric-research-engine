import json
import pytest
from tools.jsonl_reader import read_conversation, REQUIRED_LOGS_DIR_MSG


def test_logs_dir_is_required():
    with pytest.raises(ValueError, match="logs-dir"):
        read_conversation(sample_id="x", logs_dir=None)


def test_reads_and_deidentifies(tmp_path):
    # 造一个 fake session jsonl
    f = tmp_path / "sess.jsonl"
    f.write_text("\n".join(json.dumps(x) for x in [
        {"type": "user", "message": {"role": "user", "content": "why does it work?"}},
        {"type": "assistant", "message": {"role": "assistant", "content": "because X"}},
    ]), encoding="utf-8")
    turns = read_conversation(sample_id="sess", logs_dir=str(tmp_path))
    assert turns[0]["speaker"] == "user"
    assert "why does it work" in turns[0]["text"]
    # 去标识：返回结构里不含任何绝对路径
    assert all("logs_dir" not in t and "/" not in t.get("path", "") for t in turns)
