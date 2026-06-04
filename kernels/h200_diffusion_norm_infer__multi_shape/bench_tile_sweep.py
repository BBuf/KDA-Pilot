"""Bounded sweep for the multi-row tiled RMSNorm kernel (huge-M shapes).

Compares, per config, against BOTH the copied Triton baseline and the current
warp kernel (normv5) on the same idle-gated GPU, interleaved per sample:
- stream-saturated device rate (one event pair around 32 back-to-back enqueues)
- per-call wall (perf_counter + synchronize)

Configs are template instantiations of src/rms_norm_d128_tile16.cuh:
(rows_per_cta, threads, stream_cache). Diagnostic tool for the loop; ledger
rows are produced by benchmark_symmetric.py once a winner is integrated.

Usage (inside the container, from the synced task folder):
    REMOTE_GPU_ID=0 CUDA_VISIBLE_DEVICES=0 python3 bench_tile_sweep.py \
        [--shapes 648720,650040] [--iters 100] [--configs 16x128,16x256,8x128,32x256]
"""

from __future__ import annotations

import argparse
import os
import pathlib
import statistics
import sys
import time

TASK_DIR = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(TASK_DIR))
sys.path.insert(0, str(TASK_DIR / "src"))

import torch  # noqa: E402

from sglang.jit_kernel.utils import load_jit, make_cpp_args  # noqa: E402

from baseline.triton_norm_baseline import baseline_one_pass_rms_norm  # noqa: E402
import norm_dispatch  # noqa: E402

_TILE_CUH = str(TASK_DIR / "src" / "rms_norm_d128_tile16.cuh")
BATCH = 32


def tile_module(rows: int, threads: int, stream: bool, dtype: torch.dtype):
    targs = make_cpp_args(128, rows, threads, stream, False, dtype)
    return load_jit(
        f"kda_rms_tile_r{rows}_t{threads}_s{int(stream)}",
        *targs,
        cuda_files=[_TILE_CUH],
        cuda_wrappers=[("rms_norm_tile", f"RmsNormTileKernel<{targs}>::run")],
    )


def device_batch(fn):
    ev_a = torch.cuda.Event(enable_timing=True)
    ev_b = torch.cuda.Event(enable_timing=True)
    ev_a.record()
    for _ in range(BATCH):
        fn()
    ev_b.record()
    torch.cuda.synchronize()
    return ev_a.elapsed_time(ev_b) * 1e3 / BATCH


def wall_call(fn):
    t0 = time.perf_counter()
    fn()
    torch.cuda.synchronize()
    return (time.perf_counter() - t0) * 1e6


def measure(legs: dict, iters: int):
    """Interleaved measurement across all legs, order rotated per sample."""
    names = list(legs)
    for fn in legs.values():
        for _ in range(20):
            fn()
    torch.cuda.synchronize()
    dev = {n: [] for n in names}
    wall = {n: [] for n in names}
    n_dev = max(10, iters // 10)
    for i in range(n_dev):
        for n in names[i % len(names):] + names[:i % len(names)]:
            dev[n].append(device_batch(legs[n]))
    for i in range(iters):
        for n in names[i % len(names):] + names[:i % len(names)]:
            wall[n].append(wall_call(legs[n]))
    return {n: (statistics.median(dev[n]), statistics.median(wall[n])) for n in names}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--shapes", default="648720,650040")
    ap.add_argument("--iters", type=int, default=100)
    ap.add_argument("--configs", default="16x128,16x256,8x128,32x256",
                    help="comma list of RxT[s] (s suffix = streaming cache hints)")
    args = ap.parse_args()

    remote_gpu = os.environ.get("REMOTE_GPU_ID", "")
    first = os.environ.get("CUDA_VISIBLE_DEVICES", "").split(",")[0].strip()
    if not remote_gpu or remote_gpu != first:
        sys.exit("GPU pin mismatch: REMOTE_GPU_ID must equal first CUDA_VISIBLE_DEVICES entry")

    dtype = torch.bfloat16
    torch.manual_seed(0)
    configs = []
    for tok in args.configs.split(","):
        tok = tok.strip()
        stream = tok.endswith("s")
        r, t = tok.rstrip("s").split("x")
        configs.append((int(r), int(t), stream))

    mods = {}
    for r, t, s in configs:
        key = f"tile{r}x{t}{'s' if s else ''}"
        print(f"[build] {key} ...", flush=True)
        mods[key] = tile_module(r, t, s, dtype)

    warp_mod = norm_dispatch._rms_module(128, dtype, False)

    for m_str in args.shapes.split(","):
        m = int(m_str.strip())
        x = torch.randn(m, 128, device="cuda", dtype=dtype)
        w = torch.randn(128, device="cuda", dtype=dtype)
        ref = baseline_one_pass_rms_norm(x, w, 1e-6)

        legs = {}
        legs["triton_base"] = lambda x=x, w=w: baseline_one_pass_rms_norm(x, w, 1e-6)

        def warp_fn(x=x, w=w):
            y = torch.empty_like(x)
            warp_mod.rms_norm(x, w, y, 1e-6)
            return y

        legs["warp_normv5"] = warp_fn

        for key, mod in mods.items():
            def tile_fn(x=x, w=w, mod=mod):
                y = torch.empty_like(x)
                mod.rms_norm_tile(x, w, y, 1e-6)
                return y
            out = tile_fn()
            if torch.isnan(out).any() or torch.isinf(out).any():
                sys.exit(f"{key}: NaN/Inf at M={m}")
            torch.testing.assert_close(out, ref, atol=5e-2, rtol=5e-2)
            exact = torch.equal(out, ref)
            print(f"[correct] {key} M={m}: assert_close OK (bitwise-equal={exact})")
            legs[key] = tile_fn

        res = measure(legs, args.iters)
        base_dev, base_wall = res["triton_base"]
        print(f"\n== M={m} (D=128 bf16; medians; dev = stream-saturated rate) ==")
        for n, (d, wl) in res.items():
            print(f"  {n:14s} dev={d:8.2f}us (x{base_dev/d:5.3f})  wall={wl:8.2f}us (x{base_wall/wl:5.3f})")
        print()
        del x, w, ref, legs
        torch.cuda.empty_cache()


if __name__ == "__main__":
    main()
