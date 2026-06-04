#!/usr/bin/env python3
"""Validate the INTEGRATED kda_kernels.install() path on a live B200 + smoke benchmark.

This exercises the SHIPPED overlay end-to-end (kda_kernels.install() -> the
arch dispatcher -> the promoted b200 wrapper -> the CUDA kernel), as production
would, and measures latency through the swapped public SGLang symbols to confirm
the dispatcher adds no per-call tax that would erase small-shape wins.

Idle-gated like benchmark.py: the PARENT process validates GPU idleness with
nvidia-smi BEFORE any CUDA work, spawns a `--worker` child that runs the actual
validation, and re-validates idleness AFTER the child has fully exited. Both
states are embedded in the emitted JSON; the parent refuses to run on a busy
GPU unless --allow-busy is passed (in which case idle_gated is false).

Run inside the sglang container on an idle B200, with the kda_kernels package on
PYTHONPATH:
    PYTHONPATH=<repo_root> CUDA_VISIBLE_DEVICES=<idle> python kda_install_validate.py
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import os
import statistics
import subprocess
import sys
import tempfile
import time

import torch

KDIR = os.path.dirname(os.path.abspath(__file__))


def _gpu_state(gpu_id: str) -> dict:
    """Query nvidia-smi for the physical GPU: utilization, memory, compute procs."""
    try:
        u = subprocess.check_output(
            ["nvidia-smi", "--query-gpu=utilization.gpu,memory.used", "--format=csv,noheader,nounits", "-i", str(gpu_id)],
            text=True,
        ).strip()
        procs = subprocess.check_output(
            ["nvidia-smi", "--query-compute-apps=pid,used_memory", "--format=csv,noheader,nounits", "-i", str(gpu_id)],
            text=True,
        ).strip()
        util, mem = (x.strip() for x in u.split(","))
        n = len([ln for ln in procs.splitlines() if ln.strip()])
        return {"util_pct": int(float(util)), "mem_used_mib": int(float(mem)), "n_compute_procs": n,
                "procs": procs.replace("\n", "|") or "none"}
    except Exception as e:  # pragma: no cover
        return {"error": repr(e)}


def _is_idle(state: dict) -> bool:
    # Idle == no compute process, <=2 GiB resident, <=10% util on the target GPU.
    if "error" in state:
        return False
    return state["n_compute_procs"] == 0 and state["mem_used_mib"] <= 2048 and state["util_pct"] <= 10


def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, os.path.join(KDIR, rel))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def _median_us(fn, args, warmup=20, iters=100):
    for _ in range(warmup):
        fn(*args)
    torch.cuda.synchronize()
    s = [torch.cuda.Event(enable_timing=True) for _ in range(iters)]
    e = [torch.cuda.Event(enable_timing=True) for _ in range(iters)]
    for i in range(iters):
        s[i].record()
        fn(*args)
        e[i].record()
    torch.cuda.synchronize()
    return statistics.median([s[i].elapsed_time(e[i]) * 1000.0 for i in range(iters)])


def _geomean(xs):
    xs = [x for x in xs if math.isfinite(x) and x > 0]
    return math.exp(sum(math.log(x) for x in xs) / len(xs)) if xs else float("nan")


def _run_worker() -> dict:
    """The CUDA-touching validation body; runs in a child process so the parent's
    after-idle check observes a GPU with the CUDA context fully torn down."""
    corr = _load("corr", os.path.join("tests", "test_correctness.py"))
    import sglang.jit_kernel.diffusion.triton.rotary as rmod
    import sglang.jit_kernel.diffusion.triton.ltx2_rotary as lmod
    import kda_kernels

    res = {"kda_kernels_from": kda_kernels.__file__}
    cases = corr.make_cases()
    orig_rotary = rmod.apply_rotary_embedding
    orig_ltx2 = lmod.apply_ltx2_split_rotary_emb

    # ---- install: kda_kernels swaps the SGLang public symbols ----
    res["install_status"] = kda_kernels.install()
    try:
        res["swapped_rotary"] = rmod.apply_rotary_embedding is not orig_rotary
        res["swapped_ltx2"] = lmod.apply_ltx2_split_rotary_emb is not orig_ltx2

        # correctness through the integrated public API (now dispatcher -> CUDA).
        # Compare per case and free immediately -- holding all 11 reference outputs
        # inflates the in-loop allocator and contaminates the benchmark below.
        md = 0.0
        for c in cases:
            base = orig_rotary(*c["args"]) if c["kind"] == "standard" else orig_ltx2(*c["args"])
            disp = rmod.apply_rotary_embedding if c["kind"] == "standard" else lmod.apply_ltx2_split_rotary_emb
            got = disp(*c["args"])
            md = max(md, (got.float() - base.float()).abs().max().item())
            del base, got
        torch.cuda.empty_cache()
        res["integrated_oracle"] = {"shapes": len(cases), "max_abs_diff": md, "bit_exact": md == 0.0}

        # integrated-path smoke benchmark: swapped public symbol vs original baseline
        speedups = []
        rows = []
        for c in cases:
            base = orig_rotary if c["kind"] == "standard" else orig_ltx2
            disp = rmod.apply_rotary_embedding if c["kind"] == "standard" else lmod.apply_ltx2_split_rotary_emb
            bt = _median_us(base, c["args"])
            ct = _median_us(disp, c["args"])
            sp = bt / ct if ct > 0 else float("nan")
            speedups.append(sp)
            rows.append({"name": c["name"], "base_us": round(bt, 2), "kda_us": round(ct, 2), "speedup": round(sp, 3)})
        res["integrated_benchmark"] = {"geomean": round(_geomean(speedups), 4), "rows": rows}

        # non-captured (bf16, non-captured shape) must fall back to baseline via the public API
        g = torch.Generator(device="cuda").manual_seed(7)
        xf = torch.randn(1, 1024, 8, 128, generator=g, device="cuda", dtype=torch.float32).bfloat16()
        cf = torch.randn(1024, 64, generator=g, device="cuda", dtype=torch.float32)
        exp = orig_rotary(xf, cf, cf, False)
        got = rmod.apply_rotary_embedding(xf, cf, cf, False)
        res["integrated_fallback"] = {"max_abs_diff": (got.float() - exp.float()).abs().max().item()}
    finally:
        res["uninstall_status"] = kda_kernels.uninstall()

    res["restored_rotary"] = rmod.apply_rotary_embedding is orig_rotary
    res["restored_ltx2"] = lmod.apply_ltx2_split_rotary_emb is orig_ltx2
    return res


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--allow-busy", action="store_true", help="skip the idle gate (NOT for promotion evidence)")
    ap.add_argument("--worker", action="store_true", help="internal: CUDA validation child process")
    ap.add_argument("--tmp", type=str, default="", help="internal: worker results path")
    args = ap.parse_args()

    if args.worker:
        json.dump(_run_worker(), open(args.tmp, "w"), default=str)
        return 0

    # -------- parent: owns the idle gate; never initializes CUDA --------
    visible = os.environ.get("CUDA_VISIBLE_DEVICES", "")
    gpu_id = visible.split(",")[0] if visible else "0"

    pre = _gpu_state(gpu_id)
    if not args.allow_busy and not _is_idle(pre):
        raise SystemExit(f"GPU {gpu_id} not idle BEFORE install validation (refusing to run): {pre}")

    tmp = tempfile.NamedTemporaryFile(suffix=".json", delete=False, dir=KDIR)
    tmp.close()
    cmd = [sys.executable, os.path.abspath(__file__), "--worker", "--tmp", tmp.name]
    rc = subprocess.run(cmd).returncode
    try:
        with open(tmp.name) as fh:
            res = json.load(fh)
    except Exception as e:
        res = {"error": f"could not read worker results: {e!r}"}
    finally:
        if os.path.exists(tmp.name):
            os.unlink(tmp.name)
    if rc != 0 or "kda_kernels_from" not in res:
        raise SystemExit(f"worker failed (rc={rc}): {res}")

    time.sleep(3)  # let the GPU settle after the CUDA worker process has exited
    post = _gpu_state(gpu_id)
    res["gpu_id"] = gpu_id
    res["idle_before"] = {"idle": _is_idle(pre), **pre}
    res["idle_after"] = {"idle": _is_idle(post), **post}
    res["idle_gated"] = bool(_is_idle(pre) and _is_idle(post))
    print(json.dumps(res, indent=2, default=str))
    return 0 if res["idle_gated"] or args.allow_busy else 1


if __name__ == "__main__":
    raise SystemExit(main())
