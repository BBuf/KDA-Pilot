"""Correctness harness for ``b200_diffusion_rotary_embedding__multi_shape``.

Validates the two SGLang diffusion rotary-embedding entry points and the native
CUDA candidate against:
  * a pure-FP32 PyTorch reference implementing the exact recovered rotation
    (adjacent-pair for the standard kernel; split-half for LTX-2), and
  * the SGLang Triton baseline (production reference, primary oracle), and
  * an exact-numeric-order LTX-2 reference (bf16-round on x*cos) that the baseline
    and candidate must both track tightly.

Recovered contract (see ``interface.md``, pinned SGLang commit 0b65588c1):
  * ``apply_rotary_embedding(x, cos, sin, interleaved=False)`` -> NEW tensor,
    adjacent pairs (x[2i], x[2i+1]); cos/sin token-shared.
  * ``apply_ltx2_split_rotary_emb(x, cos, sin)`` -> NEW tensor, split-half
    (x[i], x[i+half]); cos/sin per-(B,H,token); baseline rounds x*cos to bf16
    before the fp32 sine add.

Tolerance: SGLang-style dynamic bound — within ``floor + k * bf16_quant_noise``.

Run standalone:  python tests/test_correctness.py
Run under pytest: KDA_RUN_CORRECTNESS=1 pytest -q tests/test_correctness.py
"""

from __future__ import annotations

import hashlib
import importlib.util
import os
from pathlib import Path
from typing import Any

import pytest

try:
    import torch
except ImportError:  # pragma: no cover - CUDA env owns the real run
    torch = None  # type: ignore

KERNEL_SLUG = "b200_diffusion_rotary_embedding__multi_shape"
OP_TYPE = "rotary_embedding"
KERNEL_DIR = Path(__file__).resolve().parents[1]

_TOL_K = 6.0
_TOL_FLOOR = 1.5e-3

pytestmark = pytest.mark.skipif(
    torch is None or os.environ.get("KDA_RUN_CORRECTNESS") != "1",
    reason="Set KDA_RUN_CORRECTNESS=1 (and run on a CUDA box) to execute correctness cases.",
)


# ---------------------------------------------------------------------------
# Module loading
# ---------------------------------------------------------------------------
def _load(name: str, relpath: str):
    path = KERNEL_DIR / relpath
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None, path
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _register():
    return _load(f"kda_{KERNEL_SLUG}_register", "src/register.py")


def _wrapper():
    return _load(f"kda_{KERNEL_SLUG}_wrapper", "src/wrapper.py")


def _sglang_standard():
    from sglang.jit_kernel.diffusion.triton.rotary import apply_rotary_embedding

    return apply_rotary_embedding


def _sglang_ltx2():
    from sglang.jit_kernel.diffusion.triton.ltx2_rotary import apply_ltx2_split_rotary_emb

    return apply_ltx2_split_rotary_emb


# ---------------------------------------------------------------------------
# References
# ---------------------------------------------------------------------------
def ref_standard(x, cos, sin, interleaved: bool):
    head_size = x.shape[-1]
    if interleaved and cos.shape[-1] == head_size:
        cos_u, sin_u = cos[..., ::2], sin[..., ::2]
    else:
        cos_u, sin_u = cos, sin
    xf = x.float()
    x1, x2 = xf[..., 0::2], xf[..., 1::2]
    cf, sf = cos_u.float(), sin_u.float()
    if xf.dim() == 4:
        cf = cf.view(1, cf.shape[0], 1, cf.shape[1])
        sf = sf.view(1, sf.shape[0], 1, sf.shape[1])
    else:
        cf = cf.view(cf.shape[0], 1, cf.shape[1])
        sf = sf.view(sf.shape[0], 1, sf.shape[1])
    o1 = x1 * cf - x2 * sf
    o2 = x1 * sf + x2 * cf
    return torch.stack((o1, o2), dim=-1).flatten(-2)  # FP32 mathematical ideal


def _ltx2_split(x, cos, sin, *, bf16_round: bool):
    B, S, inner = x.shape
    _, H, _, half = cos.shape
    head_dim = 2 * half
    xf = x.float().view(B, S, H, head_dim)
    x_first, x_second = xf[..., :half], xf[..., half:]
    cosp = cos.permute(0, 2, 1, 3).float()
    sinp = sin.permute(0, 2, 1, 3).float()
    if bf16_round:  # match the baseline numeric order exactly
        fc = (x_first * cosp).to(torch.bfloat16).float()
        sc = (x_second * cosp).to(torch.bfloat16).float()
        out_first = fc - x_second * sinp
        out_second = sc + x_first * sinp
    else:  # pure FP32 mathematical ideal
        out_first = x_first * cosp - x_second * sinp
        out_second = x_second * cosp + x_first * sinp
    return torch.cat((out_first, out_second), dim=-1).reshape(B, S, inner)


def ref_ltx2(x, cos, sin):
    return _ltx2_split(x, cos, sin, bf16_round=False)


def ref_ltx2_exact(x, cos, sin):
    return _ltx2_split(x, cos, sin, bf16_round=True)


# ---------------------------------------------------------------------------
# Case table
# ---------------------------------------------------------------------------
def _seed(name: str) -> int:
    return int(hashlib.md5(name.encode()).hexdigest()[:8], 16)  # stable across processes


def _standard_case(name, x_shape, num_tokens, head_size, interleaved, optimization):
    def build():
        g = torch.Generator(device="cuda").manual_seed(_seed(name))
        x = torch.randn(*x_shape, generator=g, device="cuda", dtype=torch.bfloat16)
        width = head_size if interleaved else head_size // 2
        ang = torch.randn(num_tokens, width, generator=g, device="cuda", dtype=torch.float32)
        return {"x": x, "cos": ang.cos(), "sin": ang.sin(), "interleaved": interleaved}

    return {"name": name, "kind": "standard", "build": build, "optimization": optimization}


def _ltx2_case(name, B, S, H, half, optimization):
    inner = H * 2 * half

    def build():
        g = torch.Generator(device="cuda").manual_seed(_seed(name))
        x = torch.randn(B, S, inner, generator=g, device="cuda", dtype=torch.bfloat16)
        ang = torch.randn(B, S, H, half, generator=g, device="cuda", dtype=torch.float32)
        cos = ang.cos().to(torch.bfloat16).permute(0, 2, 1, 3)  # [B,H,S,half] non-contig
        sin = ang.sin().to(torch.bfloat16).permute(0, 2, 1, 3)
        return {"x": x, "cos": cos, "sin": sin}

    return {"name": name, "kind": "ltx2", "build": build, "optimization": optimization}


def make_cases() -> list[dict[str, Any]]:
    cases: list[dict[str, Any]] = []
    cases.append(_standard_case("std__hunyuanvideo__B1S27030H24D128", (1, 27030, 24, 128), 27030, 128, False, True))
    for nt in (1, 129, 2048):
        cases.append(_standard_case(f"std__reg__S{nt}H8D128_il0", (nt, 8, 128), nt, 128, False, False))
    cases.append(_standard_case("std__reg__S2048H24D128_il0", (2048, 24, 128), 2048, 128, False, False))
    cases.append(_standard_case("std__reg__S256H8D64_il0", (256, 8, 64), 256, 64, False, False))
    cases.append(_standard_case("std__reg__S256H8D128_il1", (256, 8, 128), 256, 128, True, False))
    for name, B, S, half in [
        ("ltx2__ti2v__B1S1536h64", 1, 1536, 64), ("ltx2__ti2v__B1S126h32", 1, 126, 32),
        ("ltx2__ti2v__B1S1536h32", 1, 1536, 32), ("ltx2__ti2v__B1S6144h64", 1, 6144, 64),
        ("ltx2__ti2v__B1S6144h32", 1, 6144, 32), ("ltx2__two__B2S6144h64", 2, 6144, 64),
        ("ltx2__two__B2S126h32", 2, 126, 32), ("ltx2__two__B2S6144h32", 2, 6144, 32),
        ("ltx2__two__B1S24576h64", 1, 24576, 64), ("ltx2__two__B1S24576h32", 1, 24576, 32),
    ]:
        cases.append(_ltx2_case(name, B, S, 32, half, True))
    return cases


def baseline(case, inp):
    if case["kind"] == "standard":
        return _sglang_standard()(inp["x"], inp["cos"], inp["sin"], inp["interleaved"])
    return _sglang_ltx2()(inp["x"], inp["cos"], inp["sin"])


def reference(case, inp):
    if case["kind"] == "standard":
        return ref_standard(inp["x"], inp["cos"], inp["sin"], inp["interleaved"])
    return ref_ltx2(inp["x"], inp["cos"], inp["sin"])


def candidate(case, inp, wrapper):
    if case["kind"] == "standard":
        return wrapper.apply_rotary_embedding(inp["x"], inp["cos"], inp["sin"], inp["interleaved"])
    return wrapper.apply_ltx2_split_rotary_emb(inp["x"], inp["cos"], inp["sin"])


# ---------------------------------------------------------------------------
# Comparison
# ---------------------------------------------------------------------------
def _check_no_nan_inf(t, name):
    assert not torch.isnan(t).any(), f"{name} contains NaN"
    assert not torch.isinf(t).any(), f"{name} contains Inf"


def _dyn_tol(ref_fp32):
    quant = (ref_fp32 - ref_fp32.to(torch.bfloat16).float()).abs().max().item()
    return _TOL_FLOOR + _TOL_K * quant


def compare(actual, ref_fp32, name):
    a, r = actual.float(), ref_fp32.float()
    _check_no_nan_inf(a, name)
    assert a.shape == r.shape, f"{name} shape {tuple(a.shape)} != {tuple(r.shape)}"
    return (a - r).abs().max().item(), _dyn_tol(r)


def compare_to_baseline(actual, base, name):
    a, b = actual.float(), base.float()
    _check_no_nan_inf(a, name)
    assert a.shape == b.shape, f"{name} shape mismatch"
    quant = b.abs().max().item() * (2.0 ** -8)  # ~1 bf16 ulp at peak magnitude
    return (a - b).abs().max().item(), _TOL_FLOOR + _TOL_K * quant


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------
def test_register_metadata_and_exports() -> None:
    reg = _register()
    spec = reg.register()
    assert spec["name"] == KERNEL_SLUG and spec["op_type"] == OP_TYPE and callable(spec["callable"])
    assert set(reg.EXPORTS.keys()) == {"apply_rotary_embedding", "apply_ltx2_split_rotary_emb"}
    for fn in reg.EXPORTS.values():
        assert callable(fn)


def test_baseline_matches_fp32_reference() -> None:
    failures = []
    for case in make_cases():
        inp = case["build"]()
        max_err, atol = compare(baseline(case, inp), reference(case, inp), case["name"])
        if max_err > atol:
            failures.append((case["name"], max_err, atol))
    assert not failures, f"baseline vs FP32 reference exceeded tolerance: {failures}"


def test_ltx2_baseline_tracks_exact_numeric_order() -> None:
    # The baseline follows the recovered bf16-round numeric order, so it must match the
    # exact-order reference within ~2 bf16 ulp; and that round must be OBSERVABLE (exact
    # vs pure-fp32 differ), which is what makes the tight candidate-vs-baseline check
    # meaningful — a candidate that dropped the round would deviate by ~1 ulp.
    observable = False
    for case in make_cases():
        if case["kind"] != "ltx2":
            continue
        inp = case["build"]()
        base = baseline(case, inp).float()
        exact = ref_ltx2_exact(inp["x"], inp["cos"], inp["sin"]).float()
        pure = ref_ltx2(inp["x"], inp["cos"], inp["sin"]).float()
        if (exact - pure).abs().max().item() > 0.0:
            observable = True
        tol = _TOL_FLOOR + 2.0 * (base.abs().max().item() * (2.0 ** -8))  # ~2 ulp
        err_exact = (base - exact).abs().max().item()
        assert err_exact <= tol, f"{case['name']}: baseline does not track exact order ({err_exact} > {tol})"
    assert observable, "bf16-round on x*cos was never observable across LTX-2 cases"


def test_candidate_matches_baseline_and_dispatches() -> None:
    wrapper = _wrapper()
    ran = 0
    for case in make_cases():
        if not case["optimization"]:
            continue  # production signatures only must take the CUDA path
        inp = case["build"]()
        base = baseline(case, inp)
        cand = candidate(case, inp, wrapper)
        which = "standard" if case["kind"] == "standard" else "ltx2"
        assert wrapper.last_dispatch_path(which) == "cuda", f"{case['name']} did not take cuda path"
        max_err, atol = compare_to_baseline(cand, base, case["name"])
        assert max_err <= atol, f"{case['name']}: candidate vs baseline {max_err} > {atol}"
        ran += 1
    assert ran == 11, f"expected 11 production signatures, ran {ran}"


def test_dispatch_gates_reject_unsupported() -> None:
    # Only the CAPTURED signatures are routed to CUDA; everything else (incl. non-captured
    # but otherwise-valid shapes) must fall back to the SGLang baseline.
    wrapper = _wrapper()
    g = torch.Generator(device="cuda").manual_seed(7)

    # standard: a non-captured shape (4,8,128) must NOT be supported (fallback), nor variants.
    x = torch.randn(4, 8, 128, generator=g, device="cuda", dtype=torch.bfloat16)
    cos = torch.randn(4, 64, generator=g, device="cuda", dtype=torch.float32)
    sin = torch.randn(4, 64, generator=g, device="cuda", dtype=torch.float32)
    assert not wrapper._supported_standard(x, cos, sin, False)  # non-captured shape -> fallback
    assert not wrapper._supported_standard(x, cos, sin, True)  # interleaved
    assert not wrapper._supported_standard(x.half(), cos, sin, False)  # non-bf16
    assert not wrapper._supported_standard(x.cpu(), cos, sin, False)  # cpu
    assert not wrapper._supported_standard(x, cos.half(), sin.half(), False)  # cos dtype
    # captured standard (1,27030,24,128) IS supported (also exercised in the candidate test).
    xc = torch.empty(1, 27030, 24, 128, device="cuda", dtype=torch.bfloat16)
    cc = torch.empty(27030, 64, device="cuda", dtype=torch.float32)
    assert wrapper._supported_standard(xc, cc, cc, False)
    del xc, cc

    # ltx2: captured (1,1536,64) supported; non-captured tuples / heads / half -> fallback.
    def _ltx2(B, S, H, half):
        x_ = torch.randn(B, S, H * 2 * half, generator=g, device="cuda", dtype=torch.bfloat16)
        c_ = torch.randn(B, S, H, half, generator=g, device="cuda", dtype=torch.bfloat16).permute(0, 2, 1, 3)
        s_ = torch.randn(B, S, H, half, generator=g, device="cuda", dtype=torch.bfloat16).permute(0, 2, 1, 3)
        return x_, c_, s_
    xl, cl, sl = _ltx2(1, 1536, 32, 64)
    assert wrapper._supported_ltx2(xl, cl, sl)  # captured
    assert not wrapper._supported_ltx2(xl.half(), cl, sl)  # non-bf16 x
    assert not wrapper._supported_ltx2(xl.cpu(), cl.cpu(), sl.cpu())  # cpu
    assert not wrapper._supported_ltx2(*_ltx2(2, 1536, 32, 64))  # non-captured (B,S,half) tuple
    assert not wrapper._supported_ltx2(*_ltx2(1, 512, 32, 64))  # non-captured seq_len
    assert not wrapper._supported_ltx2(*_ltx2(1, 1536, 16, 64))  # num_heads != 32
    assert not wrapper._supported_ltx2(*_ltx2(1, 1536, 32, 16))  # half not in {32,64}


def _misaligned_view(shape, dtype):
    """A contiguous tensor whose data_ptr() is NOT 16-byte aligned (sliced/offset view)."""
    numel = 1
    for s in shape:
        numel *= s
    base = torch.empty(numel + 8, device="cuda", dtype=dtype)
    for off in range(1, 8):
        v = base.narrow(0, off, numel)
        if v.data_ptr() % 16 != 0:
            return v.view(*shape)
    return None


def test_dispatch_rejects_misaligned_views() -> None:
    # A contiguous tensor can still have a non-16-byte-aligned base pointer; the int4-vectorized
    # CUDA kernels require 16-byte alignment, so misaligned captured-shape inputs must fall back.
    wrapper = _wrapper()
    g = torch.Generator(device="cuda").manual_seed(13)
    cos = torch.randn(27030, 64, generator=g, device="cuda", dtype=torch.float32)
    xm = _misaligned_view((1, 27030, 24, 128), torch.bfloat16)
    if xm is not None:
        assert xm.is_contiguous() and xm.data_ptr() % 16 != 0  # precondition
        assert not wrapper._supported_standard(xm, cos, cos, False)  # misaligned x -> fallback
        del xm
    xl = _misaligned_view((1, 126, 32 * 64), torch.bfloat16)
    cl = torch.randn(1, 126, 32, 32, generator=g, device="cuda", dtype=torch.bfloat16).permute(0, 2, 1, 3)
    sl = torch.randn(1, 126, 32, 32, generator=g, device="cuda", dtype=torch.bfloat16).permute(0, 2, 1, 3)
    if xl is not None:
        assert not wrapper._supported_ltx2(xl, cl, sl)  # misaligned x -> fallback
    xl2 = torch.randn(1, 126, 32 * 64, generator=g, device="cuda", dtype=torch.bfloat16)
    cm = _misaligned_view((1, 126, 32, 32), torch.bfloat16)
    if cm is not None:
        assert not wrapper._supported_ltx2(xl2, cm.permute(0, 2, 1, 3), sl)  # misaligned cos -> fallback


def test_multi_gpu_launches_on_input_device() -> None:
    # The CUDA kernel must launch on the INPUT tensors' device, not the process-current device.
    # With inputs on cuda:1 while current is cuda:0, an unguarded launch hits the wrong GPU.
    if torch.cuda.device_count() < 2:
        pytest.skip("needs >= 2 visible CUDA devices (e.g. CUDA_VISIBLE_DEVICES=<a>,<b>)")
    wrapper = _wrapper()
    dev = torch.device("cuda:1")
    g = torch.Generator(device=dev).manual_seed(21)
    try:
        # LTX-2 small captured on cuda:1
        xl = torch.randn(1, 126, 32 * 64, generator=g, device=dev, dtype=torch.bfloat16)
        ang = torch.randn(1, 126, 32, 32, generator=g, device=dev, dtype=torch.float32)
        cl = ang.cos().to(torch.bfloat16).permute(0, 2, 1, 3)
        sl = ang.sin().to(torch.bfloat16).permute(0, 2, 1, 3)
        # standard captured on cuda:1
        xs = torch.randn(1, 27030, 24, 128, generator=g, device=dev, dtype=torch.bfloat16)
        angs = torch.randn(27030, 64, generator=g, device=dev, dtype=torch.float32)
        coss, sins = angs.cos(), angs.sin()
        with torch.cuda.device(dev):  # baselines computed with the correct current device
            base_l = _sglang_ltx2()(xl, cl, sl)
            base_s = _sglang_standard()(xs, coss, sins, False)
        torch.cuda.set_device(0)  # MISMATCH: current device cuda:0, tensors on cuda:1
        out_l = wrapper.apply_ltx2_split_rotary_emb(xl, cl, sl)  # CUDAGuard must retarget cuda:1
        out_s = wrapper.apply_rotary_embedding(xs, coss, sins, False)
        torch.cuda.synchronize(dev)
        assert wrapper.last_dispatch_path("ltx2") == "cuda" and out_l.device == dev
        assert wrapper.last_dispatch_path("standard") == "cuda" and out_s.device == dev
        assert (out_l.float() - base_l.float()).abs().max().item() <= 1e-3
        assert (out_s.float() - base_s.float()).abs().max().item() <= 0.06  # ~1-2 bf16 ulp
    finally:
        torch.cuda.set_device(0)


def test_fallback_runs_baseline() -> None:
    # interleaved=True (head_dim 128) is unsupported -> fallback -> matches baseline.
    wrapper = _wrapper()
    g = torch.Generator(device="cuda").manual_seed(11)
    x = torch.randn(256, 8, 128, generator=g, device="cuda", dtype=torch.bfloat16)
    cos = torch.randn(256, 128, generator=g, device="cuda", dtype=torch.float32)
    sin = torch.randn(256, 128, generator=g, device="cuda", dtype=torch.float32)
    out = wrapper.apply_rotary_embedding(x, cos, sin, True)
    assert wrapper.last_dispatch_path("standard") == "fallback"
    base = _sglang_standard()(x, cos, sin, True)
    assert torch.equal(out, base)  # same baseline call -> identical


def test_mutation_contract_out_of_place() -> None:
    wrapper = _wrapper()
    for case in make_cases():
        if not case["optimization"]:
            continue
        inp = case["build"]()
        x_before = inp["x"].clone()
        out = candidate(case, inp, wrapper)
        assert out.data_ptr() != inp["x"].data_ptr(), f"{case['name']} not a new tensor"
        assert torch.equal(inp["x"], x_before), f"{case['name']} mutated input x"
        assert out.shape == inp["x"].shape and out.dtype == inp["x"].dtype


if __name__ == "__main__":
    assert torch is not None and torch.cuda.is_available(), "needs CUDA"
    cases = make_cases()
    wrapper = _wrapper()
    print(f"# {len(cases)} cases | device={torch.cuda.get_device_name(0)}")
    n_fail = 0
    for case in cases:
        inp = case["build"]()
        base = baseline(case, inp)
        ref = reference(case, inp)
        be, ba = compare(base, ref, case["name"])
        prod = case["optimization"]
        cand = candidate(case, inp, wrapper) if prod else None
        if prod:
            which = "standard" if case["kind"] == "standard" else "ltx2"
            path = wrapper.last_dispatch_path(which)
            ce, ca = compare_to_baseline(cand, base, case["name"])
            ok = (be <= ba) and (ce <= ca) and path == "cuda"
            n_fail += 0 if ok else 1
            print(f"[{'OK ' if ok else 'FAIL'}] {case['name']:<34} base_vs_ref={be:.4f}/{ba:.4f} "
                  f"cand_vs_base={ce:.4f}/{ca:.4f} path={path}")
        else:
            ok = be <= ba
            n_fail += 0 if ok else 1
            print(f"[{'OK ' if ok else 'FAIL'}] {case['name']:<34} base_vs_ref={be:.4f}/{ba:.4f} (fallback-shape)")
    print(f"# {len(cases)-n_fail}/{len(cases)} ok")
    raise SystemExit(1 if n_fail else 0)
