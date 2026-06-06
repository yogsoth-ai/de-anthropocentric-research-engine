from optimizer.gate import batch_pass_ratio, converged


def pretrain(fake_batch_fn=None, run_batch_fn=None, weights=None,
             max_safety=1000, emitter=None, n=6, m=8):
    """PT6 主循环。无迭代上限（max_safety 仅防失控）；只靠收敛闸停。
    收敛后冻结（调用方负责落盘）。每 batch 样本累积入 dataset（pretrain-result-as-dataset）。
    emitter 可选：埋 run_start/batch_start/batch_done/converged/run_end 观测事件。"""
    run = fake_batch_fn or run_batch_fn
    if emitter:
        emitter.emit("run_start", n=n, m=m)
    ratios, all_samples = [], []
    i = 0
    while i < max_safety:
        batch_id = f"batch{i}"
        if emitter:
            emitter.emit("batch_start", batch_id=batch_id)
        out = run(batch_id, weights)
        all_samples.extend(out.get("samples", []))
        r = batch_pass_ratio(out["topic_pass_flags"])
        ratios.append(r)
        i += 1
        if emitter:
            emitter.emit("batch_done", batch_id=batch_id, pass_ratio=r,
                         topic_pass_flags=out["topic_pass_flags"],
                         recent_ratios=ratios[-3:],
                         any_rigor_floor=out.get("any_rigor_floor", False))
        if converged(ratios):
            if emitter:
                emitter.emit("converged", num_batches=i, ratios=ratios)
                emitter.emit("run_end", converged=True, total_samples=len(all_samples))
            return {"converged": True, "num_batches": i, "ratios": ratios,
                    "samples": all_samples}
    if emitter:
        emitter.emit("run_end", converged=False, total_samples=len(all_samples))
    return {"converged": False, "num_batches": i, "ratios": ratios,
            "samples": all_samples}
