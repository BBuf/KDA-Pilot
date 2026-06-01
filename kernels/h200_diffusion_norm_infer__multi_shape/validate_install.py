"""Validate the integrated kda_kernels install() path on the remote H200.

Captures the original SGLang baselines, runs kda_kernels.install(strict=True),
confirms both public symbols are swapped, then checks correctness (six perf
shapes + select01 oracle), fallback (one unsupported case per entry point), and
a smoke benchmark -- all through the installed SGLang-callable module attributes.
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
swapped_norm = sw_norm is not base_norm
swapped_rms = sw_rms is not base_rms
print(f"norm_infer swapped={swapped_norm} -> {sw_norm.__module__}")
print(f"triton_one_pass_rms_norm swapped={swapped_rms} -> {sw_rms.__module__}")


def ref_rms(x, w):
    xf = x.float()
    return (xf * torch.rsqrt(xf.pow(2).mean(-1, keepdim=True) + EPS) * w.float()).to(x.dtype)


def ref_ln(x, w, b):
    xf = x.float(); m = xf.mean(-1, keepdim=True); v = (xf - m).pow(2).mean(-1, keepdim=True)
    return ((xf - m) * torch.rsqrt(v + EPS) * w.float() + b.float()).to(x.dtype)


ok = swapped_norm and swapped_rms
for M, N in [(648720, 128), (1320, 128), (650040, 128), (16384, 128), (4096, 128)]:
    x = torch.randn(M, N, device=DEV, dtype=torch.bfloat16); w = torch.randn(N, device=DEV, dtype=torch.bfloat16)
    y = sw_rms(x, w, EPS); yb = base_rms(x, w, EPS); torch.cuda.synchronize()
    db = (y.float() - yb.float()).abs().max().item(); dr = (y.float() - ref_rms(x, w).float()).abs().max().item()
    good = db < 5e-2 and not torch.isnan(y).any()
    ok &= good
    print(f"  rms {M}x{N}: vs_base={db:.2e} vs_ref={dr:.2e} {'OK' if good else 'FAIL'}")

x = torch.randn(8640, 5120, device=DEV, dtype=torch.float32)
w = torch.randn(5120, device=DEV, dtype=torch.float32); b = torch.randn(5120, device=DEV, dtype=torch.float32)
y = sw_norm(x, w, b, EPS, is_rms_norm=False); yb = base_norm(x, w, b, EPS, is_rms_norm=False); torch.cuda.synchronize()
db = (y.float() - yb.float()).abs().max().item(); good = db < 1e-4
ok &= good
print(f"  ln 8640x5120: vs_base={db:.2e} {'OK' if good else 'FAIL'}")

# Fallback (unsupported -> baseline; must equal the original baseline exactly)
xf16 = torch.randn(256, 128, device=DEV, dtype=torch.float16); wf16 = torch.randn(128, device=DEV, dtype=torch.float16)
fb1 = torch.equal(sw_rms(xf16, wf16, EPS), base_rms(xf16, wf16, EPS))
xr = torch.randn(256, 512, device=DEV, dtype=torch.float32); wr = torch.randn(512, device=DEV, dtype=torch.float32)
fb2 = torch.equal(sw_norm(xr, wr, None, EPS, is_rms_norm=True), base_norm(xr, wr, None, EPS, is_rms_norm=True))
ok &= fb1 and fb2
print(f"  fallback fp16-rms={fb1} rmsnorm-via-norm_infer={fb2}")

# select01 modulation oracle through the installed norm_infer
def modulate(fn, x, w, b, sc, sh):
    n = fn(x.view(-1, x.shape[-1]), w, b, EPS, is_rms_norm=False).view_as(x)
    return n * (1 + sc.unsqueeze(1)) + sh.unsqueeze(1)
xx = torch.randn(2, 128, 3072, device=DEV, dtype=torch.bfloat16)
ww = torch.randn(3072, device=DEV, dtype=torch.bfloat16); bb = torch.randn(3072, device=DEV, dtype=torch.bfloat16)
sc = torch.randn(2, 3072, device=DEV, dtype=torch.bfloat16); sh = torch.randn(2, 3072, device=DEV, dtype=torch.bfloat16)
od = (modulate(sw_norm, xx, ww, bb, sc, sh).float() - modulate(base_norm, xx, ww, bb, sc, sh).float()).abs().max().item()
ok &= od < 5e-2
print(f"  select01 oracle (installed norm_infer): vs_base={od:.2e}")


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
