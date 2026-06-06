from optimizer.gate import batch_pass_ratio, converged


def pretrain(fake_batch_fn=None, run_batch_fn=None, weights=None, max_safety=1000):
    """PT6 主循环。无迭代上限（max_safety 仅防失控）；只靠收敛闸停。
    收敛后冻结（调用方负责落盘）。每 batch 样本累积入 dataset（pretrain-result-as-dataset）。"""
    run = fake_batch_fn or run_batch_fn
    ratios, all_samples = [], []
    n = 0
    while n < max_safety:
        batch_id = f"batch{n}"
        out = run(batch_id, weights)
        all_samples.extend(out.get("samples", []))
        ratios.append(batch_pass_ratio(out["topic_pass_flags"]))
        n += 1
        if out.get("any_rigor_floor"):
            # 端点塌（RR-1）→ 记录，交由调用方/用户决断（不静默继续假装收敛）
            pass
        if converged(ratios):
            return {"converged": True, "num_batches": n, "ratios": ratios,
                    "samples": all_samples}
    return {"converged": False, "num_batches": n, "ratios": ratios, "samples": all_samples}
