#!/usr/bin/env python3
"""End-to-end validation of the INTEGRATED kda_kernels overlay for the two
diffusion rotary-embedding swap functions on H200.

Unlike tests/test_correctness.py (which loads the task src/ directly), this
exercises the *promoted* production path the way patches/sglang_kda_kernels.patch
activates it:

    capture baselines -> kda_kernels.install() -> assert BOTH SGLang module
    attributes were swapped to the kda dispatcher -> call the swapped symbols on
    the 6 captured production shapes -> confirm each routes to the h200 impl
    ("cuda"), matches the captured SGLang baseline (atol=rtol=1e-2), is NaN/Inf
    free, returns a NEW tensor of the input dtype (functional contract), and is
    faster than the captured SGLang baseline. Reports the geomean speedup.

Run (inside a container, on an idle H200):

    PYTHONPATH=<kernel-pilot-root>:<sglang>/python CUDA_VISIBLE_DEVICES=<idle> \
        python validate_overlay.py

<kernel-pilot-root> must be the directory containing the kda_kernels/ package
under test; <sglang>/python must be the source checkout that carries
sglang.jit_kernel.diffusion.
"""
from __future__ import annotations

import math
import statistics
import sys

import torch

ATOL, RTOL = 1e-2, 1e-2
KEY_STD = "sglang.jit_kernel.diffusion.triton.rotary:apply_rotary_embedding"
KEY_LTX2 = "sglang.jit_kernel.diffusion.triton.ltx2_rotary:apply_ltx2_split_rotary_emb"

# The 6 deduplicated production shapes (identical construction to
# tests/test_correctness.py: standard seed 0, then LTX-2 seeds 1..5).
LTX2_SPECS = [
    ("ltx2__B1_S1536_H32_half64__bf16", 1, 1536, 32, 64),
    ("ltx2__B1_S126_H32_half32__bf16", 1, 126, 32, 32),
    ("ltx2__B1_S1536_H32_half32__bf16", 1, 1536, 32, 32),
    ("ltx2__B1_S6144_H32_half64__bf16", 1, 6144, 32, 64),
    ("ltx2__B1_S6144_H32_half32__bf16", 1, 6144, 32, 32),
]


def build_standard(B, T, H, D, *, seed):
    g = torch.Generator(device="cuda").manual_seed(seed)
    x = torch.randn(B, T, H, D, device="cuda", dtype=torch.float32, generator=g).to(torch.bfloat16)
    angles = torch.randn(T, D // 2, device="cuda", dtype=torch.float32, generator=g)
    cos = torch.cos(angles).contiguous()
    sin = torch.sin(angles).contiguous()
    return (x, cos, sin, False)


def build_ltx2(B, S, H, half, *, seed):
    g = torch.Generator(device="cuda").manual_seed(seed)
    D = half * 2
    x = (torch.randn(B, S, H * D, device="cuda", dtype=torch.float32, generator=g) * 1e-1).to(torch.bfloat16)
    angles = torch.randn(B, S, H, half, device="cuda", dtype=torch.float32, generator=g)
    cos = torch.cos(angles).to(torch.bfloat16).contiguous().permute(0, 2, 1, 3)  # (B,H,S,half) non-contig
    sin = torch.sin(angles).to(torch.bfloat16).contiguous().permute(0, 2, 1, 3)
    return (x, cos, sin)


def make_cases():
    cases = [("hunyuanvideo__std__B1_T27030_H24_D128__bf16", "standard", build_standard(1, 27030, 24, 128, seed=0))]
    for i, (name, B, S, H, half) in enumerate(LTX2_SPECS, start=1):
        cases.append((name, "ltx2", build_ltx2(B, S, H, half, seed=i)))
    return cases


def median_us(fn, args, warmup=25, iters=100):
    for _ in range(warmup):
        fn(*args)
    torch.cuda.synchronize()
    s = torch.cuda.Event(enable_timing=True)
    e = torch.cuda.Event(enable_timing=True)
    xs = []
    for _ in range(iters):
        s.record()
        fn(*args)
        e.record()
        torch.cuda.synchronize()
        xs.append(s.elapsed_time(e) * 1000.0)  # ms -> us
    return statistics.median(sorted(xs))


def main() -> int:
    assert torch.cuda.is_available(), "CUDA required"
    print(f"device={torch.cuda.get_device_name(0)} capability={torch.cuda.get_device_capability(0)}")

    import sglang.jit_kernel.diffusion.triton.rotary as R
    import sglang.jit_kernel.diffusion.triton.ltx2_rotary as L

    base_std = R.apply_rotary_embedding          # capture BEFORE install
    base_ltx2 = L.apply_ltx2_split_rotary_emb
    print(f"baseline std.__module__={getattr(base_std, '__module__', '?')} ltx2.__module__={getattr(base_ltx2, '__module__', '?')}")

    import kda_kernels
    results = kda_kernels.install()              # == what the patch runs on import
    by_key = {r[0]: r for r in results}
    print(f"install std  -> {by_key.get(KEY_STD)}")
    print(f"install ltx2 -> {by_key.get(KEY_LTX2)}")
    assert by_key.get(KEY_STD) and by_key[KEY_STD][2] == "swapped", f"standard NOT swapped: {by_key.get(KEY_STD)}"
    assert by_key.get(KEY_LTX2) and by_key[KEY_LTX2][2] == "swapped", f"ltx2 NOT swapped: {by_key.get(KEY_LTX2)}"
    assert KEY_STD in kda_kernels.status() and KEY_LTX2 in kda_kernels.status(), "status() missing keys"

    swapped_std = R.apply_rotary_embedding       # AFTER install
    swapped_ltx2 = L.apply_ltx2_split_rotary_emb
    assert swapped_std is not base_std and swapped_ltx2 is not base_ltx2, "module attribute(s) not swapped"
    for nm, fn in (("std", swapped_std), ("ltx2", swapped_ltx2)):
        assert "kda_kernels" in (getattr(fn, "__module__", "") or ""), f"{nm} not from kda_kernels: {fn.__module__}"
    print(f"swapped std.__module__={swapped_std.__module__} ltx2.__module__={swapped_ltx2.__module__}")

    import kda_kernels.diffusion.rotary_embedding._impls.h200.wrapper as h200w  # dispatch telemetry

    fails = 0
    speedups = []
    print()
    print(f"{'shape':40s} {'api':8s} {'route':8s} {'newobj':6s} {'close':6s} {'nan':5s} "
          f"{'maxd':>10s} {'base_us':>9s} {'swap_us':>9s} {'speedup':>9s}")
    for name, api, args in make_cases():
        swapped = swapped_std if api == "standard" else swapped_ltx2
        base = base_std if api == "standard" else base_ltx2

        ref = base(*args)
        h200w._LAST_DISPATCH[api] = None
        out = swapped(*args)
        route = h200w._LAST_DISPATCH[api]
        x = args[0]
        newobj = (out is not x) and (out.dtype == x.dtype) and (out.shape == x.shape)
        maxd = (out.float() - ref.float()).abs().max().item()
        nan = bool(torch.isnan(out).any() or torch.isinf(out).any())
        try:
            torch.testing.assert_close(out.float(), ref.float(), atol=ATOL, rtol=RTOL)
            close = True
        except AssertionError as ex:
            close = False
            print(f"  CLOSE_FAIL {name}: {str(ex).splitlines()[0]}")
        if not (newobj and route == "cuda" and close and not nan):
            fails += 1

        tb = median_us(base, args)
        ts = median_us(swapped, args)
        sp = tb / ts if ts > 0 else float("nan")
        speedups.append(sp)
        print(f"{name:40s} {api:8s} {route or '?':8s} {str(newobj):6s} {str(close):6s} {str(nan):5s} "
              f"{maxd:10.4f} {tb:9.2f} {ts:9.2f} {sp:8.4f}x")

    pos = [x for x in speedups if math.isfinite(x) and x > 0]
    gm = math.exp(sum(math.log(x) for x in pos) / len(pos)) if pos else float("nan")
    print()
    print(f"GEOMEAN speedup (integrated install() overlay vs SGLang baseline) = {gm:.4f}x over {len(pos)} shapes")
    print(f"CORRECTNESS: {'PASS' if fails == 0 else f'FAIL ({fails}/{len(speedups)} shapes)'}")
    print(f"OVERALL: {'PASS' if fails == 0 and gm > 1.0 else 'CHECK'}")
    return 0 if (fails == 0 and gm > 1.0) else 1


if __name__ == "__main__":
    sys.exit(main())
