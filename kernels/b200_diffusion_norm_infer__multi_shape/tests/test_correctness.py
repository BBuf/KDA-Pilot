"""Correctness harness for ``b200_diffusion_norm_infer__multi_shape``.

Skipped unless ``KDA_RUN_CORRECTNESS=1`` (run on the remote B200 inside the
``sglang_bbuf`` container). Covers:
- the six captured production shapes verbatim (1 LayerNorm + 5 RMSNorm),
- the canonical regression grid from ``test_qwen_image_modulation.py``
  (LayerNorm via ``norm_infer``; CI subset by default, full grid with
  ``KDA_FULL_REGRESSION=1``),
- RMS one-pass cross-validation at ``D=128`` on small row counts,
- adversarial inputs (zeros, near-constant, large-offset, mixed-sign).

``baseline(case)`` is the SGLang oracle; ``candidate(case)`` routes through
``src/register.py::optimized_wrapper``. Both build the SAME seeded inputs so the
comparison is exact. Dynamic tolerances: fp32 ``1e-5``, bf16/fp16 ``5e-2``.
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


KERNEL_SLUG = "b200_diffusion_norm_infer__multi_shape"
OP_TYPE = "layer_or_rms_norm_infer"
KERNEL_DIR = Path(__file__).resolve().parents[1]

pytestmark = pytest.mark.skipif(
    os.environ.get("KDA_RUN_CORRECTNESS") != "1",
    reason="Set KDA_RUN_CORRECTNESS=1 (on the remote B200) to run correctness.",
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


def _dtype(name: str):
    return {"fp16": torch.float16, "bf16": torch.bfloat16, "fp32": torch.float32}[name]


def _tol(dtype) -> tuple[float, float]:
    # Mirrors test_qwen_image_modulation.py: fp32 strict, bf16/fp16 loose.
    if dtype == torch.float32:
        return 1e-5, 1e-5
    return 5e-2, 5e-2


def _full_regression() -> bool:
    return os.environ.get("KDA_FULL_REGRESSION") == "1"


# ---------------------------------------------------------------------------
# Case construction
# ---------------------------------------------------------------------------
def make_cases() -> list[dict[str, Any]]:
    cases: list[dict[str, Any]] = []

    # --- 1) Six captured production shapes (VERBATIM; never broadened) -------
    # helios: norm_infer LayerNorm, fp32, [8640, 5120], weight+bias, eps=1e-6.
    cases.append(
        dict(
            name="helios__fp32__M8640N5120",
            kind="norm_infer", M=8640, N=5120, dtype="fp32",
            eps=1e-6, is_rms_norm=False, has_weight=True, has_bias=True,
            input_kind="randn", warmup=25, iters=100, seed=1001,
            production=True,
        )
    )
    # hunyuanvideo / zimage: triton_one_pass_rms_norm, bf16, D=128.
    for s, seed in [(648720, 1002), (1320, 1003), (650040, 1004), (16384, 1005), (4096, 1006)]:
        cases.append(
            dict(
                name=f"rms__bf16__S{s}D128",
                kind="rms_onepass", S=s, D=128, dtype="bf16",
                eps=1e-6, input_kind="randn", warmup=25, iters=100, seed=seed,
                production=True,
            )
        )

    # --- 2) Canonical LayerNorm regression grid (norm_infer, is_rms_norm=False)
    if _full_regression():
        batches, seqs, hiddens, dtypes = [1, 2, 4], [6, 33, 128, 257], [512, 1024, 1536, 3072], ["fp16", "bf16", "fp32"]
    else:  # CI subset (test_qwen_image_modulation.py) + fp32 for the strict path
        batches, seqs, hiddens, dtypes = [1, 2], [6, 128], [512, 3072], ["fp16", "bf16", "fp32"]
    seed = 2000
    for b in batches:
        for s in seqs:
            for h in hiddens:
                for dt in dtypes:
                    seed += 1
                    cases.append(
                        dict(
                            name=f"reg_ln__{dt}__B{b}S{s}H{h}",
                            kind="norm_infer", M=b * s, N=h, dtype=dt,
                            eps=1e-6, is_rms_norm=False, has_weight=True, has_bias=True,
                            input_kind="randn", warmup=5, iters=20, seed=seed,
                        )
                    )

    # --- 3) RMS one-pass cross-validation at D=128 on small row counts -------
    for m, seed in [(6, 3001), (128, 3002), (768, 3003)]:
        cases.append(
            dict(
                name=f"reg_rms__bf16__S{m}D128",
                kind="rms_onepass", S=m, D=128, dtype="bf16",
                eps=1e-6, input_kind="randn", warmup=5, iters=20, seed=seed,
            )
        )

    # --- 4) Adversarial numerical inputs (LayerNorm path; AC-4) --------------
    for ik, seed in [("zeros", 4001), ("const", 4002), ("offset", 4003), ("mixed", 4004)]:
        cases.append(
            dict(
                name=f"adv_ln__fp32__{ik}__M128N3072",
                kind="norm_infer", M=128, N=3072, dtype="fp32",
                eps=1e-6, is_rms_norm=False, has_weight=True, has_bias=True,
                input_kind=ik, warmup=2, iters=5, seed=seed, adversarial=True,
            )
        )
    # out=preallocated coverage (AC-4 / norm_infer out semantics)
    cases.append(
        dict(
            name="ln_out_preallocated__fp32__M256N1024",
            kind="norm_infer", M=256, N=1024, dtype="fp32",
            eps=1e-6, is_rms_norm=False, has_weight=True, has_bias=True,
            input_kind="randn", use_out=True, warmup=2, iters=5, seed=5001,
        )
    )

    for c in cases:
        strict = c["dtype"] == "fp32"  # torch-free (make_cases runs at collection)
        c.setdefault("atol", 1e-5 if strict else 5e-2)
        c.setdefault("rtol", 1e-5 if strict else 5e-2)
    return cases


# ---------------------------------------------------------------------------
# Deterministic seeded inputs (shared by baseline + candidate; 1-entry cache)
# ---------------------------------------------------------------------------
_INPUT_CACHE: dict[str, dict[str, Any]] = {}


def _fill(x: torch.Tensor, kind: str) -> torch.Tensor:
    if kind == "randn":
        return x
    if kind == "zeros":
        return torch.zeros_like(x)
    if kind == "const":  # near-constant row: 1.0 + tiny noise
        return torch.ones_like(x) + 1e-4 * x
    if kind == "offset":  # large DC offset
        return x + 1.0e4
    if kind == "mixed":  # large mixed-sign magnitudes
        return x * 1.0e3
    raise ValueError(f"unknown input_kind {kind}")


def _make_inputs(case: dict[str, Any]) -> dict[str, Any]:
    name = case["name"]
    if name in _INPUT_CACHE:
        return _INPUT_CACHE[name]
    _INPUT_CACHE.clear()  # bound memory to one case at a time
    assert torch is not None and torch.cuda.is_available(), "CUDA required"
    dev = "cuda"
    dt = _dtype(case["dtype"])
    torch.manual_seed(case["seed"])
    if case["kind"] == "norm_infer":
        M, N = case["M"], case["N"]
        x = _fill(torch.randn(M, N, device=dev, dtype=torch.float32), case["input_kind"]).to(dt)
        weight = torch.randn(N, device=dev, dtype=dt) if case.get("has_weight") else None
        bias = torch.randn(N, device=dev, dtype=dt) if case.get("has_bias") else None
        out = torch.empty_like(x) if case.get("use_out") else None
        inp = dict(x=x, weight=weight, bias=bias, out=out)
    elif case["kind"] == "rms_onepass":
        S, D = case["S"], case["D"]
        x = _fill(torch.randn(S, D, device=dev, dtype=torch.float32), case["input_kind"]).to(dt)
        w = torch.randn(D, device=dev, dtype=dt)
        inp = dict(x=x, w=w)
    else:
        raise ValueError(case["kind"])
    _INPUT_CACHE[name] = inp
    return inp


def _sglang_baselines():
    from sglang.jit_kernel.diffusion.triton.norm import norm_infer
    from sglang.jit_kernel.diffusion.triton.rmsnorm_onepass import (
        triton_one_pass_rms_norm,
    )

    return norm_infer, triton_one_pass_rms_norm


def baseline(case: dict[str, Any]) -> Any:
    norm_infer, triton_one_pass_rms_norm = _sglang_baselines()
    inp = _make_inputs(case)
    if case["kind"] == "norm_infer":
        return norm_infer(
            inp["x"], inp["weight"], inp["bias"], case["eps"],
            is_rms_norm=case["is_rms_norm"], out=inp["out"],
        )
    return triton_one_pass_rms_norm(inp["x"], inp["w"], case["eps"])


def candidate(case: dict[str, Any]) -> Any:
    module = _load_register_module()
    wrapper = getattr(module, "optimized_wrapper")
    inp = _make_inputs(case)
    if case["kind"] == "norm_infer":
        return wrapper(
            inp["x"], inp["weight"], inp["bias"], case["eps"],
            is_rms_norm=case["is_rms_norm"], out=inp["out"],
            dispatcher_hint="norm_infer",
        )
    return wrapper(inp["x"], inp["w"], case["eps"], dispatcher_hint="rms_onepass")


# ---------------------------------------------------------------------------
# Validators (unchanged scaffold helpers)
# ---------------------------------------------------------------------------
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
    atol = case.get("atol", 5e-2)
    rtol = case.get("rtol", 5e-2)
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
    if isinstance(actual, dict):
        assert isinstance(expected, dict), f"{path} expected dict"
        assert actual.keys() == expected.keys(), f"{path} keys mismatch"
        for key in actual:
            _assert_close(actual[key], expected[key], case=case, path=f"{path}.{key}")
        return
    assert actual == expected, f"{path} value mismatch"


def test_register_metadata() -> None:
    module = _load_register_module()
    assert hasattr(module, "register")
    spec = module.register()
    assert spec["name"] == KERNEL_SLUG
    assert spec["op_type"] == OP_TYPE
    assert callable(spec["callable"])


def _layernorm_fp64_ref(case: dict[str, Any]):
    """Mathematically-correct LayerNorm in fp64 (the 'truth' for adversarial inputs)."""
    inp = _make_inputs(case)
    x = inp["x"].double()
    mean = x.mean(dim=1, keepdim=True)
    var = ((x - mean) ** 2).mean(dim=1, keepdim=True)  # population variance, matches kernel
    y = (x - mean) / torch.sqrt(var + case["eps"])
    if inp["weight"] is not None:
        y = y * inp["weight"].double()
    if inp["bias"] is not None:
        y = y + inp["bias"].double()
    return y


def _run_adversarial(case: dict[str, Any]) -> None:
    # Ill-conditioned fp32 inputs (near-constant / large-offset / mixed-sign /
    # zeros) make exact agreement between two different fp32 reduction orders
    # unrealistic. Correctness here = candidate is finite AND no worse than the
    # SGLang baseline relative to an fp64 reference (SGLang-style dynamic
    # tolerance: candidate error <= K * baseline error + floor).
    ref = _layernorm_fp64_ref(case)
    base = baseline(case)
    cand = candidate(case)
    _assert_no_nan_inf(cand, path=case["name"])
    assert cand.shape == base.shape, f"{case['name']} shape {cand.shape} != {base.shape}"
    err_base = (base.double() - ref).abs().max().item()
    err_cand = (cand.double() - ref).abs().max().item()
    K, floor = 4.0, 1e-3
    assert err_cand <= K * err_base + floor, (
        f"{case['name']}: candidate err {err_cand:.3e} exceeds {K}x baseline err "
        f"{err_base:.3e} + {floor:.0e}"
    )


@pytest.mark.parametrize("case", make_cases(), ids=lambda c: c["name"])
def test_correctness_cases(case: dict[str, Any]) -> None:
    if case.get("adversarial"):
        _run_adversarial(case)
        return
    expected = baseline(case)
    actual = candidate(case)
    _assert_close(actual, expected, case=case, path=case.get("name", "out"))
