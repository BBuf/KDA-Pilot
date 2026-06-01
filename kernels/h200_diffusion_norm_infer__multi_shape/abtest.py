"""Same-process A/B: time baseline vs candidate back-to-back per shape on the
same GPU, eliminating cross-process GPU-state drift. Diagnostic only."""
import importlib.util, pathlib, statistics, time, torch

KD = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("c", KD / "tests" / "test_correctness.py")
c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c)


def wall(fn, case, warmup, iters):
    for _ in range(warmup): fn(case)
    torch.cuda.synchronize()
    s = []
    for _ in range(iters):
        t0 = time.perf_counter(); fn(case); torch.cuda.synchronize()
        s.append((time.perf_counter() - t0) * 1e6)
    return statistics.median(s)


for case in c.make_cases():
    if case["group"] != "perf":
        continue
    w, it = 30, 200
    b = wall(c.baseline, case, w, it)
    cand = wall(c.candidate, case, w, it)
    print(f"{case['name']:32s} base={b:8.2f}us cand={cand:8.2f}us  speedup={b/cand:5.2f}x")
