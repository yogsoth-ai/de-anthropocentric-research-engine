import json
from pathlib import Path


class TraceEmitter:
    """实时观测流。每次 emit append 一行 jsonl；transcript 全文单独落 .md。
    设备本地、gitignore、不进提交物。隐私红线：只放相对路径。"""

    def __init__(self, run_id, run_dir, clock=None):
        self.run_id = run_id
        self.run_dir = Path(run_dir)
        self.run_dir.mkdir(parents=True, exist_ok=True)
        (self.run_dir / "transcripts").mkdir(exist_ok=True)
        self._trace = self.run_dir / "trace.jsonl"
        self._seq = 0
        # clock 可注入（脚本环境禁用 argless Date）；默认用 datetime
        self._clock = clock or self._default_clock

    @staticmethod
    def _default_clock():
        from datetime import datetime, timezone
        return datetime.now(timezone.utc).isoformat()

    def emit(self, event, **fields):
        rec = {"ts": self._clock(), "run_id": self.run_id, "event": event,
               "seq": self._seq}
        rec.update(fields)
        with open(self._trace, "a", encoding="utf-8") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        self._seq += 1
        return rec

    def save_transcript(self, sample_id, text):
        """落对话全文，返回相对路径（绝不返回绝对/含 log 的路径）。"""
        rel = f"transcripts/{sample_id}.md"
        (self.run_dir / rel).write_text(text, encoding="utf-8")
        return rel
