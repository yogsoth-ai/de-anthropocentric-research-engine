from dataclasses import dataclass


@dataclass
class DialogueResult:
    spec_text: str
    transcript: list
    completability: str  # "ok" | "failed"


def run_dialogue(card, topic, sim_fn, exec_fn):
    """三层嵌套的中间层：驱动 模拟器↔执行器 对话。
    F8 两段：先 f8_pressure_turns 轮施压，再 f8_closing_turns 轮收尾。"""
    history, transcript = [], []
    # 施压段
    for _ in range(card["f8_pressure_turns"]):
        u = sim_fn(history, "pressure")
        transcript.append({"speaker": "user", "text": u})
        a = exec_fn(history + [u])
        transcript.append({"speaker": "assistant", "text": a})
        history += [u, a]
    # 收尾段：用户停止加新要求，执行器走 formated-specs→load formated-result
    for _ in range(card["f8_closing_turns"]):
        u = sim_fn(history, "closing")
        transcript.append({"speaker": "user", "text": u})
        a = exec_fn(history + [u])
        transcript.append({"speaker": "assistant", "text": a})
        history += [u, a]
    spec_text = exec_fn(history + ["FINALIZE: load formated-result"])
    completability = "ok" if spec_text and "design" in spec_text else "failed"
    return DialogueResult(spec_text=spec_text, transcript=transcript, completability=completability)
