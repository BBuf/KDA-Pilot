"""Correctness harness for ``b200_diffusion_rotary_embedding__multi_shape``.

Oracle (per the recovered contract and repo README): the SGLang diffusion Triton
baselines ``apply_rotary_embedding`` / ``apply_ltx2_split_rotary_emb`` are the
production reference, cross-checked against a PyTorch FP32 recomputation with
SGLang-style dynamic BF16-aware tolerances. (``test_rope.py`` exercises a
different function -- LLM q/k ``apply_rope_inplace`` -- and is style guidance
only, not the oracle here.)

Skipped unless ``KDA_RUN_CORRECTNESS=1`` (runs on the remote B200 in the
sglang_bbuf container). Build of the candidate goes through SGLang jit_kernel.
"""

from __future__ import annotations

import importlib.util
import os
from pathlib import Path
from typing import Any

import pytest

try:
    import torch
except ImportError:  # pragma: no cover - CUDA env owns the real run
    torch = None


KERNEL_SLUG = "b200_diffusion_rotary_embedding__multi_shape"
OP_TYPE = "rotary_embedding"
KERNEL_DIR = Path(__file__).resolve().parents[1]

pytestmark = pytest.mark.skipif(
    os.environ.get("KDA_RUN_CORRECTNESS") != "1",
    reason="Set KDA_RUN_CORRECTNESS=1 on the remote B200 to run correctness.",
)


def _load_register_module():
    register_py = KERNEL_DIR / "src" / "register.py"
    spec = importlib.util.spec_from_file_location(
        f"kda_kernel_{KERNEL_SLUG}_register", register_py
    )
    assert spec is not None and spec.loader is not None, register_py
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# Load the register module exactly once. Re-loading it per call would re-exec
# wrapper.py and re-dlopen the jit module every invocation, adding a multi-ms
# fixed tax that has nothing to do with the kernel (it would dominate timing).
_REGISTER_MODULE = None


def _register_module():
    global _REGISTER_MODULE
    if _REGISTER_MODULE is None:
        _REGISTER_MODULE = _load_register_module()
    return _REGISTER_MODULE


# --------------------------------------------------------------------------
# Input builders (reproduce the captured production layouts exactly)
# --------------------------------------------------------------------------
def _standard_inputs(tokens: int, heads: int, head_dim: int, *, seed: int = 0):
    g = torch.Generator(device="cuda").manual_seed(seed)
    x = torch.randn(1, tokens, heads, head_dim, generator=g, device="cuda", dtype=torch.float32).bfloat16()
    half = head_dim // 2
    cos = torch.randn(tokens, half, generator=g, device="cuda", dtype=torch.float32)
    sin = torch.randn(tokens, half, generator=g, device="cuda", dtype=torch.float32)
    return x, cos, sin


def _ltx2_inputs(batch: int, seq: int, heads: int, half: int, *, seed: int = 0):
    head_dim = 2 * half
    inner = heads * head_dim
    g = torch.Generator(device="cuda").manual_seed(seed)
    x = torch.randn(batch, seq, inner, generator=g, device="cuda", dtype=torch.float32).bfloat16()
    # Captured cos/sin are (B, H, S, half) NON-contiguous: a transposed view of a
    # contiguous (B, S, H, half) buffer -> head stride=half, seq stride=H*half.
    cos_c = torch.randn(batch, seq, heads, half, generator=g, device="cuda", dtype=torch.float32).bfloat16()
    sin_c = torch.randn(batch, seq, heads, half, generator=g, device="cuda", dtype=torch.float32).bfloat16()
    cos = cos_c.permute(0, 2, 1, 3)
    sin = sin_c.permute(0, 2, 1, 3)
    return x, cos, sin


# --------------------------------------------------------------------------
# FP32 references (true math; the bf16 baselines carry a small quantization bias)
# --------------------------------------------------------------------------
def _ref_standard(x, cos, sin):
    xf = x.float()
    b, t, h, d = xf.shape
    x1 = xf[..., 0:d:2]
    x2 = xf[..., 1:d:2]
    c = cos.float().view(1, t, 1, d // 2)
    s = sin.float().view(1, t, 1, d // 2)
    out = torch.empty_like(xf)
    out[..., 0:d:2] = x1 * c - x2 * s
    out[..., 1:d:2] = x2 * c + x1 * s
    return out


def _ref_ltx2(x, cos, sin):
    b, s, inner = x.shape
    _, heads, _, half = cos.shape
    head_dim = 2 * half
    xf = x.float().view(b, s, heads, head_dim)
    x_first = xf[..., :half]
    x_second = xf[..., half:]
    cf = cos.float().permute(0, 2, 1, 3)
    sf = sin.float().permute(0, 2, 1, 3)
    out = torch.empty_like(xf)
    out[..., :half] = x_first * cf - x_second * sf
    out[..., half:] = x_second * cf + x_first * sf
    return out.view(b, s, inner)


# --------------------------------------------------------------------------
# Configured cases: 1 standard + 10 LTX-2 unique captured signatures
# --------------------------------------------------------------------------
def make_cases() -> list[dict[str, Any]]:
    if torch is None or not torch.cuda.is_available():
        return []
    cases: list[dict[str, Any]] = []

    x, cos, sin = _standard_inputs(27030, 24, 128, seed=1)
    cases.append(
        {
            "name": "hunyuanvideo__standard__1x27030x24x128",
            "kind": "standard",
            "entry": "apply_rotary_embedding",
            "args": (x, cos, sin, False),
            "ref": _ref_standard,
            "warmup": 50,
            "iters": 300,
        }
    )

    ltx2_specs = [
        ("ltx23_ti2v__1x1536x4096__half64", 1, 1536, 32, 64),
        ("ltx23_ti2v__1x126x2048__half32", 1, 126, 32, 32),
        ("ltx23_ti2v__1x1536x2048__half32", 1, 1536, 32, 32),
        ("ltx23_ti2v__1x6144x4096__half64", 1, 6144, 32, 64),
        ("ltx23_ti2v__1x6144x2048__half32", 1, 6144, 32, 32),
        ("ltx23_two__2x6144x4096__half64", 2, 6144, 32, 64),
        ("ltx23_two__2x126x2048__half32", 2, 126, 32, 32),
        ("ltx23_two__2x6144x2048__half32", 2, 6144, 32, 32),
        ("ltx23_two__1x24576x4096__half64", 1, 24576, 32, 64),
        ("ltx23_two__1x24576x2048__half32", 1, 24576, 32, 32),
    ]
    for i, (name, b, s, h, half) in enumerate(ltx2_specs):
        x, cos, sin = _ltx2_inputs(b, s, h, half, seed=100 + i)
        cases.append(
            {
                "name": name,
                "kind": "ltx2",
                "entry": "apply_ltx2_split_rotary_emb",
                "args": (x, cos, sin),
                "ref": _ref_ltx2,
                "warmup": 50,
                "iters": 300,
            }
        )
    return cases


def baseline(case: dict[str, Any]) -> Any:
    """SGLang diffusion Triton baseline (the production oracle)."""
    if case["kind"] == "standard":
        from sglang.jit_kernel.diffusion.triton.rotary import apply_rotary_embedding as fn
    else:
        from sglang.jit_kernel.diffusion.triton.ltx2_rotary import apply_ltx2_split_rotary_emb as fn
    return fn(*case["args"])


def candidate(case: dict[str, Any]) -> Any:
    module = _register_module()
    fn = module.EXPORTS[case["entry"]]
    return fn(*case["args"])


def _assert_no_nan_inf(value: Any, *, path: str) -> None:
    assert not torch.isnan(value).any(), f"{path} contains NaN"
    assert not torch.isinf(value).any(), f"{path} contains Inf"


def _check_case(case: dict[str, Any]) -> dict[str, float]:
    args = case["args"]
    x = args[0]
    x_before = x.clone()

    base = baseline(case)
    cand = candidate(case)
    ref = case["ref"](*args[:3])

    # out-of-place: the input must not be mutated by either path
    assert torch.equal(x, x_before), f"{case['name']}: input tensor was mutated (not out-of-place)"
    _assert_no_nan_inf(base, path=f"{case['name']}:baseline")
    _assert_no_nan_inf(cand, path=f"{case['name']}:candidate")

    assert cand.shape == base.shape == x.shape, f"{case['name']}: shape mismatch"
    assert cand.dtype == base.dtype == x.dtype, f"{case['name']}: dtype mismatch"

    bf = base.float()
    cf = cand.float()
    base_err = (bf - ref).abs().max().item()
    cand_err = (cf - ref).abs().max().item()
    pair_diff = (cf - bf).abs().max().item()

    # Dynamic BF16-aware bound: candidate's error vs FP32 must not exceed a small
    # multiple of the baseline's own bf16 quantization noise (plus a small floor).
    floor = 2.0 ** -7
    bound = max(2.0 * base_err, floor)
    assert cand_err <= bound, f"{case['name']}: cand_err {cand_err} > bound {bound} (base_err {base_err})"
    # Candidate must track the production oracle (baseline) closely.
    assert pair_diff <= bound, f"{case['name']}: pair_diff {pair_diff} > bound {bound}"

    return {"base_err": base_err, "cand_err": cand_err, "pair_diff": pair_diff}


def test_register_metadata() -> None:
    module = _load_register_module()
    assert hasattr(module, "register")
    spec = module.register()
    assert spec["name"] == KERNEL_SLUG
    assert spec["op_type"] == OP_TYPE
    assert callable(spec["callable"])
    assert "apply_rotary_embedding" in spec["exports"]
    assert "apply_ltx2_split_rotary_emb" in spec["exports"]


def test_correctness_cases() -> None:
    cases = make_cases()
    assert cases, "No correctness cases (need CUDA). Fill make_cases() before optimizing."
    assert len(cases) == 11, f"expected 11 unique signatures, got {len(cases)}"
    for case in cases:
        stats = _check_case(case)
        print(
            f"{case['name']}: base_err={stats['base_err']:.3e} "
            f"cand_err={stats['cand_err']:.3e} pair_diff={stats['pair_diff']:.3e}"
        )


def _assert_falls_back(kind: str, args: tuple) -> None:
    """After the public symbol is swapped to the wrapper, a non-captured signature
    must reach the bound ORIGINAL baseline EXACTLY ONCE (no recursion) and take NO
    CUDA fast path. We spy on the wrapper's captured baseline (call-count) and make
    the CUDA loader raise if invoked, so output-equality cannot mask a stray fast path."""
    module = _register_module()
    w = module._wrapper  # the wrapper module backing EXPORTS
    import sglang.jit_kernel.diffusion.triton.rotary as rmod
    import sglang.jit_kernel.diffusion.triton.ltx2_rotary as lmod

    if kind == "standard":
        pub_mod, pub_name, orig_attr, load_attr = rmod, "apply_rotary_embedding", "_original_rotary", "_load_standard"
    else:
        pub_mod, pub_name, orig_attr, load_attr = lmod, "apply_ltx2_split_rotary_emb", "_original_ltx2", "_load_ltx2"

    pub_orig = getattr(pub_mod, pub_name)
    expected = pub_orig(*args)  # true baseline output, captured before any swap
    wfn = module.EXPORTS[pub_name]

    true_baseline = getattr(w, orig_attr)
    assert true_baseline is not None, "wrapper did not capture the original baseline at import"
    calls = {"n": 0}

    def spy(*a, **k):
        calls["n"] += 1
        return true_baseline(*a, **k)

    def boom(*a, **k):
        raise AssertionError(f"CUDA fast path must NOT run for a non-captured {kind} signature")

    saved_orig = getattr(w, orig_attr)
    saved_load = getattr(w, load_attr)
    try:
        setattr(w, orig_attr, spy)       # spy on the captured original baseline
        setattr(w, load_attr, boom)      # any CUDA fast-path build must fail the test
        setattr(pub_mod, pub_name, wfn)  # simulate install() public-symbol swap
        got = wfn(*args)
    finally:
        setattr(pub_mod, pub_name, pub_orig)
        setattr(w, orig_attr, saved_orig)
        setattr(w, load_attr, saved_load)

    assert calls["n"] == 1, f"{kind}: bound original baseline reached {calls['n']} times (expected exactly 1)"
    torch.testing.assert_close(got.float(), expected.float(), rtol=0, atol=0)


def test_fallback_non_captured() -> None:
    """Every non-captured class must fall back to the baseline (recursion-safe)."""
    if torch is None or not torch.cuda.is_available():
        pytest.skip("needs CUDA")
    g = torch.Generator(device="cuda").manual_seed(7)

    # 1) fp16 (non-captured dtype) standard
    x = torch.randn(1, 64, 8, 128, generator=g, device="cuda", dtype=torch.float32).half()
    cos = torch.randn(64, 64, generator=g, device="cuda", dtype=torch.float32)
    sin = torch.randn(64, 64, generator=g, device="cuda", dtype=torch.float32)
    _assert_falls_back("standard", (x, cos, sin, False))

    # 2) bf16 standard with a NON-captured shape (wrong tokens/heads)
    x = torch.randn(1, 1024, 8, 128, generator=g, device="cuda", dtype=torch.float32).bfloat16()
    cos = torch.randn(1024, 64, generator=g, device="cuda", dtype=torch.float32)
    sin = torch.randn(1024, 64, generator=g, device="cuda", dtype=torch.float32)
    _assert_falls_back("standard", (x, cos, sin, False))

    # 3) bf16 LTX-2 with a NON-captured (B,S,inner) shape (S=512), captured NC cos/sin layout
    x, cos, sin = _ltx2_inputs(1, 512, 32, 64, seed=11)
    _assert_falls_back("ltx2", (x, cos, sin))

    # 4) bf16 LTX-2 with a CAPTURED shape but CONTIGUOUS cos/sin (not the captured NC view)
    bsz, seq, heads, half = 1, 1536, 32, 64
    inner = heads * 2 * half
    xx = torch.randn(bsz, seq, inner, generator=g, device="cuda", dtype=torch.float32).bfloat16()
    cos_c = torch.randn(bsz, heads, seq, half, generator=g, device="cuda", dtype=torch.float32).bfloat16().contiguous()
    sin_c = torch.randn(bsz, heads, seq, half, generator=g, device="cuda", dtype=torch.float32).bfloat16().contiguous()
    assert cos_c.is_contiguous()  # contiguous (B,H,S,half) is NOT the captured NC layout
    _assert_falls_back("ltx2", (xx, cos_c, sin_c))


def test_dispatch_predicates() -> None:
    """The CUDA gate must be True for captured signatures and False for every
    non-captured class — route narrowing stays visible without reading benchmarks."""
    if torch is None or not torch.cuda.is_available():
        pytest.skip("needs CUDA")
    w = _register_module()._wrapper
    g = torch.Generator(device="cuda").manual_seed(3)

    # captured -> True
    xs, cs, ss = _standard_inputs(27030, 24, 128, seed=1)
    assert w._is_standard_fast(xs, cs, ss, False) is True
    xl, cl, sl = _ltx2_inputs(1, 1536, 32, 64, seed=1)
    assert w._is_ltx2_fast(xl, cl, sl) is True

    # non-captured -> False
    x_fp16 = torch.randn(1, 64, 8, 128, generator=g, device="cuda", dtype=torch.float32).half()
    c_small = torch.randn(64, 64, generator=g, device="cuda", dtype=torch.float32)
    assert w._is_standard_fast(x_fp16, c_small, c_small, False) is False  # fp16 dtype
    x_bf = torch.randn(1, 1024, 8, 128, generator=g, device="cuda", dtype=torch.float32).bfloat16()
    c_bf = torch.randn(1024, 64, generator=g, device="cuda", dtype=torch.float32)
    assert w._is_standard_fast(x_bf, c_bf, c_bf, False) is False  # non-captured shape
    assert w._is_standard_fast(xs, cs, ss, True) is False  # interleaved=True
    xn, cn, sn = _ltx2_inputs(1, 512, 32, 64, seed=2)
    assert w._is_ltx2_fast(xn, cn, sn) is False  # non-captured seq
    inner = 32 * 2 * 64
    xc = torch.randn(1, 1536, inner, generator=g, device="cuda", dtype=torch.float32).bfloat16()
    cc = torch.randn(1, 32, 1536, 64, generator=g, device="cuda", dtype=torch.float32).bfloat16().contiguous()
    assert w._is_ltx2_fast(xc, cc, cc) is False  # contiguous cos/sin (wrong layout)
