#!/usr/bin/env python3
"""In-place-aware benchmark for ``h200_diffusion_qknorm_rope__multi_shape``.

Times the SGLang fused baseline (``sglang.jit_kernel.diffusion.qknorm_rope.
fused_inplace_qknorm_rope``) against the optimized candidate (``src/register.py``
-> ``optimized_wrapper``) over the 9 captured production shapes on one idle H200.

The op is IN PLACE, so pristine ``q``/``k`` are restored (via ``copy_``, untimed)
before EVERY timed sample; timing uses CUDA events; the JIT/extension build is
warmed outside the timed region. Per-shape + geomean rows are appended to
``benchmark.csv`` with full provenance (candidate source hash, exact command,
host, GPU id/model, dispatch path, build flags, SGLang version/commit).

Run on the H200 box:
  PYTHONPATH=<repo>/python CUDA_VISIBLE_DEVICES=<idle> \
    KDA_HOST=ion8-h200 KDA_GPU_ID=<idle> python benchmark.py
"""

from __future__ import annotations

import csv
import hashlib
import importlib
import importlib.util
import math
import os
import statistics
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import torch

KERNEL_DIR = Path(__file__).resolve().parent
KERNEL_SLUG = "h200_diffusion_qknorm_rope__multi_shape"
ROPE_BASE = 10000.0
BUILD_FLAGS = "-O3 --use_fast_math -lineinfo"

# (name, tokens, num_heads, head_dim, rope_dim, is_neox, eps)
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


def _load_register():
    register_py = KERNEL_DIR / "src" / "register.py"
    spec = importlib.util.spec_from_file_location(f"kda_{KERNEL_SLUG}_register", register_py)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _wrapper():
    _load_register()  # ensures src/ on sys.path
    return importlib.import_module("wrapper")


def _make_cos_sin(rope_dim, max_pos, base=ROPE_BASE):
    inv = 1.0 / (base ** (torch.arange(0, rope_dim, 2, dtype=torch.float32, device="cuda") / rope_dim))
    t = torch.arange(max_pos, dtype=torch.float32, device="cuda")
    f = torch.einsum("i,j->ij", t, inv)
    return torch.cat((f.cos(), f.sin()), dim=-1)


def _src_hash():
    h = hashlib.sha256()
    for f in sorted((KERNEL_DIR / "src").rglob("*")):
        if f.is_file() and f.suffix in (".cu", ".cuh", ".cpp", ".h", ".py"):
            h.update(f.read_bytes())
    return h.hexdigest()[:16]


def _sglang_provenance():
    import sglang

    ver = getattr(sglang, "__version__", "?")
    commit = "?"
    try:
        repo = Path(sglang.__file__).resolve().parents[2]
        commit = subprocess.check_output(
            ["git", "-C", str(repo), "rev-parse", "--short", "HEAD"], text=True
        ).strip()
    except Exception:
        pass
    return ver, commit


def _time(run, restore, warmup=30, iters=200):
    for _ in range(warmup):
        restore(); run()
    torch.cuda.synchronize()
    s = torch.cuda.Event(enable_timing=True)
    e = torch.cuda.Event(enable_timing=True)
    samples = []
    for _ in range(iters):
        restore()  # untimed pristine restore
        torch.cuda.synchronize()
        s.record(); run(); e.record()
        torch.cuda.synchronize()
        samples.append(s.elapsed_time(e) * 1000.0)  # ms -> us
    return samples


def _summary(samples):
    o = sorted(samples)
    n = len(o)
    def pct(p):
        return o[min(n - 1, max(0, round((n - 1) * p)))]
    return {
        "median": statistics.median(o),
        "mean": statistics.mean(o),
        "std": statistics.pstdev(o) if n > 1 else 0.0,
        "min": o[0],
        "p10": pct(0.10),
        "p90": pct(0.90),
    }


def _geomean(values):
    v = [x for x in values if math.isfinite(x) and x > 0]
    return math.exp(sum(math.log(x) for x in v) / len(v)) if v else float("nan")


def main():
    assert torch.cuda.is_available(), "CUDA required"
    reg = _load_register()
    wrap = _wrapper()
    cand = reg.optimized_wrapper
    from sglang.jit_kernel.diffusion.qknorm_rope import fused_inplace_qknorm_rope as baseline

    host = os.environ.get("KDA_HOST", "?")
    gpu_id = os.environ.get("KDA_GPU_ID", os.environ.get("CUDA_VISIBLE_DEVICES", "?"))
    gpu_model = torch.cuda.get_device_name(0)
    src_hash = _src_hash()
    sg_ver, sg_commit = _sglang_provenance()
    container = os.environ.get("KDA_CONTAINER", "?")
    workdir = os.environ.get("KDA_REMOTE_WORKDIR", os.getcwd())
    gpu_state = os.environ.get("KDA_GPU_STATE_FILE", "profile/round0_ncu/gpu_state.md")
    # Exact ssh/docker/env/cwd command that produced this run (set by the driver script);
    # no placeholders -- this is the literal command, recorded for reproducibility.
    cmd = os.environ.get("KDA_CMD", "(KDA_CMD not set: pass the exact ssh/docker/env command)")
    now = datetime.now(timezone.utc).isoformat()
    print(f"host={host} gpu={gpu_id} model={gpu_model} src={src_hash} sglang={sg_ver}@{sg_commit}")
    print(f"container={container} workdir={workdir} gpu_state={gpu_state}")
    print(f"exact_cmd={cmd}")

    rows = []
    speedups = []
    for name, T, H, D, rope, neox, eps in CAPTURED:
        gen = torch.Generator(device="cuda").manual_seed(0)
        q0 = torch.randn(T, H, D, device="cuda", dtype=torch.bfloat16, generator=gen)
        k0 = torch.randn(T, H, D, device="cuda", dtype=torch.bfloat16, generator=gen)
        qw = torch.randn(D, device="cuda", dtype=torch.bfloat16, generator=gen)
        kw = torch.randn(D, device="cuda", dtype=torch.bfloat16, generator=gen)
        pos = torch.randint(0, T, (T,), device="cuda", dtype=torch.int64)
        cache = _make_cos_sin(rope, T)
        q = q0.clone(); k = k0.clone()

        def restore():
            q.copy_(q0); k.copy_(k0)

        run_base = lambda: baseline(q, k, qw, kw, cache, pos, is_neox=neox, eps=eps, rope_dim=rope)
        run_cand = lambda: cand(q, k, qw, kw, cache, pos, is_neox=neox, eps=eps, rope_dim=rope)

        b = _summary(_time(run_base, restore))
        # confirm candidate hits CUDA path
        restore(); cand(q, k, qw, kw, cache, pos, is_neox=neox, eps=eps, rope_dim=rope)
        path = wrap.last_dispatch_path()
        c = _summary(_time(run_cand, restore))
        sp = b["median"] / c["median"] if c["median"] > 0 else float("nan")
        speedups.append(sp)
        print(f"{name:24s} base={b['median']:.3f}us cand={c['median']:.3f}us speedup={sp:.4f}x path={path}")
        rows.append([
            now, KERNEL_SLUG, name, "median_us",
            f"{b['median']:.4f}", f"{c['median']:.4f}", f"{sp:.4f}x",
            (f"path={path} base_mean={b['mean']:.3f} base_std={b['std']:.3f} base_min={b['min']:.3f} "
             f"base_p10={b['p10']:.3f} base_p90={b['p90']:.3f} cand_mean={c['mean']:.3f} cand_std={c['std']:.3f} "
             f"cand_min={c['min']:.3f} cand_p10={c['p10']:.3f} cand_p90={c['p90']:.3f} "
             f"host={host} gpu_id={gpu_id} gpu={gpu_model} src_hash={src_hash} sglang={sg_ver}@{sg_commit} "
             f"build_flags='{BUILD_FLAGS}' arch=sm_90 container={container} workdir={workdir} "
             f"gpu_state={gpu_state} exact_cmd=\"{cmd}\""),
        ])

    gm = _geomean(speedups)
    print(f"GEOMEAN speedup across {len(speedups)} shapes = {gm:.4f}x")
    rows.append([
        now, KERNEL_SLUG, "all_captured_shapes", "geomean_speedup_x", "", "", f"{gm:.4f}x",
        f"host={host} gpu_id={gpu_id} gpu={gpu_model} src_hash={src_hash} sglang={sg_ver}@{sg_commit} "
        f"n={len(speedups)} container={container} workdir={workdir} gpu_state={gpu_state} exact_cmd=\"{cmd}\"",
    ])

    csv_path = KERNEL_DIR / "benchmark.csv"
    write_header = not csv_path.exists() or csv_path.stat().st_size == 0
    with csv_path.open("a", newline="") as f:
        w = csv.writer(f)
        if write_header:
            w.writerow(["utc", "slug", "shape", "metric", "baseline", "candidate", "speedup", "notes"])
        w.writerows(rows)
    print(f"wrote {len(rows)} rows to {csv_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
