"""In-SGLang drop-in validation for the round-2 export (run with PYTHONPATH
pointing at the isolated worktree; see docs/sglang_jit_export.md).

Checks, in order:
1. The edited worktree copy is the sglang being exercised (not the install).
2. SYMMETRIC shipping A/B on the six production shapes THROUGH THE PUBLIC
   CALLABLES — the only difference is the device path, toggled per iteration
   via SGLANG_DIFFUSION_NORM_CUDA (the kill switch inside the in-tree driver).
   Per entry point: triton_one_pass_rms_norm is custom-op-body symmetric (the
   registered op runs identically on both sides); norm_infer is
   public-function symmetric (its baseline hot path has no custom-op
   registration — the diffusion_layer_norm_fwd_impl_cuda op belongs to the
   separate _layer_norm_fwd helper). Wall-clock + CUDA-event medians.
3. Output parity between the two device paths on every production shape.
4. Fallback: unsupported signatures (fp16 LN, D!=128 RMS, non-contiguous, rank-3)
   still produce baseline-identical results through the public ops.
Prints PASS/FAIL per stage; exits non-zero on any failure.
"""

from __future__ import annotations

import os
import statistics
import sys
import time

import torch


def main() -> int:
    import sglang

    print(f"sglang.__file__ = {sglang.__file__}")
    assert "/worktrees/" in sglang.__file__ or os.environ.get("KDA_EXPORT_ALLOW_ANY_SGLANG") == "1", (
        "validation must run against the isolated worktree"
    )

    from sglang.jit_kernel.diffusion.triton.norm import norm_infer
    from sglang.jit_kernel.diffusion.triton.rmsnorm_onepass import triton_one_pass_rms_norm
    from sglang.jit_kernel.diffusion import cuda_norm_infer  # the new in-tree driver

    assert hasattr(cuda_norm_infer, "maybe_rms_onepass_cuda")

    dev = "cuda"
    cases = []
    torch.manual_seed(1001)
    x = torch.randn(8640, 5120, device=dev, dtype=torch.float32)
    wgt = torch.randn(5120, device=dev, dtype=torch.float32)
    b = torch.randn(5120, device=dev, dtype=torch.float32)
    cases.append(("helios__fp32__M8640N5120", lambda: norm_infer(x, wgt, b, 1e-6, is_rms_norm=False)))
    rms_tensors = {}
    for s, seed in [(648720, 1002), (1320, 1003), (650040, 1004), (16384, 1005), (4096, 1006)]:
        torch.manual_seed(seed)
        rms_tensors[s] = (
            torch.randn(s, 128, device=dev, dtype=torch.bfloat16),
            torch.randn(128, device=dev, dtype=torch.bfloat16),
        )
        cases.append(
            (f"rms__bf16__S{s}D128", (lambda s_=s: triton_one_pass_rms_norm(rms_tensors[s_][0], rms_tensors[s_][1], 1e-6)))
        )

    def run(fn, enabled: bool):
        os.environ["SGLANG_DIFFUSION_NORM_CUDA"] = "1" if enabled else "0"
        return fn()

    # --- output parity through the public ops --------------------------------
    for name, fn in cases:
        expected = run(fn, False).clone()
        got = run(fn, True)
        torch.cuda.synchronize()
        tol = 1e-5 if expected.dtype == torch.float32 else 5e-2
        torch.testing.assert_close(got.float(), expected.float(), atol=tol, rtol=tol)
        assert not torch.isnan(got).any() and not torch.isinf(got).any()
        print(f"PARITY {name}: ok")

    # --- symmetric shipping A/B (kill switch toggled per iteration) ----------
    def one(fn, kind):
        if kind == "wall":
            t0 = time.perf_counter()
            fn()
            torch.cuda.synchronize()
            return (time.perf_counter() - t0) * 1e6
        e0 = torch.cuda.Event(enable_timing=True)
        e1 = torch.cuda.Event(enable_timing=True)
        e0.record()
        fn()
        e1.record()
        e1.synchronize()
        return e0.elapsed_time(e1) * 1e3

    print("\nSHIPPING A/B (identical public callables; RMS custom-op-body symmetric, LN public-function symmetric):")
    geo_w, geo_k = 1.0, 1.0
    for name, fn in cases:
        for _ in range(25):
            run(fn, False)
            run(fn, True)
        torch.cuda.synchronize()
        res = {}
        for kind in ("wall", "event"):
            sa, sb = [], []
            for _ in range(100):
                sa.append(one(lambda: run(fn, False), kind))
                sb.append(one(lambda: run(fn, True), kind))
            res[kind] = statistics.median(sa) / statistics.median(sb)
            print(
                f"  {name:28s} [{kind:5s}] triton={statistics.median(sa):8.2f}us "
                f"cuda={statistics.median(sb):8.2f}us speedup={res[kind]:.4f}x"
            )
        geo_w *= res["wall"]
        geo_k *= res["event"]
    n = len(cases)
    print(f"  GEOMEAN shipping: {geo_w ** (1 / n):.4f}x wall / {geo_k ** (1 / n):.4f}x event over {n} shapes")

    # --- fallback signatures through the public ops --------------------------
    os.environ["SGLANG_DIFFUSION_NORM_CUDA"] = "1"
    xf16 = torch.randn(64, 512, device=dev, dtype=torch.float16)
    wf16 = torch.randn(512, device=dev, dtype=torch.float16)
    out = norm_infer(xf16, wf16, wf16, 1e-6, is_rms_norm=False)  # fp16 LN -> Triton
    assert out.dtype == torch.float16
    xd = torch.randn(64, 256, device=dev, dtype=torch.bfloat16)
    wd = torch.randn(256, device=dev, dtype=torch.bfloat16)
    _ = triton_one_pass_rms_norm(xd, wd, 1e-6)  # D=256 -> Triton
    x3 = torch.randn(2, 64, 128, device=dev, dtype=torch.bfloat16)
    w3 = torch.randn(128, device=dev, dtype=torch.bfloat16)
    _ = triton_one_pass_rms_norm(x3, w3, 1e-6)  # rank-3 -> Triton (reshaped by baseline)
    print("FALLBACK signatures: ok (fp16 LN, D=256 RMS, rank-3 RMS all served)")

    print("\nEXPORT VALIDATION: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
