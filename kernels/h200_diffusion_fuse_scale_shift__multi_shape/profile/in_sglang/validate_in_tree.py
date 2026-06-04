#!/usr/bin/env python3
"""In-tree shipping-path validation: oracle parity, fallback, and smoke benchmark.

Runs against a PATCHED task-owned sglang worktree (PYTHONPATH must point at
<worktree>/python). Candidate and baseline go through the IDENTICAL public
SGLang callables in sglang.jit_kernel.diffusion.triton.scale_shift — only the
module-level native toggle differs between sides, so wrapper, dispatch, and
any registration layer above are byte-identical for both measurements.

Phases:
1. routing check  — native actually serves each production row (harness-side
   counting wrappers; removed before timing)
2. parity         — native vs original Triton outputs within oracle tolerances
   for all 15 production rows (plus finite checks)
3. fallback       — out-of-contract signatures behave identically with the
   native path enabled (reach the original Triton body)
4. smoke benchmark— per-row interleaved phase blocks (off/on/off/on...), sync
   wall + device events, idle-GPU checks via the container-safe pid-delta rule

Usage:
  CUDA_VISIBLE_DEVICES=<id> PYTHONPATH=<worktree>/python python \
      profile/in_sglang/validate_in_tree.py --gpu-id <physical-id> --json out.json
"""

from __future__ import annotations

import argparse
import json
import statistics
import sys
import time
from pathlib import Path

KERNEL_DIR = Path(__file__).resolve().parents[2]
if str(KERNEL_DIR) not in sys.path:
    sys.path.insert(0, str(KERNEL_DIR))

import torch  # noqa: E402

from bench import cases as cases_mod  # noqa: E402
from bench import reference as ref_mod  # noqa: E402
from bench.benchmark import _stats, gpu_snapshot  # noqa: E402

from sglang.jit_kernel.diffusion import scale_shift_kda as kda  # noqa: E402
from sglang.jit_kernel.diffusion.triton import scale_shift as public  # noqa: E402

PUBLIC_FNS = {
    cases_mod.OP_SCALE_SHIFT: public.fuse_scale_shift_kernel,
    cases_mod.OP_SELECT01: public.fuse_layernorm_scale_shift_gate_select01_kernel,
    cases_mod.OP_RESIDUAL: public.fuse_residual_layernorm_scale_shift_gate_select01_kernel,
}


def _as_tuple(out):
    return out if isinstance(out, tuple) else (out,)


def _set_native(on: bool) -> None:
    kda.ENABLED = on


def routing_check(device) -> dict:
    counts = {"fuse_scale_shift": 0, "select01": 0, "residual": 0}
    orig = (kda.try_native_fuse_scale_shift, kda.try_native_layernorm_select01,
            kda.try_native_residual_layernorm_select01)

    def wrap(fn, key):
        def inner(*a, **k):
            out = fn(*a, **k)
            if out is not None:
                counts[key] += 1
            return out
        return inner

    kda.try_native_fuse_scale_shift = wrap(orig[0], "fuse_scale_shift")
    kda.try_native_layernorm_select01 = wrap(orig[1], "select01")
    kda.try_native_residual_layernorm_select01 = wrap(orig[2], "residual")
    try:
        _set_native(True)
        for case in cases_mod.production_cases():
            args, kwargs = case.build(device)
            PUBLIC_FNS[case.op](*args, **kwargs)
        torch.cuda.synchronize()
    finally:
        (kda.try_native_fuse_scale_shift, kda.try_native_layernorm_select01,
         kda.try_native_residual_layernorm_select01) = orig
    assert counts["fuse_scale_shift"] == 13, counts
    assert counts["select01"] == 1 and counts["residual"] == 1, counts
    return counts


def parity_check(device) -> list[dict]:
    results = []
    for case in cases_mod.production_cases():
        args, kwargs = case.build(device)
        fn = PUBLIC_FNS[case.op]
        _set_native(False)
        ref_out = _as_tuple(fn(*args, **kwargs))
        _set_native(True)
        nat_out = _as_tuple(fn(*args, **kwargs))
        atol, rtol = ref_mod.fixed_tol(case.x_dtype)
        for name, a, b in zip(("out", "res", "gate"), nat_out, ref_out):
            assert torch.isfinite(a).all(), (case.case_id, name)
            torch.testing.assert_close(a, b, atol=atol, rtol=rtol)
        maxdiff = max(
            (a.float() - b.float()).abs().max().item()
            for a, b in zip(nat_out, ref_out)
        )
        results.append({"case_id": case.case_id, "max_abs_diff": maxdiff})
    return results


def fallback_check(device) -> list[str]:
    checked = []
    g = torch.Generator(device=device); g.manual_seed(7)
    x64 = torch.randn((2, 33, 512), generator=g, device=device, dtype=torch.float64)
    s64 = torch.randn((2, 512), generator=g, device=device, dtype=torch.float64)
    _set_native(False)
    ref = public.fuse_scale_shift_kernel(x64, s64, s64, scale_constant=0)
    _set_native(True)
    out = public.fuse_scale_shift_kernel(x64, s64, s64, scale_constant=0)
    assert torch.equal(ref, out), "fp64 fallback diverged"
    checked.append("fp64 -> original Triton body, identical result")

    xnc = torch.randn((2, 33, 1024), generator=g, device=device, dtype=torch.bfloat16)[:, :, :512]
    sb = torch.randn((2, 512), generator=g, device=device, dtype=torch.bfloat16)
    for on in (False, True):
        _set_native(on)
        try:
            public.fuse_scale_shift_kernel(xnc, sb, sb, scale_constant=0)
            raise SystemExit("expected AssertionError for non-contiguous x")
        except AssertionError:
            pass
    checked.append("non-contiguous x -> AssertionError both modes")

    xc = torch.randn((2, 33, 512), dtype=torch.bfloat16)
    sc = torch.randn((2, 512), dtype=torch.bfloat16)
    for on in (False, True):
        _set_native(on)
        try:
            public.fuse_scale_shift_kernel(xc, sc, sc, scale_constant=0)
            raise SystemExit("expected AssertionError for CPU tensors")
        except AssertionError:
            pass
    checked.append("CPU tensors -> AssertionError both modes")
    return checked


def bench_row(case, device, *, iters: int) -> dict:
    fn = PUBLIC_FNS[case.op]
    args, kwargs = case.build(device)
    for on in (False, True):  # warmup both paths (incl. autotune / jit cache)
        _set_native(on)
        for _ in range(15):
            fn(*args, **kwargs)
    torch.cuda.synchronize()

    samples = {False: {"sync": [], "dev": []}, True: {"sync": [], "dev": []}}
    order = [False, True, True, False]  # ABBA blocks cancel drift
    block = max(10, iters // 8)
    for phase in range(8):
        on = order[phase % 4]
        _set_native(on)
        evs = [(torch.cuda.Event(True), torch.cuda.Event(True)) for _ in range(block)]
        for i in range(block):
            t0 = time.perf_counter()
            evs[i][0].record()
            fn(*args, **kwargs)
            evs[i][1].record()
            torch.cuda.synchronize()
            samples[on]["sync"].append((time.perf_counter() - t0) * 1e6)
        for e0, e1 in evs:
            samples[on]["dev"].append(e0.elapsed_time(e1) * 1e3)
    _set_native(True)

    row = {"case_id": case.case_id, "op": case.op, "n_per_side": len(samples[True]["sync"])}
    for key, label in (("sync", "sync_wall"), ("dev", "device_ev")):
        base = _stats(samples[False][key])
        cand = _stats(samples[True][key])
        row[label] = {
            "base_median_us": round(base["median_us"], 2),
            "cand_median_us": round(cand["median_us"], 2),
            "speedup_median": round(base["median_us"] / cand["median_us"], 4),
        }
    return row


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--gpu-id", required=True)
    ap.add_argument("--iters", type=int, default=160)
    ap.add_argument("--json", default="")
    args = ap.parse_args()

    snap_before = gpu_snapshot(args.gpu_id)
    device = torch.device("cuda")
    report = {
        "worktree_module": public.__file__,
        "gpu_name": torch.cuda.get_device_name(device),
        "gpu_id": args.gpu_id,
        "idle_before": snap_before.get("idle"),
        "torch": torch.__version__,
    }

    report["routing"] = routing_check(device)
    print("routing:", report["routing"])
    report["parity"] = parity_check(device)
    print(f"parity: {len(report['parity'])}/15 rows within oracle tolerances")
    report["fallback"] = fallback_check(device)
    print("fallback:", *report["fallback"], sep="\n  ")

    rows = []
    import math
    for case in cases_mod.production_cases():
        row = bench_row(case, device, iters=args.iters)
        rows.append(row)
        print(f"  {row['case_id']:60s} sync {row['sync_wall']['base_median_us']:9.1f} -> "
              f"{row['sync_wall']['cand_median_us']:9.1f} us ({row['sync_wall']['speedup_median']:.3f}x) | "
              f"dev {row['device_ev']['base_median_us']:9.1f} -> "
              f"{row['device_ev']['cand_median_us']:9.1f} us ({row['device_ev']['speedup_median']:.3f}x)")
    report["bench"] = rows
    for label in ("sync_wall", "device_ev"):
        gm = math.exp(sum(math.log(r[label]["speedup_median"]) for r in rows) / len(rows))
        report[f"geomean_{label}"] = round(gm, 4)
        print(f"geomean {label}: {report[f'geomean_{label}']}")

    snap_after = gpu_snapshot(args.gpu_id, baseline_pids=set(snap_before.get("procs") or []))
    report["idle_after"] = snap_after.get("idle")
    report["valid"] = bool(snap_before.get("idle")) and bool(snap_after.get("idle"))
    print(f"valid={report['valid']}")

    if args.json:
        Path(args.json).parent.mkdir(parents=True, exist_ok=True)
        Path(args.json).write_text(json.dumps(report, indent=1))
        print("report:", args.json)
    return 0 if report["valid"] else 1


if __name__ == "__main__":
    sys.exit(main())
