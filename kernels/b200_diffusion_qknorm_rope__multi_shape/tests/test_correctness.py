"""Correctness harness for ``b200_diffusion_qknorm_rope__multi_shape``.

Skipped unless ``KDA_RUN_CORRECTNESS=1`` is set (the real run owns the CUDA
environment on the remote NVIDIA B200 box via the ``ion-b200`` skill).

Semantics recovered from the SGLang baseline
(``sglang/jit_kernel/diffusion/qknorm_rope.py`` +
``csrc/diffusion/qknorm_rope.cuh``):

- ``fused_inplace_qknorm_rope(q, k, q_weight, k_weight, cos_sin_cache, positions,
  *, is_neox, eps=1e-6, head_dim=0, rope_dim=0) -> None`` mutates ``q`` and ``k``
  IN PLACE (per-head RMS norm with weight, then RoPE by ``positions``).
- The semantic oracle is the SGLang split path:
  ``fused_inplace_qknorm`` (bf16) followed by
  ``flashinfer.rope.apply_rope_with_cos_sin_cache_inplace``, compared at
  ``ATOL=8e-2, RTOL=1e-2`` (identical to
  ``python/sglang/jit_kernel/tests/diffusion/test_qknorm_rope.py``).

Inputs follow the SGLang test/benchmark convention (cos/sin cache sized to
``MAX_SEQ_LEN`` with randomized positions) so the comparison is fair against
SGLang's own harnesses and exercises arbitrary RoPE positions rather than the
identity mapping.
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


KERNEL_SLUG = "b200_diffusion_qknorm_rope__multi_shape"
OP_TYPE = "qknorm_rope_inplace"
KERNEL_DIR = Path(__file__).resolve().parents[1]

# Tolerances and RoPE constants mirror the SGLang reference test exactly.
ATOL = 8e-2
RTOL = 1e-2
MAX_SEQ_LEN = 131072
ROPE_BASE = 10000.0

pytestmark = pytest.mark.skipif(
    os.environ.get("KDA_RUN_CORRECTNESS") != "1",
    reason="Set KDA_RUN_CORRECTNESS=1 on the CUDA box (ion-b200) to run.",
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


def _torch_dtype(name: str):
    return {"bfloat16": torch.bfloat16, "float16": torch.float16}[name]


def _position_dtype(name: str):
    return {"int32": torch.int32, "int64": torch.int64}[name]


# --- Production shapes (verbatim from prompt.md / docs/captured_shapes_b200.jsonl) ---
# All head_dim=128, rope_dim=128, is_neox=False, bfloat16, int64 positions.
_PRODUCTION_ROWS = [
    # (preset, bucket, num_tokens, num_heads, eps)
    ("joyai-edit", "large", 7904, 32, 1e-6),
    ("qwen", "large", 4096, 24, 1e-6),
    ("qwen-edit", "large", 8424, 24, 1e-6),
    ("zimage", "large", 4096, 30, 1e-5),
    ("zimage", "large", 4128, 30, 1e-5),
    ("qwen", "small", 19, 24, 1e-6),
    ("qwen", "small", 47, 24, 1e-6),
    ("qwen-edit", "small", 195, 24, 1e-6),
    ("qwen-edit", "small", 189, 24, 1e-6),
    ("zimage", "small", 32, 30, 1e-5),
]

# --- CI-grid fallback probes (AC-1.1): the optimized kernel must either match
# the oracle or fall back to the SGLang baseline for these. eps=1e-6 per the
# SGLang test. Kept small/cheap; they exercise the unsupported tail. ---
_CI_FALLBACK_ROWS = [
    # (name_suffix, num_tokens, num_heads, head_dim, rope_dim, is_neox, position_dtype)
    ("hd64_rd64", 257, 8, 64, 64, False, "int64"),
    ("hd256_rd128", 257, 8, 256, 128, False, "int64"),
    ("hd128_rd64_neox", 129, 24, 128, 64, True, "int64"),  # rotary lanes 64/4=16 (pow2)
    ("hd128_rd128_int32pos", 129, 24, 128, 128, False, "int32"),
    ("hd128_heads8", 257, 8, 128, 128, False, "int64"),
]


def make_cases() -> list[dict[str, Any]]:
    """All configured correctness/benchmark cases."""

    cases: list[dict[str, Any]] = []
    for preset, bucket, num_tokens, num_heads, eps in _PRODUCTION_ROWS:
        cases.append(
            {
                "name": f"{preset}__{bucket}__B{num_tokens}_H{num_heads}_D128_R128",
                "preset": preset,
                "bucket": bucket,
                "num_tokens": num_tokens,
                "num_heads": num_heads,
                "head_dim": 128,
                "rope_dim": 128,
                "is_neox": False,
                "eps": eps,
                "dtype": "bfloat16",
                "position_dtype": "int64",
                "ci_fallback": False,
                "atol": ATOL,
                "rtol": RTOL,
                "warmup": 25,
                "iters": 100,
            }
        )
    for suffix, num_tokens, num_heads, head_dim, rope_dim, is_neox, pos_dt in _CI_FALLBACK_ROWS:
        cases.append(
            {
                "name": f"cifallback__{suffix}__B{num_tokens}_H{num_heads}",
                "preset": "ci-grid",
                "bucket": "ci_fallback",
                "num_tokens": num_tokens,
                "num_heads": num_heads,
                "head_dim": head_dim,
                "rope_dim": rope_dim,
                "is_neox": is_neox,
                "eps": 1e-6,
                "dtype": "bfloat16",
                "position_dtype": pos_dt,
                "ci_fallback": True,
                "atol": ATOL,
                "rtol": RTOL,
                "warmup": 10,
                "iters": 50,
            }
        )
    return cases


def _create_cos_sin_cache(rope_dim: int, device: str) -> "torch.Tensor":
    """[MAX_SEQ_LEN, rope_dim] float32 cache: concat(cos, sin) halves.

    Identical construction to the SGLang reference test/benchmark.
    """
    inv_freq = 1.0 / (
        ROPE_BASE
        ** (torch.arange(0, rope_dim, 2, dtype=torch.float32, device=device) / rope_dim)
    )
    t = torch.arange(MAX_SEQ_LEN, dtype=torch.float32, device=device)
    freqs = torch.einsum("i,j->ij", t, inv_freq)
    return torch.cat((freqs.cos(), freqs.sin()), dim=-1)


def _make_inputs(case: dict[str, Any], device: str = "cuda") -> dict[str, "torch.Tensor"]:
    """Deterministic, seeded inputs so baseline() and candidate() get identical data."""
    dtype = _torch_dtype(case["dtype"])
    pos_dtype = _position_dtype(case["position_dtype"])
    n, h, d, r = case["num_tokens"], case["num_heads"], case["head_dim"], case["rope_dim"]

    seed = (n * 1_000_003 + h * 8191 + d * 127 + r * 17 + int(case["is_neox"])) & 0x7FFFFFFF
    g = torch.Generator(device=device)
    g.manual_seed(seed)

    return {
        "q": torch.randn(n, h, d, device=device, dtype=dtype, generator=g),
        "k": torch.randn(n, h, d, device=device, dtype=dtype, generator=g),
        "q_weight": torch.randn(d, device=device, dtype=dtype, generator=g),
        "k_weight": torch.randn(d, device=device, dtype=dtype, generator=g),
        "cos_sin_cache": _create_cos_sin_cache(r, device),
        "positions": torch.randint(0, MAX_SEQ_LEN, (n,), device=device, dtype=pos_dtype, generator=g),
    }


def _run_oracle(inputs: dict[str, "torch.Tensor"], case: dict[str, Any]) -> tuple:
    """SGLang split-path oracle: separate qknorm (bf16) + FlashInfer RoPE, in place."""
    from flashinfer.rope import apply_rope_with_cos_sin_cache_inplace

    from sglang.jit_kernel.norm import fused_inplace_qknorm

    q, k = inputs["q"], inputs["k"]
    fused_inplace_qknorm(q, k, inputs["q_weight"], inputs["k_weight"], eps=case["eps"])
    apply_rope_with_cos_sin_cache_inplace(
        positions=inputs["positions"].long(),
        query=q.view(q.shape[0], -1),
        key=k.view(k.shape[0], -1),
        head_size=q.shape[-1],
        cos_sin_cache=inputs["cos_sin_cache"],
        is_neox=case["is_neox"],
    )
    return q, k


def baseline(case: dict[str, Any]) -> Any:
    """Semantic oracle result (mutated q, k) for one configured case."""
    inputs = _make_inputs(case)
    return _run_oracle(inputs, case)


def candidate(case: dict[str, Any]) -> Any:
    """Candidate result (mutated q, k) via the registered optimized wrapper."""
    module = _load_register_module()
    wrapper = getattr(module, "optimized_wrapper")
    inputs = _make_inputs(case)
    q, k = inputs["q"], inputs["k"]
    wrapper(
        q,
        k,
        inputs["q_weight"],
        inputs["k_weight"],
        inputs["cos_sin_cache"],
        inputs["positions"],
        is_neox=case["is_neox"],
        eps=case["eps"],
        head_dim=case["head_dim"],
        rope_dim=case["rope_dim"],
    )
    return q, k


def _assert_no_nan_inf(value: Any, *, path: str) -> None:
    if torch is not None and isinstance(value, torch.Tensor):
        assert not torch.isnan(value).any(), f"{path} contains NaN"
        assert not torch.isinf(value).any(), f"{path} contains Inf"
    elif isinstance(value, (tuple, list)):
        for i, item in enumerate(value):
            _assert_no_nan_inf(item, path=f"{path}[{i}]")
    elif isinstance(value, dict):
        for key, item in value.items():
            _assert_no_nan_inf(item, path=f"{path}.{key}")


def _assert_close(actual: Any, expected: Any, *, case: dict[str, Any], path: str = "out") -> None:
    atol = case.get("atol", ATOL)
    rtol = case.get("rtol", RTOL)
    _assert_no_nan_inf(actual, path=path)
    if torch is not None and isinstance(actual, torch.Tensor):
        assert isinstance(expected, torch.Tensor), f"{path} expected tensor, got {type(expected)}"
        assert actual.shape == expected.shape, f"{path} shape {actual.shape} != {expected.shape}"
        torch.testing.assert_close(actual.float(), expected.float(), atol=atol, rtol=rtol)
        return
    if isinstance(actual, (tuple, list)):
        assert isinstance(expected, type(actual)), f"{path} type mismatch"
        assert len(actual) == len(expected), f"{path} length mismatch"
        for i, (a_item, e_item) in enumerate(zip(actual, expected)):
            _assert_close(a_item, e_item, case=case, path=f"{path}[{i}]")
        return
    assert actual == expected, f"{path} value mismatch"


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
    for case in cases:
        expected = baseline(case)
        actual = candidate(case)
        _assert_close(actual, expected, case=case, path=case.get("name", "out"))
