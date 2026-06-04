"""Correctness harness for h200_diffusion_qknorm_rope__multi_shape.

Two tiers:
- CPU-runnable: register metadata, the PyTorch semantic fallback, the in-place mutation contract,
  fallback-dispatch negatives, and the double-install / re-entrancy guard.
- CUDA-gated (remote H200): the 9 captured production shapes and a CI-equivalent regression slice
  compared against the split SGLang oracle (``fused_inplace_qknorm`` + FlashInfer RoPE), plus a
  cross-check that the PyTorch reference matches that oracle.

Run: ``pytest tests/test_correctness.py -v`` (set ``CUDA_VISIBLE_DEVICES`` on the remote box).
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from typing import Any, Optional

import pytest

try:
    import torch
except ImportError:  # pragma: no cover
    torch = None

KERNEL_SLUG = "h200_diffusion_qknorm_rope__multi_shape"
OP_TYPE = "qknorm_rope_inplace"
KERNEL_DIR = Path(__file__).resolve().parents[1]
SRC_DIR = KERNEL_DIR / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

ATOL = 8e-2
RTOL = 1e-2
MAX_SEQ_LEN = 131072
ROPE_BASE = 10000.0
DTYPE = torch.bfloat16 if torch is not None else None

requires_torch = pytest.mark.skipif(torch is None, reason="torch not available")
requires_cuda = pytest.mark.skipif(
    torch is None or not torch.cuda.is_available(), reason="needs CUDA H200"
)

# 9 captured production shapes (verbatim): (name, tokens, num_heads, eps). All head_dim=128,
# rope_dim=128, is_neox=False, bf16. See docs/captured_shapes_h200.jsonl.
CAPTURED_SHAPES = [
    ("qwen_t4096", 4096, 24, 1e-6),
    ("qwen_t19", 19, 24, 1e-6),
    ("qwen_t47", 47, 24, 1e-6),
    ("qwenedit_t8424", 8424, 24, 1e-6),
    ("qwenedit_t195", 195, 24, 1e-6),
    ("qwenedit_t189", 189, 24, 1e-6),
    ("zimage_t4096", 4096, 30, 1e-5),
    ("zimage_t32", 32, 30, 1e-5),
    ("zimage_t4128", 4128, 30, 1e-5),
]

# CI-equivalent regression slice (mirrors get_ci_test_range CI values in test_qknorm_rope.py).
GRID_BS = [1, 9, 129, 257, 2049, 4097]
GRID_HEADS = [8, 24]
GRID_HEAD_DIM = [64, 128, 256]
GRID_ROPE = {64: [64], 128: [64, 128], 256: [64, 128, 256]}
GRID_IS_NEOX = [False, True]
GRID_POS_DTYPE = ["int32", "int64"]


def _load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None, path
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _register():
    return _load_module(f"kda_{KERNEL_SLUG}_register", SRC_DIR / "register.py")


def _wrapper():
    import wrapper  # src/ is on sys.path

    return wrapper


def create_cos_sin_cache(rope_dim: int, num_rows: int, device, base: float = ROPE_BASE):
    inv_freq = 1.0 / (
        base ** (torch.arange(0, rope_dim, 2, dtype=torch.float32, device=device) / rope_dim)
    )
    t = torch.arange(num_rows, dtype=torch.float32, device=device)
    freqs = torch.einsum("i,j->ij", t, inv_freq)
    return torch.cat((freqs.cos(), freqs.sin()), dim=-1)


def _pos_dtype(name: str):
    return torch.int32 if name == "int32" else torch.int64


def _make_positions(kind: str, tokens: int, hi: int, device, dtype):
    hi = max(1, hi)
    if kind == "arange":
        p = torch.arange(tokens, device=device) % hi
    elif kind == "zero":
        p = torch.zeros(tokens, device=device, dtype=torch.long)
    elif kind == "repeat":
        period = max(1, hi // 4)
        p = torch.arange(tokens, device=device) % period
    elif kind == "shuffle":
        if tokens <= hi:
            p = torch.randperm(hi, device=device)[:tokens]
        else:
            p = torch.randint(0, hi, (tokens,), device=device)
    else:  # "random"
        p = torch.randint(0, hi, (tokens,), device=device)
    return p.to(dtype)


def _build_inputs(tokens, num_heads, head_dim, rope_dim, device, *, cache_rows=None, seed=0):
    g = torch.Generator(device="cpu").manual_seed(seed)
    cache_rows = cache_rows or tokens
    q = torch.randn(tokens, num_heads, head_dim, generator=g, dtype=DTYPE).to(device)
    k = torch.randn(tokens, num_heads, head_dim, generator=g, dtype=DTYPE).to(device)
    q_weight = torch.randn(head_dim, generator=g, dtype=DTYPE).to(device)
    k_weight = torch.randn(head_dim, generator=g, dtype=DTYPE).to(device)
    cos_sin_cache = create_cos_sin_cache(rope_dim, cache_rows, device=device)
    return dict(
        q=q, k=k, q_weight=q_weight, k_weight=k_weight,
        cos_sin_cache=cos_sin_cache, cache_rows=cache_rows,
    )


def split_oracle(q, k, q_weight, k_weight, cos_sin_cache, positions, is_neox, eps):
    """SGLang split oracle: separate qknorm kernel + FlashInfer RoPE. CUDA-only."""
    from flashinfer.rope import apply_rope_with_cos_sin_cache_inplace

    from sglang.jit_kernel.norm import fused_inplace_qknorm

    fused_inplace_qknorm(q, k, q_weight, k_weight, eps)
    apply_rope_with_cos_sin_cache_inplace(
        positions=positions.long(),
        query=q.view(q.shape[0], -1),
        key=k.view(k.shape[0], -1),
        head_size=q.shape[-1],
        cos_sin_cache=cos_sin_cache,
        is_neox=is_neox,
    )


def _assert_no_nan_inf(t, name="out"):
    assert not torch.isnan(t).any(), f"{name} has NaN"
    assert not torch.isinf(t).any(), f"{name} has Inf"


# --------------------------------------------------------------------------------------
# benchmark.py compatibility (the dual-level harness is finalized in the remote phase)
# --------------------------------------------------------------------------------------
def make_cases() -> list[dict[str, Any]]:
    cases = []
    for name, tokens, num_heads, eps in CAPTURED_SHAPES:
        cases.append(dict(
            name=name, tokens=tokens, num_heads=num_heads, head_dim=128, rope_dim=128,
            is_neox=False, eps=eps, atol=ATOL, rtol=RTOL, warmup=25, iters=100,
        ))
    return cases


def _case_inputs(case):
    if "_inputs" not in case:
        device = "cuda" if (torch is not None and torch.cuda.is_available()) else "cpu"
        b = _build_inputs(case["tokens"], case["num_heads"], case["head_dim"], case["rope_dim"], device)
        b["positions"] = _make_positions("arange", case["tokens"], b["cache_rows"], device, torch.int64)
        b["q0"], b["k0"] = b["q"].clone(), b["k"].clone()
        case["_inputs"] = b
    return case["_inputs"]


def baseline(case):
    b = _case_inputs(case)
    b["q"].copy_(b["q0"]); b["k"].copy_(b["k0"])
    split_oracle(b["q"], b["k"], b["q_weight"], b["k_weight"], b["cos_sin_cache"], b["positions"], case["is_neox"], case["eps"])
    return b["q"], b["k"]


def candidate(case):
    b = _case_inputs(case)
    b["q"].copy_(b["q0"]); b["k"].copy_(b["k0"])
    _register().optimized_wrapper(
        b["q"], b["k"], b["q_weight"], b["k_weight"], b["cos_sin_cache"], b["positions"],
        is_neox=case["is_neox"], eps=case["eps"], rope_dim=case["rope_dim"],
    )
    return b["q"], b["k"]


# --------------------------------------------------------------------------------------
# CPU-runnable tests
# --------------------------------------------------------------------------------------
def test_register_metadata():
    spec = _register().register()
    assert spec["name"] == KERNEL_SLUG
    assert spec["op_type"] == OP_TYPE
    assert callable(spec["callable"])


@requires_torch
def test_inplace_contract_and_fallback_reference():
    """On CPU the wrapper takes the semantic fallback; verify in-place + read-only contract."""
    w = _wrapper()
    device = "cpu"
    b = _build_inputs(33, 8, 128, 128, device, seed=1)
    positions = _make_positions("shuffle", 33, b["cache_rows"], device, torch.int64)
    q, k = b["q"].clone(), b["k"].clone()
    qw0, kw0 = b["q_weight"].clone(), b["k_weight"].clone()
    cache0, pos0 = b["cos_sin_cache"].clone(), positions.clone()

    w.optimized_wrapper(q, k, b["q_weight"], b["k_weight"], b["cos_sin_cache"], positions,
                        is_neox=False, eps=1e-6, rope_dim=128)
    assert w.get_last_dispatch() == "fallback"
    _assert_no_nan_inf(q, "q"); _assert_no_nan_inf(k, "k")
    # read-only inputs unchanged
    assert torch.equal(b["q_weight"], qw0) and torch.equal(b["k_weight"], kw0)
    assert torch.equal(b["cos_sin_cache"], cache0) and torch.equal(positions, pos0)
    # q/k actually mutated
    assert not torch.equal(q, b["q"]) and not torch.equal(k, b["k"])
    # result equals an independent semantic-reference computation
    qr, kr = b["q"].clone(), b["k"].clone()
    w.semantic_reference_inplace(qr, kr, b["q_weight"], b["k_weight"], b["cos_sin_cache"], positions,
                                 is_neox=False, eps=1e-6, head_dim=128, rope_dim=128)
    torch.testing.assert_close(q.float(), qr.float(), atol=0, rtol=0)
    torch.testing.assert_close(k.float(), kr.float(), atol=0, rtol=0)


@requires_torch
@pytest.mark.parametrize("is_neox", [False, True])
def test_semantic_reference_runs_neox_variants(is_neox):
    w = _wrapper()
    b = _build_inputs(16, 8, 128, 128, "cpu", seed=2)
    positions = _make_positions("arange", 16, b["cache_rows"], "cpu", torch.int32)
    q, k = b["q"].clone(), b["k"].clone()
    w.semantic_reference_inplace(q, k, b["q_weight"], b["k_weight"], b["cos_sin_cache"], positions,
                                 is_neox=is_neox, eps=1e-6, head_dim=128, rope_dim=128)
    _assert_no_nan_inf(q); _assert_no_nan_inf(k)


@requires_torch
def test_double_install_guard():
    """If the fallback delegate re-enters the wrapper, the guard must raise (no infinite loop)."""
    w = _wrapper()
    b = _build_inputs(8, 8, 128, 128, "cpu", seed=3)
    positions = _make_positions("arange", 8, b["cache_rows"], "cpu", torch.int64)
    prev = w.BASELINE_DELEGATE
    try:
        w.BASELINE_DELEGATE = w.optimized_wrapper  # simulate candidate installed as its own baseline
        with pytest.raises(RuntimeError, match="recursive"):
            w.optimized_wrapper(b["q"], b["k"], b["q_weight"], b["k_weight"], b["cos_sin_cache"], positions,
                                is_neox=False, eps=1e-6, rope_dim=128)
    finally:
        w.BASELINE_DELEGATE = prev


@requires_torch
def test_unsupported_inputs_fall_back():
    """A spread of unsupported signatures must dispatch 'fallback' without raising."""
    w = _wrapper()
    dev = "cuda" if torch.cuda.is_available() else "cpu"
    base = _build_inputs(16, 8, 128, 128, dev, seed=4)
    pos = _make_positions("arange", 16, base["cache_rows"], dev, torch.int64)

    def fresh():
        return base["q"].clone(), base["k"].clone()

    # (name, q, k, q_weight, k_weight, cache, positions, kwargs, exact_match_vs_reference)
    variants = []
    # fp16 dtype
    qh, kh = fresh()
    variants.append(("fp16", qh.half(), kh.half(), base["q_weight"].half(), base["k_weight"].half(),
                     base["cos_sin_cache"], pos, dict(is_neox=False, rope_dim=128), True))
    # non-contiguous last dim (strided slice of a wider tensor)
    qnc = torch.randn(16, 8, 256, device=dev, dtype=DTYPE)[:, :, ::2]
    knc = torch.randn(16, 8, 256, device=dev, dtype=DTYPE)[:, :, ::2]
    variants.append(("noncontig", qnc, knc, base["q_weight"], base["k_weight"],
                     base["cos_sin_cache"], pos, dict(is_neox=False, rope_dim=128), True))
    # int16 positions (unsupported dtype)
    variants.append(("int16_pos", *fresh(), base["q_weight"], base["k_weight"],
                     base["cos_sin_cache"], pos.to(torch.int16), dict(is_neox=False, rope_dim=128), True))
    # wrong-shaped weight (2-D, right numel): old gate would reach TensorMatcher and raise; the gate
    # must reject it to the semantic fallback (which handles the right-numel reshape) -> no raise.
    variants.append(("wrong_weight_dim", *fresh(), base["q_weight"].reshape(1, 128), base["k_weight"],
                     base["cos_sin_cache"], pos, dict(is_neox=False, rope_dim=128), True))
    # misaligned weight: contiguous [128] starting at a 2-byte offset -> the kernel's AlignedVector
    # (16-byte) weight load would be misaligned, so it must fall back, not enter the fast path.
    misw = torch.randn(136, device=dev, dtype=DTYPE)[1:1 + 128]
    assert misw.is_contiguous() and (misw.data_ptr() % 16) != 0
    variants.append(("misaligned_qweight", *fresh(), misw, base["k_weight"],
                     base["cos_sin_cache"], pos, dict(is_neox=False, rope_dim=128), True))
    # aliased q/k (same storage): falls back; in-place order is intentionally undefined, so we
    # only require fallback + finiteness (no exact-match vs a non-aliased reference).
    qa, _ = fresh()
    variants.append(("aliased", qa, qa, base["q_weight"], base["k_weight"],
                     base["cos_sin_cache"], pos, dict(is_neox=False, rope_dim=128), False))

    for name, q, k, qw, kw, cache, positions, kw_extra, exact in variants:
        q_in, k_in = q.clone(), k.clone()
        w.optimized_wrapper(q, k, qw, kw, cache, positions, eps=1e-6, **kw_extra)
        assert w.get_last_dispatch() == "fallback", name
        _assert_no_nan_inf(q, f"{name}.q"); _assert_no_nan_inf(k, f"{name}.k")
        if exact:
            qr, kr = q_in.clone(), k_in.clone()
            w.semantic_reference_inplace(qr, kr, qw, kw, cache, positions,
                                         is_neox=kw_extra["is_neox"], eps=1e-6,
                                         head_dim=q_in.shape[-1], rope_dim=kw_extra["rope_dim"])
            torch.testing.assert_close(q.float(), qr.float(), atol=0, rtol=0)
            torch.testing.assert_close(k.float(), kr.float(), atol=0, rtol=0)


@requires_torch
def test_overlaps_predicate():
    """Byte-range overlap detection: identical and partially-overlapping views overlap; disjoint don't."""
    w = _wrapper()
    big = torch.randn(64, 8, 128, dtype=DTYPE)  # contiguous
    assert w._overlaps(big[:32], big[:32])         # identical
    assert w._overlaps(big[:32], big[16:48])       # partial overlap (rows 16-31 shared), different data_ptr
    assert not w._overlaps(big[:16], big[48:64])   # disjoint slices of the same buffer
    assert not w._overlaps(torch.randn(32, 8, 128, dtype=DTYPE), torch.randn(32, 8, 128, dtype=DTYPE))  # separate allocs


@requires_torch
def test_overlapping_views_fall_back():
    """Overlapping (non-identical) q/k views must take the fallback, not the native CUDA fast path."""
    w = _wrapper()
    dev = "cuda" if torch.cuda.is_available() else "cpu"
    big = torch.randn(96, 24, 128, device=dev, dtype=DTYPE)
    q = big[:32]              # rows 0..31
    k = big[16:48]           # rows 16..47 — overlaps q on rows 16..31, distinct data_ptr
    assert w._overlaps(q, k)
    b = _build_inputs(32, 24, 128, 128, dev, seed=9)
    pos = _make_positions("arange", 32, 32, dev, torch.int64)
    w.optimized_wrapper(q, k, b["q_weight"], b["k_weight"], b["cos_sin_cache"], pos,
                        is_neox=False, eps=1e-6, rope_dim=128)
    assert w.get_last_dispatch() == "fallback"  # overlap -> never the native in-place kernel


# --------------------------------------------------------------------------------------
# CUDA-gated tests (remote H200): the split SGLang oracle + the candidate fast path
# --------------------------------------------------------------------------------------
@requires_cuda
def test_semantic_reference_matches_oracle():
    """The PyTorch FP32 reference must match the split SGLang oracle within tolerance."""
    w = _wrapper()
    for is_neox in (False, True):
        b = _build_inputs(257, 8, 128, 128, "cuda", seed=5)
        pos = _make_positions("shuffle", 257, b["cache_rows"], "cuda", torch.int64)
        q_o, k_o = b["q"].clone(), b["k"].clone()
        q_r, k_r = b["q"].clone(), b["k"].clone()
        split_oracle(q_o, k_o, b["q_weight"], b["k_weight"], b["cos_sin_cache"], pos, is_neox, 1e-6)
        w.semantic_reference_inplace(q_r, k_r, b["q_weight"], b["k_weight"], b["cos_sin_cache"], pos,
                                     is_neox=is_neox, eps=1e-6, head_dim=128, rope_dim=128)
        torch.testing.assert_close(q_r.float(), q_o.float(), atol=ATOL, rtol=RTOL)
        torch.testing.assert_close(k_r.float(), k_o.float(), atol=ATOL, rtol=RTOL)


@requires_cuda
@pytest.mark.parametrize("name,tokens,num_heads,eps", CAPTURED_SHAPES)
@pytest.mark.parametrize("pos_kind", ["arange", "zero", "repeat", "shuffle"])
@pytest.mark.parametrize("pos_dt", ["int32", "int64"])
def test_captured_shapes(name, tokens, num_heads, eps, pos_kind, pos_dt):
    w = _wrapper()
    reg = _register()
    head_dim = rope_dim = 128
    b = _build_inputs(tokens, num_heads, head_dim, rope_dim, "cuda", seed=hash((name, pos_kind)) & 0xFFFF)
    pos = _make_positions(pos_kind, tokens, b["cache_rows"], "cuda", _pos_dtype(pos_dt))
    q_o, k_o = b["q"].clone(), b["k"].clone()
    q_c, k_c = b["q"].clone(), b["k"].clone()
    split_oracle(q_o, k_o, b["q_weight"], b["k_weight"], b["cos_sin_cache"], pos, False, eps)
    reg.optimized_wrapper(q_c, k_c, b["q_weight"], b["k_weight"], b["cos_sin_cache"], pos,
                          is_neox=False, eps=eps, rope_dim=rope_dim)
    assert w.get_last_dispatch() == "cuda", f"{name} should use the fast path"
    _assert_no_nan_inf(q_c, "q"); _assert_no_nan_inf(k_c, "k")
    torch.testing.assert_close(q_c.float(), q_o.float(), atol=ATOL, rtol=RTOL)
    torch.testing.assert_close(k_c.float(), k_o.float(), atol=ATOL, rtol=RTOL)


@requires_cuda
def test_misaligned_cos_sin_cache_still_oracle_correct():
    """A cos/sin cache whose BASE pointer is not 16-byte aligned must still be oracle-correct on
    the native CUDA dispatch: the kernel launcher guards the base alignment and routes such
    inputs to the scalar-load one-head path instead of the float4 fast path."""
    w = _wrapper()
    tokens, num_heads, head_dim, rope_dim, eps = 4096, 24, 128, 128, 1e-6
    b = _build_inputs(tokens, num_heads, head_dim, rope_dim, "cuda", seed=77)
    cache = b["cos_sin_cache"]
    rows = cache.shape[0]
    # Same cache values on a deliberately 4-byte-offset base: contiguous [rows, rope_dim] float32
    # view with data_ptr() % 16 == 4.
    backing = torch.empty(rows * rope_dim + 4, device="cuda", dtype=torch.float32)
    mis = backing[1 : 1 + rows * rope_dim].view(rows, rope_dim)
    mis.copy_(cache)
    assert mis.is_contiguous()
    assert mis.data_ptr() % 16 != 0, "test setup must produce a misaligned base"
    pos = _make_positions("shuffle", tokens, rows, "cuda", torch.int64)
    q_o, k_o = b["q"].clone(), b["k"].clone()
    q_c, k_c = b["q"].clone(), b["k"].clone()
    split_oracle(q_o, k_o, b["q_weight"], b["k_weight"], cache, pos, False, eps)
    w.optimized_wrapper(q_c, k_c, b["q_weight"], b["k_weight"], mis, pos,
                        is_neox=False, eps=eps, rope_dim=rope_dim)
    assert w.get_last_dispatch() == "cuda", "misaligned cache stays on the native dispatch"
    _assert_no_nan_inf(q_c, "q"); _assert_no_nan_inf(k_c, "k")
    torch.testing.assert_close(q_c.float(), q_o.float(), atol=ATOL, rtol=RTOL)
    torch.testing.assert_close(k_c.float(), k_o.float(), atol=ATOL, rtol=RTOL)


@requires_cuda
@pytest.mark.parametrize("batch_size", GRID_BS)
@pytest.mark.parametrize("num_heads", GRID_HEADS)
@pytest.mark.parametrize("head_dim", GRID_HEAD_DIM)
@pytest.mark.parametrize("is_neox", GRID_IS_NEOX)
@pytest.mark.parametrize("pos_dt", GRID_POS_DTYPE)
def test_regression_grid(batch_size, num_heads, head_dim, is_neox, pos_dt):
    w = _wrapper()
    reg = _register()
    for rope_dim in GRID_ROPE[head_dim]:
        if is_neox:
            epw = head_dim // 32
            lanes = rope_dim // epw
            if lanes < 2 or (lanes & (lanes - 1)):
                continue
        b = _build_inputs(batch_size, num_heads, head_dim, rope_dim, "cuda",
                          cache_rows=MAX_SEQ_LEN, seed=batch_size + head_dim + rope_dim)
        pos = _make_positions("random", batch_size, MAX_SEQ_LEN, "cuda", _pos_dtype(pos_dt))
        q_o, k_o = b["q"].clone(), b["k"].clone()
        q_c, k_c = b["q"].clone(), b["k"].clone()
        split_oracle(q_o, k_o, b["q_weight"], b["k_weight"], b["cos_sin_cache"], pos, is_neox, 1e-6)
        reg.optimized_wrapper(q_c, k_c, b["q_weight"], b["k_weight"], b["cos_sin_cache"], pos,
                              is_neox=is_neox, eps=1e-6, rope_dim=rope_dim)
        assert w.get_last_dispatch() in ("cuda", "fallback")
        _assert_no_nan_inf(q_c); _assert_no_nan_inf(k_c)
        torch.testing.assert_close(q_c.float(), q_o.float(), atol=ATOL, rtol=RTOL)
        torch.testing.assert_close(k_c.float(), k_o.float(), atol=ATOL, rtol=RTOL)


if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-v"]))
