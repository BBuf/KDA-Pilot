#!/usr/bin/env python3
"""Isolated benchmark for ``b200_diffusion_qknorm_rope__multi_shape``.

Times the **current SGLang fused baseline** (`fused_inplace_qknorm_rope`, the
kernel this task must beat) against the registered candidate, on a verified-idle
NVIDIA B200, and appends a structured row per shape to ``benchmark.csv``.

Three explicit, auditable callables keep the oracle and baseline distinct
(see BL-20260601-benchmark-baseline-not-oracle):
- ``run_oracle``                -> split-path correctness reference (NOT timed here)
- ``run_sglang_fused_baseline`` -> the SGLang fused kernel to beat (timed)
- ``run_candidate``             -> the registered optimized candidate (timed)

Timing methodology (matches SGLang's ``run_benchmark_no_cudagraph`` intent):
CUDA-event timing (NOT host ``time.perf_counter``), no CUDA graph capture; inputs
built once per case; the in-place op timed repeatedly (RMS-norm + RoPE is
magnitude-stable under repetition). Per shape: median/mean/std/min/p10/p90 (us)
and an equal-weight geomean of per-shape median speedups over production rows.
``KDA_BENCH_INNER`` (default 1) averages that many back-to-back calls per sample.
``nvidia-smi`` idle snapshots are captured immediately before AND after each row.

Usage (inside sglang_bbuf on ion-b200):
  CUDA_VISIBLE_DEVICES=<idle> python benchmark.py             # isolated baseline-vs-candidate rows
  CUDA_VISIBLE_DEVICES=<idle> python benchmark.py --sanity    # quick ~1.0x check
  CUDA_VISIBLE_DEVICES=<idle> python benchmark.py --device-fair  # device-only A/B (symmetric JIT modules)
  CUDA_VISIBLE_DEVICES=<idle> PYTHONPATH=<repo-root> python benchmark.py --integrated  # LITERAL install path

The PRODUCTION performance claim comes from ``--integrated``: it runs the real
``kda_kernels.install()`` overlay (the public SGLang symbol replaced exactly once) and times
the original baseline vs the INSTALLED public symbol. The plain isolated mode and
``--device-fair`` are diagnostic — the isolated mode's candidate path bypasses the baseline's
``register_custom_op`` layer, so its large-shape numbers carry a known call-path asymmetry
(see BL-candidate-bypasses-custom-op-asymmetry); trust ``--integrated`` for production deltas.
"""

from __future__ import annotations

import csv
import importlib.util
import math
import os
import shlex
import socket
import statistics
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

try:
    import torch
except ImportError:  # pragma: no cover
    torch = None


KERNEL_DIR = Path(__file__).resolve().parent

# All candidate source files whose dirtiness must be reflected in benchmark provenance:
# the registration forwarder, the dispatch/wrapper logic, AND the CUDA kernel itself.
_CANDIDATE_SRC_FILES = (
    "src/register.py",
    "src/wrapper.py",
    "src/qknorm_rope_candidate.cuh",
)

CSV_COLUMNS = [
    "timestamp", "preset", "bucket", "name",
    "num_tokens", "num_heads", "head_dim", "rope_dim", "is_neox", "eps",
    "dtype", "position_dtype", "ci_fallback",
    "baseline_median_us", "baseline_mean_us", "baseline_std_us",
    "baseline_min_us", "baseline_p10_us", "baseline_p90_us",
    "cand_median_us", "cand_mean_us", "cand_std_us",
    "cand_min_us", "cand_p10_us", "cand_p90_us",
    "speedup_x", "iters", "inner",
    "command", "git_commit", "candidate_source_version",
    "host", "gpu_physical_index", "gpu_logical_index", "gpu_name", "gpu_uuid",
    "cuda_visible_devices", "idle_before", "idle_after",
]


def _load_module(rel_path: str, mod_name: str):
    path = KERNEL_DIR / rel_path
    spec = importlib.util.spec_from_file_location(mod_name, path)
    assert spec is not None and spec.loader is not None, path
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _git(*args: str) -> str:
    try:
        return subprocess.check_output(["git", *args], cwd=str(KERNEL_DIR), stderr=subprocess.DEVNULL).decode().strip()
    except Exception:
        return "unknown"


def _candidate_source_version() -> str:
    # On the remote box the synced tree is not a git repo, so honor an explicit
    # KDA_GIT_COMMIT (the local commit the sync corresponds to) for exact provenance.
    env = os.environ.get("KDA_GIT_COMMIT")
    if env:
        return env[:9]
    commit = _git("rev-parse", "--short", "HEAD")
    # Flag +dirty if ANY candidate source (forwarder, dispatch wrapper, or CUDA kernel) has
    # uncommitted edits — not just register.py — so a row can never be attributed to a clean
    # commit while the actual dispatch/device logic was locally modified.
    dirty = _git("status", "--porcelain", "--", *_CANDIDATE_SRC_FILES)
    return f"{commit}{'+dirty' if dirty and dirty != 'unknown' else ''}"


def _physical_gpu_index() -> str:
    cvd = os.environ.get("CUDA_VISIBLE_DEVICES", "")
    return cvd.split(",")[0].strip() if cvd else "unset"


def _gpu_provenance() -> dict[str, str]:
    physical = _physical_gpu_index()
    logical = str(torch.cuda.current_device())
    name = torch.cuda.get_device_name(torch.cuda.current_device())
    uuid = "unavailable"
    if physical not in ("", "unset"):
        try:
            uuid = subprocess.check_output(
                ["nvidia-smi", "-i", physical, "--query-gpu=uuid", "--format=csv,noheader"],
                stderr=subprocess.DEVNULL,
            ).decode().strip()
        except Exception:
            uuid = "unavailable"
    return {
        "gpu_physical_index": physical,
        "gpu_logical_index": logical,
        "gpu_name": name,
        "gpu_uuid": uuid,
        "cuda_visible_devices": os.environ.get("CUDA_VISIBLE_DEVICES", "unset"),
    }


def _nvidia_smi_snapshot(physical_id: str | None = None) -> str:
    """Compact util/mem snapshot for the selected GPU (or all); '' if unavailable."""
    cmd = ["nvidia-smi", "--query-gpu=index,utilization.gpu,memory.used,memory.total",
           "--format=csv,noheader,nounits"]
    if physical_id and physical_id not in ("", "unset"):
        cmd[1:1] = ["-i", physical_id]
    try:
        out = subprocess.check_output(cmd, stderr=subprocess.DEVNULL).decode().strip()
        return " | ".join(line.strip().replace(",", " ") for line in out.splitlines())
    except Exception:
        return "unavailable"


# --- The three distinct callables (oracle stays correctness-only) ---

def _apply(fn: Callable, inputs: dict, case: dict) -> None:
    fn(
        inputs["q"], inputs["k"], inputs["q_weight"], inputs["k_weight"],
        inputs["cos_sin_cache"], inputs["positions"],
        is_neox=case["is_neox"], eps=case["eps"],
        head_dim=case["head_dim"], rope_dim=case["rope_dim"],
    )


def run_oracle(correctness, inputs: dict, case: dict):
    """Split-path correctness reference. NOT used for timing."""
    return correctness._run_oracle(inputs, case)


def _fused_baseline_callable():
    from sglang.jit_kernel.diffusion.qknorm_rope import fused_inplace_qknorm_rope
    return fused_inplace_qknorm_rope


def run_sglang_fused_baseline(baseline_fn, inputs: dict, case: dict) -> None:
    """The current SGLang fused kernel — the baseline to beat (timed).

    `baseline_fn` is resolved ONCE by the caller, so the timed closure carries no
    per-call import/module-lookup overhead and is symmetric with the candidate
    path (which caches its callable in src/register.py).
    """
    _apply(baseline_fn, inputs, case)


def run_candidate(wrapper, inputs: dict, case: dict) -> None:
    """The registered optimized candidate (timed)."""
    _apply(wrapper, inputs, case)


def _time_cuda_events(fn: Callable[[], Any], *, warmup: int, iters: int, inner: int) -> list[float]:
    for _ in range(warmup):
        fn()
    torch.cuda.synchronize()
    samples: list[float] = []
    for _ in range(iters):
        start = torch.cuda.Event(enable_timing=True)
        end = torch.cuda.Event(enable_timing=True)
        start.record()
        for _ in range(inner):
            fn()
        end.record()
        torch.cuda.synchronize()
        samples.append((start.elapsed_time(end) * 1e3) / inner)  # ms -> us, per call
    return samples


def _summary(samples: list[float]) -> dict[str, float]:
    ordered = sorted(samples)

    def pct(p: float) -> float:
        index = min(len(ordered) - 1, max(0, round((len(ordered) - 1) * p)))
        return ordered[index]

    return {
        "median": statistics.median(ordered), "mean": statistics.mean(ordered),
        "std": statistics.pstdev(ordered) if len(ordered) > 1 else 0.0,
        "min": ordered[0], "p10": pct(0.10), "p90": pct(0.90),
    }


def _geom_mean(values: list[float]) -> float:
    """Geometric mean; hard-errors on any missing/invalid/nonpositive value."""
    if not values:
        raise ValueError("geom_mean: no production speedups to aggregate")
    for v in values:
        if not math.isfinite(v) or v <= 0:
            raise ValueError(f"geom_mean: invalid speedup {v!r}; refusing to aggregate a broken run")
    return math.exp(sum(math.log(v) for v in values) / len(values))


def _bench_case(correctness, case, candidate_fn, *, inner, physical_id):
    warmup = int(case.get("warmup", 25))
    iters = int(case.get("iters", 100))
    base_inputs = correctness._make_inputs(case)
    cand_inputs = correctness._make_inputs(case)

    baseline_fn = _fused_baseline_callable()  # resolve ONCE, before timing (symmetry)
    idle_before = _nvidia_smi_snapshot(physical_id)
    b = _summary(_time_cuda_events(lambda: run_sglang_fused_baseline(baseline_fn, base_inputs, case), warmup=warmup, iters=iters, inner=inner))
    c = _summary(_time_cuda_events(lambda: run_candidate(candidate_fn, cand_inputs, case), warmup=warmup, iters=iters, inner=inner))
    idle_after = _nvidia_smi_snapshot(physical_id)

    speedup = (b["median"] / c["median"]) if c["median"] > 0 else float("nan")
    return b, c, speedup, idle_before, idle_after


def _device_fair_main(correctness, wrapper) -> int:
    """Device-only A/B: time the baseline's direct JIT module vs the candidate's
    direct JIT module (SYMMETRIC call paths — both bypass register_custom_op), with
    INTERLEAVED sampling (alternate baseline/candidate per sample) to cancel
    shared-box clock/contention drift. Isolates the device kernel change; does not
    write benchmark.csv. Variant via KDA_CAND_VARIANT (warp|staged) selects the device
    kernel class for the fairness sanity (warp = faithful port ~1.0x; staged = the win)."""
    from sglang.jit_kernel.diffusion.qknorm_rope import _jit_qknorm_rope_module

    variant = os.environ.get("KDA_CAND_VARIANT", "staged")
    kernel_class = {"warp": "QKNormRopeKernel", "staged": "QKNormRopeStagedKernel"}.get(variant, "QKNormRopeStagedKernel")
    inner = int(os.environ.get("KDA_BENCH_INNER", "1"))
    cases = [c for c in correctness.make_cases() if not c.get("ci_fallback")]
    prov = _gpu_provenance()
    print(f"[device-fair] variant={variant} ({kernel_class}) gpu={prov['gpu_name']} phys={prov['gpu_physical_index']}")

    def apply(mod, inp, case):
        mod.qknorm_rope(inp["q"], inp["k"], inp["q_weight"], inp["k_weight"],
                        inp["cos_sin_cache"], inp["positions"], case["eps"])

    speedups = []
    for case in cases:
        base_mod = _jit_qknorm_rope_module(case["head_dim"], case["rope_dim"], case["is_neox"], torch.bfloat16)
        cand_mod = wrapper._candidate_module(case["head_dim"], case["rope_dim"], case["is_neox"], torch.bfloat16, kernel_class)
        bi = correctness._make_inputs(case)
        ci = correctness._make_inputs(case)
        base_fn = lambda: apply(base_mod, bi, case)
        cand_fn = lambda: apply(cand_mod, ci, case)
        for _ in range(int(case.get("warmup", 25))):
            base_fn(); cand_fn()
        torch.cuda.synchronize()
        bs, cs = [], []
        for _ in range(int(case.get("iters", 100))):  # interleaved: cancels slow drift
            bs.append(_time_cuda_events(base_fn, warmup=0, iters=1, inner=inner)[0])
            cs.append(_time_cuda_events(cand_fn, warmup=0, iters=1, inner=inner)[0])
        b, c = _summary(bs), _summary(cs)
        sp = b["median"] / c["median"] if c["median"] > 0 else float("nan")
        speedups.append(sp)
        print(f"{case['name']:>44s}  device-fair speedup={sp:.4f}x  base_direct={b['median']:.3f}us  cand_direct={c['median']:.3f}us")
    print(f"\n[device-fair] variant={variant} production geomean = {_geom_mean(speedups):.4f}x over {len(speedups)} shapes")
    return 0


_SGL_QKNORM_PATH = "sglang.jit_kernel.diffusion.qknorm_rope"
_KDA_REGISTRY_KEY = f"{_SGL_QKNORM_PATH}:fused_inplace_qknorm_rope"


def _ensure_kda_kernels_importable() -> Path:
    """Put the repo root (the dir containing the ``kda_kernels`` package) on sys.path so
    ``import kda_kernels`` resolves. The literal install-path benchmark needs the exported
    overlay, which lives at the repo root, not inside this kernel folder."""
    here = KERNEL_DIR
    for _ in range(8):
        if (here / "kda_kernels" / "__init__.py").exists():
            if str(here) not in sys.path:
                sys.path.insert(0, str(here))
            return here
        here = here.parent
    raise SystemExit(
        "kda_kernels package not found above KERNEL_DIR; sync the repo root (kda_kernels/) "
        "alongside this kernel folder before running --integrated."
    )


def _integrated_main(correctness) -> int:
    """LITERAL integrated install-path A/B (AC-4) — the production delta of installing the
    candidate. Captures the ORIGINAL SGLang baseline public op, runs
    ``kda_kernels.install(force=True, strict=True)`` to monkey-patch the public symbol with
    the generated KDA overlay dispatcher (exactly ONE layer — the real production path, not a
    re-wrapped custom op), asserts the swap, then times the original baseline vs the
    INSTALLED public symbol INTERLEAVED on identical inputs. Appends ``name__install`` rows +
    ``GEOMEAN_install`` to benchmark.csv. Restores the baseline on exit."""
    import importlib

    qmod = importlib.import_module(_SGL_QKNORM_PATH)
    baseline_op = qmod.fused_inplace_qknorm_rope  # captured BEFORE install (the original)

    _ensure_kda_kernels_importable()
    import kda_kernels

    results = kda_kernels.install(force=True, strict=True)
    status = next((st for (sp, _kp, st) in results if sp == _KDA_REGISTRY_KEY), None)
    if status != "swapped":
        raise SystemExit(f"[install] kda_kernels.install did not swap {_KDA_REGISTRY_KEY!r}: {results}")
    installed_op = qmod.fused_inplace_qknorm_rope  # now the generated KDA overlay dispatcher
    if installed_op is baseline_op:
        raise SystemExit("[install] installed public symbol is still the baseline")
    inst_mod = getattr(installed_op, "__module__", "")
    if not inst_mod.startswith("kda_kernels"):
        raise SystemExit(f"[install] installed symbol is not from kda_kernels: {inst_mod!r}")

    inner = int(os.environ.get("KDA_BENCH_INNER", "1"))
    cases = [c for c in correctness.make_cases() if not c.get("ci_fallback")]
    command = shlex.join([sys.executable, *sys.argv])
    git_commit = os.environ.get("KDA_GIT_COMMIT") or _git("rev-parse", "HEAD")
    cand_ver = _candidate_source_version()
    host = socket.gethostname()
    prov = _gpu_provenance()
    physical_id = _physical_gpu_index()

    def call(fn, inp, case):
        fn(inp["q"], inp["k"], inp["q_weight"], inp["k_weight"], inp["cos_sin_cache"],
           inp["positions"], is_neox=case["is_neox"], eps=case["eps"],
           head_dim=case["head_dim"], rope_dim=case["rope_dim"])

    csv_path = KERNEL_DIR / "benchmark.csv"
    write_header = (not csv_path.exists()) or csv_path.stat().st_size == 0
    speedups, rows = [], []
    print(f"[install] swapped {_KDA_REGISTRY_KEY} -> {inst_mod}.fused_inplace_qknorm_rope; "
          f"baseline custom-op vs installed overlay dispatcher; gpu={prov['gpu_name']} phys={physical_id}")
    try:
        for case in cases:
            bi, ci = correctness._make_inputs(case), correctness._make_inputs(case)
            bfn, cfn = lambda: call(baseline_op, bi, case), lambda: call(installed_op, ci, case)
            for _ in range(int(case.get("warmup", 25))):
                bfn(); cfn()
            torch.cuda.synchronize()
            idle_before = _nvidia_smi_snapshot(physical_id)
            bs, cs = [], []
            for _ in range(int(case.get("iters", 100))):  # interleaved: cancels slow drift
                bs.append(_time_cuda_events(bfn, warmup=0, iters=1, inner=inner)[0])
                cs.append(_time_cuda_events(cfn, warmup=0, iters=1, inner=inner)[0])
            idle_after = _nvidia_smi_snapshot(physical_id)
            b, c = _summary(bs), _summary(cs)
            sp = b["median"] / c["median"] if c["median"] > 0 else float("nan")
            speedups.append(sp)
            rows.append([
                datetime.now(timezone.utc).isoformat(), case.get("preset"), case.get("bucket"), case["name"] + "__install",
                case["num_tokens"], case["num_heads"], case["head_dim"], case["rope_dim"], case["is_neox"], case["eps"],
                case["dtype"], case["position_dtype"], case.get("ci_fallback", False),
                f"{b['median']:.4f}", f"{b['mean']:.4f}", f"{b['std']:.4f}", f"{b['min']:.4f}", f"{b['p10']:.4f}", f"{b['p90']:.4f}",
                f"{c['median']:.4f}", f"{c['mean']:.4f}", f"{c['std']:.4f}", f"{c['min']:.4f}", f"{c['p10']:.4f}", f"{c['p90']:.4f}",
                f"{sp:.4f}", case.get("iters", 100), inner, command, git_commit, cand_ver + "+install", host,
                prov["gpu_physical_index"], prov["gpu_logical_index"], prov["gpu_name"], prov["gpu_uuid"],
                prov["cuda_visible_devices"], idle_before, idle_after,
            ])
            print(f"{case['name']:>44s}  install speedup={sp:.4f}x  base={b['median']:.3f}us  installed={c['median']:.3f}us")
    finally:
        kda_kernels.uninstall()  # restore the original baseline regardless of outcome
        restored = qmod.fused_inplace_qknorm_rope is baseline_op
        print(f"[install] uninstalled; baseline restored={restored}")

    geomean = _geom_mean(speedups)
    with csv_path.open("a", newline="") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(CSV_COLUMNS)
        writer.writerows(rows)
        summary = {col: "" for col in CSV_COLUMNS}
        summary.update({"name": "GEOMEAN_install", "speedup_x": f"{geomean:.4f}", "command": command,
                        "git_commit": git_commit, "candidate_source_version": cand_ver + "+install", "host": host,
                        "gpu_name": prov["gpu_name"], "cuda_visible_devices": prov["cuda_visible_devices"]})
        writer.writerow([summary[col] for col in CSV_COLUMNS])
    print(f"\n[install] production geomean = {geomean:.4f}x over {len(speedups)} shapes (literal kda_kernels.install path)")
    return 0


def main() -> int:
    if torch is None or not torch.cuda.is_available():
        raise SystemExit("CUDA is required. Run inside the sglang_bbuf container on ion-b200.")

    if "--integrated" in sys.argv:
        correctness = _load_module("tests/test_correctness.py", "kda_correctness")
        return _integrated_main(correctness)

    if "--device-fair" in sys.argv:
        correctness = _load_module("tests/test_correctness.py", "kda_correctness")
        wrapper = _load_module("src/wrapper.py", "kda_wrapper")
        return _device_fair_main(correctness, wrapper)

    sanity = "--sanity" in sys.argv
    correctness = _load_module("tests/test_correctness.py", "kda_correctness")
    register = _load_module("src/register.py", "kda_register")
    candidate_fn = getattr(register, "optimized_wrapper")

    cases = [c for c in correctness.make_cases() if not c.get("ci_fallback")]  # production only
    if not cases:
        raise SystemExit("No production benchmark cases.")

    inner = int(os.environ.get("KDA_BENCH_INNER", "1"))
    physical_id = _physical_gpu_index()

    if sanity:
        for case in cases[:3]:
            case = {**case, "warmup": 10, "iters": 30}
            _b, _c, sp, _ib, _ia = _bench_case(correctness, case, candidate_fn, inner=inner, physical_id=physical_id)
            print(f"[sanity] {case['name']:>44s}  candidate/fused-baseline speedup={sp:.4f}x "
                  f"(expect ~1.0x while candidate routes to baseline)")
        return 0

    command = shlex.join([sys.executable, *sys.argv])
    git_commit = os.environ.get("KDA_GIT_COMMIT") or _git("rev-parse", "HEAD")
    cand_ver = _candidate_source_version()
    host = socket.gethostname()
    prov = _gpu_provenance()

    csv_path = KERNEL_DIR / "benchmark.csv"
    write_header = (not csv_path.exists()) or csv_path.stat().st_size == 0

    speedups: list[float] = []
    rows: list[list[Any]] = []
    for case in cases:
        b, c, speedup, idle_before, idle_after = _bench_case(correctness, case, candidate_fn, inner=inner, physical_id=physical_id)
        speedups.append(speedup)
        rows.append([
            datetime.now(timezone.utc).isoformat(), case.get("preset"), case.get("bucket"), case["name"],
            case["num_tokens"], case["num_heads"], case["head_dim"], case["rope_dim"], case["is_neox"], case["eps"],
            case["dtype"], case["position_dtype"], case.get("ci_fallback", False),
            f"{b['median']:.4f}", f"{b['mean']:.4f}", f"{b['std']:.4f}", f"{b['min']:.4f}", f"{b['p10']:.4f}", f"{b['p90']:.4f}",
            f"{c['median']:.4f}", f"{c['mean']:.4f}", f"{c['std']:.4f}", f"{c['min']:.4f}", f"{c['p10']:.4f}", f"{c['p90']:.4f}",
            f"{speedup:.4f}", case.get("iters", 100), inner,
            command, git_commit, cand_ver, host,
            prov["gpu_physical_index"], prov["gpu_logical_index"], prov["gpu_name"], prov["gpu_uuid"],
            prov["cuda_visible_devices"], idle_before, idle_after,
        ])
        print(f"{case['name']:>44s}  speedup={speedup:.4f}x  fused_baseline={b['median']:.3f}us  cand={c['median']:.3f}us")

    geomean = _geom_mean(speedups)  # hard-errors if any row is invalid

    with csv_path.open("a", newline="") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(CSV_COLUMNS)
        writer.writerows(rows)
        # GEOMEAN is an aggregate over the per-shape rows above; idle_before/idle_after
        # are captured per measured shape, so they are intentionally blank here.
        summary = {c: "" for c in CSV_COLUMNS}
        summary.update({
            "name": "GEOMEAN_production", "speedup_x": f"{geomean:.4f}",
            "command": command, "git_commit": git_commit, "candidate_source_version": cand_ver,
            "host": host, "gpu_physical_index": prov["gpu_physical_index"],
            "gpu_logical_index": prov["gpu_logical_index"], "gpu_name": prov["gpu_name"],
            "gpu_uuid": prov["gpu_uuid"], "cuda_visible_devices": prov["cuda_visible_devices"],
        })
        writer.writerow([summary[c] for c in CSV_COLUMNS])

    print(f"\nproduction geomean speedup = {geomean:.4f}x over {len(speedups)} shapes  "
          f"(gpu phys={prov['gpu_physical_index']} {prov['gpu_name']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
