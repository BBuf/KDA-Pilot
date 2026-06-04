"""In-SGLang drop-in smoke test: correctness echo + symmetric A/B benchmark.

Runs against the patched export checkout (must be first on PYTHONPATH).
Both sides of the A/B go through the IDENTICAL public custom op
(`sglang.jit_kernel...fused_*`); only the in-body routing differs via
``set_native_enabled`` — the cleanest shipping-shaped comparison.

Checks per representative case:
  1. native output vs original CuTe output within the SGLang test tolerance;
  2. interleaved median latency for both modes;
plus a fallback probe (rms goes through the original path bitwise) and a
custom-op registration assertion.
"""

from __future__ import annotations

import importlib.util
import statistics
import sys
import time
from pathlib import Path

import torch

WORKSPACE = Path(__file__).resolve().parents[1]

# Representative unique signatures, one per major bucket.
SMOKE_CASE_IDS = [
    "nss-b1-s176400-d5120-bf16-s11D.bf16-s11D.bf16-eps1e-06",   # huge bf16 bcast
    "nss-b1-s11040-d5120-bf16-s1SD.fp32-s1SD.fp32-eps1e-06",    # per-token fp32 (parity bucket)
    "nss-b1-s47-d3072-bf16-s1D.bf16-s1D.bf16-eps1e-06",         # tiny rows
    "srnss-b1-s8424-d3072-bf16-g11D.bf16-s11D.bf16-s11D.bf16-eps1e-06",  # gated mid
    "srnss-b1-s37800-d5120-bf16-g11D.fp32-wD.fp32-s1.bf16-s1.bf16-eps1e-06",  # wan affine
    "srnss-b1-s44100-d5120-bf16-gnone-s11D.bf16-s11D.bf16-eps1e-06",  # gnone huge
]


def _load(name, path):
    if name in sys.modules:
        return sys.modules[name]
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def main() -> int:
    import sglang

    sglang_file = Path(sglang.__file__).resolve()
    assert "sglang_export" in str(sglang_file), f"wrong sglang resolved: {sglang_file}"

    from sglang.jit_kernel.diffusion.cutedsl.scale_residual_norm_scale_shift import (
        fused_norm_scale_shift,
        fused_scale_residual_norm_scale_shift,
    )
    from sglang.jit_kernel.diffusion import norm_scale_shift_native as native

    # Registration preserved: the public ops resolve through torch.ops.
    assert callable(torch.ops.sglang.fused_norm_scale_shift)
    assert callable(torch.ops.sglang.fused_scale_residual_norm_scale_shift)
    print(f"[ok] sglang resolved to export checkout: {sglang_file}")
    print("[ok] custom ops registered: sglang::fused_norm_scale_shift, "
          "sglang::fused_scale_residual_norm_scale_shift")

    shapes = _load("kda_shapes", WORKSPACE / "bench" / "shapes.py")
    cases = {c.case_id: c for c in shapes.load_unique_cases()[0]}

    def call_for(case, tensors):
        sig = case.sig
        if sig.kernel == shapes.NSS:
            x, weight, bias, scale, shift = tensors
            return lambda: fused_norm_scale_shift(
                x, weight, bias, scale, shift, sig.norm_type, sig.eps
            )
        residual, x, gate, weight, bias, scale, shift = tensors
        return lambda: fused_scale_residual_norm_scale_shift(
            residual, x, gate, weight, bias, scale, shift, sig.norm_type, sig.eps
        )

    failures = []
    print(f"{'case':70s} {'orig_us':>9s} {'native_us':>9s} {'speedup':>8s}")
    for case_id in SMOKE_CASE_IDS:
        case = cases[case_id]
        tensors, _, _ = shapes.build_inputs(case, device="cuda", seed=20260604)
        call = call_for(case, tensors)

        native.set_native_enabled(False)
        ref = call()
        native.set_native_enabled(True)
        out = call()
        torch.cuda.synchronize()
        ref_t = ref if isinstance(ref, torch.Tensor) else ref[0]
        out_t = out if isinstance(out, torch.Tensor) else out[0]
        try:
            torch.testing.assert_close(out_t, ref_t, atol=5e-2, rtol=5e-2)
            if not isinstance(ref, torch.Tensor):
                torch.testing.assert_close(out[1], ref[1], atol=5e-2, rtol=5e-2)
        except AssertionError as exc:
            failures.append((case_id, str(exc).splitlines()[0]))
            continue

        # interleaved A/B through the identical public op
        for enabled in (True, False):
            native.set_native_enabled(enabled)
            for _ in range(15):
                call()
        torch.cuda.synchronize()
        samples = {True: [], False: []}
        for _ in range(50):
            for enabled in (False, True):
                native.set_native_enabled(enabled)
                t0 = time.perf_counter()
                call()
                torch.cuda.synchronize()
                samples[enabled].append((time.perf_counter() - t0) * 1e6)
        o = statistics.median(samples[False])
        n = statistics.median(samples[True])
        print(f"{case_id:70s} {o:9.1f} {n:9.1f} {o / n:7.3f}x")
        del tensors
        torch.cuda.empty_cache()

    # Fallback probe: rms must take the original path (outputs bitwise equal
    # between enabled/disabled because the native glue returns None for rms).
    x = torch.randn(1, 256, 3072, device="cuda", dtype=torch.bfloat16)
    sc = torch.randn(1, 1, 3072, device="cuda", dtype=torch.bfloat16) * 0.5
    native.set_native_enabled(True)
    y_enabled = fused_norm_scale_shift(x, None, None, sc, sc, "rms", 1e-5)
    native.set_native_enabled(False)
    y_disabled = fused_norm_scale_shift(x, None, None, sc, sc, "rms", 1e-5)
    native.set_native_enabled(True)
    assert torch.equal(y_enabled, y_disabled), "rms fallback probe mismatch"
    print("[ok] fallback probe: rms routes through the original CuTe path (bitwise)")

    if failures:
        print("FAILURES:")
        for cid, msg in failures:
            print(f"  {cid}: {msg}")
        return 1
    print("SMOKE PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
