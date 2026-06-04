"""One-time parity cross-check: pinned baseline/ copies vs installed sglang.

Validates the round-2 pinned-baseline lane (see docs/baseline_source.md):

1. OUTPUT PARITY — for the six production shapes, the pinned copy and the
   installed sglang public callable must produce bitwise-identical outputs on
   identical seeded inputs (same Triton source, so anything else is a bug in
   the pinning).
2. TIMING DELTA — interleaved A/B (installed vs pinned) quantifies the host
   layer the pinned lane strips (custom-op registration wrapper on the RMS
   path; none expected on the LN path). Rows land in benchmark.csv under
   candidate id ``baseline-parity-r2`` with baseline=installed,
   candidate=pinned, so the host-layer delta is recorded explicitly and can
   never be silently folded into a device-kernel claim.

Run remotely (idle B200, container):
    CUDA_VISIBLE_DEVICES=<id> python bench/parity_check_r2.py
"""

from __future__ import annotations

import csv
import importlib.util
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

import torch

KERNEL_DIR = Path(__file__).resolve().parents[1]


def _load_by_path(fq_name: str, path: Path):
    if fq_name in sys.modules:
        return sys.modules[fq_name]
    spec = importlib.util.spec_from_file_location(fq_name, path)
    assert spec is not None and spec.loader is not None, path
    module = importlib.util.module_from_spec(spec)
    sys.modules[fq_name] = module
    spec.loader.exec_module(module)
    return module


_corr = _load_by_path("kda_parity_corr", KERNEL_DIR / "tests" / "test_correctness.py")
_bench = _load_by_path("kda_parity_bench", KERNEL_DIR / "benchmark.py")
_pinned = _load_by_path("kda_pinned_baseline", KERNEL_DIR / "baseline" / "__init__.py")


def _production_cases():
    return [c for c in _corr.make_cases() if c.get("production")]


def _call_installed(case, inp):
    norm_infer, rms = _corr._sglang_baselines()
    if case["kind"] == "norm_infer":
        return norm_infer(inp["x"], inp["weight"], inp["bias"], case["eps"],
                          is_rms_norm=case["is_rms_norm"], out=None)
    return rms(inp["x"], inp["w"], case["eps"])


def _call_pinned(case, inp):
    if case["kind"] == "norm_infer":
        return _pinned.norm_infer(inp["x"], inp["weight"], inp["bias"], case["eps"],
                                  is_rms_norm=case["is_rms_norm"], out=None)
    return _pinned.triton_one_pass_rms_norm(inp["x"], inp["w"], case["eps"])


def main() -> int:
    prov = _bench._provenance()
    cid = "baseline-parity-r2"
    rows = []
    print(f"PARITY pinned({_pinned.UPSTREAM_COMMIT}) vs installed sglang | "
          f"gpu={prov['gpu_model']}#{prov['gpu_id']} host={prov['host']}")

    for case in _production_cases():
        name = case["name"]
        inp = _corr._make_inputs(case)

        # --- output parity (fresh outputs both sides; no shared out buffer) ---
        out_installed = _call_installed(case, inp)
        out_pinned = _call_pinned(case, inp)
        torch.cuda.synchronize()
        bitwise = torch.equal(out_installed, out_pinned)
        assert bitwise, f"{name}: pinned copy output differs from installed sglang"

        # --- timing delta (interleaved; installed is the 'baseline' side) -----
        fa = lambda c: _call_installed(c, inp)  # noqa: E731
        fb = lambda c: _call_pinned(c, inp)  # noqa: E731
        for kind in ("wall_clock", "kernel_event"):
            sa, sb = _bench._time_pair(fa, fb, case, warmup=case["warmup"],
                                       iters=case["iters"], kind=kind)
            a, b = _bench._summary(sa), _bench._summary(sb)
            ratio = a["median_us"] / b["median_us"] if b["median_us"] else float("nan")
            rows.append((name, kind, a, b, ratio))
            print(f"{name:32s} [{kind:12s}] installed={a['median_us']:.2f}us "
                  f"pinned={b['median_us']:.2f}us installed/pinned={ratio:.3f}x "
                  f"(bitwise_equal=True)")

    csv_path = KERNEL_DIR / "benchmark.csv"
    new_file = not csv_path.exists()
    with csv_path.open("a", newline="") as f:
        writer = csv.writer(f)
        if new_file:
            writer.writerow(["timestamp_utc", "candidate_id", "case_name", "metric",
                             "baseline_us", "candidate_us", "speedup_x", "notes"])
        for name, kind, a, b, ratio in rows:
            notes = (
                f"metric_kind={kind} interleaved=1 parity=bitwise_equal "
                f"baseline=installed_sglang candidate=pinned_baseline_copy "
                f"installed_mean_us={a['mean_us']:.3f} installed_std_us={a['std_us']:.3f} "
                f"pinned_mean_us={b['mean_us']:.3f} pinned_std_us={b['std_us']:.3f} "
                f"pinned_p10_us={b['p10_us']:.3f} pinned_p90_us={b['p90_us']:.3f} "
                f"warmup={25} iters={100} gpu_model={prov['gpu_model']} gpu_id={prov['gpu_id']} "
                f"host={prov['host']} container={prov['container']} "
                f"sglang_commit={prov['sglang_commit']} pinned_commit={_pinned.UPSTREAM_COMMIT} "
                f"slug=b200_diffusion_norm_infer__multi_shape cand={cid}"
            )
            writer.writerow([
                datetime.now(timezone.utc).isoformat(), cid, name, "median_us",
                f"{a['median_us']:.6f}", f"{b['median_us']:.6f}", f"{ratio:.6f}x", notes,
            ])
    print(f"PARITY OK — 6/6 bitwise equal; rows appended to {csv_path.name} under {cid}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
