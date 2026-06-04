"""Dispatch-symmetric in-SGLang arbiter benchmark for the diffusion norm kernels.

Runs against ONE patched SGLang checkout (the task-owned worktree must be first
on PYTHONPATH): the same public symbols, the same wrapper and registration, the
same inserted dispatch branch — with the native routes disabled or enabled via
environment toggles (SGLANG_NATIVE_NORM_INFER / SGLANG_NATIVE_ONE_PASS_RMS_NORM).
Comparing a toggled-off run against a toggled-on run isolates the shipped
implementation change; clean-vs-patched comparisons are NOT used.

Measures the PUBLIC entry points (sglang.jit_kernel.diffusion.triton.norm:
norm_infer, ...rmsnorm_onepass:triton_one_pass_rms_norm) on the six captured
production shapes with the two-pass methodology (per-call wall; stream-saturated
batched device rate). With --toggle on it also runs fallback probes (guard
evaluates False AND output matches a torch fp32 reference) and a torch.compile
smoke over the registered custom op.

Usage (inside the container):
    PYTHONPATH=<worktree>/python REMOTE_GPU_ID=0 CUDA_VISIBLE_DEVICES=0 \
        python3 bench_intree_arbiter.py --toggle on  [--iters 200] [--json out.json]
"""

from __future__ import annotations

import argparse
import json
import os
import statistics
import subprocess
import sys
import time

ap = argparse.ArgumentParser()
ap.add_argument("--toggle", required=True, choices=["on", "off"])
ap.add_argument("--iters", type=int, default=200)
ap.add_argument("--warmup", type=int, default=30)
ap.add_argument("--json", default="")
ap.add_argument("--probes", action="store_true", help="run fallback probes + compile smoke (toggle on only)")
args = ap.parse_args()

VAL = "1" if args.toggle == "on" else "0"
os.environ["SGLANG_NATIVE_NORM_INFER"] = VAL
os.environ["SGLANG_NATIVE_ONE_PASS_RMS_NORM"] = VAL

remote_gpu = os.environ.get("REMOTE_GPU_ID", "")
first = os.environ.get("CUDA_VISIBLE_DEVICES", "").split(",")[0].strip()
if not remote_gpu or remote_gpu != first:
    sys.exit("GPU pin mismatch: REMOTE_GPU_ID must equal first CUDA_VISIBLE_DEVICES entry")


def gpu_state():
    out = subprocess.run(
        ["nvidia-smi", "--query-gpu=utilization.gpu,memory.used",
         "--format=csv,noheader,nounits", "-i", remote_gpu],
        capture_output=True, text=True, check=True).stdout.strip()
    util, mem = [int(v) for v in out.split(",")]
    apps = subprocess.run(
        ["nvidia-smi", "--query-compute-apps=pid", "--format=csv,noheader", "-i", remote_gpu],
        capture_output=True, text=True, check=True).stdout.strip()
    return {"util": util, "mem_mib": mem, "apps": len([l for l in apps.splitlines() if l.strip()])}


state_before = gpu_state()
if state_before["apps"] != 0 or state_before["util"] != 0 or state_before["mem_mib"] > 150:
    sys.exit(f"GPU {remote_gpu} not idle before run: {state_before}")

import torch  # noqa: E402

import sglang  # noqa: E402
from sglang.jit_kernel.diffusion.triton import norm as norm_mod  # noqa: E402
from sglang.jit_kernel.diffusion.triton import rmsnorm_onepass as rms_mod  # noqa: E402

print(f"[env] sglang from {sglang.__file__}")
print(f"[env] toggles = {VAL} (norm_infer, one_pass_rms_norm)")

SHAPES = [
    ("helios__f32__M8640N5120", "ln", 8640, 5120, torch.float32),
    ("hunyuan__bf16__M648720D128", "rms", 648720, 128, torch.bfloat16),
    ("hunyuan__bf16__M1320D128", "rms", 1320, 128, torch.bfloat16),
    ("hunyuan__bf16__M650040D128", "rms", 650040, 128, torch.bfloat16),
    ("zimage__bf16__M16384D128", "rms", 16384, 128, torch.bfloat16),
    ("zimage__bf16__M4096D128", "rms", 4096, 128, torch.bfloat16),
]

BATCH = 32


def wall_call(fn):
    t0 = time.perf_counter()
    fn()
    torch.cuda.synchronize()
    return (time.perf_counter() - t0) * 1e6


def device_batch(fn):
    ev_a = torch.cuda.Event(enable_timing=True)
    ev_b = torch.cuda.Event(enable_timing=True)
    ev_a.record()
    for _ in range(BATCH):
        fn()
    ev_b.record()
    torch.cuda.synchronize()
    return ev_a.elapsed_time(ev_b) * 1e3 / BATCH


def rms_torch_ref(x, w, eps):
    xf = x.float()
    rstd = torch.rsqrt(xf.pow(2).mean(-1, keepdim=True) + eps)
    return (xf * rstd * w.float()).to(x.dtype)


def ln_torch_ref(x, w, b, eps):
    xf = x.float()
    mu = xf.mean(-1, keepdim=True)
    var = (xf - mu).pow(2).mean(-1, keepdim=True)
    return ((xf - mu) * torch.rsqrt(var + eps) * w.float() + b.float()).to(x.dtype)


results = {"toggle": args.toggle, "shapes": {}, "gate_before": state_before}
torch.manual_seed(0)

# Confirm the gate state matches the toggle (the inserted branch must exist in
# BOTH runs; only its enablement differs). Gates are keyed on the tensor
# device; the harness pins one device, so index 0 is the device under test.
gate_dev = torch.cuda.current_device()
gate_ln = norm_mod._can_use_native_ln_infer(5120, gate_dev)
gate_rms = rms_mod._can_use_native_one_pass_rms(128, gate_dev)
expected = args.toggle == "on"
assert gate_ln == expected and gate_rms == expected, (
    f"gate mismatch: ln={gate_ln} rms={gate_rms} expected={expected}"
)
print(f"[gate] _can_use_native_ln_infer(5120, {gate_dev})={gate_ln}, "
      f"_can_use_native_one_pass_rms(128, {gate_dev})={gate_rms}")

for name, kind, m, n, dtype in SHAPES:
    x = torch.randn(m, n, device="cuda", dtype=dtype)
    w = torch.randn(n, device="cuda", dtype=dtype)
    if kind == "ln":
        b = torch.randn(n, device="cuda", dtype=dtype)
        fn = lambda: norm_mod.norm_infer(x, w, b, eps=1e-6, is_rms_norm=False)
        ref = ln_torch_ref(x, w, b, 1e-6)
        tol = 1e-5
    else:
        fn = lambda: rms_mod.triton_one_pass_rms_norm(x, w, 1e-6)
        ref = rms_torch_ref(x, w, 1e-6)
        tol = 5e-2
    out = fn()
    assert not torch.isnan(out).any() and not torch.isinf(out).any(), f"{name}: NaN/Inf"
    torch.testing.assert_close(out, ref, atol=tol, rtol=tol)
    del out, ref

    for _ in range(args.warmup):
        fn()
    torch.cuda.synchronize()
    wall = [wall_call(fn) for _ in range(args.iters)]
    devr = [device_batch(fn) for _ in range(max(10, args.iters // 10))]
    results["shapes"][name] = {
        "wall_median_us": round(statistics.median(wall), 4),
        "wall_mean_us": round(statistics.fmean(wall), 4),
        "wall_std_us": round(statistics.pstdev(wall), 4),
        "wall_min_us": round(min(wall), 4),
        "wall_p10_us": round(sorted(wall)[int(0.10 * (len(wall) - 1))], 4),
        "wall_p90_us": round(sorted(wall)[int(0.90 * (len(wall) - 1))], 4),
        "device_rate_median_us": round(statistics.median(devr), 4),
    }
    print(f"{name:30s} wall={results['shapes'][name]['wall_median_us']:9.2f}us "
          f"dev_rate={results['shapes'][name]['device_rate_median_us']:8.2f}us")
    del x, w
    if kind == "ln":
        del b
    torch.cuda.empty_cache()

if args.probes:
    assert args.toggle == "on", "probes are meaningful with the native routes enabled"
    print("[probes] fallback eligibility + output checks (native ON)")

    def rms_guard(x, w):
        return bool(
            x.is_cuda and x.dtype == torch.bfloat16 and x.shape[-1] == 128
            and x.is_contiguous() and w.dtype == x.dtype and w.numel() == 128
            and w.is_contiguous()
            and rms_mod._can_use_native_one_pass_rms(128, x.device.index)
        )

    # fp16 input: dynamic guard must be False; public output matches torch ref.
    x = torch.randn(256, 128, device="cuda", dtype=torch.float16)
    w = torch.randn(128, device="cuda", dtype=torch.float16)
    assert rms_guard(x, w) is False
    torch.testing.assert_close(rms_mod.triton_one_pass_rms_norm(x, w, 1e-6),
                               rms_torch_ref(x, w, 1e-6), atol=5e-2, rtol=5e-2)
    print("  probe fp16 rms: guard False + output==ref OK")

    # Non-contiguous (row-sliced) bf16: guard False; output matches torch ref.
    xb = torch.randn(512, 128, device="cuda", dtype=torch.bfloat16)[::2]
    wb = torch.randn(128, device="cuda", dtype=torch.bfloat16)
    assert xb.is_contiguous() is False and rms_guard(xb, wb) is False
    torch.testing.assert_close(rms_mod.triton_one_pass_rms_norm(xb, wb, 1e-6),
                               rms_torch_ref(xb.contiguous(), wb, 1e-6), atol=5e-2, rtol=5e-2)
    print("  probe non-contiguous rms: guard False + output==ref OK")

    # is_rms_norm=True on norm_infer must bypass the LN fast path.
    xl = torch.randn(64, 5120, device="cuda", dtype=torch.float32)
    wl = torch.randn(5120, device="cuda", dtype=torch.float32)
    out = norm_mod.norm_infer(xl, wl, None, eps=1e-6, is_rms_norm=True)
    torch.testing.assert_close(out, rms_torch_ref(xl, wl, 1e-6), atol=1e-5, rtol=1e-5)
    print("  probe is_rms_norm=True norm_infer: fast path bypassed + output==ref OK")

    # torch.compile smoke through the registered custom op.
    assert hasattr(torch.ops.sglang, "triton_one_pass_rms_norm_cuda"), "custom op not registered"
    xc = torch.randn(4096, 128, device="cuda", dtype=torch.bfloat16)
    wc = torch.randn(128, device="cuda", dtype=torch.bfloat16)
    eager = rms_mod.triton_one_pass_rms_norm(xc, wc, 1e-6)
    compiled = torch.compile(lambda a, b: rms_mod.triton_one_pass_rms_norm(a, b, 1e-6))
    comp = compiled(xc, wc)
    torch.testing.assert_close(comp, eager, atol=0.0, rtol=0.0)
    print("  probe torch.compile: registered op present, compiled == eager (bitwise) OK")
    results["probes"] = "all-passed"

state_after = gpu_state()
results["gate_after"] = state_after
if state_after["apps"] > 1:
    print(f"WARNING: {state_after['apps']} compute apps after run — treat as invalid")
    results["invalid"] = "gpu-not-exclusive-after"

if args.json:
    with open(args.json, "w") as f:
        json.dump(results, f, indent=1)
    print(f"[out] wrote {args.json}")
