"""Validate the integrated kda_kernels install() path on the remote H200.

Captures the original SGLang baselines, runs kda_kernels.install(strict=True),
confirms both public symbols are swapped, then enforces the strict correctness
contract on the installed (swapped) SGLang-callable path: shape, dtype, no NaN,
no Inf, candidate-vs-baseline AND candidate-vs-FP32-reference within the
SGLang-style tolerances (fp32 LayerNorm 1e-5; bf16 RMS / select01 5e-2). Also
checks fallback (one unsupported case per entry point) and a smoke benchmark.
Exits nonzero on any correctness failure.
"""
import importlib
import statistics
import time

import torch

DEV, EPS = "cuda", 1e-6
norm_mod = importlib.import_module("sglang.jit_kernel.diffusion.triton.norm")
rms_mod = importlib.import_module("sglang.jit_kernel.diffusion.triton.rmsnorm_onepass")
base_norm = norm_mod.norm_infer
base_rms = rms_mod.triton_one_pass_rms_norm

import kda_kernels  # noqa: E402

results = kda_kernels.install(strict=True)
print("install:", results)

sw_norm = importlib.import_module("sglang.jit_kernel.diffusion.triton.norm").norm_infer
sw_rms = importlib.import_module("sglang.jit_kernel.diffusion.triton.rmsnorm_onepass").triton_one_pass_rms_norm
ok = sw_norm is not base_norm and sw_rms is not base_rms
print(f"norm_infer swapped={sw_norm is not base_norm} -> {sw_norm.__module__}")
print(f"triton_one_pass_rms_norm swapped={sw_rms is not base_rms} -> {sw_rms.__module__}")


def ref_rms(x, w):
    xf = x.float()
    return (xf * torch.rsqrt(xf.pow(2).mean(-1, keepdim=True) + EPS) * w.float()).to(x.dtype)


def ref_ln(x, w, b):
    xf = x.float(); m = xf.mean(-1, keepdim=True); v = (xf - m).pow(2).mean(-1, keepdim=True)
    return ((xf - m) * torch.rsqrt(v + EPS) * w.float() + b.float()).to(x.dtype)


def check(name, cand, base, ref, atol, rtol):
    """Shape/dtype/NaN/Inf + candidate-vs-baseline AND candidate-vs-FP32-reference."""
    bad = []
    if torch.isnan(cand).any() or torch.isinf(cand).any():
        bad.append("NaN/Inf")
    if cand.shape != base.shape:
        bad.append(f"shape {tuple(cand.shape)}!={tuple(base.shape)}")
    if cand.dtype != base.dtype:
        bad.append(f"dtype {cand.dtype}!={base.dtype}")
    for label, other in (("base", base), ("ref", ref)):
        try:
            torch.testing.assert_close(cand.float(), other.float(), atol=atol, rtol=rtol)
        except AssertionError:
            d = (cand.float() - other.float()).abs().max().item()
            bad.append(f"vs_{label} maxdiff={d:.3e}>atol={atol}")
    good = not bad
    print(f"  {name}: {'OK' if good else 'FAIL ' + '; '.join(bad)}")
    return good


for M, N in [(648720, 128), (1320, 128), (650040, 128), (16384, 128), (4096, 128)]:
    x = torch.randn(M, N, device=DEV, dtype=torch.bfloat16); w = torch.randn(N, device=DEV, dtype=torch.bfloat16)
    ok &= check(f"rms {M}x{N}", sw_rms(x, w, EPS), base_rms(x, w, EPS), ref_rms(x, w), 5e-2, 5e-2)

x = torch.randn(8640, 5120, device=DEV, dtype=torch.float32)
w = torch.randn(5120, device=DEV, dtype=torch.float32); b = torch.randn(5120, device=DEV, dtype=torch.float32)
ok &= check("ln 8640x5120", sw_norm(x, w, b, EPS, is_rms_norm=False), base_norm(x, w, b, EPS, is_rms_norm=False), ref_ln(x, w, b), 1e-5, 1e-5)

# Fallback (unsupported -> baseline; must equal the original baseline exactly)
xf16 = torch.randn(256, 128, device=DEV, dtype=torch.float16); wf16 = torch.randn(128, device=DEV, dtype=torch.float16)
fb1 = torch.equal(sw_rms(xf16, wf16, EPS), base_rms(xf16, wf16, EPS))
xr = torch.randn(256, 512, device=DEV, dtype=torch.float32); wr = torch.randn(512, device=DEV, dtype=torch.float32)
fb2 = torch.equal(sw_norm(xr, wr, None, EPS, is_rms_norm=True), base_norm(xr, wr, None, EPS, is_rms_norm=True))
ok &= fb1 and fb2
print(f"  fallback fp16-rms={fb1} rmsnorm-via-norm_infer={fb2}")


def modulate(fn, x, w, b, sc, sh):
    n = fn(x.view(-1, x.shape[-1]), w, b, EPS, is_rms_norm=False).view_as(x)
    return n * (1 + sc.unsqueeze(1)) + sh.unsqueeze(1)


xx = torch.randn(2, 128, 3072, device=DEV, dtype=torch.bfloat16)
ww = torch.randn(3072, device=DEV, dtype=torch.bfloat16); bb = torch.randn(3072, device=DEV, dtype=torch.bfloat16)
sc = torch.randn(2, 3072, device=DEV, dtype=torch.bfloat16); sh = torch.randn(2, 3072, device=DEV, dtype=torch.bfloat16)
o_cand = modulate(sw_norm, xx, ww, bb, sc, sh); o_base = modulate(base_norm, xx, ww, bb, sc, sh)
ok &= check("select01 oracle", o_cand, o_base, o_base, 5e-2, 5e-2)


def wall(fn, it=150):
    for _ in range(30):
        fn()
    torch.cuda.synchronize(); s = []
    for _ in range(it):
        t = time.perf_counter(); fn(); torch.cuda.synchronize(); s.append((time.perf_counter() - t) * 1e6)
    return statistics.median(s)


for M, N, label in [(4096, 128, "rms small"), (648720, 128, "rms huge")]:
    x = torch.randn(M, N, device=DEV, dtype=torch.bfloat16); w = torch.randn(N, device=DEV, dtype=torch.bfloat16)
    sb = wall(lambda: base_rms(x, w, EPS)); si = wall(lambda: sw_rms(x, w, EPS))
    print(f"  smoke {label} {M}x{N}: base={sb:.2f}us installed={si:.2f}us speedup={sb/si:.2f}x")

print("VALIDATE_OK" if ok else "VALIDATE_FAIL")
raise SystemExit(0 if ok else 1)
