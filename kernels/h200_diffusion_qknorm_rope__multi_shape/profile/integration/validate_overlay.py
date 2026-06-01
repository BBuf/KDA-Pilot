#!/usr/bin/env python3
"""End-to-end validation of the INTEGRATED kda_kernels overlay for
fused_inplace_qknorm_rope on H200.

Unlike tests/test_correctness.py (which loads src/ directly), this exercises the
*promoted* production path the way `patches/sglang_kda_kernels.patch` activates
it:

    capture baseline -> kda_kernels.install() -> assert the SGLang module
    attribute was swapped to the kda dispatcher -> call the swapped symbol on the
    9 captured shapes -> confirm it routes to the h200 impl, matches the oracle
    (sglang fused_inplace_qknorm + flashinfer RoPE, ATOL=8e-2/RTOL=1e-2), returns
    None (in place), and is faster than the captured SGLang baseline.

Run (inside the container, on an idle H200):

    PYTHONPATH=<kernel-pilot-root>:<sglang>/python CUDA_VISIBLE_DEVICES=<idle> \
        python validate_overlay.py

`<kernel-pilot-root>` must be the directory that contains the `kda_kernels/`
package (so `import kda_kernels` resolves the overlay under test).
"""
from __future__ import annotations

import math
import statistics
import sys

import torch

ATOL, RTOL, ROPE_BASE = 8e-2, 1e-2, 10000.0
KEY = "sglang.jit_kernel.diffusion.qknorm_rope:fused_inplace_qknorm_rope"

# (name, tokens, num_heads, head_dim, rope_dim, is_neox, eps) -- the 9 captured shapes
CAPTURED = [
    ("qwen__T4096_H24", 4096, 24, 128, 128, False, 1e-6),
    ("qwen__T19_H24", 19, 24, 128, 128, False, 1e-6),
    ("qwen__T47_H24", 47, 24, 128, 128, False, 1e-6),
    ("qwen_edit__T8424_H24", 8424, 24, 128, 128, False, 1e-6),
    ("qwen_edit__T195_H24", 195, 24, 128, 128, False, 1e-6),
    ("qwen_edit__T189_H24", 189, 24, 128, 128, False, 1e-6),
    ("zimage__T4096_H30", 4096, 30, 128, 128, False, 1e-5),
    ("zimage__T32_H30", 32, 30, 128, 128, False, 1e-5),
    ("zimage__T4128_H30", 4128, 30, 128, 128, False, 1e-5),
]


def make_cos_sin(rope_dim, max_pos, base=ROPE_BASE):
    inv = 1.0 / (base ** (torch.arange(0, rope_dim, 2, dtype=torch.float32, device="cuda") / rope_dim))
    t = torch.arange(max_pos, dtype=torch.float32, device="cuda")
    f = torch.einsum("i,j->ij", t, inv)
    return torch.cat((f.cos(), f.sin()), dim=-1)


def oracle(q, k, qw, kw, cache, pos, is_neox):
    from flashinfer.rope import apply_rope_with_cos_sin_cache_inplace
    from sglang.jit_kernel.norm import fused_inplace_qknorm

    fused_inplace_qknorm(q, k, qw, kw)
    apply_rope_with_cos_sin_cache_inplace(
        positions=pos.long(),
        query=q.view(q.shape[0], -1),
        key=k.view(k.shape[0], -1),
        head_size=q.shape[-1],
        cos_sin_cache=cache,
        is_neox=is_neox,
    )


def median_us(run, restore, warmup=25, iters=150):
    for _ in range(warmup):
        restore(); run()
    torch.cuda.synchronize()
    s = torch.cuda.Event(enable_timing=True)
    e = torch.cuda.Event(enable_timing=True)
    xs = []
    for _ in range(iters):
        restore(); torch.cuda.synchronize()
        s.record(); run(); e.record()
        torch.cuda.synchronize()
        xs.append(s.elapsed_time(e) * 1000.0)
    return statistics.median(sorted(xs))


def main() -> int:
    assert torch.cuda.is_available(), "CUDA required"
    print(f"device={torch.cuda.get_device_name(0)} capability={torch.cuda.get_device_capability(0)}")

    import sglang.jit_kernel.diffusion.qknorm_rope as qr
    baseline = qr.fused_inplace_qknorm_rope                      # capture BEFORE install
    print(f"baseline.__module__={getattr(baseline, '__module__', '?')}")

    import kda_kernels
    results = kda_kernels.install()                             # == what the patch runs on import
    res = [r for r in results if r[0] == KEY]
    print(f"install result for qknorm_rope: {res}")
    assert res and res[0][2] == "swapped", f"qknorm_rope NOT swapped: {res}"
    assert KEY in kda_kernels.status(), f"status() missing key: {kda_kernels.status()}"

    swapped = qr.fused_inplace_qknorm_rope                       # AFTER install
    assert swapped is not baseline, "module attribute was not swapped"
    assert "kda_kernels" in (getattr(swapped, "__module__", "") or ""), swapped.__module__
    print(f"swapped.__module__={swapped.__module__}")

    import kda_kernels.diffusion.qknorm_rope._impls.h200.wrapper as h200w  # dispatch telemetry

    fails = 0
    speedups = []
    print()
    print(f"{'shape':24s} {'ret_none':8s} {'path':8s} {'close':6s} {'nan':5s} "
          f"{'maxd_q':>9s} {'maxd_k':>9s} {'base_us':>9s} {'swap_us':>9s} {'speedup':>9s}")
    for name, T, H, D, rope, neox, eps in CAPTURED:
        g = torch.Generator(device="cuda").manual_seed(0)
        q0 = torch.randn(T, H, D, device="cuda", dtype=torch.bfloat16, generator=g)
        k0 = torch.randn(T, H, D, device="cuda", dtype=torch.bfloat16, generator=g)
        qw = torch.randn(D, device="cuda", dtype=torch.bfloat16, generator=g)
        kw = torch.randn(D, device="cuda", dtype=torch.bfloat16, generator=g)
        pos = torch.randint(0, T, (T,), device="cuda", dtype=torch.int64)
        cache = make_cos_sin(rope, T)

        qref, kref = q0.clone(), k0.clone()
        oracle(qref, kref, qw, kw, cache, pos, neox)

        qc, kc = q0.clone(), k0.clone()
        ret = swapped(qc, kc, qw, kw, cache, pos, is_neox=neox, eps=eps, rope_dim=rope)
        path = h200w.last_dispatch_path()
        maxd_q = (qref.float() - qc.float()).abs().max().item()
        maxd_k = (kref.float() - kc.float()).abs().max().item()
        nan = bool(torch.isnan(qc).any() or torch.isnan(kc).any()
                   or torch.isinf(qc).any() or torch.isinf(kc).any())
        try:
            torch.testing.assert_close(qc.float(), qref.float(), atol=ATOL, rtol=RTOL)
            torch.testing.assert_close(kc.float(), kref.float(), atol=ATOL, rtol=RTOL)
            close = True
        except AssertionError as ex:
            close = False
            print(f"  CLOSE_FAIL {name}: {ex}")
        if not ((ret is None) and (path == "cuda") and close and (not nan)):
            fails += 1

        q, k = q0.clone(), k0.clone()

        def restore():
            q.copy_(q0); k.copy_(k0)

        tb = median_us(lambda: baseline(q, k, qw, kw, cache, pos, is_neox=neox, eps=eps, rope_dim=rope), restore)
        ts = median_us(lambda: swapped(q, k, qw, kw, cache, pos, is_neox=neox, eps=eps, rope_dim=rope), restore)
        sp = tb / ts if ts > 0 else float("nan")
        speedups.append(sp)
        print(f"{name:24s} {str(ret is None):8s} {path or '?':8s} {str(close):6s} {str(nan):5s} "
              f"{maxd_q:9.4f} {maxd_k:9.4f} {tb:9.2f} {ts:9.2f} {sp:8.4f}x")

    pos_sp = [x for x in speedups if math.isfinite(x) and x > 0]
    gm = math.exp(sum(math.log(x) for x in pos_sp) / len(pos_sp)) if pos_sp else float("nan")
    print()
    print(f"GEOMEAN speedup (integrated overlay vs SGLang baseline) = {gm:.4f}x over {len(pos_sp)} shapes")
    print(f"CORRECTNESS: {'PASS' if fails == 0 else f'FAIL ({fails}/{len(CAPTURED)} shapes)'}")
    print(f"OVERALL: {'PASS' if fails == 0 and gm > 1.0 else 'CHECK'}")
    return 0 if fails == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
