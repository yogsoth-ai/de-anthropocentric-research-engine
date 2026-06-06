from dataclasses import dataclass


@dataclass
class DialogueResult:
    spec_text: str
    transcript: list
    completability: str  # "ok" | "failed"
    transcript_path: str = ""  # 观测流相对路径（无 emitter 时为空）


def _emit_turn(emitter, transcript, speaker, text, phase, turn_idx, sample_id):
    transcript.append({"speaker": speaker, "text": text})
    if emitter:
        emitter.emit("dialogue_turn", sample_id=sample_id, phase=phase,
                     turn_idx=turn_idx, speaker=speaker,
                     text_excerpt=text[:200])


def run_dialogue(card, topic, sim_fn, exec_fn, emitter=None, sample_id=""):
    """三层嵌套的中间层：驱动 模拟器↔执行器 对话。F8 两段。
    emitter 可选：给观测流逐轮发 dialogue_turn 并落 transcript 全文。"""
    history, transcript = [], []
    # 施压段
    for i in range(card["f8_pressure_turns"]):
        u = sim_fn(history, "pressure")
        _emit_turn(emitter, transcript, "user", u, "pressure", i, sample_id)
        a = exec_fn(history + [u])
        _emit_turn(emitter, transcript, "assistant", a, "pressure", i, sample_id)
        history += [u, a]
    # 收尾段：用户停止加新要求，执行器走 formated-specs→load formated-result
    for i in range(card["f8_closing_turns"]):
        u = sim_fn(history, "closing")
        _emit_turn(emitter, transcript, "user", u, "closing", i, sample_id)
        a = exec_fn(history + [u])
        _emit_turn(emitter, transcript, "assistant", a, "closing", i, sample_id)
        history += [u, a]
    spec_text = exec_fn(history + ["FINALIZE: load formated-result"])
    completability = "ok" if spec_text and "design" in spec_text else "failed"
    tpath = ""
    if emitter and sample_id:
        full = "\n".join(f'{t["speaker"]}: {t["text"]}' for t in transcript)
        tpath = emitter.save_transcript(sample_id, full)
    return DialogueResult(spec_text=spec_text, transcript=transcript,
                          completability=completability, transcript_path=tpath)
