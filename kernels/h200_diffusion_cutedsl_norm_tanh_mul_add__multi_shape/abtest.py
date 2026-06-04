"""LOCAL DIAGNOSTIC ONLY — never citable as evidence. Sequential wall-clock
medians without alternating order, CUDA events, idle refusal, or provenance.
All admissible numbers come from benchmark.py (interleaved AB/BA machinery,
CSV evidence rows)."""

import importlib.util
import pathlib
import statistics
import time

import torch

KD = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("c", KD / "tests" / "test_correctness.py")
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)


def wall(fn, case, warmup, iters):
    for _ in range(warmup):
        fn(case)
    torch.cuda.synchronize()
    s = []
    for _ in range(iters):
        t0 = time.perf_counter()
        fn(case)
        torch.cuda.synchronize()
        s.append((time.perf_counter() - t0) * 1e6)
    return statistics.median(s)


if __name__ == "__main__":
    for case in c.make_cases():
        if not case.get("bench"):
            continue
        w, it = 30, 200
        b = wall(c.baseline, case, w, it)
        cand = wall(c.candidate, case, w, it)
        print(
            f"{case['name']:48s} base={b:9.2f}us cand={cand:9.2f}us "
            f"speedup={b / cand:5.2f}x"
        )
