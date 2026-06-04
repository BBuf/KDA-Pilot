"""One-time parity check: vendored baseline copy vs the real SGLang public op.

Run as three separate process invocations (never mixing the real SGLang and the
snapshot alias in one process):

    python bench/parity_check.py --side real --out <dir>/real
    python bench/parity_check.py --side copy --out <dir>/copy
    python bench/parity_check.py --compare <dir>/real <dir>/copy

Each side materializes identical deterministic inputs per unique captured
signature (same seed/GPU/torch), runs its entry points, and saves outputs.
The compare step demands bitwise equality (identical kernel source compiled in
identical environments); any mismatch is reported with max abs diff.

This is provenance evidence only — it is NOT part of the benchmark loop.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

BENCH_DIR = Path(__file__).resolve().parent
KERNEL_DIR = BENCH_DIR.parent


def _load_shapes():
    spec = importlib.util.spec_from_file_location("kda_shapes", BENCH_DIR / "shapes.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules["kda_shapes"] = mod  # dataclasses resolves cls.__module__ here
    spec.loader.exec_module(mod)
    return mod


def _real_entry_points():
    from sglang.jit_kernel.diffusion.cutedsl.scale_residual_norm_scale_shift import (
        fused_norm_scale_shift,
        fused_scale_residual_norm_scale_shift,
    )

    import sglang

    src = Path(sglang.__file__).resolve()
    assert "upstream_jit_kernel" not in str(src), "real side resolved to snapshot!"
    return fused_norm_scale_shift, fused_scale_residual_norm_scale_shift, str(src)


def _copy_entry_points():
    spec = importlib.util.spec_from_file_location(
        "kda_baseline_entry", KERNEL_DIR / "baseline" / "entry.py"
    )
    entry = importlib.util.module_from_spec(spec)
    sys.modules["kda_baseline_entry"] = entry
    spec.loader.exec_module(entry)
    return (
        entry.fused_norm_scale_shift,
        entry.fused_scale_residual_norm_scale_shift,
        "baseline/upstream_jit_kernel (snapshot alias)",
    )


def run_side(side: str, out_dir: Path, seed: int):
    import torch

    shapes = _load_shapes()
    cases, total = shapes.load_unique_cases()
    nss, srnss, provenance = (
        _real_entry_points() if side == "real" else _copy_entry_points()
    )
    out_dir.mkdir(parents=True, exist_ok=True)
    meta = {
        "side": side,
        "provenance": provenance,
        "torch": torch.__version__,
        "cuda": torch.version.cuda,
        "device_name": torch.cuda.get_device_name(0),
        "seed": seed,
        "total_rows": total,
        "cases": [c.case_id for c in cases],
    }
    for case in cases:
        tensors, norm_type, eps = shapes.build_inputs(case, device="cuda", seed=seed)
        if case.sig.kernel == shapes.NSS:
            y = nss(*tensors, norm_type, eps)
            payload = {"y": y.cpu()}
        else:
            y, res_out = srnss(*tensors, norm_type, eps)
            payload = {"y": y.cpu(), "res_out": res_out.cpu()}
        torch.cuda.synchronize()
        torch.save(payload, out_dir / f"{case.case_id}.pt")
        print(f"[{side}] {case.case_id} done")
    (out_dir / "meta.json").write_text(json.dumps(meta, indent=2))
    print(f"[{side}] wrote {len(cases)} cases to {out_dir} ({provenance})")


def compare(real_dir: Path, copy_dir: Path) -> int:
    import torch

    real_meta = json.loads((real_dir / "meta.json").read_text())
    copy_meta = json.loads((copy_dir / "meta.json").read_text())
    assert real_meta["cases"] == copy_meta["cases"], "case lists differ"
    failures = []
    for case_id in real_meta["cases"]:
        a = torch.load(real_dir / f"{case_id}.pt", weights_only=True)
        b = torch.load(copy_dir / f"{case_id}.pt", weights_only=True)
        for key in a:
            if torch.equal(a[key], b[key]):
                continue
            diff = (a[key].float() - b[key].float()).abs().max().item()
            failures.append((case_id, key, diff))
    if failures:
        print("PARITY FAIL (non-bitwise outputs):")
        for case_id, key, diff in failures:
            print(f"  {case_id}.{key}: max_abs_diff={diff:.3e}")
        return 1
    print(
        f"PARITY PASS: {len(real_meta['cases'])} unique signatures bitwise-identical "
        f"(real={real_meta['provenance']} vs copy={copy_meta['provenance']})"
    )
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--side", choices=["real", "copy"])
    ap.add_argument("--out", type=Path)
    ap.add_argument("--compare", nargs=2, type=Path, metavar=("REAL_DIR", "COPY_DIR"))
    ap.add_argument("--seed", type=int, default=20260604)
    args = ap.parse_args()
    if args.compare:
        sys.exit(compare(*args.compare))
    if not args.side or not args.out:
        ap.error("--side and --out required (or --compare)")
    run_side(args.side, args.out, args.seed)


if __name__ == "__main__":
    main()
