"""In-place-aware correctness for ``h200_diffusion_qknorm_rope__multi_shape``.

The op is IN PLACE (mutates ``q`` and ``k``, returns ``None``), so this suite
compares the *mutated* ``q``/``k`` of the optimized candidate against the SGLang
split oracle:

    sglang.jit_kernel.norm.fused_inplace_qknorm(q, k, q_weight, k_weight)
    flashinfer.rope.apply_rope_with_cos_sin_cache_inplace(...)

(the exact oracle used by SGLang's own ``test_qknorm_rope.py``). The 9 captured
production shapes MUST hit the native CUDA path (dispatch == "cuda"); a
representative slice of the canonical regression grid MUST route to the SGLang
baseline fallback and still match the oracle. Tolerance ATOL=8e-2 / RTOL=1e-2
mirrors the SGLang reference test; NaN/Inf are rejected.

Run on the H200 GPU box with ``KDA_RUN_CORRECTNESS=1`` and
``PYTHONPATH=<repo>/python`` (so ``import sglang`` resolves to the diffusion
checkout).
"""

from __future__ import annotations

import importlib
import importlib.util
import os
from pathlib import Path

import pytest

try:
    import torch
except ImportError:  # pragma: no cover - CUDA env owns the real run
    torch = None


KERNEL_SLUG = "h200_diffusion_qknorm_rope__multi_shape"
OP_TYPE = "qknorm_rope_inplace"
KERNEL_DIR = Path(__file__).resolve().parents[1]
DEVICE = "cuda"
ROPE_BASE = 10000.0
ATOL = 8e-2
RTOL = 1e-2

pytestmark = pytest.mark.skipif(
    os.environ.get("KDA_RUN_CORRECTNESS") != "1",
    reason="Set KDA_RUN_CORRECTNESS=1 on the H200 GPU box (needs sglang+flashinfer+CUDA).",
)


def _load_register_module():
    register_py = KERNEL_DIR / "src" / "register.py"
    spec = importlib.util.spec_from_file_location(
        f"kda_{KERNEL_SLUG}_register", register_py
    )
    assert spec is not None and spec.loader is not None, register_py
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _wrapper_module():
    """Return the same top-level ``wrapper`` module the candidate dispatches through.

    ``register.py`` inserts ``src/`` onto ``sys.path`` at import, and
    ``optimized_wrapper`` does ``from wrapper import fused_inplace_qknorm_rope``,
    so importing ``wrapper`` here yields the SAME module instance (and therefore
    the same dispatch-path telemetry)."""
    _load_register_module()  # ensures src/ is on sys.path
    return importlib.import_module("wrapper")


def _make_cos_sin_cache(rope_dim: int, max_pos: int, base: float = ROPE_BASE):
    inv = 1.0 / (
        base ** (torch.arange(0, rope_dim, 2, dtype=torch.float32, device=DEVICE) / rope_dim)
    )
    t = torch.arange(max_pos, dtype=torch.float32, device=DEVICE)
    f = torch.einsum("i,j->ij", t, inv)
    return torch.cat((f.cos(), f.sin()), dim=-1)


def _oracle(q, k, q_weight, k_weight, cos_sin_cache, positions, is_neox):
    from flashinfer.rope import apply_rope_with_cos_sin_cache_inplace

    from sglang.jit_kernel.norm import fused_inplace_qknorm

    fused_inplace_qknorm(q, k, q_weight, k_weight)
    apply_rope_with_cos_sin_cache_inplace(
        positions=positions.long(),
        query=q.view(q.shape[0], -1),
        key=k.view(k.shape[0], -1),
        head_size=q.shape[-1],
        cos_sin_cache=cos_sin_cache,
        is_neox=is_neox,
    )


def _no_nan_inf(name, *tensors):
    for i, t in enumerate(tensors):
        assert not torch.isnan(t).any(), f"{name}[{i}] has NaN"
        assert not torch.isinf(t).any(), f"{name}[{i}] has Inf"


# 9 captured production shapes (the optimization targets) -> must dispatch "cuda".
# (name, tokens, num_heads, head_dim, rope_dim, is_neox, eps)
CAPTURED = [
    ("qwen__T4096_H24", 4096, 24, 128, 128, False, 1e-6),
    ("qwen__T19_H24", 19, 24, 128, 128, False, 1e-6),
    ("qwen__T47_H24", 47, 24, 128, 128, False, 1e-6),
    ("qwen_edit__T8424_H24", 8424, 24, 128, 128, False, 1e-6),
    ("qwen_edit__T195_H24", 195, 24, 128, 128, False, 1e-6),
    ("qwen_edit__T189_H24", 189, 24, 128, 128, False, 1e-6),
    ("zimage__T4096_H30", 4096, 30, 128, 128, False, 1e-5),
    ("zimage__T32_H30", 32, 30, 128, 128, False, 1e-5),
    ("zimage__T4128_H30", 4128, 30, 128, 128, False, 1e-5),
]

# Representative canonical-regression-grid slice: the first four route to the
# SGLang baseline fallback (head_dim/rope_dim/is_neox outside the fast path); the
# last exercises the int32-positions fast path (must dispatch "cuda").
# (name, tokens, num_heads, head_dim, rope_dim, is_neox, eps, pos_dtype, expect)
GRID = [
    ("grid_hd64", 129, 8, 64, 64, False, 1e-6, "int64", "fallback"),
    ("grid_hd256", 257, 8, 256, 128, False, 1e-6, "int64", "fallback"),
    ("grid_rope64", 129, 24, 128, 64, False, 1e-6, "int64", "fallback"),
    ("grid_neox", 129, 24, 128, 128, True, 1e-6, "int64", "fallback"),
    ("grid_int32", 257, 24, 128, 128, False, 1e-6, "int32", "cuda"),
]


def _run_one(tokens, num_heads, head_dim, rope_dim, is_neox, eps, pos_dtype="int64", seed=0):
    reg = _load_register_module()
    wrap = _wrapper_module()
    cand = reg.optimized_wrapper

    gen = torch.Generator(device=DEVICE).manual_seed(seed)
    q0 = torch.randn(tokens, num_heads, head_dim, device=DEVICE, dtype=torch.bfloat16, generator=gen)
    k0 = torch.randn(tokens, num_heads, head_dim, device=DEVICE, dtype=torch.bfloat16, generator=gen)
    qw = torch.randn(head_dim, device=DEVICE, dtype=torch.bfloat16, generator=gen)
    kw = torch.randn(head_dim, device=DEVICE, dtype=torch.bfloat16, generator=gen)
    pdt = torch.int32 if pos_dtype == "int32" else torch.int64
    positions = torch.randint(0, tokens, (tokens,), device=DEVICE, dtype=pdt)
    cos_sin_cache = _make_cos_sin_cache(rope_dim, tokens)

    q_ref, k_ref = q0.clone(), k0.clone()
    _oracle(q_ref, k_ref, qw, kw, cos_sin_cache, positions, is_neox)

    q_cand, k_cand = q0.clone(), k0.clone()
    ret = cand(q_cand, k_cand, qw, kw, cos_sin_cache, positions, is_neox=is_neox, eps=eps, rope_dim=rope_dim)
    path = wrap.last_dispatch_path()

    assert ret is None, "fused_inplace_qknorm_rope must return None (in place)"
    _no_nan_inf("candidate", q_cand, k_cand)
    max_q = (q_ref.float() - q_cand.float()).abs().max().item()
    max_k = (k_ref.float() - k_cand.float()).abs().max().item()
    torch.testing.assert_close(q_cand.float(), q_ref.float(), atol=ATOL, rtol=RTOL)
    torch.testing.assert_close(k_cand.float(), k_ref.float(), atol=ATOL, rtol=RTOL)
    return path, max_q, max_k


def test_register_metadata() -> None:
    module = _load_register_module()
    assert hasattr(module, "register")
    spec = module.register()
    assert spec["name"] == KERNEL_SLUG
    assert spec["op_type"] == OP_TYPE
    assert callable(spec["callable"])
    assert "fused_inplace_qknorm_rope" in module.EXPORTS


@pytest.mark.parametrize("case", CAPTURED, ids=[c[0] for c in CAPTURED])
def test_captured_shapes_cuda_path(case) -> None:
    name, tokens, num_heads, head_dim, rope_dim, is_neox, eps = case
    path, max_q, max_k = _run_one(tokens, num_heads, head_dim, rope_dim, is_neox, eps)
    assert path == "cuda", f"{name}: expected native CUDA path, got {path!r} (silent fallback)"
    print(f"{name}: path={path} max_err q={max_q:.4f} k={max_k:.4f}")


@pytest.mark.parametrize("case", GRID, ids=[c[0] for c in GRID])
def test_regression_grid(case) -> None:
    name, tokens, num_heads, head_dim, rope_dim, is_neox, eps, pos_dtype, expect = case
    path, max_q, max_k = _run_one(tokens, num_heads, head_dim, rope_dim, is_neox, eps, pos_dtype=pos_dtype)
    assert path == expect, f"{name}: expected dispatch {expect!r}, got {path!r}"
    print(f"{name}: path={path} max_err q={max_q:.4f} k={max_k:.4f}")


def test_supported_gate_rejects_unsupported() -> None:
    """The fast-path gate must reject cheaply-detectable unsupported signatures
    (they then route to the non-recursive baseline fallback)."""
    wrap = _wrapper_module()
    gen = torch.Generator(device=DEVICE).manual_seed(1)
    T, H, D = 64, 24, 128
    q = torch.randn(T, H, D, device=DEVICE, dtype=torch.bfloat16, generator=gen)
    k = torch.randn(T, H, D, device=DEVICE, dtype=torch.bfloat16, generator=gen)
    qw = torch.randn(D, device=DEVICE, dtype=torch.bfloat16, generator=gen)
    kw = torch.randn(D, device=DEVICE, dtype=torch.bfloat16, generator=gen)
    pos = torch.randint(0, T, (T,), device=DEVICE, dtype=torch.int64)
    cache = _make_cos_sin_cache(D, T)
    sup = wrap._supported

    # supported production signature -> True
    assert sup(q, k, qw, kw, cache, pos, False, 128, 128) is True
    # is_neox -> rejected
    assert sup(q, k, qw, kw, cache, pos, True, 128, 128) is False
    # head_dim != 128 -> rejected
    assert sup(q, k, qw, kw, cache, pos, False, 64, 64) is False
    # rope_dim != 128 -> rejected
    assert sup(q, k, qw, kw, cache, pos, False, 128, 64) is False
    # non-contiguous q -> rejected
    pad = torch.randn(T, H, D * 2, device=DEVICE, dtype=torch.bfloat16, generator=gen)
    q_nc = pad[:, :, :D]
    assert not q_nc.is_contiguous()
    assert sup(q_nc, k, qw, kw, cache, pos, False, 128, 128) is False
    # fp16 (wrong dtype) -> rejected
    assert sup(q.half(), k.half(), qw, kw, cache, pos, False, 128, 128) is False
    # cpu tensors -> rejected
    assert sup(q.cpu(), k.cpu(), qw, kw, cache, pos, False, 128, 128) is False
    # device mismatch -> rejected
    assert sup(q, k, qw, kw, cache, pos.cpu(), False, 128, 128) is False
    # q and k sharing storage (alias / overlap) -> rejected
    assert sup(q, q, qw, kw, cache, pos, False, 128, 128) is False


def test_positions_patterns_cuda() -> None:
    """The CUDA fast path must be correct for zero/repeat/shuffled positions in
    both int64 and int32 (positions index cos_sin_cache rows)."""
    reg = _load_register_module()
    wrap = _wrapper_module()
    cand = reg.optimized_wrapper
    from flashinfer.rope import apply_rope_with_cos_sin_cache_inplace

    from sglang.jit_kernel.norm import fused_inplace_qknorm

    T, H, D, rope = 256, 24, 128, 128
    gen = torch.Generator(device=DEVICE).manual_seed(7)
    q0 = torch.randn(T, H, D, device=DEVICE, dtype=torch.bfloat16, generator=gen)
    k0 = torch.randn(T, H, D, device=DEVICE, dtype=torch.bfloat16, generator=gen)
    qw = torch.randn(D, device=DEVICE, dtype=torch.bfloat16, generator=gen)
    kw = torch.randn(D, device=DEVICE, dtype=torch.bfloat16, generator=gen)
    cache = _make_cos_sin_cache(rope, T)
    base = torch.randint(0, T, (T,), device=DEVICE, dtype=torch.int64)
    base[: T // 4] = 0  # zeros
    base[T // 4 : T // 2] = base[0]  # repeats
    for pdt in (torch.int64, torch.int32):
        pos = base.to(pdt)
        q_ref, k_ref = q0.clone(), k0.clone()
        fused_inplace_qknorm(q_ref, k_ref, qw, kw)
        apply_rope_with_cos_sin_cache_inplace(
            positions=pos.long(), query=q_ref.view(T, -1), key=k_ref.view(T, -1),
            head_size=D, cos_sin_cache=cache, is_neox=False,
        )
        q_cand, k_cand = q0.clone(), k0.clone()
        cand(q_cand, k_cand, qw, kw, cache, pos, is_neox=False, rope_dim=rope)
        assert wrap.last_dispatch_path() == "cuda", f"pos dtype {pdt}"
        torch.testing.assert_close(q_cand.float(), q_ref.float(), atol=ATOL, rtol=RTOL)
        torch.testing.assert_close(k_cand.float(), k_ref.float(), atol=ATOL, rtol=RTOL)


# --- Wrapper-level fallback negative contract (call optimized_wrapper end-to-end) ---
# Fallback contract: every unsupported signature must record dispatch "fallback", NOT raise/recurse,
# and return baseline-equivalent (oracle-equivalent) results. The CUDA-but-outside-fast-path
# cases (is_neox, head_dim 64/256, rope_dim 64) are covered end-to-end by test_regression_grid;
# the cases below add CPU, device-mismatch, unsupported position dtype, non-contiguity,
# misalignment, fp16, and q/k aliasing.

def _oracle_cuda(q0, k0, q_weight, k_weight, cos_sin_cache, positions, is_neox):
    """Run the SGLang split oracle on CUDA bf16 copies of the inputs; returns mutated q,k."""
    from flashinfer.rope import apply_rope_with_cos_sin_cache_inplace

    from sglang.jit_kernel.norm import fused_inplace_qknorm

    qc = q0.to(device=DEVICE, dtype=torch.bfloat16).contiguous()
    kc = k0.to(device=DEVICE, dtype=torch.bfloat16).contiguous()
    qw = q_weight.to(device=DEVICE, dtype=torch.bfloat16).contiguous()
    kw = k_weight.to(device=DEVICE, dtype=torch.bfloat16).contiguous()
    cache = cos_sin_cache.to(device=DEVICE, dtype=torch.float32).contiguous()
    pos = positions.to(device=DEVICE).long()
    fused_inplace_qknorm(qc, kc, qw, kw)
    apply_rope_with_cos_sin_cache_inplace(
        positions=pos, query=qc.view(qc.shape[0], -1), key=kc.view(kc.shape[0], -1),
        head_size=qc.shape[-1], cos_sin_cache=cache, is_neox=is_neox,
    )
    return qc, kc


def _check_fallback(q_in, k_in, qw, kw, cache, pos, q0, k0, *, is_neox=False, rope_dim=128,
                    check=True, atol=ATOL, rtol=RTOL):
    reg = _load_register_module()
    wrap = _wrapper_module()
    ret = reg.optimized_wrapper(q_in, k_in, qw, kw, cache, pos, is_neox=is_neox, rope_dim=rope_dim)
    assert ret is None, "wrapper must return None (in place)"
    assert wrap.last_dispatch_path() == "fallback", f"expected fallback, got {wrap.last_dispatch_path()!r}"
    _no_nan_inf("fallback", q_in.float(), k_in.float())
    if check:
        q_exp, k_exp = _oracle_cuda(q0, k0, qw, kw, cache, pos, is_neox)
        torch.testing.assert_close(q_in.to(DEVICE, torch.bfloat16).float(), q_exp.float(), atol=atol, rtol=rtol)
        torch.testing.assert_close(k_in.to(DEVICE, torch.bfloat16).float(), k_exp.float(), atol=atol, rtol=rtol)


def _bad_inputs(device="cuda", dtype=torch.bfloat16, T=128, H=24, D=128, seed=3):
    g = torch.Generator(device=device).manual_seed(seed)
    q = torch.randn(T, H, D, device=device, dtype=dtype, generator=g)
    k = torch.randn(T, H, D, device=device, dtype=dtype, generator=g)
    qw = torch.randn(D, device=device, dtype=dtype, generator=g)
    kw = torch.randn(D, device=device, dtype=dtype, generator=g)
    pos = torch.randint(0, T, (T,), device=device, dtype=torch.int64)
    cache = _make_cos_sin_cache(D, T)
    if device != DEVICE:
        cache = cache.to(device)
    return q, k, qw, kw, pos, cache


def test_fallback_wrapper_cpu() -> None:
    q, k, qw, kw, pos, cache = _bad_inputs(device="cpu")
    _check_fallback(q.clone(), k.clone(), qw, kw, cache, pos, q.clone(), k.clone())


def test_fallback_wrapper_device_mismatch() -> None:
    q, k, qw, kw, pos, cache = _bad_inputs(device=DEVICE)
    _check_fallback(q.clone(), k.clone(), qw, kw, cache, pos.cpu(), q.clone(), k.clone())


def test_fallback_wrapper_unsupported_position_dtype() -> None:
    q, k, qw, kw, pos, cache = _bad_inputs(device=DEVICE)
    _check_fallback(q.clone(), k.clone(), qw, kw, cache, pos.to(torch.int16), q.clone(), k.clone())


def test_fallback_wrapper_noncontiguous() -> None:
    T, H, D = 128, 24, 128
    g = torch.Generator(device=DEVICE).manual_seed(4)
    pad = torch.randn(T, H, D * 2, device=DEVICE, dtype=torch.bfloat16, generator=g)
    q, k = pad[:, :, :D], pad[:, :, D:]
    assert not q.is_contiguous()
    qw = torch.randn(D, device=DEVICE, dtype=torch.bfloat16, generator=g)
    kw = torch.randn(D, device=DEVICE, dtype=torch.bfloat16, generator=g)
    pos = torch.randint(0, T, (T,), device=DEVICE, dtype=torch.int64)
    cache = _make_cos_sin_cache(D, T)
    _check_fallback(q, k, qw, kw, cache, pos, q.clone(), k.clone())


def test_fallback_wrapper_misaligned() -> None:
    T, H, D = 128, 24, 128
    g = torch.Generator(device=DEVICE).manual_seed(5)
    big = torch.randn(T * H * D + 8, device=DEVICE, dtype=torch.bfloat16, generator=g)
    q = big[1:1 + T * H * D].view(T, H, D)  # contiguous but offset 2 bytes -> not 16B aligned
    assert q.is_contiguous() and q.data_ptr() % 16 != 0
    k = torch.randn(T, H, D, device=DEVICE, dtype=torch.bfloat16, generator=g)
    qw = torch.randn(D, device=DEVICE, dtype=torch.bfloat16, generator=g)
    kw = torch.randn(D, device=DEVICE, dtype=torch.bfloat16, generator=g)
    pos = torch.randint(0, T, (T,), device=DEVICE, dtype=torch.int64)
    cache = _make_cos_sin_cache(D, T)
    _check_fallback(q, k, qw, kw, cache, pos, q.clone(), k.clone())


def test_fallback_wrapper_fp16() -> None:
    q, k, qw, kw, pos, cache = _bad_inputs(device=DEVICE, dtype=torch.float16)
    # fp16 vs the bf16 oracle -> generous cross-dtype tolerance; key contract is no-raise+fallback
    _check_fallback(q.clone(), k.clone(), qw, kw, cache, pos, q.clone(), k.clone(), atol=2.5e-1, rtol=3e-2)


def test_fallback_wrapper_aliased_no_raise() -> None:
    q, k, qw, kw, pos, cache = _bad_inputs(device=DEVICE)
    shared = q.clone()  # q and k are the SAME storage (full alias): semantics undefined
    _check_fallback(shared, shared, qw, kw, cache, pos, q.clone(), k.clone(), check=False)


def test_fallback_wrapper_qcuda_kcpu() -> None:
    # true q/k device mismatch: q on CUDA, k on CPU -> reference computes each on its own device
    q, k, qw, kw, pos, cache = _bad_inputs(device=DEVICE, seed=8)
    _check_fallback(q.clone(), k.cpu().clone(), qw, kw, cache, pos, q, k)


def test_fallback_wrapper_qcpu_kcuda() -> None:
    q, k, qw, kw, pos, cache = _bad_inputs(device=DEVICE, seed=9)
    _check_fallback(q.cpu().clone(), k.clone(), qw, kw, cache, pos, q, k)


def test_double_install_recursion_raises() -> None:
    """Recursive-baseline contract: a double-install where the bound baseline resolves back into a KDA wrapper/
    dispatcher must RAISE a clear error (not recurse, not silently use the reference)."""
    wrap = _wrapper_module()
    reg = _load_register_module()
    T, H, D = 64, 24, 128
    # CPU inputs exercise the fallback path (where the recursion guard lives) without a GPU dep.
    q = torch.randn(T, H, D, dtype=torch.bfloat16)
    k = torch.randn(T, H, D, dtype=torch.bfloat16)
    qw = torch.randn(D, dtype=torch.bfloat16)
    kw = torch.randn(D, dtype=torch.bfloat16)
    pos = torch.randint(0, T, (T,), dtype=torch.int64)
    cache = _make_cos_sin_cache(D, T).cpu()
    orig = wrap._SGLANG_BASELINE
    try:
        # (a) baseline bound to this very wrapper (identity)
        wrap._SGLANG_BASELINE = wrap.fused_inplace_qknorm_rope
        with pytest.raises(RuntimeError, match="[Rr]ecurs"):
            reg.optimized_wrapper(q.clone(), k.clone(), qw, kw, cache, pos, is_neox=False, rope_dim=D)
        # (b) baseline bound to a KDA dispatcher/overlay-shaped function (by module name)
        def fake_dispatcher(*a, **kw_):  # pragma: no cover - must never be called
            raise AssertionError("recursive baseline was called instead of raising")
        fake_dispatcher.__module__ = "kda_kernels.diffusion.qknorm_rope._dispatcher"
        wrap._SGLANG_BASELINE = fake_dispatcher
        with pytest.raises(RuntimeError, match="[Rr]ecurs"):
            reg.optimized_wrapper(q.clone(), k.clone(), qw, kw, cache, pos, is_neox=False, rope_dim=D)
    finally:
        wrap._SGLANG_BASELINE = orig
    # sanity: with the original (non-recursive) baseline restored, an unsupported CPU call no-raises
    reg.optimized_wrapper(q.clone(), k.clone(), qw, kw, cache, pos, is_neox=False, rope_dim=D)
    assert wrap.last_dispatch_path() == "fallback"
