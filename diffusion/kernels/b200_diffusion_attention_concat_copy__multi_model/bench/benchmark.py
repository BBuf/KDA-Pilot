#!/usr/bin/env python3
"""Standard standalone diffusion kernel benchmark template.

Copy this file to ``bench/benchmark.py`` for a diffusion task, then implement
``bench/adapter.py`` in the same directory. The adapter is intentionally small
so the benchmark policy stays fixed while each task owns its tensor creation and
kernel calls.

Required adapter API:

    make_case(workload: dict, *, device: torch.device, seed: int) -> Case
        Return an object with:
          inputs: tuple/list/dict of CUDA tensors and scalar args
          baseline_outputs: preallocated CUDA output tensors
          candidate_outputs: preallocated CUDA output tensors
          tolerance: {"atol": float, "rtol": float}

    call_baseline(workload: dict, inputs, outputs) -> None
    call_candidate(workload: dict, inputs, outputs) -> None
        Launch the local copied baseline and candidate through the same ABI.
        These functions must not allocate output tensors.

Optional adapter API:

    compare_outputs(workload, baseline_outputs, candidate_outputs, tolerance)
        Return {"ok": bool, "max_abs": float, "max_rel": float, "message": str}
        If absent, the default tensor comparison below is used.

Workload file shape:

    [
      {
        "id": "qwen_4096",
        "production": true,
        "function": "fused_inplace_qknorm_rope",
        "shapes": {...},
        "atol": 1e-2,
        "rtol": 1e-2
      }
    ]
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import os
import platform
import queue
import random
import statistics
import subprocess
import sys
import time
import traceback
from dataclasses import dataclass
from multiprocessing import get_context
from pathlib import Path
from typing import Any, Callable

import torch


ROOT = Path(__file__).resolve().parents[1]
BENCH_DIR = Path(__file__).resolve().parent
DEFAULT_WORKLOADS = BENCH_DIR / "workloads.json"
DEFAULT_OUTPUT = BENCH_DIR / "results.jsonl"


@dataclass
class Stats:
    median_us: float
    mean_us: float
    std_us: float
    min_us: float
    p10_us: float
    p90_us: float
    samples_us: list[float]
    inner_iterations: int


def _load_adapter():
    path = BENCH_DIR / "adapter.py"
    if not path.exists():
        raise FileNotFoundError(
            f"{path} is missing. Implement the adapter API documented at the "
            "top of bench/benchmark.py."
        )
    spec = importlib.util.spec_from_file_location("bench_adapter", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import adapter from {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    for name in ("make_case", "call_baseline", "call_candidate"):
        if not hasattr(module, name):
            raise AttributeError(f"bench/adapter.py must define {name}()")
    return module


def _as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, (list, tuple)):
        return list(value)
    if isinstance(value, dict):
        return list(value.values())
    return [value]


def _case_get(case: Any, name: str) -> Any:
    if isinstance(case, dict):
        return case[name]
    return getattr(case, name)


def _case_get_optional(case: Any, name: str, default: Any = None) -> Any:
    if isinstance(case, dict):
        return case.get(name, default)
    return getattr(case, name, default)


def _stable_u16(text: str) -> int:
    digest = hashlib.sha256(text.encode("utf-8")).digest()
    return int.from_bytes(digest[:2], "little")


def _poison_outputs(outputs: Any) -> None:
    for out in _as_list(outputs):
        if torch.is_tensor(out):
            if out.is_floating_point() or out.is_complex():
                out.fill_(float("nan"))
            else:
                out.fill_(-17)


def _default_compare(
    _workload: dict[str, Any],
    baseline_outputs: Any,
    candidate_outputs: Any,
    tolerance: dict[str, float],
) -> dict[str, Any]:
    base = _as_list(baseline_outputs)
    cand = _as_list(candidate_outputs)
    if len(base) != len(cand):
        return {
            "ok": False,
            "max_abs": math.inf,
            "max_rel": math.inf,
            "message": f"output count mismatch: baseline={len(base)} candidate={len(cand)}",
        }

    atol = float(tolerance.get("atol", 1e-2))
    rtol = float(tolerance.get("rtol", 1e-2))
    max_abs = 0.0
    max_rel = 0.0

    for idx, (lhs, rhs) in enumerate(zip(base, cand)):
        if not torch.is_tensor(lhs) or not torch.is_tensor(rhs):
            if lhs != rhs:
                return {
                    "ok": False,
                    "max_abs": math.inf,
                    "max_rel": math.inf,
                    "message": f"non-tensor output {idx} differs",
                }
            continue
        if lhs.shape != rhs.shape:
            return {
                "ok": False,
                "max_abs": math.inf,
                "max_rel": math.inf,
                "message": f"output {idx} shape mismatch: {tuple(lhs.shape)} vs {tuple(rhs.shape)}",
            }
        if lhs.dtype != rhs.dtype:
            return {
                "ok": False,
                "max_abs": math.inf,
                "max_rel": math.inf,
                "message": f"output {idx} dtype mismatch: {lhs.dtype} vs {rhs.dtype}",
            }

        lhs_f = lhs.detach().float()
        rhs_f = rhs.detach().float()
        if torch.isnan(rhs_f).any() or torch.isinf(rhs_f).any():
            return {
                "ok": False,
                "max_abs": math.inf,
                "max_rel": math.inf,
                "message": f"output {idx} has NaN or Inf",
            }
        diff = (lhs_f - rhs_f).abs()
        denom = lhs_f.abs().clamp_min(1e-12)
        rel = diff / denom
        max_abs = max(max_abs, float(diff.max().item()) if diff.numel() else 0.0)
        max_rel = max(max_rel, float(rel.max().item()) if rel.numel() else 0.0)
        ok = torch.all(diff <= (atol + rtol * lhs_f.abs()))
        if not bool(ok.item()):
            return {
                "ok": False,
                "max_abs": max_abs,
                "max_rel": max_rel,
                "message": f"output {idx} exceeds tolerance atol={atol} rtol={rtol}",
            }

    return {"ok": True, "max_abs": max_abs, "max_rel": max_rel, "message": ""}


def _call_many(fn: Callable[[], None], inner_iterations: int) -> None:
    for _ in range(inner_iterations):
        fn()


def _cuda_event_time_us(fn: Callable[[], None], inner_iterations: int) -> tuple[float, float]:
    torch.cuda.synchronize()
    start = torch.cuda.Event(enable_timing=True)
    end = torch.cuda.Event(enable_timing=True)
    wall_start = time.perf_counter()
    start.record()
    _call_many(fn, inner_iterations)
    end.record()
    end.synchronize()
    wall_end = time.perf_counter()
    elapsed_us = start.elapsed_time(end) * 1000.0 / inner_iterations
    wall_us = (wall_end - wall_start) * 1_000_000.0 / inner_iterations
    return elapsed_us, wall_us


def _calibrate_inner(
    fn: Callable[[], None],
    *,
    inner_min: int,
    inner_max: int,
    target_sample_us: float,
) -> int:
    inner = max(1, inner_min)
    while True:
        elapsed_us, _ = _cuda_event_time_us(fn, inner)
        if elapsed_us * inner >= target_sample_us or inner >= inner_max:
            return inner
        inner = min(inner * 2, inner_max)


def _percentile(values: list[float], pct: float) -> float:
    if not values:
        return math.nan
    if len(values) == 1:
        return values[0]
    ordered = sorted(values)
    rank = (len(ordered) - 1) * pct
    lo = math.floor(rank)
    hi = math.ceil(rank)
    if lo == hi:
        return ordered[lo]
    weight = rank - lo
    return ordered[lo] * (1.0 - weight) + ordered[hi] * weight


def _stats(samples_us: list[float], inner_iterations: int) -> Stats:
    return Stats(
        median_us=statistics.median(samples_us),
        mean_us=statistics.mean(samples_us),
        std_us=statistics.stdev(samples_us) if len(samples_us) > 1 else 0.0,
        min_us=min(samples_us),
        p10_us=_percentile(samples_us, 0.10),
        p90_us=_percentile(samples_us, 0.90),
        samples_us=samples_us,
        inner_iterations=inner_iterations,
    )


def _stats_dict(stats: Stats) -> dict[str, Any]:
    return {
        "median_us": stats.median_us,
        "mean_us": stats.mean_us,
        "std_us": stats.std_us,
        "min_us": stats.min_us,
        "p10_us": stats.p10_us,
        "p90_us": stats.p90_us,
        "samples_us": stats.samples_us,
        "inner_iterations": stats.inner_iterations,
    }


def _run_one_workload(workload: dict[str, Any], args: argparse.Namespace) -> dict[str, Any]:
    adapter = _load_adapter()
    device = torch.device(args.device)
    torch.cuda.set_device(device)
    torch.set_grad_enabled(False)

    baseline_samples: list[float] = []
    candidate_samples: list[float] = []
    baseline_wall_samples: list[float] = []
    candidate_wall_samples: list[float] = []
    baseline_inner = args.inner_iterations_min
    candidate_inner = args.inner_iterations_min

    compare = getattr(adapter, "compare_outputs", _default_compare)
    workload_id = str(workload.get("id") or workload.get("name") or workload.get("function"))
    if not workload_id:
        raise ValueError("each workload needs an id/name/function field")

    for trial in range(args.num_trials):
        seed = args.seed + trial * 1_000_003 + _stable_u16(workload_id)
        random.seed(seed)
        torch.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
        case = adapter.make_case(workload, device=device, seed=seed)
        inputs = _case_get(case, "inputs")
        baseline_outputs = _case_get(case, "baseline_outputs")
        candidate_outputs = _case_get(case, "candidate_outputs")
        tolerance = _case_get_optional(case, "tolerance") or {
            "atol": float(workload.get("atol", args.atol)),
            "rtol": float(workload.get("rtol", args.rtol)),
        }

        baseline_fn = lambda: adapter.call_baseline(
            workload, inputs, baseline_outputs
        )
        candidate_fn = lambda: adapter.call_candidate(
            workload, inputs, candidate_outputs
        )

        _poison_outputs(baseline_outputs)
        _poison_outputs(candidate_outputs)
        baseline_fn()
        candidate_fn()
        torch.cuda.synchronize()
        correctness = compare(
            workload, baseline_outputs, candidate_outputs, tolerance
        )
        if not correctness.get("ok", False):
            return {
                "id": workload_id,
                "status": "INCORRECT",
                "workload": workload,
                "correctness": correctness,
            }

        for _ in range(args.warmup_runs):
            baseline_fn()
            candidate_fn()
        torch.cuda.synchronize()

        if trial == 0:
            baseline_inner = _calibrate_inner(
                baseline_fn,
                inner_min=args.inner_iterations_min,
                inner_max=args.inner_iterations_max,
                target_sample_us=args.target_sample_us,
            )
            candidate_inner = _calibrate_inner(
                candidate_fn,
                inner_min=args.inner_iterations_min,
                inner_max=args.inner_iterations_max,
                target_sample_us=args.target_sample_us,
            )

        order = ("baseline", "candidate")
        if random.Random(seed).randint(0, 1):
            order = ("candidate", "baseline")

        trial_values: dict[str, tuple[float, float]] = {}
        for side in order:
            if side == "baseline":
                trial_values[side] = _cuda_event_time_us(baseline_fn, baseline_inner)
            else:
                trial_values[side] = _cuda_event_time_us(candidate_fn, candidate_inner)

        base_us, base_wall_us = trial_values["baseline"]
        cand_us, cand_wall_us = trial_values["candidate"]
        baseline_samples.append(base_us)
        candidate_samples.append(cand_us)
        baseline_wall_samples.append(base_wall_us)
        candidate_wall_samples.append(cand_wall_us)

    baseline = _stats(baseline_samples, baseline_inner)
    candidate = _stats(candidate_samples, candidate_inner)
    speedup = baseline.median_us / candidate.median_us if candidate.median_us > 0 else math.inf
    return {
        "id": workload_id,
        "status": "PASSED",
        "production": bool(workload.get("production", True)),
        "workload": workload,
        "baseline": _stats_dict(baseline),
        "candidate": _stats_dict(candidate),
        "baseline_wall_us": baseline_wall_samples,
        "candidate_wall_us": candidate_wall_samples,
        "speedup": speedup,
    }


def _worker_main(
    workload: dict[str, Any],
    args_dict: dict[str, Any],
    result_queue: Any,
) -> None:
    try:
        ns = argparse.Namespace(**args_dict)
        result_queue.put(_run_one_workload(workload, ns))
    except BaseException:
        result_queue.put(
            {
                "id": workload.get("id") or workload.get("name") or "<unknown>",
                "status": "ERROR",
                "workload": workload,
                "error": traceback.format_exc(),
            }
        )


def _run_isolated(workload: dict[str, Any], args: argparse.Namespace) -> dict[str, Any]:
    ctx = get_context("spawn")
    result_queue = ctx.Queue()
    proc = ctx.Process(target=_worker_main, args=(workload, vars(args), result_queue))
    proc.start()
    proc.join(args.timeout_seconds)
    if proc.is_alive():
        proc.terminate()
        proc.join(10)
        return {
            "id": workload.get("id") or workload.get("name") or "<unknown>",
            "status": "TIMEOUT",
            "workload": workload,
            "timeout_seconds": args.timeout_seconds,
        }
    try:
        return result_queue.get_nowait()
    except queue.Empty:
        return {
            "id": workload.get("id") or workload.get("name") or "<unknown>",
            "status": "ERROR",
            "workload": workload,
            "error": f"worker exited with code {proc.exitcode} and returned no result",
        }


def _gpu_name() -> str:
    if not torch.cuda.is_available():
        return "cuda-unavailable"
    return torch.cuda.get_device_name(torch.cuda.current_device())


def _nvidia_smi() -> str:
    try:
        return subprocess.check_output(
            [
                "nvidia-smi",
                "--query-gpu=index,name,utilization.gpu,memory.used,memory.total",
                "--format=csv,noheader",
            ],
            text=True,
            stderr=subprocess.STDOUT,
            timeout=5,
        ).strip()
    except Exception as exc:
        return f"unavailable: {exc}"


def _provenance(args: argparse.Namespace, workloads: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "task_dir": str(ROOT),
        "command": " ".join(sys.argv),
        "python": sys.version,
        "platform": platform.platform(),
        "torch": torch.__version__,
        "torch_cuda": torch.version.cuda,
        "cuda_available": torch.cuda.is_available(),
        "gpu": _gpu_name(),
        "nvidia_smi_before": _nvidia_smi(),
        "workload_count": len(workloads),
        "settings": {
            "warmup_runs": args.warmup_runs,
            "num_trials": args.num_trials,
            "inner_iterations_min": args.inner_iterations_min,
            "inner_iterations_max": args.inner_iterations_max,
            "target_sample_us": args.target_sample_us,
            "timeout_seconds": args.timeout_seconds,
            "isolated": args.isolated,
        },
    }


def _headline(results: list[dict[str, Any]]) -> dict[str, Any]:
    passed = [r for r in results if r.get("status") == "PASSED"]
    production = [r for r in passed if r.get("production", True)]
    speedups = [float(r["speedup"]) for r in production if float(r["speedup"]) > 0]
    if not speedups:
        return {"production_workloads": len(production), "geomean_speedup": None}
    log_mean = sum(math.log(x) for x in speedups) / len(speedups)
    return {
        "production_workloads": len(production),
        "geomean_speedup": math.exp(log_mean),
        "arithmetic_mean_speedup": statistics.mean(speedups),
        "min_speedup": min(speedups),
        "max_speedup": max(speedups),
    }


def _load_workloads(path: Path, only: list[str] | None) -> list[dict[str, Any]]:
    data = json.loads(path.read_text())
    if not isinstance(data, list):
        raise ValueError(f"{path} must contain a JSON list")
    if not only:
        return data
    selected = set(only)
    return [
        w for w in data
        if str(w.get("id") or w.get("name") or w.get("function")) in selected
    ]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workloads", type=Path, default=DEFAULT_WORKLOADS)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--device", default="cuda:0")
    parser.add_argument("--only", nargs="*", help="run only workload ids listed here")
    parser.add_argument("--seed", type=int, default=1234)
    parser.add_argument("--warmup-runs", type=int, default=10)
    parser.add_argument("--num-trials", type=int, default=7)
    parser.add_argument("--inner-iterations-min", type=int, default=1)
    parser.add_argument("--inner-iterations-max", type=int, default=2048)
    parser.add_argument("--target-sample-us", type=float, default=1000.0)
    parser.add_argument("--timeout-seconds", type=int, default=900)
    parser.add_argument("--atol", type=float, default=1e-2)
    parser.add_argument("--rtol", type=float, default=1e-2)
    parser.add_argument("--no-isolated", dest="isolated", action="store_false")
    parser.set_defaults(isolated=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not torch.cuda.is_available():
        raise SystemExit("CUDA is required for this benchmark")
    workloads = _load_workloads(args.workloads, args.only)
    if not workloads:
        raise SystemExit(f"no workloads selected from {args.workloads}")

    args.out.parent.mkdir(parents=True, exist_ok=True)
    provenance = _provenance(args, workloads)
    results: list[dict[str, Any]] = []
    with args.out.open("w") as f:
        f.write(json.dumps({"event": "provenance", **provenance}) + "\n")
        for workload in workloads:
            workload_id = workload.get("id") or workload.get("name") or workload.get("function")
            print(f"== workload {workload_id} ==", flush=True)
            result = _run_isolated(workload, args) if args.isolated else _run_one_workload(workload, args)
            results.append(result)
            f.write(json.dumps({"event": "result", **result}) + "\n")
            f.flush()
            if result.get("status") == "PASSED":
                print(
                    f"PASSED speedup={result['speedup']:.4f} "
                    f"baseline={result['baseline']['median_us']:.3f}us "
                    f"candidate={result['candidate']['median_us']:.3f}us",
                    flush=True,
                )
            else:
                print(f"{result.get('status')} {result.get('error') or result.get('correctness')}", flush=True)

        summary = {
            "event": "summary",
            "headline": _headline(results),
            "passed": sum(r.get("status") == "PASSED" for r in results),
            "total": len(results),
            "nvidia_smi_after": _nvidia_smi(),
        }
        f.write(json.dumps(summary) + "\n")

    print(json.dumps(summary, indent=2))
    return 0 if summary["passed"] == summary["total"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
