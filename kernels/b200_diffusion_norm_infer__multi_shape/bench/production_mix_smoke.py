"""Production-mix steady-state smoke through the PUBLIC dispatcher route.

Replays a HunyuanVideo-denoise-like call mix (the captured large-S signatures
dominate, with the small [1320,128] signature interleaved — shapes verbatim from
docs/captured_shapes_b200.jsonl) through ``src/register.py::optimized_wrapper``,
alternating per iteration between baseline routing (CUDA disabled → installed
SGLang Triton for every call) and the shipped routing (huge-S → tiled kernel,
small → warp kernel). This is the dirty-L2 steady-state regime the single-shape
interleaved A/B approximates, now with the real multi-shape production mix and
the real dispatcher in the loop.

Usage (remote, idle B200, container):
    CUDA_VISIBLE_DEVICES=<id> python bench/production_mix_smoke.py \
        --candidate-id cand-0011-mix-smoke
"""

from __future__ import annotations

import argparse
import csv
import importlib.util
import statistics
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import torch

KERNEL_DIR = Path(__file__).resolve().parents[1]
# One synthetic denoise step: the huge-S signatures dominate HunyuanVideo's norm
# traffic; the small per-frame signature appears between them.
STEP_MIX = [(648720, 1002), (1320, 1003), (650040, 1004), (648720, 1002)]
D = 128
WARMUP_STEPS = 5
STEPS = 30


def _load_by_path(fq_name: str, path: Path):
    if fq_name in sys.modules:
        return sys.modules[fq_name]
    spec = importlib.util.spec_from_file_location(fq_name, path)
    assert spec is not None and spec.loader is not None, path
    module = importlib.util.module_from_spec(spec)
    sys.modules[fq_name] = module
    spec.loader.exec_module(module)
    return module


_bench = _load_by_path("kda_mix_bench", KERNEL_DIR / "benchmark.py")
_register = _load_by_path("kda_mix_register", KERNEL_DIR / "src" / "register.py")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--candidate-id", required=True)
    args = ap.parse_args()

    tensors = {}
    for s, seed in dict.fromkeys(STEP_MIX):
        torch.manual_seed(seed)
        tensors[s] = (
            torch.randn(s, D, device="cuda", dtype=torch.bfloat16),
            torch.randn(D, device="cuda", dtype=torch.bfloat16),
        )

    def one_step():
        for s, _ in STEP_MIX:
            x, w = tensors[s]
            _register.optimized_wrapper(x, w, 1e-6, dispatcher_hint="rms_onepass")

    def step_with_routing(enabled: bool) -> float:
        _register._CUDA_ENABLED = enabled
        torch.cuda.synchronize()
        t0 = time.perf_counter()
        one_step()
        torch.cuda.synchronize()
        return (time.perf_counter() - t0) * 1e6

    # Routing sanity: with CUDA enabled the huge shapes must produce the same
    # values as the baseline route (tolerance gate before timing).
    for s, _ in dict.fromkeys(STEP_MIX):
        x, w = tensors[s]
        _register._CUDA_ENABLED = False
        expected = _register.optimized_wrapper(x, w, 1e-6, dispatcher_hint="rms_onepass").clone()
        _register._CUDA_ENABLED = True
        got = _register.optimized_wrapper(x, w, 1e-6, dispatcher_hint="rms_onepass")
        torch.cuda.synchronize()
        torch.testing.assert_close(got.float(), expected.float(), atol=5e-2, rtol=5e-2)

    for _ in range(WARMUP_STEPS):
        step_with_routing(False)
        step_with_routing(True)

    base_us, cand_us = [], []
    for _ in range(STEPS):
        base_us.append(step_with_routing(False))
        cand_us.append(step_with_routing(True))
    _register._CUDA_ENABLED = True

    mb, mc = statistics.median(base_us), statistics.median(cand_us)
    ratio = mb / mc
    prov = _bench._provenance()
    print(
        f"production-mix step ({len(STEP_MIX)} calls): baseline-routed={mb:.1f}us "
        f"shipped-routed={mc:.1f}us speedup={ratio:.4f}x "
        f"(means {statistics.mean(base_us):.1f}/{statistics.mean(cand_us):.1f}, steps={STEPS})"
    )

    with (KERNEL_DIR / "benchmark.csv").open("a", newline="") as f:
        writer = csv.writer(f)
        notes = (
            f"metric_kind=wall_clock interleaved=1 lane=production_mix_smoke "
            f"step_mix=S648720x2+S1320+S650040 calls_per_step={len(STEP_MIX)} steps={STEPS} "
            f"baseline=installed_sglang_routing candidate=shipped_dispatcher_routing "
            f"baseline_mean_us={statistics.mean(base_us):.3f} cand_mean_us={statistics.mean(cand_us):.3f} "
            f"baseline_std_us={statistics.pstdev(base_us):.3f} cand_std_us={statistics.pstdev(cand_us):.3f} "
            f"gpu_model={prov['gpu_model']} gpu_id={prov['gpu_id']} host={prov['host']} "
            f"container={prov['container']} sglang_commit={prov['sglang_commit']} "
            f"source_hash={prov['source_hash']} slug=b200_diffusion_norm_infer__multi_shape "
            f"cand={args.candidate_id}"
        )
        writer.writerow([
            datetime.now(timezone.utc).isoformat(), args.candidate_id,
            "production_mix_step", "median_us", f"{mb:.6f}", f"{mc:.6f}", f"{ratio:.6f}x", notes,
        ])
    print("row appended to benchmark.csv")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
