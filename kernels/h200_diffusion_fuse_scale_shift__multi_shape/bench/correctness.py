#!/usr/bin/env python3
"""Correctness runner: candidate (solution/ dispatcher) vs vendored baseline vs FP32 reference.

Suites (bench/cases.py): production (15 captured rows), grid (canonical
regression grid), negative (out-of-contract parity). Every comparison applies
NaN/Inf guards, the oracle's fixed tolerances, and the dynamic
quantization-noise cross-check (bench/reference.py).

Routing contract enforced:
- While an op has no native kernel (native_status False), fallback is expected.
- Once native exists: grid cases MUST route native; production cases route
  native unless their bucket is a recorded perf-fallback decision.

Usage:
  python bench/correctness.py [--suite all|production|grid|negative]
                              [--filter SUBSTR] [--list] [--self-check]
                              [--json PATH] [--max-cases N]
Env: KDA_CI=1 selects the upstream CI subsets.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
import traceback
from pathlib import Path

KERNEL_DIR = Path(__file__).resolve().parents[1]
if str(KERNEL_DIR) not in sys.path:
    sys.path.insert(0, str(KERNEL_DIR))

import torch  # noqa: E402

from bench import cases as cases_mod  # noqa: E402
from bench import reference as ref_mod  # noqa: E402

_BANNED_MODULE_PREFIXES = ("sglang.jit_kernel.diffusion", "sglang.multimodal_gen")

_OUTPUT_NAMES = {
    cases_mod.OP_SCALE_SHIFT: ("y",),
    cases_mod.OP_SELECT01: ("output", "gate_out"),
    cases_mod.OP_RESIDUAL: ("output", "residual_out", "gate_out"),
}

_RUNTIME = None


def _runtime():
    """Lazy-load the Triton baseline and the dispatcher (CUDA box only)."""
    global _RUNTIME
    if _RUNTIME is None:
        from baseline import scale_shift as baseline_mod
        from solution import dispatch

        baseline_fns = {
            cases_mod.OP_SCALE_SHIFT: baseline_mod.fuse_scale_shift_kernel,
            cases_mod.OP_SELECT01: baseline_mod.fuse_layernorm_scale_shift_gate_select01_kernel,
            cases_mod.OP_RESIDUAL: (
                baseline_mod.fuse_residual_layernorm_scale_shift_gate_select01_kernel
            ),
        }
        dispatch_fns = {
            cases_mod.OP_SCALE_SHIFT: dispatch.fuse_scale_shift_kernel,
            cases_mod.OP_SELECT01: dispatch.fuse_layernorm_scale_shift_gate_select01_kernel,
            cases_mod.OP_RESIDUAL: (
                dispatch.fuse_residual_layernorm_scale_shift_gate_select01_kernel
            ),
        }
        _RUNTIME = (baseline_fns, dispatch_fns, dispatch)
    return _RUNTIME


_REF_FNS = {
    cases_mod.OP_SCALE_SHIFT: ref_mod.ref_fuse_scale_shift,
    cases_mod.OP_SELECT01: ref_mod.ref_layernorm_select01,
    cases_mod.OP_RESIDUAL: ref_mod.ref_residual_layernorm_select01,
}


def _as_tuple(out):
    return out if isinstance(out, tuple) else (out,)


def _assert_no_banned_imports() -> None:
    bad = [m for m in sys.modules if m.startswith(_BANNED_MODULE_PREFIXES)]
    if bad:
        raise RuntimeError(
            "no-live-SGLang gate violated: harness imported banned modules: "
            + ", ".join(sorted(bad))
        )


def _expected_route(case, dispatch) -> str:
    """Return 'native', 'fallback', or 'any' for normal-compare cases."""
    if not dispatch.native_status().get(case.op, False):
        return "fallback"
    if case.suite == "grid":
        return "native"
    if case.suite == "production":
        bucket = case.meta.get("bucket") or case.case_id
        if bucket in dispatch.PERF_FALLBACK.get(case.op, set()):
            return "fallback"
        return "native"
    return "any"


def run_case(case, device: torch.device) -> dict:
    record = {"case_id": case.case_id, "op": case.op, "suite": case.suite, "status": "pass"}
    baseline_fns, dispatch_fns, dispatch = _runtime()
    base_fn = baseline_fns[case.op]
    cand_fn = dispatch_fns[case.op]

    if case.kind == "error_parity":
        args, kwargs = case.build(device)
        base_exc = cand_exc = None
        try:
            base_fn(*args, **kwargs)
        except Exception as exc:  # noqa: BLE001 - parity check needs the type
            base_exc = type(exc)
        dispatch.consume_last_route()  # clear any stale route
        try:
            cand_fn(*args, **kwargs)
        except Exception as exc:  # noqa: BLE001
            cand_exc = type(exc)
        route = dispatch.consume_last_route()
        if base_exc is None or not issubclass(base_exc, case.expected_errors):
            raise AssertionError(
                f"{case.case_id}: baseline raised {base_exc}, expected {case.expected_errors}"
            )
        if cand_exc is not base_exc:
            raise AssertionError(
                f"{case.case_id}: error parity broken: baseline={base_exc} candidate={cand_exc}"
            )
        # Out-of-contract signatures must never have entered a native kernel.
        if route is None or route[0] != "fallback":
            raise AssertionError(
                f"{case.case_id}: out-of-contract input did not route to fallback: {route}"
            )
        record["error_type"] = base_exc.__name__
        record["route"] = route
        return record

    args, kwargs = case.build(device)
    base_out = _as_tuple(base_fn(*args, **kwargs))
    cand_out = _as_tuple(cand_fn(*args, **kwargs))
    route = dispatch.consume_last_route()
    record["route"] = route

    if case.kind == "fallback_parity":
        if route is None or route[0] != "fallback":
            raise AssertionError(f"{case.case_id}: expected fallback route, got {route}")
        for name, b, c in zip(_OUTPUT_NAMES[case.op], base_out, cand_out):
            if not torch.equal(b, c):
                raise AssertionError(f"{case.case_id}: fallback output {name} != baseline")
        return record

    expected = _expected_route(case, dispatch)
    if expected != "any":
        if route is None or route[0] != expected:
            raise AssertionError(
                f"{case.case_id}: route mismatch: expected {expected}, got {route} "
                f"(native_status={dispatch.native_status()})"
            )

    ref_out = _as_tuple(_REF_FNS[case.op](*args, **kwargs))
    metrics = []
    for name, c, b, r in zip(_OUTPUT_NAMES[case.op], cand_out, base_out, ref_out):
        metrics.append(ref_mod.check_outputs(
            name, c, b, r, case.x_dtype, tol_override=case.tol_override))
    record["metrics"] = metrics
    return record


def comparator_self_check() -> None:
    """Verify the comparator rejects corruption and NaN (runs on CPU)."""
    torch.manual_seed(0)
    ref32 = torch.randn(64, 64, dtype=torch.float32)
    base = ref32.to(torch.bfloat16)

    ref_mod.check_outputs("selfcheck_good", base.clone(), base, ref32, torch.bfloat16)

    failed = False
    try:
        bad = (base.float() + 0.5).to(torch.bfloat16)
        ref_mod.check_outputs("selfcheck_corrupt", bad, base, ref32, torch.bfloat16)
    except ref_mod.ToleranceError:
        failed = True
    if not failed:
        raise AssertionError("comparator self-check FAILED: corruption not caught")

    failed = False
    try:
        nan = base.clone()
        nan[0, 0] = float("nan")
        ref_mod.check_outputs("selfcheck_nan", nan, base, ref32, torch.bfloat16)
    except ref_mod.ToleranceError:
        failed = True
    if not failed:
        raise AssertionError("comparator self-check FAILED: NaN not caught")
    print("comparator self-check: OK (corruption and NaN both rejected)")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--suite", default="all",
                    choices=["all", "production", "grid", "negative"])
    ap.add_argument("--filter", default="", help="substring filter on case ids")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--self-check", action="store_true")
    ap.add_argument("--json", default="", help="write a JSON report to this path")
    ap.add_argument("--max-cases", type=int, default=0, help="debug: cap case count")
    args = ap.parse_args()

    if args.self_check:
        comparator_self_check()
        return 0

    suites = ("production", "grid", "negative") if args.suite == "all" else (args.suite,)
    case_list = [c for c in cases_mod.all_cases(suites) if args.filter in c.case_id]
    if args.max_cases:
        case_list = case_list[: args.max_cases]

    if args.list:
        for c in case_list:
            print(f"{c.suite:11s} {c.op:18s} {c.case_id}")
        print(f"total: {len(case_list)} cases (KDA_CI={'1' if cases_mod._ci_enabled() else '0'})")
        return 0

    if not torch.cuda.is_available():
        print("ERROR: CUDA device required (run inside the remote container)", file=sys.stderr)
        return 2

    device = torch.device("cuda")
    print(f"device: {torch.cuda.get_device_name(device)}  cases: {len(case_list)}  "
          f"CI={'1' if cases_mod._ci_enabled() else '0'}")

    results, failures = [], []
    t0 = time.time()
    for i, case in enumerate(case_list):
        try:
            rec = run_case(case, device)
        except Exception as exc:  # noqa: BLE001 - collect all failures
            rec = {
                "case_id": case.case_id, "op": case.op, "suite": case.suite,
                "status": "fail", "error": f"{type(exc).__name__}: {exc}",
                "traceback": traceback.format_exc(limit=6),
            }
            failures.append(rec)
            print(f"[FAIL {len(failures):3d}] {case.case_id}\n        {rec['error']}")
        results.append(rec)
        if (i + 1) % 200 == 0:
            print(f"  ... {i + 1}/{len(case_list)} ({time.time() - t0:.1f}s)")

    _assert_no_banned_imports()

    n_pass = sum(1 for r in results if r["status"] == "pass")
    route_counts: dict[str, int] = {}
    for r in results:
        rt = r.get("route")
        if rt:
            route_counts[rt[0]] = route_counts.get(rt[0], 0) + 1
    summary = {
        "total": len(results), "pass": n_pass, "fail": len(failures),
        "routes": route_counts, "elapsed_s": round(time.time() - t0, 1),
        "ci_subset": cases_mod._ci_enabled(),
        "native_status": _runtime()[2].native_status(),
        "device": torch.cuda.get_device_name(device),
        "torch": torch.__version__,
    }
    print(json.dumps(summary, indent=2))

    if args.json:
        out_path = Path(args.json)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps({"summary": summary, "results": results}, indent=1))
        print(f"report written: {out_path}")

    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
