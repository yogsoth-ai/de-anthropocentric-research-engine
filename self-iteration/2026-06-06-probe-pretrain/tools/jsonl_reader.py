import json
from pathlib import Path

REQUIRED_LOGS_DIR_MSG = "logs-dir is required (no default); privacy red line"


def read_conversation(sample_id: str, logs_dir):
    """读完整 session jsonl，返回去标识的对话轮次。
    隐私红线：logs_dir 必填、无默认；返回内容不含任何 log 路径。"""
    if not logs_dir:
        raise ValueError(REQUIRED_LOGS_DIR_MSG)
    path = Path(logs_dir) / f"{sample_id}.jsonl"
    turns = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        obj = json.loads(line)
        msg = obj.get("message", {})
        role = msg.get("role") or obj.get("type", "")
        content = msg.get("content", "")
        if isinstance(content, list):
            content = " ".join(c.get("text", "") for c in content if isinstance(c, dict))
        if role in ("user", "assistant"):
            turns.append({"speaker": role, "text": content})
    return turns
