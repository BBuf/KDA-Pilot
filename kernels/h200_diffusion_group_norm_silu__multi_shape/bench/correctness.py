#!/usr/bin/env python3
"""Correctness suite for the fused GroupNorm+SiLU task.

Covers, before any benchmark result may count:

* the 48 production signatures (fp16, num_groups=32, eps=1e-6) from
  bench/workloads.json through the direct entry, candidate vs an eager oracle
  and vs the copied baseline;
* the wrapper path (module-based) on the canonical 2D/3D rows (fp16/bf16) and
  on representative production shapes;
* the canonical regression grid from docs/diffusion_correctness_contract.md:
  (2,64,32,32), (1,64,4,16,16), (4,128), (1,128,20,256,256) for
  fp16/bf16/fp32 at eps=1e-5 with per-dtype tolerances;
* edge handling: misaligned storage offset and non-contiguous input (values
  must stay correct regardless of which internal path runs);
* methodology self-tests: NaN-poisoned outputs catch a skipped kernel; the
  upstream baseline really takes its Triton path on production rows (and
  demonstrably would not under grad mode).

Oracle: F.silu(F.group_norm(x, num_groups, weight, bias, eps)) in the case
dtype (eager PyTorch accumulates GroupNorm statistics in fp32 internally).

Exit code 0 only if every selected case passes. `--skip-candidate` validates
the baseline/harness alone (pre-build); full runs require the solution build.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import torch
import torch.nn.functional as F
from torch import nn

TASK_ROOT = Path(__file__).resolve().parents[1]
if str(TASK_ROOT) not in sys.path:
    sys.path.insert(0, str(TASK_ROOT))

from baseline.binding import (  # noqa: E402
    group_norm_silu_baseline,
    group_norm_silu_baseline_apply,
    triton_path_active,
    uses_chunked_path,
)

TOLERANCES = {
    torch.float16: {"atol": 3e-3, "rtol": 3e-3},
    torch.bfloat16: {"atol": 7e-2, "rtol": 2e-2},
    torch.float32: {"atol": 1e-5, "rtol": 1e-5},
}
PRODUCTION_EPS = 1e-6
CONTRACT_EPS = 1e-5
NUM_GROUPS = 32

REGRESSION_SHAPES = [
    (2, 64, 32, 32),
    (1, 64, 4, 16, 16),
    (4, 128),
    (1, 128, 20, 256, 256),
]
WRAPPER_CONTRACT_SHAPES = [(2, 64, 32, 32), (1, 64, 4, 16, 16)]

_failures: list[str] = []
_passes = 0


def _record(name: str, ok: bool, detail: str = "") -> None:
    global _passes
    if ok:
        _passes += 1
        print(f"PASS {name}")
    else:
        _failures.append(f"{name}: {detail}")
        print(f"FAIL {name}: {detail}")


def oracle(x, weight, bias, num_groups, eps):
    return F.silu(F.group_norm(x, num_groups, weight=weight, bias=bias, eps=eps))


def close(name, got, ref, dtype) -> None:
    tol = TOLERANCES[dtype]
    if torch.isnan(got).any() or torch.isinf(got).any():
        _record(name, False, "NaN/Inf in output")
        return
    diff = (got.float() - ref.float()).abs()
    bound = tol["atol"] + tol["rtol"] * ref.float().abs()
    bad = (diff > bound).sum().item()
    max_abs = diff.max().item() if diff.numel() else 0.0
    _record(name, bad == 0, f"{bad} elems exceed tol, max_abs={max_abs:.3e}")


def make_inputs(shape, dtype, device):
    x = torch.randn(shape, device=device, dtype=dtype)
    weight = torch.randn(shape[1], device=device, dtype=dtype)
    bias = torch.randn(shape[1], device=device, dtype=dtype)
    return x, weight, bias


def candidate_fn():
    # The destination-passing variant keeps the poison checks meaningful (the
    # CUDA regimes overwrite the poisoned buffer in place).
    from solution.binding import group_norm_silu_candidate_into

    return group_norm_silu_candidate_into


def run_candidate(cand, x, weight, bias, num_groups, eps):
    out = torch.full_like(x, float("nan"))
    cand(x, weight, bias, num_groups, eps, out)
    return out


def production_rows():
    data = json.loads((TASK_ROOT / "bench" / "workloads.json").read_text())
    return [w for w in data if w.get("production")]


def suite_production(device, cand) -> None:
    for w in production_rows():
        shape = tuple(w["shapes"]["x"])
        torch.manual_seed(0xC0FFEE ^ hash(shape) & 0xFFFF)
        x, weight, bias = make_inputs(shape, torch.float16, device)
        if not triton_path_active(x, weight, bias, NUM_GROUPS):
            _record(f"prod_gate_{shape}", False, "baseline would take eager fallback")
            continue
        ref = oracle(x, weight, bias, NUM_GROUPS, PRODUCTION_EPS)
        base = group_norm_silu_baseline(x, weight, bias, NUM_GROUPS, PRODUCTION_EPS)
        close(f"prod_base_vs_oracle_{shape}", base, ref, torch.float16)
        if cand is not None:
            got = run_candidate(cand, x, weight, bias, NUM_GROUPS, PRODUCTION_EPS)
            close(f"prod_cand_vs_oracle_{shape}", got, ref, torch.float16)
            close(f"prod_cand_vs_base_{shape}", got, base, torch.float16)


def suite_regression(device, cand) -> None:
    for shape in REGRESSION_SHAPES:
        for dtype in (torch.float16, torch.bfloat16, torch.float32):
            torch.manual_seed(0xBEEF ^ (len(shape) << 8) ^ shape[1])
            x, weight, bias = make_inputs(shape, dtype, device)
            ref = oracle(x, weight, bias, NUM_GROUPS, CONTRACT_EPS)
            base = group_norm_silu_baseline(x, weight, bias, NUM_GROUPS, CONTRACT_EPS)
            tag = f"{shape}_{str(dtype).split('.')[-1]}"
            close(f"reg_base_vs_oracle_{tag}", base, ref, dtype)
            if cand is not None:
                got = run_candidate(cand, x, weight, bias, NUM_GROUPS, CONTRACT_EPS)
                close(f"reg_cand_vs_oracle_{tag}", got, ref, dtype)


def suite_wrapper(device, cand) -> None:
    cases = [
        (shape, dtype, CONTRACT_EPS)
        for shape in WRAPPER_CONTRACT_SHAPES
        for dtype in (torch.float16, torch.bfloat16)
    ]
    # Every wrapper diagnostic workload row gets exact coverage, plus a spread
    # of production shapes through the same module-based path.
    data = json.loads((TASK_ROOT / "bench" / "workloads.json").read_text())
    for w in data:
        if not w.get("production") and w.get("function") == "apply_group_norm_silu":
            dtype = {"float16": torch.float16, "bfloat16": torch.bfloat16,
                     "float32": torch.float32}[w.get("dtype", "float16")]
            cases.append((tuple(w["shapes"]["x"]), dtype, float(w["eps"])))
    prod = production_rows()
    for w in (prod[0], prod[len(prod) // 2], prod[-1]):
        cases.append((tuple(w["shapes"]["x"]), torch.float16, PRODUCTION_EPS))

    for shape, dtype, eps in cases:
        torch.manual_seed(0xAB ^ shape[1])
        x, weight, bias = make_inputs(shape, dtype, device)
        norm = nn.GroupNorm(NUM_GROUPS, shape[1], eps=eps, affine=True)
        norm = norm.to(device=device, dtype=dtype)
        with torch.no_grad():
            norm.weight.copy_(weight)
            norm.bias.copy_(bias)
        norm.requires_grad_(False)
        act = nn.SiLU()
        tag = f"{shape}_{str(dtype).split('.')[-1]}_eps{eps:g}"
        ref = oracle(x, weight, bias, NUM_GROUPS, eps)
        base = group_norm_silu_baseline_apply(x, norm, act)
        close(f"wrap_base_vs_oracle_{tag}", base, ref, dtype)
        if cand is not None:
            got = run_candidate(
                cand, x, norm.weight, norm.bias, int(norm.num_groups), float(norm.eps)
            )
            close(f"wrap_cand_vs_oracle_{tag}", got, ref, dtype)


def suite_edge(device, cand) -> None:
    # Misaligned base pointer: contiguous fp16 view whose data_ptr is offset by
    # one element (2 bytes) from the allocation start.
    shape = (1, 256, 3, 48, 40)
    numel = 1
    for d in shape:
        numel *= d
    torch.manual_seed(0xA11)
    backing = torch.randn(numel + 1, device=device, dtype=torch.float16)
    x = backing[1:].view(shape)
    assert x.is_contiguous() and x.storage_offset() == 1
    weight = torch.randn(shape[1], device=device, dtype=torch.float16)
    bias = torch.randn(shape[1], device=device, dtype=torch.float16)
    ref = oracle(x, weight, bias, NUM_GROUPS, PRODUCTION_EPS)
    base = group_norm_silu_baseline(x, weight, bias, NUM_GROUPS, PRODUCTION_EPS)
    close("edge_misaligned_base_vs_oracle", base, ref, torch.float16)
    if cand is not None:
        got = run_candidate(cand, x, weight, bias, NUM_GROUPS, PRODUCTION_EPS)
        close("edge_misaligned_cand_vs_oracle", got, ref, torch.float16)

    # Non-contiguous input: channels-last-ish permutation. Values must stay
    # correct whichever internal path handles it.
    shape = (1, 128, 5, 64, 64)
    torch.manual_seed(0xA12)
    base_t = torch.randn(
        (shape[0], shape[2], shape[3], shape[4], shape[1]),
        device=device,
        dtype=torch.float16,
    )
    x = base_t.permute(0, 4, 1, 2, 3)
    assert not x.is_contiguous()
    weight = torch.randn(shape[1], device=device, dtype=torch.float16)
    bias = torch.randn(shape[1], device=device, dtype=torch.float16)
    ref = oracle(x, weight, bias, NUM_GROUPS, PRODUCTION_EPS)
    base = group_norm_silu_baseline(x, weight, bias, NUM_GROUPS, PRODUCTION_EPS)
    close("edge_noncontig_base_vs_oracle", base, ref, torch.float16)
    if cand is not None:
        got = run_candidate(cand, x, weight, bias, NUM_GROUPS, PRODUCTION_EPS)
        close("edge_noncontig_cand_vs_oracle", got, ref, torch.float16)


def suite_methodology(device, cand) -> None:
    # Poison detection: an untouched NaN-poisoned output must be flagged, and a
    # real kernel call must clear every poisoned cell.
    shape = (1, 512, 2, 24, 20)
    torch.manual_seed(0xD0)
    x, weight, bias = make_inputs(shape, torch.float16, device)
    poisoned = torch.full_like(x, float("nan"))
    _record("method_poison_detects_skip", bool(torch.isnan(poisoned).all()))
    if cand is not None:
        cand(x, weight, bias, NUM_GROUPS, PRODUCTION_EPS, poisoned)
        _record(
            "method_poison_cleared_by_kernel",
            not torch.isnan(poisoned).any(),
            "candidate left poisoned cells",
        )

    # Grad-mode trap: under grad the upstream gate must refuse the Triton path.
    with torch.enable_grad():
        _record(
            "method_grad_mode_gate_closes",
            not triton_path_active(x, weight, bias, NUM_GROUPS),
            "gate stayed open under grad mode",
        )

    # Triton-path authenticity on live kernels: profile one small-path call and
    # one chunked-path call; a Triton kernel name must appear (eager
    # F.group_norm would show aten native_group_norm kernels instead).
    from torch.profiler import ProfilerActivity, profile

    for label, shape in (("one_pass", (1, 512, 2, 24, 20)), ("chunked", (1, 256, 9, 128, 128))):
        x, weight, bias = make_inputs(shape, torch.float16, device)
        assert uses_chunked_path(x, NUM_GROUPS) == (label == "chunked")
        group_norm_silu_baseline(x, weight, bias, NUM_GROUPS, PRODUCTION_EPS)
        with profile(activities=[ProfilerActivity.CUDA]) as prof:
            group_norm_silu_baseline(x, weight, bias, NUM_GROUPS, PRODUCTION_EPS)
            torch.cuda.synchronize()
        names = []
        for e in prof.key_averages():
            key = getattr(e, "key", None) or getattr(e, "name", "")
            dev_time = (
                getattr(e, "self_device_time_total", 0)
                or getattr(e, "self_cuda_time_total", 0)
                or 0
            )
            if key and dev_time > 0:
                names.append(key)
        triton_hits = [n for n in names if "group_norm" in n and "native" not in n]
        eager_hits = [n for n in names if "native_group_norm" in n or "RowwiseMoments" in n]
        _record(
            f"method_triton_path_{label}",
            bool(triton_hits) and not eager_hits,
            f"cuda kernels seen: {names[:8]}",
        )
        print(f"  [{label}] cuda kernels: {triton_hits or names[:8]}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--device", default="cuda:0")
    parser.add_argument(
        "--suite",
        default="all",
        choices=["all", "production", "regression", "wrapper", "edge", "methodology"],
    )
    parser.add_argument("--skip-candidate", action="store_true")
    args = parser.parse_args()

    if not torch.cuda.is_available():
        raise SystemExit("CUDA required")
    device = torch.device(args.device)
    torch.cuda.set_device(device)
    torch.set_grad_enabled(False)

    cand = None if args.skip_candidate else candidate_fn()

    suites = {
        "production": suite_production,
        "regression": suite_regression,
        "wrapper": suite_wrapper,
        "edge": suite_edge,
        "methodology": suite_methodology,
    }
    selected = suites.values() if args.suite == "all" else [suites[args.suite]]
    for fn in selected:
        fn(device, cand)

    leaked = sorted(m for m in sys.modules if m == "sglang" or m.startswith("sglang."))
    _record("purity_no_sglang_modules", not leaked, f"leaked: {leaked[:5]}")

    print(f"\n{_passes} passed, {len(_failures)} failed")
    if _failures:
        for f in _failures:
            print(f"  FAILED: {f}")
        return 1
    print("CORRECTNESS_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
