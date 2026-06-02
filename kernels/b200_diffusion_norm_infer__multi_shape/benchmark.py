#!/usr/bin/env python3
"""Schema-compliant benchmark for ``b200_diffusion_norm_infer__multi_shape``.

Times the SGLang baseline vs the optimized candidate on the SIX production shapes
(``case["production"]``) on the currently selected GPU, and appends rows to
``benchmark.csv`` following ``docs/schemas.md``:

- PRIMARY metric: wrapper-inclusive wall-clock (``perf_counter`` + ``cuda.synchronize``)
  -> ``metric_kind=wall_clock``; this captures dispatcher/wrapper overhead.
- SECONDARY metric: kernel-only time via CUDA events -> ``metric_kind=kernel_event``.

Per (shape, metric_kind): one row with baseline_us, candidate_us, speedup_x, and a
``key=value`` notes field (mean/p10/p90/std, iters, warmup, gpu, host, container,
candidate id). A production-only geometric-mean row is written for each metric_kind.
Full provenance (sglang/cuda/torch versions, source hash, command) is recorded in
``solutions.jsonl`` joined by ``candidate_id``.

Force the CUDA path with ``KDA_REQUIRE_CUDA=1`` (otherwise the candidate falls back
to the baseline and the comparison is meaningless). Reuses the correctness harness's
``make_cases`` / ``baseline`` / ``candidate``.
"""

from __future__ import annotations

import csv
import hashlib
import importlib.util
import math
import os
import socket
import statistics
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

try:
    import torch
except ImportError:  # pragma: no cover
    torch = None


KERNEL_SLUG = "b200_diffusion_norm_infer__multi_shape"
KERNEL_DIR = Path(__file__).resolve().parent
_CUH = KERNEL_DIR / "src" / "norm_cuda" / "diffusion_norm_infer.cuh"
# Every file that materially defines the measured candidate (kernel + dispatcher).
_SRC_FILES = [KERNEL_DIR / "src" / "register.py", _CUH]


def _combined_source_hash() -> str:
    """Deterministic sha256 over the repo-relative-path-prefixed contents of all
    measured sources. Repo-relative (not basename) so distinct files that share a
    basename cannot collide and the fingerprint is stable across checkout dirs."""
    h = hashlib.sha256()
    for p in sorted(_SRC_FILES, key=lambda q: q.relative_to(KERNEL_DIR).as_posix()):
        rel = p.relative_to(KERNEL_DIR).as_posix()
        h.update(rel.encode())
        h.update(b"\0")
        h.update(p.read_bytes() if p.exists() else b"")
        h.update(b"\0")
    return h.hexdigest()[:16]


def _load_correctness_module():
    test_py = KERNEL_DIR / "tests" / "test_correctness.py"
    spec = importlib.util.spec_from_file_location("kda_correctness_scaffold", test_py)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _sync() -> None:
    if torch is not None and torch.cuda.is_available():
        torch.cuda.synchronize()


def _provenance() -> dict[str, str]:
    gpu_model = "unknown"
    cuda_ver = "unknown"
    torch_ver = "unknown"
    if torch is not None and torch.cuda.is_available():
        gpu_model = torch.cuda.get_device_name(0)
        cuda_ver = str(torch.version.cuda)
        torch_ver = str(torch.__version__)
    src_hash = _combined_source_hash()
    return {
        "candidate_id": os.environ.get("KDA_CANDIDATE_ID", "cand-0001-bench"),
        "gpu_model": gpu_model.replace(" ", "_"),
        "gpu_id": os.environ.get("CUDA_VISIBLE_DEVICES", "?"),
        "host": os.environ.get("KDA_HOST", socket.gethostname()),
        "container": os.environ.get("KDA_CONTAINER", "sglang_bbuf"),
        "sglang_commit": os.environ.get("KDA_SGLANG_COMMIT", "unset")[:12],
        "cuda": cuda_ver,
        "torch": torch_ver,
        "source_hash": src_hash,
    }


def _one(fn: Callable[[dict], Any], case: dict, kind: str) -> float:
    if kind == "wall_clock":
        start = time.perf_counter()
        fn(case)
        _sync()
        return (time.perf_counter() - start) * 1e6
    # kernel_event: GPU-only time via CUDA events (excludes Python/launch overhead)
    e0 = torch.cuda.Event(enable_timing=True)
    e1 = torch.cuda.Event(enable_timing=True)
    e0.record()
    fn(case)
    e1.record()
    e1.synchronize()
    return e0.elapsed_time(e1) * 1e3  # ms -> us


def _time_pair(fa, fb, case: dict, *, warmup: int, iters: int, kind: str):
    """INTERLEAVE A and B per iteration so slow GPU-clock drift / throttling
    cancels in the A/B ratio. Measuring A fully then B fully gave unstable
    cross-block ratios (a clock change between blocks corrupts the speedup)."""
    for _ in range(warmup):
        fa(case)
        fb(case)
    _sync()
    sa, sb = [], []
    for _ in range(iters):
        sa.append(_one(fa, case, kind))
        sb.append(_one(fb, case, kind))
    return sa, sb


def _summary(samples: list[float]) -> dict[str, float]:
    ordered = sorted(samples)

    def pct(p: float) -> float:
        index = min(len(ordered) - 1, max(0, round((len(ordered) - 1) * p)))
        return ordered[index]

    return {
        "median_us": statistics.median(ordered),
        "mean_us": statistics.mean(ordered),
        "std_us": statistics.pstdev(ordered) if len(ordered) > 1 else 0.0,
        "min_us": ordered[0],
        "p10_us": pct(0.10),
        "p90_us": pct(0.90),
    }


def _geom_mean(values: list[float]) -> float:
    cleaned = [v for v in values if math.isfinite(v) and v > 0]
    if not cleaned:
        return float("nan")
    return math.exp(sum(math.log(v) for v in cleaned) / len(cleaned))


def _row(writer, *, candidate_id, case_name, metric, baseline_us, candidate_us, speedup, notes):
    writer.writerow([
        datetime.now(timezone.utc).isoformat(),
        candidate_id,
        case_name,
        metric,
        f"{baseline_us:.6f}" if baseline_us is not None else "",
        f"{candidate_us:.6f}" if candidate_us is not None else "",
        f"{speedup:.6f}x" if (speedup is not None and math.isfinite(speedup)) else "",
        notes,
    ])


def main() -> int:
    correctness = _load_correctness_module()
    cases = [c for c in correctness.make_cases() if c.get("production")]
    if not cases:
        raise SystemExit("No production cases found.")
    prov = _provenance()
    cid = prov["candidate_id"]
    print(
        f"PROVENANCE candidate_id={cid} source_hash={prov['source_hash']} "
        f"sglang_commit={prov['sglang_commit']} cuda={prov['cuda']} torch={prov['torch']} "
        f"gpu={prov['gpu_model']}#{prov['gpu_id']} host={prov['host']} container={prov['container']}"
    )
    prov_note = (
        f"gpu_model={prov['gpu_model']} gpu_id={prov['gpu_id']} host={prov['host']} "
        f"container={prov['container']} slug={KERNEL_SLUG} cand={cid}"
    )

    timers = ["wall_clock", "kernel_event"]
    speedups_by_kind: dict[str, list[float]] = {k: [] for k in timers}

    csv_path = KERNEL_DIR / "benchmark.csv"
    new_file = (not csv_path.exists()) or csv_path.stat().st_size == 0
    with csv_path.open("a", newline="") as f:
        writer = csv.writer(f, lineterminator="\n")
        if new_file:  # self-reproducing header (append-safe: only when fresh)
            writer.writerow([
                "timestamp_utc", "candidate_id", "case_name", "metric",
                "baseline_us", "candidate_us", "speedup_x", "notes",
            ])
        for case in cases:
            name = case.get("name", "unknown")
            warmup = int(case.get("warmup", 25))
            iters = int(case.get("iters", 100))
            for kind in timers:
                bs, cs = _time_pair(correctness.baseline, correctness.candidate, case,
                                    warmup=warmup, iters=iters, kind=kind)
                b = _summary(bs)
                c = _summary(cs)
                spd = (b["median_us"] / c["median_us"]) if c["median_us"] > 0 else float("nan")
                spd_min = (b["min_us"] / c["min_us"]) if c["min_us"] > 0 else float("nan")
                speedups_by_kind[kind].append(spd)
                notes = (
                    f"metric_kind={kind} interleaved=1 baseline_mean_us={b['mean_us']:.3f} "
                    f"baseline_std_us={b['std_us']:.3f} baseline_min_us={b['min_us']:.3f} "
                    f"baseline_p10_us={b['p10_us']:.3f} baseline_p90_us={b['p90_us']:.3f} "
                    f"cand_mean_us={c['mean_us']:.3f} "
                    f"cand_std_us={c['std_us']:.3f} cand_p10_us={c['p10_us']:.3f} "
                    f"cand_p90_us={c['p90_us']:.3f} cand_min_us={c['min_us']:.3f} "
                    f"speedup_min_x={spd_min:.4f} warmup={warmup} iters={iters} {prov_note}"
                )
                _row(writer, candidate_id=cid, case_name=name, metric="median_us",
                     baseline_us=b["median_us"], candidate_us=c["median_us"], speedup=spd, notes=notes)
                print(f"{name:32s} [{kind:12s}] baseline={b['median_us']:.2f}us "
                      f"cand={c['median_us']:.2f}us speedup={spd:.3f}x (min {spd_min:.3f}x)")
        for kind in timers:
            geo = _geom_mean(speedups_by_kind[kind])
            _row(writer, candidate_id=cid, case_name="production_geomean", metric="geomean_speedup_x",
                 baseline_us=None, candidate_us=None, speedup=geo,
                 notes=f"metric_kind={kind} interleaved=1 n_shapes={len(cases)} {prov_note}")
            print(f"GEOMEAN [{kind}] = {geo:.4f}x over {len(cases)} production shapes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
