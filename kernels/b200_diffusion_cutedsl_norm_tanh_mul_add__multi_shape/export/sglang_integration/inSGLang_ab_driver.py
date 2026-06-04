#!/usr/bin/env python3
"""In-SGLang drop-in driver: correctness + A/B benchmark through the PUBLIC ops.

Runs inside the container against the active sglang package, with the drop-in
patch APPLIED (the routing module must be importable). Two modes:
- correctness: public custom ops vs the fp32 semantic reference on the 4
  captured zimage signatures, plus the gate-verified fallback probe — the
  mixed-dtype scale case must be rejected by ``native_supported(...)`` AND its
  public-op output (CuTe fallback branch) must match the reference within the
  production tolerances.
- bench: wall-synced timing of the public Python callables. The promotion
  arbiter is DISPATCH-SYMMETRIC: run once with the native routes disabled
  (``SGLANG_NATIVE_NORM_TANH_V1=0 SGLANG_NATIVE_NORM_TANH_V2=0`` -> CuTe route)
  and once with them enabled (native route), both in the SAME patched checkout,
  so wrapper, custom-op registration, and the dispatch branch are identical on
  both sides. Full stats are also dumped to export/arbiter_runs/<tag>.json.

Usage: python inSGLang_ab_driver.py {correctness|bench} <tag>
"""

import json
import os
import statistics
import sys
import time

import torch

from sglang.jit_kernel.diffusion.cutedsl.norm_tanh_mul_add_norm_scale import (
    fused_norm_tanh_mul_add,
    fused_norm_tanh_mul_add_norm_scale,
)

SHAPES = [4096, 4128]
D = 3840
EPS = 1e-5
WARMUP, ITERS = 50, 200


def make_inputs(S: int, seed: int = 7):
    g = torch.Generator(device="cuda")
    g.manual_seed(seed)

    def rand(shape, offset=0.0, sc=1.0):
        t = torch.randn(shape, generator=g, device="cuda", dtype=torch.float32)
        return (t * sc + offset).to(torch.bfloat16).contiguous()

    return {
        "x": rand((1, S, D)),
        "w": rand((D,), offset=1.0, sc=0.2),
        "scale": rand((1, 1, D)),
        "shift": rand((1, S, D)),
        "w2": rand((D,), offset=1.0, sc=0.2),
        "scale2": rand((1, 1, D)),
    }


def reference(t, second: bool):
    xf = t["x"].float()
    n = xf * torch.rsqrt(xf.pow(2).mean(-1, keepdim=True) + EPS) * t["w"].float()
    n = n.to(torch.bfloat16).float()
    y = (n * torch.tanh(t["scale"].float()) + t["shift"].float()).to(torch.bfloat16)
    if not second:
        return y
    yf = y.float()
    n2 = yf * torch.rsqrt(yf.pow(2).mean(-1, keepdim=True) + EPS) * t["w2"].float()
    n2 = n2.to(torch.bfloat16).float()
    y2 = (n2 * (1.0 + t["scale2"].float())).to(torch.bfloat16)
    return y, y2


def check_close(a, b, label):
    a_t = a if isinstance(a, tuple) else (a,)
    b_t = b if isinstance(b, tuple) else (b,)
    for i, (x, y) in enumerate(zip(a_t, b_t)):
        torch.testing.assert_close(
            x.float(), y.float(), atol=5e-2, rtol=5e-2,
            msg=lambda m, l=label, j=i: f"{l}[{j}]: {m}",
        )


def run_correctness() -> None:
    # Runs against the PATCHED checkout, so the routing module must be importable.
    from sglang.jit_kernel.diffusion.norm_tanh_modulation import native_supported

    for S in SHAPES:
        t = make_inputs(S)
        y = fused_norm_tanh_mul_add(t["x"], t["w"], None, t["scale"], t["shift"], "rms", EPS)
        check_close(y, reference(t, False), f"v1_S{S}")
        out = fused_norm_tanh_mul_add_norm_scale(
            t["x"], t["w"], None, t["scale"], t["shift"], t["w2"], None, t["scale2"], "rms", EPS
        )
        check_close(out, reference(t, True), f"v2_S{S}")
        # Fallback probe: mixed-dtype scale is public-valid but native-ineligible.
        # Verify the gate rejects it, the public op still answers through the
        # CuTe fallback branch, and the output matches the reference within the
        # production tolerance (not merely NaN-free).
        scale_fp16 = t["scale"].to(torch.float16)
        assert native_supported(
            t["x"], t["w"], None, scale_fp16, t["shift"], None, None, None, "rms"
        ) is False, "mixed-dtype scale must be rejected by the native gate"
        y_fb = fused_norm_tanh_mul_add(
            t["x"], t["w"], None, scale_fp16, t["shift"], "rms", EPS
        )
        t_fb = dict(t)
        t_fb["scale"] = scale_fp16
        check_close(y_fb, reference(t_fb, False), f"fallback_mixed_dtype_S{S}")
    print("IN_SGLANG_CORRECTNESS_PASS (incl. gate-verified fallback vs reference)")


def run_bench(tag: str) -> None:
    results = {}
    for S in SHAPES:
        t = make_inputs(S)
        for name, fn in (
            ("v1", lambda: fused_norm_tanh_mul_add(
                t["x"], t["w"], None, t["scale"], t["shift"], "rms", EPS)),
            ("v2", lambda: fused_norm_tanh_mul_add_norm_scale(
                t["x"], t["w"], None, t["scale"], t["shift"], t["w2"], None, t["scale2"], "rms", EPS)),
        ):
            for _ in range(WARMUP):
                fn()
            torch.cuda.synchronize()
            samples = []
            for _ in range(ITERS):
                t0 = time.perf_counter()
                fn()
                torch.cuda.synchronize()
                samples.append((time.perf_counter() - t0) * 1e6)
            ordered = sorted(samples)
            results[f"{name}_S{S}"] = {
                "median_us": round(statistics.median(ordered), 3),
                "mean_us": round(statistics.mean(ordered), 3),
                "std_us": round(statistics.pstdev(ordered), 3),
                "p10_us": round(ordered[len(ordered) // 10], 3),
                "p90_us": round(ordered[(len(ordered) * 9) // 10], 3),
                "min_us": round(ordered[0], 3),
            }
    payload = {
        "tag": tag,
        "warmup": WARMUP,
        "iters": ITERS,
        "cuda_visible_devices": os.environ.get("CUDA_VISIBLE_DEVICES", ""),
        "results": results,
    }
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "arbiter_runs")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, f"{tag}.json"), "w") as f:
        json.dump(payload, f, indent=1)
    print(json.dumps(payload))


if __name__ == "__main__":
    mode = sys.argv[1]
    tag = sys.argv[2] if len(sys.argv) > 2 else "untagged"
    if mode == "correctness":
        run_correctness()
    else:
        run_bench(tag)
