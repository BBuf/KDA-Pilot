"""SELECTION SWEEP for wave-2 kernel variants — diagnostic, device-level.

Builds every wave-2 variant export, gates each on bitwise equality with the
in-module anchor (the variants change scheduling/launch shape, not arithmetic
order, so outputs must be torch.equal) plus allclose vs the vendored baseline,
then times each variant against the anchor with alternating interleaved
CUDA-event medians at the captured S=4096 production shape.

The winner is then promoted through the FULL admissible pipeline
(tests/test_correctness.py suite + benchmark.py interleaved A/B); numbers
printed here are selection evidence only.
"""

import statistics
import sys
from pathlib import Path

import torch

KERNEL_DIR = Path(__file__).resolve().parent
if str(KERNEL_DIR) not in sys.path:
    sys.path.insert(0, str(KERNEL_DIR))

import baseline as vendored  # noqa: E402

CUH = KERNEL_DIR / "src" / "norm_tanh_mul_add_candidate.cuh"
SEQ, D, EPS = 4096, 3840, 1e-5

SINGLE_VARIANTS = {
    "s_base": (False, False, False),
    "s_tp": (True, False, False),
    "s_ts": (False, True, False),
    "s_tp_ts": (True, True, False),
}
DUAL_VARIANTS = {
    "d_base": (False, False, False),
    "d_lb": (False, False, True),
    "d_tp": (True, False, False),
    "d_ts": (False, True, False),
    "d_lb_tp": (True, False, True),
    "d_lb_tp_ts": (True, True, True),
}


def _module():
    from sglang.jit_kernel.utils import load_jit

    wrappers = []
    for name, (tp, ts, lb) in SINGLE_VARIANTS.items():
        wrappers.append((name, f"NormTanhMulAddSingleV2<bf16_t, {str(tp).lower()}, "
                               f"{str(ts).lower()}, {str(lb).lower()}>::run"))
    for name, (tp, ts, lb) in DUAL_VARIANTS.items():
        wrappers.append((name, f"NormTanhMulAddDualV2<bf16_t, {str(tp).lower()}, "
                               f"{str(ts).lower()}, {str(lb).lower()}>::run"))
    return load_jit("kda_h200_norm_tanh_mul_add_wave2",
                    cuda_files=[str(CUH)], cuda_wrappers=wrappers)


def _interleaved_gpu_us(fa, fb, warmup=20, iters=100):
    for _ in range(warmup):
        fa()
        fb()
    torch.cuda.synchronize()
    med = {}
    evs = {"a": [], "b": []}
    for i in range(iters):
        order = (("a", fa), ("b", fb)) if i % 2 == 0 else (("b", fb), ("a", fa))
        for tag, fn in order:
            e0 = torch.cuda.Event(enable_timing=True)
            e1 = torch.cuda.Event(enable_timing=True)
            e0.record()
            fn()
            e1.record()
            torch.cuda.synchronize()
            evs[tag].append(e0.elapsed_time(e1) * 1e3)
    med["a"] = statistics.median(evs["a"])
    med["b"] = statistics.median(evs["b"])
    return med


def main() -> int:
    torch.manual_seed(20260604)
    dt = torch.bfloat16
    mod = _module()

    x = torch.randn(SEQ, D, device="cuda", dtype=dt)
    w = torch.randn(D, device="cuda", dtype=dt)
    sc = torch.randn(D, device="cuda", dtype=dt)
    sh = torch.randn(SEQ, D, device="cuda", dtype=dt)
    w2 = torch.randn(D, device="cuda", dtype=dt)
    sc2 = torch.randn(D, device="cuda", dtype=dt)
    tanh_buf = torch.empty(D, device="cuda", dtype=torch.float32)

    # Vendored-baseline sanity references (3-D public signatures).
    base_y = vendored.fused_norm_tanh_mul_add(
        x.view(1, SEQ, D), w, None, sc.view(1, 1, D), sh.view(1, SEQ, D), "rms", EPS)
    base_yd, base_y2d = vendored.fused_norm_tanh_mul_add_norm_scale(
        x.view(1, SEQ, D), w, None, sc.view(1, 1, D), sh.view(1, SEQ, D),
        w2, None, sc2.view(1, 1, D), "rms", EPS)

    def run_single(name):
        y = torch.empty_like(x)
        getattr(mod, name)(x, w, sc, sh, tanh_buf, y, EPS)
        return y

    def run_dual(name):
        y = torch.empty_like(x)
        y2 = torch.empty_like(x)
        getattr(mod, name)(x, w, sc, sh, w2, sc2, tanh_buf, y, y2, EPS)
        return y, y2

    print("=== correctness gates ===")
    anchor_y = run_single("s_base")
    torch.cuda.synchronize()
    assert torch.allclose(anchor_y.float(), base_y.view(SEQ, D).float(), atol=5e-2, rtol=5e-2)
    for name in SINGLE_VARIANTS:
        y = run_single(name)
        torch.cuda.synchronize()
        ok = torch.equal(y, anchor_y)
        print(f"{name:12s} bitwise-vs-anchor={'OK' if ok else 'FAIL'}")
        assert ok, name
    anchor_yd, anchor_y2d = run_dual("d_base")
    torch.cuda.synchronize()
    assert torch.allclose(anchor_yd.float(), base_yd.view(SEQ, D).float(), atol=5e-2, rtol=5e-2)
    assert torch.allclose(anchor_y2d.float(), base_y2d.view(SEQ, D).float(), atol=5e-2, rtol=5e-2)
    for name in DUAL_VARIANTS:
        yd, y2d = run_dual(name)
        torch.cuda.synchronize()
        ok = torch.equal(yd, anchor_yd) and torch.equal(y2d, anchor_y2d)
        print(f"{name:12s} bitwise-vs-anchor={'OK' if ok else 'FAIL'}")
        assert ok, name

    print("=== interleaved device timing vs anchor (S=4096) ===")
    for name in SINGLE_VARIANTS:
        if name == "s_base":
            continue
        med = _interleaved_gpu_us(lambda: run_single("s_base"), lambda n=name: run_single(n))
        print(f"{name:12s} anchor={med['a']:8.3f}us variant={med['b']:8.3f}us "
              f"speedup={med['a'] / med['b']:.4f}x")
    for name in DUAL_VARIANTS:
        if name == "d_base":
            continue
        med = _interleaved_gpu_us(lambda: run_dual("d_base"), lambda n=name: run_dual(n))
        print(f"{name:12s} anchor={med['a']:8.3f}us variant={med['b']:8.3f}us "
              f"speedup={med['a'] / med['b']:.4f}x")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
