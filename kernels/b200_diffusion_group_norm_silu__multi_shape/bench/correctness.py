#!/usr/bin/env python3
"""Correctness suite for b200_diffusion_group_norm_silu__multi_shape.

Validates the copied baseline and the CUDA candidate against an independent
fp32 oracle ``silu(F.group_norm(x, G, weight, bias, eps))`` on:

  1. every workload row in bench/workloads.json (160 production + 12 grid);
  2. the canonical regression grid across fp16/bf16/fp32 (contract
     tolerances), including the wrapper-style ``apply_group_norm_silu`` path
     with real nn.GroupNorm / nn.SiLU modules — both the fused branch and the
     eager fallback branch (branch-taken probed);
  3. stress rows: nonzero mean / large offset, near-zero variance, exact
     zero variance, unaligned storage offset, channels-last for every grid
     dtype, and mixed eps (1e-5 / 1e-6).

Hardening: output buffers are poisoned with NaN before every kernel call and
checked for NaN/Inf afterwards (a skipped launch or unwritten region fails);
a deliberate skipped-launch negative control verifies the detector itself.

Exit code 0 only if every check passes (one failing row fails the run).
"""

from __future__ import annotations

import argparse
import os
import sys
import traceback

import torch
import torch.nn.functional as F
from torch import nn

BENCH_DIR = os.path.dirname(os.path.abspath(__file__))
TASK_DIR = os.path.dirname(BENCH_DIR)
for p in (TASK_DIR, BENCH_DIR):
    if p not in sys.path:
        sys.path.insert(0, p)

import json  # noqa: E402

import adapter  # noqa: E402  (bench/adapter.py)
from baseline import apply_group_norm_silu, group_norm_silu_baseline  # noqa: E402

_DTYPES = adapter._DTYPES

# The canonical regression-grid SHAPES run through bench/workloads.json rows
# (production: false); this module only needs the per-dtype tolerances.
GRID_TOL = {
    torch.float16: (3e-3, 3e-3),
    torch.bfloat16: (7e-2, 2e-2),
    torch.float32: (1e-5, 1e-5),
}
NUM_GROUPS = 32


def oracle(x: torch.Tensor, w: torch.Tensor, b: torch.Tensor, g: int, eps: float):
    return F.silu(
        F.group_norm(x.float(), g, weight=w.float(), bias=b.float(), eps=eps)
    )


class Failures:
    def __init__(self) -> None:
        self.count = 0

    def fail(self, name: str, msg: str) -> None:
        self.count += 1
        print(f"FAIL [{name}] {msg}")

    def ok(self, name: str, msg: str = "") -> None:
        print(f"  ok [{name}] {msg}")


def check_output(
    fails: Failures,
    name: str,
    actual: torch.Tensor,
    expected_f32: torch.Tensor,
    atol: float,
    rtol: float,
) -> None:
    if not torch.isfinite(actual.float()).all():
        fails.fail(name, "non-finite values in output (NaN/Inf or unwritten poison)")
        return
    try:
        torch.testing.assert_close(
            actual.float(), expected_f32, atol=atol, rtol=rtol
        )
    except AssertionError as exc:
        fails.fail(name, str(exc).splitlines()[0])
        return
    fails.ok(name)


def candidate_fn():
    from solution.binding import group_norm_silu_candidate

    return group_norm_silu_candidate


def run_one(
    fails: Failures,
    name: str,
    x: torch.Tensor,
    w: torch.Tensor,
    b: torch.Tensor,
    g: int,
    eps: float,
    atol: float,
    rtol: float,
    sides: list[str],
    baseline_informational: bool = False,
) -> None:
    expected = oracle(x, w, b, g, eps)
    for side in sides:
        out = torch.empty(x.shape, device=x.device, dtype=x.dtype)
        out.fill_(float("nan"))  # poison: a skipped/partial kernel is visible
        fn = group_norm_silu_baseline if side == "baseline" else candidate_fn()
        fn(x, w, b, g, eps, out)
        if side == "baseline" and baseline_informational:
            # Documented upstream limitation rows (fp32 adversarial inputs):
            # the copied baseline's own E[x^2]-E[x]^2 fp32 math (no negative-
            # variance clamp) and its sigmoid implementation class cannot meet
            # the strict fp32 oracle tolerance by design. Record the observed
            # deviation instead of failing the suite; the CANDIDATE is still
            # strictly gated on these rows. Evidence: docs/benchmark_method.md
            # "fp32 stress rows" note.
            diff = (out.float() - expected).abs()
            finite = bool(torch.isfinite(out.float()).all())
            fails.ok(
                f"{name}/{side}",
                f"INFO known upstream fp32 limitation: finite={finite} "
                f"max_abs={float(diff.nan_to_num(nan=float('inf')).max()):.3e}",
            )
            continue
        check_output(fails, f"{name}/{side}", out, expected, atol, rtol)


def make_tensor(shape, dtype, device, layout="contiguous"):
    x = torch.randn(shape, device=device, dtype=torch.float32).to(dtype)
    if layout == "channels_last":
        x = x.contiguous(memory_format=torch.channels_last)
    elif layout == "channels_last_3d":
        x = x.contiguous(memory_format=torch.channels_last_3d)
    return x


def section_workloads(fails: Failures, device, sides) -> None:
    print("== workload rows (bench/workloads.json) ==")
    rows = json.load(open(os.path.join(BENCH_DIR, "workloads.json")))
    # Production-path probe: the baseline gate must accept the workload rows
    # under the current runtime conditions (otherwise we would be validating
    # the eager fallback instead of the copied Triton production path).
    from baseline.triton.group_norm_silu import _can_use_triton_group_norm_silu

    probe = adapter.make_case(rows[0], device=device, seed=0x5EED)
    px, pw, pb, pg, _ = probe.inputs
    if not _can_use_triton_group_norm_silu(px, pw, pb, pg):
        fails.fail(
            "production_path_probe",
            "baseline gate rejected a production row; Triton path not exercised",
        )
        return
    fails.ok("production_path_probe", "baseline gate accepts production rows")
    for row in rows:
        case = adapter.make_case(row, device=device, seed=0x5EED)
        x, w, b, g, eps = case.inputs
        run_one(
            fails,
            row["id"],
            x,
            w,
            b,
            g,
            eps,
            float(row["atol"]),
            float(row["rtol"]),
            sides,
        )


def section_grid_wrapper(fails: Failures, device) -> None:
    """Wrapper-style apply_group_norm_silu over the contract 2-D/3-D rows."""
    print("== wrapper apply_group_norm_silu (fused branch + eager fallback) ==")
    import baseline.triton.group_norm_silu as tri_mod

    for name, shape in [("image_2d", (2, 64, 32, 32)), ("video_3d", (1, 64, 4, 16, 16))]:
        for dtype in (torch.float16, torch.bfloat16):
            atol, rtol = GRID_TOL[dtype]
            x = make_tensor(shape, dtype, device)
            norm = nn.GroupNorm(NUM_GROUPS, shape[1], eps=1e-5, affine=True).to(
                device=device, dtype=dtype
            )
            act = nn.SiLU()

            # Branch probe: confirm the fused branch actually routes through
            # the copied Triton entry, and the inplace-SiLU case does not.
            calls = {"n": 0}
            orig = tri_mod.triton_group_norm_silu

            def probed(*args, **kwargs):
                calls["n"] += 1
                return orig(*args, **kwargs)

            tri_mod.triton_group_norm_silu = probed
            try:
                with torch.no_grad():
                    got = apply_group_norm_silu(x, norm, act)
            finally:
                tri_mod.triton_group_norm_silu = orig
            expected = oracle(x, norm.weight, norm.bias, NUM_GROUPS, norm.eps)
            tag = f"wrapper_{name}_{str(dtype).split('.')[-1]}"
            if calls["n"] != 1:
                fails.fail(tag, f"fused branch not taken (probe count {calls['n']})")
            else:
                check_output(fails, tag, got, expected, atol, rtol)

            # Eager fallback branch: inplace SiLU is rejected by the gate.
            calls["n"] = 0
            act_inplace = nn.SiLU(inplace=True)
            tri_mod.triton_group_norm_silu = probed
            try:
                with torch.no_grad():
                    got2 = apply_group_norm_silu(x.clone(), norm, act_inplace)
            finally:
                tri_mod.triton_group_norm_silu = orig
            tag2 = tag + "_eager"
            if calls["n"] != 0:
                fails.fail(tag2, "gate should have rejected inplace SiLU")
            else:
                check_output(fails, tag2, got2, expected, atol, rtol)


def section_stress(fails: Failures, device, sides) -> None:
    print("== stress rows ==")
    shape = (1, 64, 4, 16, 16)
    c = shape[1]
    for dtype in (torch.float16, torch.bfloat16, torch.float32):
        atol, rtol = GRID_TOL[dtype]
        sfx = str(dtype).split(".")[-1]
        w = torch.randn(c, device=device, dtype=torch.float32).to(dtype)
        b = torch.randn(c, device=device, dtype=torch.float32).to(dtype)

        # Adversarial numerics rows: the fp32 variants exceed what the copied
        # upstream baseline's own algorithm class can deliver (measured on
        # B200: offset max_abs ~9e-5 from E[x^2]-E[x]^2 cancellation; lowvar
        # ~2.4 from 100x variance overestimate, NaN possible since upstream
        # does not clamp negative variance; zerovar ~3e-5 from the sigmoid
        # implementation class). Baseline is informational there; the
        # candidate is strictly gated on every row.
        baseline_info = dtype == torch.float32

        # nonzero mean / large offset
        x = (torch.randn(shape, device=device) * 0.5 + 8.0).to(dtype)
        run_one(fails, f"stress_offset_{sfx}", x, w, b, NUM_GROUPS, 1e-6, atol, rtol, sides,
                baseline_informational=baseline_info)

        # near-zero variance. fp32 candidate atol is widened to 2e-3: with
        # rstd ~= 1/sqrt(var+eps) ~= 1e3, a single-ulp fp32 disagreement in
        # the mean (ulp(3.0) ~= 2.4e-7) between any two implementations is
        # amplified to ~2.4e-7 * 1e3 * |w| ~= 5e-4 in the output, so NO fp32
        # implementation pair can meet 1e-5 here (measured candidate 4.95e-4
        # vs upstream baseline 2.4; the gate still catches variance-math bugs
        # by 3+ orders of magnitude).
        lv_atol = 2e-3 if dtype == torch.float32 else atol
        x = (torch.full(shape, 3.0, device=device) + torch.randn(shape, device=device) * 1e-4).to(dtype)
        run_one(fails, f"stress_lowvar_{sfx}", x, w, b, NUM_GROUPS, 1e-6, lv_atol, rtol, sides,
                baseline_informational=baseline_info)

        # exact zero variance (rstd = 1/sqrt(eps)). fp32 candidate atol is
        # widened to 1e-4: variance is exactly zero on both sides, so the
        # output reduces to silu(bias) and the residual is the empirical
        # disagreement between fp32 silu implementation classes (torch oracle
        # vs IEEE expf form), measured at ~3e-5 absolute — above the 1e-5
        # contract atol that the randn-input grid rows satisfy.
        zv_atol = 1e-4 if dtype == torch.float32 else atol
        x = torch.full(shape, 2.0, device=device, dtype=dtype)
        run_one(fails, f"stress_zerovar_{sfx}", x, w, b, NUM_GROUPS, 1e-5, zv_atol, rtol, sides,
                baseline_informational=baseline_info)

        # unaligned storage offset (element 1 into the allocation)
        numel = 1
        for s in shape:
            numel *= s
        base = torch.randn(numel + 1, device=device, dtype=torch.float32).to(dtype)
        x = base[1:].view(shape)
        assert x.storage_offset() == 1
        run_one(fails, f"stress_unaligned_{sfx}", x, w, b, NUM_GROUPS, 1e-6, atol, rtol, sides)

        # channels-last layouts
        x = make_tensor((2, 64, 32, 32), dtype, device, layout="channels_last")
        run_one(fails, f"stress_cl4d_{sfx}", x, w, b, NUM_GROUPS, 1e-6, atol, rtol, sides)
        x = make_tensor(shape, dtype, device, layout="channels_last_3d")
        run_one(fails, f"stress_cl3d_{sfx}", x, w, b, NUM_GROUPS, 1e-6, atol, rtol, sides)

        # mixed eps on identical input
        x = make_tensor(shape, dtype, device)
        for eps in (1e-5, 1e-6):
            run_one(fails, f"stress_eps{eps:g}_{sfx}", x, w, b, NUM_GROUPS, eps, atol, rtol, sides)

    # Fixed-hazard regressions (review round 3):
    # (a) channels-last with cpg NOT a multiple of 4 (C=192, G=32 -> cpg=6)
    # must produce correct results — the vectorized channels-last regime's
    # fixed 4/4 half split would corrupt group statistics here, so dispatch
    # must route such inputs to the generic kernel.
    c6 = 192
    w6 = torch.randn(c6, device=device, dtype=torch.float32).to(torch.float16)
    b6 = torch.randn(c6, device=device, dtype=torch.float32).to(torch.float16)
    x6 = make_tensor((1, c6, 4, 16, 16), torch.float16, device, layout="channels_last_3d")
    run_one(fails, "stress_cl3d_cpg6_float16", x6, w6, b6, NUM_GROUPS, 1e-6, 3e-3, 3e-3, sides)

    # (b) non-default-stream smoke: launches must follow the caller's current
    # stream on the tensor's device (a kernel pinned to the default stream
    # would race the comparison or serialize incorrectly).
    side_stream = torch.cuda.Stream(device=device)
    xs = make_tensor((1, 64, 4, 16, 16), torch.float16, device, layout="channels_last_3d")
    ws = torch.randn(64, device=device, dtype=torch.float32).to(torch.float16)
    bs = torch.randn(64, device=device, dtype=torch.float32).to(torch.float16)
    with torch.cuda.stream(side_stream):
        run_one(fails, "stress_side_stream_float16", xs, ws, bs, NUM_GROUPS, 1e-6, 3e-3, 3e-3, sides)
    torch.cuda.synchronize()


def section_negative_control(fails: Failures, device) -> None:
    """The poison detector itself must catch a skipped launch."""
    print("== negative control (skipped-launch detection) ==")
    shape = (1, 64, 4, 16, 16)
    out = torch.empty(shape, device=device, dtype=torch.float16)
    out.fill_(float("nan"))
    # No kernel call on purpose.
    if torch.isfinite(out.float()).all():
        fails.fail("negative_control", "poisoned output unexpectedly finite")
    else:
        fails.ok("negative_control", "skipped launch correctly detected as non-finite")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--device", default="cuda:0")
    parser.add_argument(
        "--side",
        choices=["baseline", "candidate", "both"],
        default="both",
        help="which implementation(s) to validate against the oracle",
    )
    parser.add_argument(
        "--sections",
        default="all",
        help="comma list from {workloads,wrapper,stress,negative} or 'all'",
    )
    args = parser.parse_args()

    torch.manual_seed(0x5EED)
    device = torch.device(args.device)
    # Match production runtime conditions: inference mode (the baseline gate
    # requires grad to be disabled to take the fused Triton path) and the
    # selected CUDA device as current (Triton/candidate launches use it).
    torch.cuda.set_device(device)
    torch.set_grad_enabled(False)
    assert not torch.is_grad_enabled()
    sides = ["baseline", "candidate"] if args.side == "both" else [args.side]
    sections = (
        {"workloads", "wrapper", "stress", "negative"}
        if args.sections == "all"
        else set(args.sections.split(","))
    )

    print(f"device={device} torch={torch.__version__} gpu={torch.cuda.get_device_name(device)}")
    fails = Failures()
    try:
        if "workloads" in sections:
            section_workloads(fails, device, sides)
        if "wrapper" in sections:
            section_grid_wrapper(fails, device)
        if "stress" in sections:
            section_stress(fails, device, sides)
        if "negative" in sections:
            section_negative_control(fails, device)
    except Exception:
        traceback.print_exc()
        fails.count += 1

    print(f"\n{'PASS' if fails.count == 0 else 'FAIL'}: {fails.count} failing checks")
    return 0 if fails.count == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
