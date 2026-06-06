import json
import subprocess


def _default_codex(skill: str, payload: dict) -> str:
    """真实现：call 出一个 codex session，load 指定 skill，喂 payload，取回 JSON。
    （--task 入口与实际 codex 参数在设备上 PT 阶段对齐；此处给出骨架。）"""
    proc = subprocess.run(
        ["codex", "exec", "--skill", skill],
        input=json.dumps(payload, ensure_ascii=False),
        capture_output=True, text=True, timeout=600,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"codex {skill} failed: {proc.stderr[:500]}")
    return proc.stdout.strip()


def parse_loss1(raw: str) -> dict:
    return json.loads(raw)


def parse_loss2(raw: str) -> dict:
    return json.loads(raw)


def run_loss1(transcript, card, codex_fn=_default_codex):
    raw = codex_fn("injection-fidelity", {"transcript": transcript, "card": card})
    return parse_loss1(raw)


def run_loss2(topic_samples, intended_order, codex_fn=_default_codex):
    raw = codex_fn("ladder-quality-order",
                   {"samples": topic_samples, "intended_order": intended_order})
    return parse_loss2(raw)
