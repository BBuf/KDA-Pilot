"""Validate the integrated kda_kernels install() path on the remote H200.

Captures the original SGLang baselines, runs kda_kernels.install(strict=True),
confirms BOTH public symbols (triton_group_norm_silu, apply_group_norm_silu) are
swapped, then enforces the strict contract on the installed (swapped) callable path:
the native candidate actually runs for supported production buckets (dispatch path in
{small,large}, matches the eager F.silu(F.group_norm(...)) oracle, no NaN/Inf), and
unsupported / giant signatures fall back BIT-EXACTLY to the original baseline. Also a
smoke benchmark vs the captured baseline. Exits nonzero on any failure.

Run under no_grad: the candidate gate requires not torch.is_grad_enabled().
"""
import importlib
import statistics
import time

import torch
import torch.nn.functional as F
from torch import nn

DEV = "cuda"
_TOL = {"float16": (3e-3, 3e-3), "bfloat16": (7e-2, 2e-2)}

# --- capture the ORIGINAL baselines BEFORE install() --------------------------------
tmod = importlib.import_module("sglang.jit_kernel.diffusion.triton.group_norm_silu")
amod = importlib.import_module("sglang.jit_kernel.diffusion.group_norm_silu")
base_triton = tmod.triton_group_norm_silu
base_apply = amod.apply_group_norm_silu

import kda_kernels  # noqa: E402

results = kda_kernels.install(strict=True)
print("install:", results)

sw_triton = importlib.import_module("sglang.jit_kernel.diffusion.triton.group_norm_silu").triton_group_norm_silu
sw_apply = importlib.import_module("sglang.jit_kernel.diffusion.group_norm_silu").apply_group_norm_silu
ok = sw_triton is not base_triton and sw_apply is not base_apply
print(f"triton_group_norm_silu swapped={sw_triton is not base_triton} -> {sw_triton.__module__}")
print(f"apply_group_norm_silu  swapped={sw_apply is not base_apply} -> {sw_apply.__module__}")
ok &= "kda_kernels" in sw_triton.__module__ and "kda_kernels" in sw_apply.__module__

try:
    _disp = importlib.import_module("kda_kernels.diffusion.group_norm_silu._impls.h200.group_norm_dispatch")
except Exception:  # pragma: no cover
    _disp = None


def path() -> str:
    return _disp.last_dispatch() if _disp is not None else "?"


def oracle(x, w, b, ng, eps):
    return F.silu(F.group_norm(x, ng, w, b, eps))


def mk(shape, dtype, ng, eps=1e-6):
    c = shape[1]
    x = torch.randn(*shape, device=DEV, dtype=dtype)
    return x, torch.randn(c, device=DEV, dtype=dtype), torch.randn(c, device=DEV, dtype=dtype), ng, eps


def check_candidate(name, shape, dtype, ng, eps=1e-6):
    """Supported bucket: native path runs (small|large), matches oracle, finite."""
    global ok
    x, w, b, ng, eps = mk(shape, dtype, ng, eps)
    out = sw_triton(x, w, b, ng, eps)
    p = path()
    ref = oracle(x, w, b, ng, eps)
    atol, rtol = _TOL[str(dtype).split(".")[-1]]
    bad = []
    if p not in ("small", "large"):
        bad.append(f"path={p}(expected candidate)")
    if torch.isnan(out).any() or torch.isinf(out).any():
        bad.append("NaN/Inf")
    try:
        torch.testing.assert_close(out.float(), ref.float(), atol=atol, rtol=rtol)
    except AssertionError:
        bad.append(f"vs_oracle maxdiff={(out.float() - ref.float()).abs().max().item():.3e}")
    good = not bad
    ok &= good
    print(f"  cand {name}: {'OK' if good else 'FAIL ' + '; '.join(bad)} (path={p})")


def check_fallback(name, shape, dtype, ng, eps=1e-6):
    """Unsupported/giant: routes to baseline and equals the ORIGINAL baseline bit-for-bit."""
    global ok
    x, w, b, ng, eps = mk(shape, dtype, ng, eps)
    out = sw_triton(x, w, b, ng, eps)
    p = path()
    base = base_triton(x, w, b, num_groups=ng, eps=eps)
    eq = torch.equal(out, base)
    good = eq and p.startswith("baseline")
    ok &= good
    print(f"  fb   {name}: {'OK' if good else 'FAIL'} (path={p}, bitwise==baseline={eq})")


def wall(fn, it=100, warmup=20):
    for _ in range(warmup):
        fn()
    torch.cuda.synchronize()
    s = []
    for _ in range(it):
        t = time.perf_counter()
        fn()
        torch.cuda.synchronize()
        s.append((time.perf_counter() - t) * 1e6)
    return statistics.median(s)


with torch.no_grad():
    assert not torch.is_grad_enabled()
    print(f"device: {torch.cuda.get_device_name(0)} cap={torch.cuda.get_device_capability(0)}")

    # direct triton entry — supported production buckets run the native candidate
    check_candidate("small  [1,512,5,32,32]   fp16", (1, 512, 5, 32, 32), torch.float16, 32)
    check_candidate("medium [1,256,9,128,40]  fp16", (1, 256, 9, 128, 40), torch.float16, 32)
    check_candidate("bf16   [1,64,4,16,16]     bf16", (1, 64, 4, 16, 16), torch.bfloat16, 32)
    # unsupported / giant fall back bit-exactly to the original baseline
    check_fallback("giant  [1,256,17,256,256] fp16", (1, 256, 17, 256, 256), torch.float16, 32)
    check_fallback("ng=16  [2,64,32,32]       fp16", (2, 64, 32, 32), torch.float16, 16, eps=1e-5)

    # apply form (the Hunyuan VAE callsite) — supported shape runs the candidate, matches eager
    norm = nn.GroupNorm(32, 512, eps=1e-6, affine=True).to(DEV, torch.float16)
    act = nn.SiLU()
    xa = torch.randn(1, 512, 5, 32, 32, device=DEV, dtype=torch.float16)
    ya = sw_apply(xa, norm, act)
    pa = path()
    ra = F.silu(norm(xa))
    a_atol, a_rtol = _TOL["float16"]
    a_bad = []
    if pa not in ("small", "large"):
        a_bad.append(f"path={pa}(expected candidate)")
    try:
        torch.testing.assert_close(ya.float(), ra.float(), atol=a_atol, rtol=a_rtol)
    except AssertionError:
        a_bad.append(f"vs_oracle maxdiff={(ya.float() - ra.float()).abs().max().item():.3e}")
    ok &= not a_bad
    print(f"  apply  [1,512,5,32,32]   fp16: {'OK' if not a_bad else 'FAIL ' + '; '.join(a_bad)} (path={pa})")

    # smoke benchmark: installed (candidate) vs original baseline on production shapes
    for shape, label in [((1, 512, 5, 32, 32), "small"), ((1, 512, 3, 128, 40), "large"), ((1, 256, 9, 128, 40), "large")]:
        x, w, b, ng, eps = mk(shape, torch.float16, 32)
        sb = wall(lambda: base_triton(x, w, b, num_groups=ng, eps=eps))
        si = wall(lambda: sw_triton(x, w, b, ng, eps))
        print(f"  smoke {label} {tuple(shape)}: base={sb:.2f}us installed={si:.2f}us speedup={sb / si:.2f}x")

print("VALIDATE_OK" if ok else "VALIDATE_FAIL")
raise SystemExit(0 if ok else 1)
