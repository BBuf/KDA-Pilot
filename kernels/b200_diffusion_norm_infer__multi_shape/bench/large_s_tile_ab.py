"""Interleaved A/B for the tiled multi-row RMSNorm vs the PINNED Triton baseline
on the two huge-S production shapes, with a paired-bootstrap 95% CI on the
median ratio (the promotion gate requires the CI lower bound to clear +2% on
each shape, in BOTH wall-clock and kernel-event timing).

Usage (remote, idle B200, container):
    CUDA_VISIBLE_DEVICES=<id> python bench/large_s_tile_ab.py \
        --candidate-id cand-0008-tile-r16-plain --rows-per-cta 16 --scheduling 0
"""

from __future__ import annotations

import argparse
import csv
import importlib.util
import random
import sys
from datetime import datetime, timezone
from pathlib import Path

import torch

KERNEL_DIR = Path(__file__).resolve().parents[1]
SHAPES = [(648720, 1002), (650040, 1004)]  # (S, seed) — verbatim production rows
D = 128
WARMUP = 25
ITERS = 100
BOOTSTRAP_RESAMPLES = 2000
BOOTSTRAP_SEED = 20260604


def _load_by_path(fq_name: str, path: Path):
    if fq_name in sys.modules:
        return sys.modules[fq_name]
    spec = importlib.util.spec_from_file_location(fq_name, path)
    assert spec is not None and spec.loader is not None, path
    module = importlib.util.module_from_spec(spec)
    sys.modules[fq_name] = module
    spec.loader.exec_module(module)
    return module


_bench = _load_by_path("kda_tile_ab_bench", KERNEL_DIR / "benchmark.py")
_pinned = _load_by_path("kda_pinned_baseline", KERNEL_DIR / "baseline" / "__init__.py")
_register = _load_by_path("kda_tile_ab_register", KERNEL_DIR / "src" / "register.py")


def _bootstrap_median_ratio_ci(sa: list[float], sb: list[float]) -> tuple[float, float, float]:
    """Paired bootstrap over interleaved iteration pairs: resample (a_i, b_i)
    pairs with replacement, take median(a*)/median(b*) per resample, return
    (point, lo95, hi95). Pairing preserves the drift cancellation that the
    interleaved schedule provides."""
    rng = random.Random(BOOTSTRAP_SEED)
    n = len(sa)
    point = sorted(sa)[n // 2] / sorted(sb)[n // 2]
    stats = []
    for _ in range(BOOTSTRAP_RESAMPLES):
        idx = [rng.randrange(n) for _ in range(n)]
        ra = sorted(sa[i] for i in idx)
        rb = sorted(sb[i] for i in idx)
        stats.append(ra[n // 2] / rb[n // 2])
    stats.sort()
    lo = stats[int(0.025 * BOOTSTRAP_RESAMPLES)]
    hi = stats[int(0.975 * BOOTSTRAP_RESAMPLES)]
    return point, lo, hi


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--candidate-id", required=True)
    ap.add_argument("--rows-per-cta", type=int, default=16, choices=(16, 32))
    ap.add_argument("--scheduling", type=int, default=0, choices=(0, 1))
    args = ap.parse_args()

    prov = _bench._provenance()
    prov["candidate_id"] = args.candidate_id
    print(
        f"PROVENANCE candidate_id={args.candidate_id} rows_per_cta={args.rows_per_cta} "
        f"scheduling={args.scheduling} source_hash={prov['source_hash']} "
        f"sglang_commit={prov['sglang_commit']} gpu={prov['gpu_model']}#{prov['gpu_id']} "
        f"host={prov['host']} pinned_commit={_pinned.UPSTREAM_COMMIT}"
    )

    rows = []
    for s, seed in SHAPES:
        torch.manual_seed(seed)
        x = torch.randn(s, D, device="cuda", dtype=torch.bfloat16)
        w = torch.randn(D, device="cuda", dtype=torch.bfloat16)
        name = f"rms__bf16__S{s}D128"

        # Correctness pre-gate on the exact benchmark tensors.
        expected = _pinned.triton_one_pass_rms_norm(x, w, 1e-6).clone()
        got = _register.tiled_rms_onepass(
            x, w, 1e-6, rows_per_cta=args.rows_per_cta, scheduling=args.scheduling
        )
        torch.cuda.synchronize()
        torch.testing.assert_close(got.float(), expected.float(), atol=5e-2, rtol=5e-2)

        case = {"name": name, "warmup": WARMUP, "iters": ITERS}
        fa = lambda c: _pinned.triton_one_pass_rms_norm(x, w, 1e-6)  # noqa: E731
        fb = lambda c: _register.tiled_rms_onepass(  # noqa: E731
            x, w, 1e-6, rows_per_cta=args.rows_per_cta, scheduling=args.scheduling
        )
        for kind in ("wall_clock", "kernel_event"):
            sa, sb = _bench._time_pair(fa, fb, case, warmup=WARMUP, iters=ITERS, kind=kind)
            a, b = _bench._summary(sa), _bench._summary(sb)
            ratio, lo, hi = _bootstrap_median_ratio_ci(sa, sb)
            rows.append((name, kind, a, b, ratio, lo, hi))
            verdict = "PASS(+2%LB)" if lo > 1.02 else ("ahead" if ratio > 1.0 else "behind")
            print(
                f"{name:28s} [{kind:12s}] pinned={a['median_us']:.2f}us "
                f"tiled={b['median_us']:.2f}us ratio={ratio:.4f}x "
                f"CI95=[{lo:.4f},{hi:.4f}] {verdict}"
            )

    csv_path = KERNEL_DIR / "benchmark.csv"
    with csv_path.open("a", newline="") as f:
        writer = csv.writer(f)
        for name, kind, a, b, ratio, lo, hi in rows:
            notes = (
                f"metric_kind={kind} interleaved=1 baseline=pinned_baseline_copy "
                f"candidate=tiled_rms rows_per_cta={args.rows_per_cta} scheduling={args.scheduling} "
                f"bootstrap_ci95_lo={lo:.4f} bootstrap_ci95_hi={hi:.4f} resamples={BOOTSTRAP_RESAMPLES} "
                f"baseline_mean_us={a['mean_us']:.3f} baseline_std_us={a['std_us']:.3f} "
                f"cand_mean_us={b['mean_us']:.3f} cand_std_us={b['std_us']:.3f} "
                f"cand_p10_us={b['p10_us']:.3f} cand_p90_us={b['p90_us']:.3f} cand_min_us={b['min_us']:.3f} "
                f"warmup={WARMUP} iters={ITERS} gpu_model={prov['gpu_model']} gpu_id={prov['gpu_id']} "
                f"host={prov['host']} container={prov['container']} sglang_commit={prov['sglang_commit']} "
                f"source_hash={prov['source_hash']} slug=b200_diffusion_norm_infer__multi_shape "
                f"cand={args.candidate_id}"
            )
            writer.writerow([
                datetime.now(timezone.utc).isoformat(), args.candidate_id, name, "median_us",
                f"{a['median_us']:.6f}", f"{b['median_us']:.6f}", f"{ratio:.6f}x", notes,
            ])
    print(f"rows appended to {csv_path.name} under {args.candidate_id}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
