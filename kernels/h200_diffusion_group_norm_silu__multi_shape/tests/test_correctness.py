"""Correctness harness for ``h200_diffusion_group_norm_silu__multi_shape``.

Skipped unless ``KDA_RUN_CORRECTNESS=1`` is set (and CUDA is available) — the real
run happens inside the remote H200 ``sglang_bbuf`` container, where ``sglang`` is
importable and a GPU exists. ``make_cases()`` is pure-Python and can be enumerated
on a CPU-only box for static validation.

Oracle: ``F.silu(F.group_norm(x, num_groups, weight, bias, eps))`` evaluated at the
SAME ``eps`` as the candidate call (this is the SGLang reference test's ``_reference``).
The SGLang baseline entry point is also checked against the same oracle and against the
candidate (parity). Tolerances follow the SGLang reference test, applied per dtype.
"""

from __future__ import annotations

import importlib.util
import json
import os
from pathlib import Path
from typing import Any

try:
    import pytest
except ImportError:  # pragma: no cover - pytest absent on some local boxes
    pytest = None

try:
    import torch
    import torch.nn as nn
    import torch.nn.functional as F
except ImportError:  # pragma: no cover - CUDA env owns the real run
    torch = None
    nn = None
    F = None


KERNEL_SLUG = "h200_diffusion_group_norm_silu__multi_shape"
OP_TYPE = "group_norm_silu"
KERNEL_DIR = Path(__file__).resolve().parents[1]
DEVICE = "cuda"

# Per-dtype tolerances, verbatim from python/sglang/jit_kernel/tests/diffusion/test_group_norm_silu.py
_TOL = {
    "float16": (3e-3, 3e-3),
    "bfloat16": (7e-2, 2e-2),
    "float32": (1e-5, 1e-5),
}

_DTYPE_FROM_STR = {}
if torch is not None:
    _DTYPE_FROM_STR = {
        "float16": torch.float16,
        "bfloat16": torch.bfloat16,
        "float32": torch.float32,
    }

if pytest is not None:
    pytestmark = pytest.mark.skipif(
        os.environ.get("KDA_RUN_CORRECTNESS") != "1",
        reason="Set KDA_RUN_CORRECTNESS=1 (with CUDA + sglang) to run the real harness.",
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


def _production_signatures() -> list[dict[str, Any]]:
    """Unique production call signatures, read verbatim from the captured JSONL.

    Uses the ``triton_group_norm_silu`` records because they carry explicit
    ``num_groups``/``eps`` kwargs and the weight/bias shapes. The 48 unique x-shapes
    are identical across both captured entry points.
    """

    jsonl = KERNEL_DIR / "docs" / "captured_shapes_h200.jsonl"
    seen: dict[tuple, dict[str, Any]] = {}
    with jsonl.open() as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            rec = json.loads(line)
            if not str(rec.get("kernel", "")).endswith("triton_group_norm_silu"):
                continue
            x = rec["args"][0]
            shape = tuple(x["shape"])
            dtype = str(x["dtype"]).replace("torch.", "")
            kwargs = rec.get("kwargs", {})
            num_groups = int(kwargs["num_groups"])
            eps = float(kwargs["eps"])
            key = (shape, dtype, num_groups, eps)
            if key not in seen:
                seen[key] = {
                    "shape": shape,
                    "dtype": dtype,
                    "num_groups": num_groups,
                    "eps": eps,
                }
    return list(seen.values())


# Regression grid, adapted from the SGLang reference test (eps=1e-5).
# image_2d (4-D), video_3d (5-D), token_2d (2-D); plus the large-tile bf16 case.
_REGRESSION_TRITON_SHAPES = [((2, 64, 32, 32), 32), ((1, 64, 4, 16, 16), 32), ((4, 128), 32)]
_REGRESSION_APPLY_SHAPES = [((2, 64, 32, 32), 32), ((1, 64, 4, 16, 16), 32)]
_REGRESSION_LARGE_TILE = ((1, 128, 20, 256, 256), 32)


def _shape_tag(shape: tuple) -> str:
    return "x".join(str(d) for d in shape)


def make_cases() -> list[dict[str, Any]]:
    """Return all configured correctness cases (production + regression).

    Each case is a pure-Python spec (no tensors): ``entry`` is ``"triton"`` or
    ``"apply"``; inputs are built deterministically per case in ``_make_inputs``.
    """

    cases: list[dict[str, Any]] = []

    def add(entry: str, shape, dtype: str, num_groups: int, eps: float, suite: str, seed: int):
        atol, rtol = _TOL[dtype]
        cases.append(
            {
                "name": f"{suite}__{entry}__{_shape_tag(tuple(shape))}__{dtype}__g{num_groups}__eps{eps:g}",
                "suite": suite,
                "entry": entry,
                "shape": tuple(shape),
                "dtype": dtype,
                "num_groups": num_groups,
                "eps": eps,
                "atol": atol,
                "rtol": rtol,
                "seed": seed,
                "warmup": 25,
                "iters": 100,
            }
        )

    # Production: both entry points exercise the same 48 fp16 shapes (eps=1e-6).
    for i, sig in enumerate(_production_signatures()):
        for entry in ("triton", "apply"):
            add(entry, sig["shape"], sig["dtype"], sig["num_groups"], sig["eps"], "prod", seed=i)

    # Regression grid (eps=1e-5).
    seed = 1000
    for shape, ng in _REGRESSION_TRITON_SHAPES:
        for dtype in ("float16", "bfloat16", "float32"):
            add("triton", shape, dtype, ng, 1e-5, "regress", seed)
            seed += 1
    for shape, ng in _REGRESSION_APPLY_SHAPES:
        for dtype in ("float16", "bfloat16"):
            add("apply", shape, dtype, ng, 1e-5, "regress", seed)
            seed += 1
    shape, ng = _REGRESSION_LARGE_TILE
    add("triton", shape, "bfloat16", ng, 1e-5, "regress_large_tile", seed)

    return cases


def _make_inputs(case: dict[str, Any]):
    dtype = _DTYPE_FROM_STR[case["dtype"]]
    shape = tuple(case["shape"])
    channels = shape[1]
    gen = torch.Generator(device=DEVICE).manual_seed(int(case.get("seed", 0)))
    x = torch.randn(shape, device=DEVICE, dtype=dtype, generator=gen)
    weight = torch.randn(channels, device=DEVICE, dtype=dtype, generator=gen)
    bias = torch.randn(channels, device=DEVICE, dtype=dtype, generator=gen)
    return x, weight, bias


def reference(x, weight, bias, num_groups: int, eps: float):
    """Ground-truth oracle: F.silu(F.group_norm(...)) at the case eps."""

    return F.silu(F.group_norm(x, num_groups, weight=weight, bias=bias, eps=eps))


def baseline(case: dict[str, Any], x, weight, bias):
    """SGLang baseline entry point for this case's entry (parity reference)."""

    from sglang.jit_kernel.diffusion.group_norm_silu import apply_group_norm_silu
    from sglang.jit_kernel.diffusion.triton.group_norm_silu import triton_group_norm_silu

    num_groups, eps = case["num_groups"], case["eps"]
    if case["entry"] == "apply":
        norm = nn.GroupNorm(num_groups, x.shape[1], eps=eps, affine=True).to(
            device=x.device, dtype=x.dtype
        )
        with torch.no_grad():
            norm.weight.copy_(weight)
            norm.bias.copy_(bias)
        return apply_group_norm_silu(x, norm, nn.SiLU())
    return triton_group_norm_silu(x, weight, bias, num_groups=num_groups, eps=eps)


def candidate(case: dict[str, Any], x, weight, bias):
    """Optimized candidate via src/register.py:optimized_wrapper.

    Defines the wrapper contract: it must accept BOTH the triton-style signature
    ``(x, weight, bias, num_groups=, eps=)`` and the apply-style signature
    ``(x, norm: nn.GroupNorm, activation: nn.SiLU)``.
    """

    wrapper = getattr(_load_register_module(), "optimized_wrapper")
    num_groups, eps = case["num_groups"], case["eps"]
    if case["entry"] == "apply":
        norm = nn.GroupNorm(num_groups, x.shape[1], eps=eps, affine=True).to(
            device=x.device, dtype=x.dtype
        )
        with torch.no_grad():
            norm.weight.copy_(weight)
            norm.bias.copy_(bias)
        return wrapper(x, norm, nn.SiLU())
    return wrapper(x, weight, bias, num_groups=num_groups, eps=eps)


def _assert_no_nan_inf(value, *, path: str) -> None:
    assert not torch.isnan(value).any(), f"{path} contains NaN"
    assert not torch.isinf(value).any(), f"{path} contains Inf"


def _assert_close(actual, expected, *, case: dict[str, Any], path: str, tol_mult: float = 1.0) -> None:
    _assert_no_nan_inf(actual, path=path)
    assert actual.shape == expected.shape, f"{path} shape {actual.shape} != {expected.shape}"
    atol = case["atol"] * tol_mult
    rtol = case["rtol"] * tol_mult
    torch.testing.assert_close(actual.float(), expected.float(), atol=atol, rtol=rtol)


def test_register_metadata() -> None:
    module = _load_register_module()
    assert hasattr(module, "register")
    spec = module.register()
    assert spec["name"] == KERNEL_SLUG
    assert spec["op_type"] == OP_TYPE
    assert callable(spec["callable"])


def test_correctness_cases() -> None:
    cases = make_cases()
    assert cases, "No correctness cases recovered. Fill make_cases() before optimizing."
    if torch is None or not torch.cuda.is_available():
        if pytest is not None:
            pytest.skip("CUDA required for correctness execution")
        return
    with torch.no_grad():
        for case in cases:
            x, weight, bias = _make_inputs(case)
            num_groups, eps = case["num_groups"], case["eps"]
            ref = reference(x, weight, bias, num_groups, eps)
            base = baseline(case, x, weight, bias)
            cand = candidate(case, x, weight, bias)
            name = case["name"]
            # Primary correctness: candidate vs the math oracle.
            _assert_close(cand, ref, case=case, path=f"{name}:cand-vs-ref")
            # Sanity: the SGLang baseline itself is within spec vs the oracle.
            _assert_close(base, ref, case=case, path=f"{name}:baseline-vs-ref")
            # Parity: candidate vs SGLang baseline (relaxed to absorb double fp16 rounding).
            _assert_close(cand, base, case=case, path=f"{name}:cand-vs-baseline", tol_mult=2.0)
            del x, weight, bias, ref, base, cand
            torch.cuda.empty_cache()


def test_production_uses_candidate() -> None:
    """Prove production candidate-bucket shapes take the NATIVE path (not a silent fallback),
    and giants take the baseline. Complements KDA_STRICT_CANDIDATE=1 (which re-raises on
    candidate-path failure) so a passing correctness run cannot be a hidden eager fallback."""
    if torch is None or not torch.cuda.is_available():
        if pytest is not None:
            pytest.skip("CUDA required")
        return
    reg = _load_register_module()
    with torch.no_grad():
        for shape, ng, expect in [
            ((1, 512, 5, 32, 32), 32, ("small", "large")),
            ((1, 512, 2, 12, 10), 32, ("small", "large")),
            ((1, 256, 9, 128, 40), 32, ("small", "large")),
            ((1, 256, 17, 256, 256), 32, ("baseline_giant",)),
        ]:
            x = torch.randn(shape, device=DEVICE, dtype=torch.float16)
            w = torch.randn(shape[1], device=DEVICE, dtype=torch.float16)
            b = torch.randn(shape[1], device=DEVICE, dtype=torch.float16)
            p = reg.selected_path(x, w, b, ng)
            assert p in expect, f"{shape}: selected_path={p}, expected one of {expect}"


def test_fallback_matrix() -> None:
    """Unsupported signatures must (a) route to the baseline (selected_path != native) and
    (b) still produce a correct result. Covers AC-4's fallback list."""
    if torch is None or not torch.cuda.is_available():
        if pytest is not None:
            pytest.skip("CUDA required")
        return
    reg = _load_register_module()
    C, ng, eps = 64, 32, 1e-5
    shape = (2, C, 32, 32)
    numel = 2 * C * 32 * 32

    def oracle(x, w, b):
        return F.silu(F.group_norm(x, ng, weight=w, bias=b, eps=eps))

    def close(out, ref, dt):
        atol, rtol = _TOL[{torch.float16: "float16", torch.bfloat16: "bfloat16", torch.float32: "float32"}[dt]]
        assert not torch.isnan(out).any() and not torch.isinf(out).any()
        torch.testing.assert_close(out.float(), ref.float(), atol=atol, rtol=rtol)

    with torch.no_grad():
        w16 = torch.randn(C, device=DEVICE, dtype=torch.float16)
        b16 = torch.randn(C, device=DEVICE, dtype=torch.float16)
        # 1. storage_offset != 0 (contiguous but 2-byte-misaligned fp16 data_ptr)
        base = torch.randn(numel + 8, device=DEVICE, dtype=torch.float16)
        x_off = base.narrow(0, 1, numel).view(shape)
        assert x_off.is_contiguous() and x_off.storage_offset() == 1
        assert reg.selected_path(x_off, w16, b16, ng) == "baseline_unsupported"
        close(reg.optimized_wrapper(x_off, w16, b16, num_groups=ng, eps=eps), oracle(x_off, w16, b16), torch.float16)
        # 2. non-contiguous
        x_nc = torch.randn(shape, device=DEVICE, dtype=torch.float16).transpose(2, 3)
        assert not x_nc.is_contiguous()
        assert reg.selected_path(x_nc, w16, b16, ng) == "baseline_unsupported"
        close(reg.optimized_wrapper(x_nc, w16, b16, num_groups=ng, eps=eps), oracle(x_nc, w16, b16), torch.float16)
        # 3. fp32 (out of native dtype support)
        x32 = torch.randn(shape, device=DEVICE, dtype=torch.float32)
        w32 = torch.randn(C, device=DEVICE, dtype=torch.float32)
        b32 = torch.randn(C, device=DEVICE, dtype=torch.float32)
        assert reg.selected_path(x32, w32, b32, ng) == "baseline_unsupported"
        close(reg.optimized_wrapper(x32, w32, b32, num_groups=ng, eps=eps), oracle(x32, w32, b32), torch.float32)
        # 3b. unexpected num_groups (16: divisible by channels but not in supported {32}) -> fallback
        x16 = torch.randn(shape, device=DEVICE, dtype=torch.float16)
        assert reg.selected_path(x16, w16, b16, 16) == "baseline_unsupported"
        close(
            reg.optimized_wrapper(x16, w16, b16, num_groups=16, eps=eps),
            F.silu(F.group_norm(x16, 16, weight=w16, bias=b16, eps=eps)),
            torch.float16,
        )
        # 4. apply form: non-affine GroupNorm -> eager fallback
        x = torch.randn(shape, device=DEVICE, dtype=torch.float16)
        norm_na = nn.GroupNorm(ng, C, eps=eps, affine=False).to(DEVICE, torch.float16)
        close(reg.optimized_wrapper(x, norm_na, nn.SiLU()), F.silu(norm_na(x)), torch.float16)
        # 5. apply form: inplace SiLU -> fallback
        norm_a = nn.GroupNorm(ng, C, eps=eps, affine=True).to(DEVICE, torch.float16)
        close(reg.optimized_wrapper(x, norm_a, nn.SiLU(inplace=True)), nn.SiLU(inplace=False)(norm_a(x)), torch.float16)
        # 6. requires_grad input -> fallback
        x_rg = torch.randn(shape, device=DEVICE, dtype=torch.float16, requires_grad=True)
        assert reg.selected_path(x_rg, w16, b16, ng) == "baseline_unsupported"
        close(reg.optimized_wrapper(x_rg, w16, b16, num_groups=ng, eps=eps), oracle(x_rg, w16, b16), torch.float16)
    # 7. grad-enabled context -> fallback
    with torch.enable_grad():
        xg = torch.randn(shape, device=DEVICE, dtype=torch.float16)
        assert reg.selected_path(xg, w16, b16, ng) == "baseline_unsupported"
        with torch.no_grad():
            close(reg.optimized_wrapper(xg, w16, b16, num_groups=ng, eps=eps), oracle(xg, w16, b16), torch.float16)


if __name__ == "__main__":
    cs = make_cases()
    print(f"make_cases(): {len(cs)} cases")
    from collections import Counter
    by_suite = Counter(c["suite"] for c in cs)
    by_entry = Counter(c["entry"] for c in cs)
    by_dtype = Counter(c["dtype"] for c in cs)
    print("by suite:", dict(by_suite))
    print("by entry:", dict(by_entry))
    print("by dtype:", dict(by_dtype))
