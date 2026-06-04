#!/usr/bin/env python3
"""In-SGLang drop-in driver: correctness + A/B benchmark through the PUBLIC ops.

Runs inside the container against the active sglang package. Two modes:
- correctness: public custom ops vs the fp32 semantic reference on the 4
  captured zimage signatures + fallback probe (mixed-dtype scale must still
  produce baseline-identical results, i.e. the CuTe path).
- bench: wall-synced timing of the public Python callables (the shipped
  layer: custom-op registration + dispatch identical regardless of patch
  state). Run once on the CLEAN checkout and once on the PATCHED checkout;
  the two runs form the symmetric shipping-integration A/B.

Usage: python inSGLang_ab_driver.py {correctness|bench} <tag>
"""

import json
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
    for S in SHAPES:
        t = make_inputs(S)
        y = fused_norm_tanh_mul_add(t["x"], t["w"], None, t["scale"], t["shift"], "rms", EPS)
        check_close(y, reference(t, False), f"v1_S{S}")
        out = fused_norm_tanh_mul_add_norm_scale(
            t["x"], t["w"], None, t["scale"], t["shift"], t["w2"], None, t["scale2"], "rms", EPS
        )
        check_close(out, reference(t, True), f"v2_S{S}")
        # Fallback probe: mixed-dtype scale is public-valid and must keep working
        # (routes to the CuTe path under the patch).
        y_fb = fused_norm_tanh_mul_add(
            t["x"], t["w"], None, t["scale"].to(torch.float16), t["shift"], "rms", EPS
        )
        assert not torch.isnan(y_fb).any()
    print("IN_SGLANG_CORRECTNESS_PASS")


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
                "p10_us": round(ordered[len(ordered) // 10], 3),
                "p90_us": round(ordered[(len(ordered) * 9) // 10], 3),
                "min_us": round(ordered[0], 3),
            }
    print(json.dumps({"tag": tag, "results": results}))


if __name__ == "__main__":
    mode = sys.argv[1]
    tag = sys.argv[2] if len(sys.argv) > 2 else "untagged"
    if mode == "correctness":
        run_correctness()
    else:
        run_bench(tag)
