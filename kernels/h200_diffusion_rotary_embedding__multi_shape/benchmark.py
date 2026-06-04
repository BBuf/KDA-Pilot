#!/usr/bin/env python3
"""Isolated benchmark for ``h200_diffusion_rotary_embedding__multi_shape``.

Reuses ``tests/test_correctness.py`` cases/baseline/candidate and appends
self-describing blocks to ``benchmark.csv``.

Modes (``--mode``):

* ``legacy``       -- the original sequential timing (all baseline reps, then all
  candidate reps). Schema unchanged for comparability with prior headlines.
* ``interleaved``  -- symmetric same-process A/B: after both sides are fully warmed
  (JIT build, Triton autotune, imports, register module cached), baseline and
  candidate samples alternate one-for-one so clock/thermal drift hits both sides
  equally. Each case also gets device-only timing (CUDA events around the call,
  alternating the same way) and a DEVICE-vs-HOST decomposition:
  ``host_residual = wall_median - device_median`` per side.
* ``both`` (default) -- legacy block first, then the interleaved block.

Shipping symmetry: each side is invoked through its full public shipping path at
the same callsite -- baseline = the SGLang public function, candidate = the
wrapped public callable (what production resolves to after the swap) -- with
identical warmup/caching treatment and allocation included on both paths (both
return a new tensor). The decomposition then isolates the device kernel from the
host/integration layer, so host-only deltas can never be claimed as kernel wins.

Provenance (host / GPU id+model / idle-before+after / commits / oracle
equivalence / command / run dir / candidate id) comes from KDA_* env vars plus
auto-collected fields (torch/CUDA/Triton versions, imported SGLang HEAD, sha1 of
the imported diffusion RoPE baseline files vs the pinned oracle) and is written
as a leading ``# provenance:`` comment so runs are comparable.
"""

from __future__ import annotations

import argparse
import csv
import importlib.util
import math
import os
import statistics
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

try:
    import torch
except ImportError:  # pragma: no cover
    torch = None


KERNEL_SLUG = "h200_diffusion_rotary_embedding__multi_shape"
KERNEL_DIR = Path(__file__).resolve().parent

_STATS = ("median", "mean", "std", "min", "p10", "p90")


def _load_correctness_module():
    test_py = KERNEL_DIR / "tests" / "test_correctness.py"
    spec = importlib.util.spec_from_file_location("kda_correctness_scaffold", test_py)
    assert spec is not None and spec.loader is not None, test_py
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _sync() -> None:
    if torch is not None and torch.cuda.is_available():
        torch.cuda.synchronize()


def _time_call(fn: Callable[[dict], Any], case: dict, *, warmup: int, iters: int) -> list[float]:
    for _ in range(warmup):
        fn(case)
    _sync()
    samples = []
    for _ in range(iters):
        start = time.perf_counter()
        fn(case)
        _sync()
        samples.append((time.perf_counter() - start) * 1e6)
    return samples


def _time_interleaved(
    fn_a: Callable[[dict], Any],
    fn_b: Callable[[dict], Any],
    case: dict,
    *,
    warmup: int,
    iters: int,
) -> tuple[list[float], list[float]]:
    """Wall-clock A/B in one process: warm both sides, then alternate samples."""
    for _ in range(warmup):
        fn_a(case)
        fn_b(case)
    _sync()
    a_samples: list[float] = []
    b_samples: list[float] = []
    for _ in range(iters):
        start = time.perf_counter()
        fn_a(case)
        _sync()
        a_samples.append((time.perf_counter() - start) * 1e6)
        start = time.perf_counter()
        fn_b(case)
        _sync()
        b_samples.append((time.perf_counter() - start) * 1e6)
    return a_samples, b_samples


def _time_device_interleaved(
    fn_a: Callable[[dict], Any],
    fn_b: Callable[[dict], Any],
    case: dict,
    *,
    warmup: int,
    iters: int,
    batch: int = 10,
) -> tuple[list[float], list[float]]:
    """Device-only (CUDA-event) A/B: pipelined batched kernel time, alternating sides.

    Each sample brackets ``batch`` back-to-back un-synced calls with one event
    pair and reports ``elapsed / batch``. Because the host runs ahead of the
    queued kernels, launch overhead overlaps execution and the span converges
    to the sum of kernel times -- the device-fair number for kernel claims
    (the same CUDA-event methodology as the prior round's kernel-vs-kernel
    cross-check). Caveat: when the kernel is shorter than the per-launch host
    cost (tiny shapes), the GPU still starves between kernels and this number
    keeps some gap -- NCU kernel time is the arbiter for those buckets.
    """
    assert torch is not None and torch.cuda.is_available(), "device timing needs CUDA"
    assert batch >= 1
    for _ in range(warmup):
        fn_a(case)
        fn_b(case)
    _sync()
    a_samples: list[float] = []
    b_samples: list[float] = []
    for _ in range(iters):
        for fn, out in ((fn_a, a_samples), (fn_b, b_samples)):
            ev_start = torch.cuda.Event(enable_timing=True)
            ev_end = torch.cuda.Event(enable_timing=True)
            ev_start.record()
            for _ in range(batch):
                fn(case)
            ev_end.record()
            _sync()
            out.append(ev_start.elapsed_time(ev_end) * 1e3 / batch)  # ms -> us/call
    return a_samples, b_samples


def _summary(samples: list[float]) -> dict[str, float]:
    ordered = sorted(samples)

    def pct(p: float) -> float:
        index = min(len(ordered) - 1, max(0, round((len(ordered) - 1) * p)))
        return ordered[index]

    return {
        "median": statistics.median(ordered),
        "mean": statistics.mean(ordered),
        "std": statistics.pstdev(ordered) if len(ordered) > 1 else 0.0,
        "min": ordered[0],
        "p10": pct(0.10),
        "p90": pct(0.90),
    }


def _geom_mean(values: list[float]) -> float:
    cleaned = [v for v in values if math.isfinite(v) and v > 0]
    if not cleaned:
        return float("nan")
    return math.exp(sum(math.log(v) for v in cleaned) / len(cleaned))


def _auto_provenance(correctness) -> dict[str, str]:
    """Auto-collected baseline-lock fields (best effort; blank when unavailable)."""
    info: dict[str, str] = {}
    if torch is not None:
        info["torch"] = str(torch.__version__)
        info["cuda"] = str(getattr(torch.version, "cuda", "") or "")
    else:
        info["torch"] = info["cuda"] = ""
    try:
        import triton  # type: ignore

        info["triton"] = str(triton.__version__)
    except Exception:
        info["triton"] = ""
    try:
        info["sglang_head"] = correctness._sglang_git_head() or ""
    except Exception:
        info["sglang_head"] = ""
    try:
        sha = correctness._imported_oracle_file_sha1()
        pin = correctness.SGLANG_ORACLE_FILE_SHA1
        info["rotary_sha1"] = str(sha.get("rotary.py", ""))[:9]
        info["ltx2_sha1"] = str(sha.get("ltx2_rotary.py", ""))[:9]
        info["oracle_pin_match"] = str(all(sha.get(k) == v for k, v in pin.items()))
    except Exception:
        info["rotary_sha1"] = info["ltx2_sha1"] = ""
        info["oracle_pin_match"] = "unknown"
    return info


def _provenance(correctness) -> str:
    gpu_model = os.environ.get("KDA_GPU_MODEL", "")
    if not gpu_model and torch is not None and torch.cuda.is_available():
        try:
            gpu_model = torch.cuda.get_device_name(0)
        except Exception:
            gpu_model = ""
    fields = {
        "candidate": os.environ.get("KDA_CANDIDATE", "native_cuda"),
        "kernel_pilot_commit": os.environ.get("KDA_KP_COMMIT", ""),
        "src_hash": os.environ.get("KDA_SRC_HASH", ""),
        "sglang_commit": os.environ.get("KDA_SGLANG_COMMIT", ""),
        "oracle_equiv": os.environ.get("KDA_ORACLE_EQUIV", ""),
        "host": os.environ.get("KDA_HOST", ""),
        "gpu_id": os.environ.get("KDA_GPU_ID", os.environ.get("CUDA_VISIBLE_DEVICES", "")),
        "gpu_model": gpu_model,
        "idle_before": os.environ.get("KDA_IDLE_BEFORE", ""),
        "idle_after": os.environ.get("KDA_IDLE_AFTER", ""),
        "run_dir": os.environ.get("KDA_RUN_DIR", ""),
        "cmd": os.environ.get("KDA_CMD", ""),
    }
    fields.update(_auto_provenance(correctness))
    return "# provenance: " + " ".join(f"{k}={v!r}" for k, v in fields.items())


def _select_cases(correctness, only: list[str]) -> list[dict[str, Any]]:
    cases = correctness.make_cases()
    if not cases:
        raise SystemExit("No benchmark cases. Fill tests/test_correctness.py first.")
    if only:
        by_name = {c.get("name"): c for c in cases}
        missing = [n for n in only if n not in by_name]
        if missing:
            raise SystemExit(f"unknown case name(s): {missing}; known: {sorted(by_name)}")
        cases = [by_name[n] for n in only]
    return cases


def _run_legacy(writer, correctness, cases, candidate_id, *, warmup_override, iters_override):
    speedups = []
    header = (
        ["ts", "candidate", "case"]
        + [f"baseline_{s}_us" for s in _STATS]
        + [f"cand_{s}_us" for s in _STATS]
        + ["speedup"]
    )
    writer.writerow(header)
    for case in cases:
        warmup = warmup_override or int(case.get("warmup", 25))
        iters = iters_override or int(case.get("iters", 100))
        b = _summary(_time_call(correctness.baseline, case, warmup=warmup, iters=iters))
        c = _summary(_time_call(correctness.candidate, case, warmup=warmup, iters=iters))
        speedup = (b["median"] / c["median"]) if c["median"] > 0 else float("nan")
        speedups.append(speedup)
        now = datetime.now(timezone.utc).isoformat()
        row = (
            [now, candidate_id, case.get("name", "unknown")]
            + [f"{b[s]:.6f}" for s in _STATS]
            + [f"{c[s]:.6f}" for s in _STATS]
            + [f"{speedup:.6f}x" if math.isfinite(speedup) else ""]
        )
        writer.writerow(row)
        print("[legacy]", case.get("name", "unknown"), "speedup_x", speedup)
    writer.writerow(
        [datetime.now(timezone.utc).isoformat(), "geomean", "all_configured_shapes"]
        + [""] * (2 * len(_STATS))
        + [f"{_geom_mean(speedups):.6f}x"]
    )
    print("[legacy] geomean_speedup_x", _geom_mean(speedups))
    return _geom_mean(speedups)


def _run_interleaved(
    writer, correctness, cases, candidate_id, *, warmup_override, iters_override, device_batch=10
):
    wall_speedups: list[float] = []
    dev_speedups: list[float] = []
    header = (
        ["ts", "candidate", "case"]
        + [f"baseline_wall_{s}_us" for s in _STATS]
        + [f"cand_wall_{s}_us" for s in _STATS]
        + [
            "wall_speedup",
            "baseline_dev_median_us",
            "baseline_dev_std_us",
            "cand_dev_median_us",
            "cand_dev_std_us",
            "device_speedup",
            "baseline_host_resid_us",
            "cand_host_resid_us",
        ]
    )
    writer.writerow(header)
    for case in cases:
        warmup = warmup_override or int(case.get("warmup", 25))
        iters = iters_override or int(case.get("iters", 100))
        bw_s, cw_s = _time_interleaved(
            correctness.baseline, correctness.candidate, case, warmup=warmup, iters=iters
        )
        bd_s, cd_s = _time_device_interleaved(
            correctness.baseline,
            correctness.candidate,
            case,
            warmup=max(5, warmup // 5),
            iters=max(20, iters // 4),
            batch=device_batch,
        )
        bw, cw = _summary(bw_s), _summary(cw_s)
        bd, cd = _summary(bd_s), _summary(cd_s)
        wall_speedup = (bw["median"] / cw["median"]) if cw["median"] > 0 else float("nan")
        dev_speedup = (bd["median"] / cd["median"]) if cd["median"] > 0 else float("nan")
        wall_speedups.append(wall_speedup)
        dev_speedups.append(dev_speedup)
        b_resid = bw["median"] - bd["median"]
        c_resid = cw["median"] - cd["median"]
        now = datetime.now(timezone.utc).isoformat()
        row = (
            [now, candidate_id, case.get("name", "unknown")]
            + [f"{bw[s]:.6f}" for s in _STATS]
            + [f"{cw[s]:.6f}" for s in _STATS]
            + [
                f"{wall_speedup:.6f}x" if math.isfinite(wall_speedup) else "",
                f"{bd['median']:.6f}",
                f"{bd['std']:.6f}",
                f"{cd['median']:.6f}",
                f"{cd['std']:.6f}",
                f"{dev_speedup:.6f}x" if math.isfinite(dev_speedup) else "",
                f"{b_resid:.6f}",
                f"{c_resid:.6f}",
            ]
        )
        writer.writerow(row)
        print(
            "[interleaved]",
            case.get("name", "unknown"),
            "wall_x",
            round(wall_speedup, 4),
            "device_x",
            round(dev_speedup, 4),
            "host_resid_us(base,cand)",
            (round(b_resid, 2), round(c_resid, 2)),
        )
    writer.writerow(
        [datetime.now(timezone.utc).isoformat(), "geomean_interleaved", "all_configured_shapes"]
        + [""] * (2 * len(_STATS))
        + [
            f"{_geom_mean(wall_speedups):.6f}x",
            "",
            "",
            "",
            "",
            f"{_geom_mean(dev_speedups):.6f}x",
            "",
            "",
        ]
    )
    print("[interleaved] geomean wall_x", _geom_mean(wall_speedups), "device_x", _geom_mean(dev_speedups))
    return _geom_mean(wall_speedups), _geom_mean(dev_speedups)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=("legacy", "interleaved", "both"), default="both")
    parser.add_argument(
        "--case",
        action="append",
        default=[],
        help="restrict to the named case(s); repeatable; default: all 6",
    )
    parser.add_argument("--warmup", type=int, default=0, help="override per-case warmup")
    parser.add_argument("--iters", type=int, default=0, help="override per-case iters")
    parser.add_argument(
        "--device-batch",
        type=int,
        default=10,
        help="back-to-back un-synced calls per device-timing sample (pipelined kernel time)",
    )
    args = parser.parse_args()

    correctness = _load_correctness_module()
    cases = _select_cases(correctness, args.case)
    candidate_id = os.environ.get("KDA_CANDIDATE", "native_cuda")
    csv_path = KERNEL_DIR / "benchmark.csv"
    with csv_path.open("a", newline="") as f:
        writer = csv.writer(f)
        f.write(_provenance(correctness) + "\n")
        if args.mode in ("legacy", "both"):
            _run_legacy(
                writer, correctness, cases, candidate_id,
                warmup_override=args.warmup, iters_override=args.iters,
            )
        if args.mode in ("interleaved", "both"):
            _run_interleaved(
                writer, correctness, cases, candidate_id,
                warmup_override=args.warmup, iters_override=args.iters,
                device_batch=args.device_batch,
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
