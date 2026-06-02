"""Correctness harness for ``b200_diffusion_norm_infer__multi_shape``.

Skipped unless ``KDA_RUN_CORRECTNESS=1`` (run on the remote B200 inside the
``sglang_bbuf`` container). Covers:
- the six captured production shapes verbatim (1 LayerNorm + 5 RMSNorm),
- the canonical regression grid from ``test_qwen_image_modulation.py``
  (LayerNorm via ``norm_infer``; CI subset by default, full grid with
  ``KDA_FULL_REGRESSION=1``),
- RMS one-pass cross-validation at ``D=128`` on small row counts,
- adversarial inputs (zeros, near-constant, large-offset, mixed-sign) judged
  candidate-vs-baseline with an fp64-referenced adaptive tolerance,
- NaN/Inf input-parity cases (candidate must match the baseline's non-finite mask),
- ``test_fallback_routing``: unsupported shapes/dtypes/layouts/weights fall back.

``baseline(case)`` is the SGLang oracle; ``candidate(case)`` routes through
``src/register.py::optimized_wrapper``. Both build the SAME seeded inputs (1-entry
cache); ``expected`` is cloned before the candidate runs so a shared/preallocated
``out`` buffer cannot alias the comparison. Dynamic tolerances: fp32 ``1e-5``,
bf16/fp16 ``5e-2``.
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

    # --- 5) NaN/Inf input parity: candidate must mark the SAME elements
    #        non-finite as the baseline (AC-4: "handled exactly as the baseline").
    cases.append(
        dict(
            name="naninf_ln__fp32__M64N1024", kind="norm_infer", M=64, N=1024, dtype="fp32",
            eps=1e-6, is_rms_norm=False, has_weight=True, has_bias=True,
            input_kind="naninf", warmup=0, iters=1, seed=6001, nan_inf=True,
        )
    )
    cases.append(
        dict(
            name="naninf_rms__bf16__S64D128", kind="rms_onepass", S=64, D=128, dtype="bf16",
            eps=1e-6, input_kind="naninf", warmup=0, iters=1, seed=6002, nan_inf=True,
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
    if kind == "naninf":  # inject NaN / +Inf / -Inf into the first rows (col 0)
        y = x.clone()
        for r, val in ((0, float("nan")), (1, float("inf")), (2, float("-inf"))):
            if y.shape[0] > r:
                y[r, 0] = val
        return y
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


_REGISTER_MODULE = None


def _register_module():
    # Load src/register.py ONCE and reuse it. Re-loading per call would reset the
    # in-process JIT module cache and re-run load_jit every time, which dominates
    # timing (a ~ms/call artifact) and corrupts benchmark numbers.
    global _REGISTER_MODULE
    if _REGISTER_MODULE is None:
        _REGISTER_MODULE = _load_register_module()
    return _REGISTER_MODULE


def candidate(case: dict[str, Any]) -> Any:
    module = _register_module()
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
    # zeros) make two different fp32 reduction orders disagree well beyond 1e-5,
    # so strict baseline-equivalence is impossible. PRIMARY check: candidate vs
    # the SGLang baseline within an adaptive tolerance scaled by the baseline's
    # own error vs an fp64 reference. DIAGNOSTIC: candidate is no worse than the
    # baseline vs the fp64 truth. (See BL-20260602-adversarial-fp32-norm-tolerance.)
    ref = _layernorm_fp64_ref(case)
    base = baseline(case)
    if isinstance(base, torch.Tensor):
        base = base.clone()
    cand = candidate(case)
    _assert_no_nan_inf(cand, path=case["name"])
    assert cand.shape == base.shape, f"{case['name']} shape {cand.shape} != {base.shape}"
    err_base = (base.double() - ref).abs().max().item()
    err_cand = (cand.double() - ref).abs().max().item()
    diff_cb = (cand.double() - base.double()).abs().max().item()
    K, floor = 4.0, 1e-3
    # PRIMARY: candidate vs SGLang baseline (adaptive tolerance).
    assert diff_cb <= (K + 1.0) * err_base + floor, (
        f"{case['name']}: |cand-base| {diff_cb:.3e} exceeds {(K + 1.0):.0f}x baseline "
        f"fp64-err {err_base:.3e} + {floor:.0e}"
    )
    # DIAGNOSTIC: candidate no worse than baseline vs fp64 truth.
    assert err_cand <= K * err_base + floor, (
        f"{case['name']}: candidate err {err_cand:.3e} exceeds {K:.0f}x baseline err "
        f"{err_base:.3e} + {floor:.0e}"
    )


def _run_nan_inf(case: dict[str, Any]) -> None:
    # AC-4: NaN/Inf inputs must be handled exactly as the baseline handles them.
    # Verify the candidate marks the SAME elements non-finite as the baseline and
    # agrees on the finite elements within the case tolerance.
    base = baseline(case)
    if isinstance(base, torch.Tensor):
        base = base.clone()
    cand = candidate(case)
    assert cand.shape == base.shape, f"{case['name']} shape {cand.shape} != {base.shape}"
    fin_b = torch.isfinite(base)
    fin_c = torch.isfinite(cand)
    assert torch.equal(fin_b, fin_c), (
        f"{case['name']}: non-finite mask mismatch (baseline finite={int(fin_b.sum())}, "
        f"candidate finite={int(fin_c.sum())})"
    )
    if fin_b.any():
        torch.testing.assert_close(
            cand[fin_b].float(), base[fin_b].float(), atol=case["atol"], rtol=case["rtol"]
        )


@pytest.mark.parametrize("case", make_cases(), ids=lambda c: c["name"])
def test_correctness_cases(case: dict[str, Any]) -> None:
    if case.get("adversarial"):
        _run_adversarial(case)
        return
    if case.get("nan_inf"):
        _run_nan_inf(case)
        return
    expected = baseline(case)
    if torch is not None and isinstance(expected, torch.Tensor):
        expected = expected.clone()  # independent of any shared/preallocated `out` buffer
    actual = candidate(case)
    if case.get("use_out"):
        provided_out = _make_inputs(case)["out"]  # cache hit -> the same object passed in
        assert actual is provided_out, f"{case['name']}: candidate did not return the provided out"
    _assert_close(actual, expected, case=case, path=case.get("name", "out"))


def _fallback_cases() -> list[dict[str, Any]]:
    return [
        # unsupported dtype / flag / layout / shape -> fall back, result == baseline
        {"name": "fb_ln_fp16", "op": "ln", "M": 8, "N": 512, "dtype": "fp16"},
        {"name": "fb_ln_rmsflag", "op": "ln", "M": 8, "N": 512, "dtype": "fp32", "is_rms_norm": True},
        {"name": "fb_ln_bigN", "op": "ln", "M": 4, "N": 16384, "dtype": "fp32"},
        {"name": "fb_ln_noncontig", "op": "ln", "M": 8, "N": 512, "dtype": "fp32", "noncontig": True},
        {"name": "fb_ln_nobias", "op": "ln", "M": 8, "N": 512, "dtype": "fp32", "no_bias": True},
        {"name": "fb_ln_outofset", "op": "ln", "M": 7, "N": 2000, "dtype": "fp32"},  # same-dtype (M,N) not configured
        {"name": "fb_rms_d64", "op": "rms", "S": 64, "D": 64, "dtype": "bf16"},
        {"name": "fb_rms_fp32", "op": "rms", "S": 64, "D": 128, "dtype": "fp32"},
        {"name": "fb_rms_outofset", "op": "rms", "S": 999, "D": 128, "dtype": "bf16"},  # same-dtype S not configured
        # invalid weight device / dtype / length on an otherwise-configured shape
        # -> must NOT route to CUDA (predicate-only; the baseline may also reject).
        {"name": "fb_ln_cpu_weight", "op": "ln", "M": 6, "N": 512, "dtype": "fp32", "wdevice": "cpu", "predicate_only": True},
        {"name": "fb_ln_wrong_wdtype", "op": "ln", "M": 6, "N": 512, "dtype": "fp32", "wdtype": "fp16", "predicate_only": True},
        {"name": "fb_ln_wrong_wlen", "op": "ln", "M": 6, "N": 512, "dtype": "fp32", "wlen_delta": 1, "predicate_only": True},
        # higher-rank RMS must not flatten into a configured 2-D (S,D)
        {"name": "fb_rms_3d", "op": "rms", "S": 6, "D": 128, "dtype": "bf16", "rms_xshape": (1, 6, 128)},
        # invalid caller-provided `out` must gate before CUDA routing
        {"name": "fb_ln_out_wrongshape", "op": "ln", "M": 6, "N": 512, "dtype": "fp32", "out_shape": (6, 256), "predicate_only": True},
        {"name": "fb_ln_out_noncontig", "op": "ln", "M": 6, "N": 512, "dtype": "fp32", "out_noncontig": True, "predicate_only": True},
    ]


@pytest.mark.parametrize("spec", _fallback_cases(), ids=lambda s: s["name"])
def test_fallback_routing(spec: dict[str, Any]) -> None:
    # Unsupported (op, dtype, layout, device, norm-type, shape, invalid weight)
    # must NOT route to CUDA: the support predicate is False; when the baseline can
    # also handle the input, the fallback result equals the SGLang baseline.
    mod = _register_module()
    norm_infer, triton_one_pass_rms_norm = _sglang_baselines()
    dev = "cuda"
    dt = _dtype(spec["dtype"])
    tol = 1e-5 if dt == torch.float32 else 5e-2
    torch.manual_seed(7000)
    if spec["op"] == "ln":
        M, N = spec["M"], spec["N"]
        if spec.get("noncontig"):
            x = torch.randn(M, N + 8, device=dev, dtype=dt)[:, :N]  # non-contiguous view
            assert not x.is_contiguous()
        else:
            x = torch.randn(M, N, device=dev, dtype=dt)
        wdt = _dtype(spec["wdtype"]) if spec.get("wdtype") else dt
        wdev = spec.get("wdevice", dev)
        wlen = N + spec.get("wlen_delta", 0)
        weight = torch.randn(wlen, device=wdev, dtype=wdt)
        bias = None if spec.get("no_bias") else torch.randn(wlen, device=wdev, dtype=wdt)
        is_rms = spec.get("is_rms_norm", False)
        out = None
        if spec.get("out_shape"):
            out = torch.empty(*spec["out_shape"], device=dev, dtype=dt)
        elif spec.get("out_noncontig"):
            out = torch.empty(M, N * 2, device=dev, dtype=dt)[:, :N]  # non-contiguous
            assert not out.is_contiguous()
        assert mod._norm_infer_supported(x, weight, bias, is_rms, out) is False
        if spec.get("predicate_only"):
            return
        got = mod.optimized_norm_infer(x, weight, bias, 1e-6, is_rms_norm=is_rms, out=out)
        exp = norm_infer(x, weight, bias, 1e-6, is_rms_norm=is_rms, out=out)
    else:
        S, D = spec["S"], spec["D"]
        xshape = spec.get("rms_xshape", (S, D))
        x = torch.randn(*xshape, device=dev, dtype=dt)
        w = torch.randn(D, device=dev, dtype=dt)
        assert mod._rms_onepass_supported(x, w) is False
        if spec.get("predicate_only"):
            return
        got = mod.optimized_triton_one_pass_rms_norm(x, w, 1e-6)
        exp = triton_one_pass_rms_norm(x, w, 1e-6)
    torch.testing.assert_close(got.float(), exp.float(), atol=tol, rtol=tol)


# --- hintless dispatch routing (regression) ---------------------------------
# optimized_wrapper must preserve BOTH public signatures even when called WITHOUT
# a dispatcher_hint (AC-5: the registered callable preserves the public contract).
# Both signatures take a 1-D weight tensor as the 2nd positional arg
# (norm_infer(x, weight, ...) and rms(x, w)), so routing MUST NOT key on its shape.
# (Regression for the Codex P2: a hintless norm_infer(x, weight, bias, eps=...) was
# misrouted to the RMS path, and keyword-only rms(x=..., w=...) to the norm path.)
_HINT_CASES = [
    # (label, args, kwargs, expected_hint) -- "x"/"w"/"b"/"o" are tensor stand-ins
    ("ln_4pos", ("x", "w", "b", 1e-6), {}, "norm_infer"),
    ("ln_eps_kw", ("x", "w", "b"), {"eps": 1e-6}, "norm_infer"),          # was misrouted to RMS
    ("ln_biasNone_eps_kw", ("x", "w", None), {"eps": 1e-6}, "norm_infer"),
    ("ln_all_kw", ("x",), {"weight": "w", "bias": "b", "eps": 1e-6}, "norm_infer"),
    ("ln_is_rms_kw", ("x", "w", "b", 1e-6), {"is_rms_norm": True}, "norm_infer"),
    ("ln_out_kw", ("x", "w", "b", 1e-6), {"out": "o"}, "norm_infer"),
    ("rms_2pos", ("x", "w"), {}, "rms_onepass"),
    ("rms_3pos_eps", ("x", "w", 1e-6), {}, "rms_onepass"),
    ("rms_eps_kw", ("x", "w"), {"eps": 1e-6}, "rms_onepass"),
    ("rms_all_kw", (), {"x": "x", "w": "w"}, "rms_onepass"),              # keyword-only RMS
    ("rms_w_kw", ("x",), {"w": "w"}, "rms_onepass"),
]


@pytest.mark.parametrize(
    "label,args,kwargs,expected", _HINT_CASES, ids=[c[0] for c in _HINT_CASES]
)
def test_infer_hint_routing(label, args, kwargs, expected) -> None:
    # Pure routing logic (no GPU/tensors needed): the call form alone must classify.
    mod = _register_module()
    assert mod._infer_hint(tuple(args), dict(kwargs)) == expected, label


def test_wrapper_hintless_dispatch_supported() -> None:
    # End-to-end: optimized_wrapper with NO dispatcher_hint must route supported
    # calls to the right path and match the typed entry point (real CUDA tensors).
    mod = _register_module()
    dev = "cuda"
    torch.manual_seed(7100)
    # fp32 LayerNorm, a supported (M,N); weight is 1-D (N,) -- the ambiguous shape.
    x = torch.randn(128, 512, device=dev, dtype=torch.float32)
    weight = torch.randn(512, device=dev, dtype=torch.float32)
    bias = torch.randn(512, device=dev, dtype=torch.float32)
    ref_ln = mod.optimized_norm_infer(x, weight, bias, 1e-6)
    for got in (
        mod.optimized_wrapper(x, weight, bias, 1e-6),           # 4 positional
        mod.optimized_wrapper(x, weight, bias, eps=1e-6),       # eps kwarg (was misrouted to RMS)
        mod.optimized_wrapper(x, weight, bias=bias, eps=1e-6),  # bias+eps kwargs
    ):
        torch.testing.assert_close(got, ref_ln, atol=1e-5, rtol=1e-5)
    # bf16 one-pass RMS, a supported (S,D); w is 1-D (D,).
    xr = torch.randn(4096, 128, device=dev, dtype=torch.bfloat16)
    w = torch.randn(128, device=dev, dtype=torch.bfloat16)
    ref_rms = mod.optimized_triton_one_pass_rms_norm(xr, w, 1e-6)
    for got in (
        mod.optimized_wrapper(xr, w),        # 2 positional
        mod.optimized_wrapper(xr, w, 1e-6),  # eps positional
        mod.optimized_wrapper(x=xr, w=w),    # keyword-only (was misrouted to norm_infer)
    ):
        torch.testing.assert_close(got.float(), ref_rms.float(), atol=5e-2, rtol=5e-2)


def test_misaligned_views_fall_back() -> None:
    # A contiguous tensor can be a VIEW with a non-zero storage offset whose
    # data_ptr() is NOT aligned to the kernel's vector width (16 B float4 for LN,
    # 8 B AlignedVector<bf16,4> for RMS). Those must fall back to the baseline; a
    # vector-aligned offset view must still route to CUDA (gate on alignment, not
    # "is it a view"). Regression for the two Codex P2 alignment findings.
    mod = _register_module()
    norm_infer, triton_one_pass_rms_norm = _sglang_baselines()
    dev = "cuda"
    torch.manual_seed(7200)

    # fp32 LayerNorm, supported (M,N)=(128,512). float4 needs a 16-byte base.
    M, N = 128, 512
    lbase = torch.randn(M * N + 8, device=dev, dtype=torch.float32)
    weight = torch.randn(N, device=dev, dtype=torch.float32)  # fresh -> aligned
    bias = torch.randn(N, device=dev, dtype=torch.float32)
    for off in (1, 2, 3):  # 4/8/12-byte offsets -> not 16-aligned
        x = lbase.narrow(0, off, M * N).view(M, N)
        assert x.is_contiguous() and x.data_ptr() % 16 != 0
        assert mod._norm_infer_supported(x, weight, bias, False, None) is False
        got = mod.optimized_norm_infer(x, weight, bias, 1e-6)
        exp = norm_infer(x, weight, bias, 1e-6)
        torch.testing.assert_close(got, exp, atol=1e-5, rtol=1e-5)
    # misaligned weight (aligned x) must also fall back.
    x_aligned = lbase.narrow(0, 4, M * N).view(M, N)  # 16-byte offset -> aligned
    assert x_aligned.data_ptr() % 16 == 0
    wbase = torch.randn(N + 4, device=dev, dtype=torch.float32)
    weight_mis = wbase.narrow(0, 1, N)
    assert weight_mis.is_contiguous() and weight_mis.data_ptr() % 16 != 0
    assert mod._norm_infer_supported(x_aligned, weight_mis, bias, False, None) is False
    torch.testing.assert_close(
        mod.optimized_norm_infer(x_aligned, weight_mis, bias, 1e-6),
        norm_infer(x_aligned, weight_mis, bias, 1e-6), atol=1e-5, rtol=1e-5,
    )
    # an aligned offset view (16-byte) is STILL routed to CUDA.
    assert mod._norm_infer_supported(x_aligned, weight, bias, False, None) is True

    # bf16 one-pass RMS, supported (S,D)=(4096,128). AlignedVector<bf16,4> needs 8 B.
    S, D = 4096, 128
    rbase = torch.randn(S * D + 8, device=dev, dtype=torch.bfloat16)
    w = torch.randn(D, device=dev, dtype=torch.bfloat16)  # fresh -> aligned
    for off in (1, 2, 3):  # 2/4/6-byte offsets -> not 8-aligned
        x = rbase.narrow(0, off, S * D).view(S, D)
        assert x.is_contiguous() and x.data_ptr() % 8 != 0
        assert mod._rms_onepass_supported(x, w) is False
        got = mod.optimized_triton_one_pass_rms_norm(x, w, 1e-6)
        exp = triton_one_pass_rms_norm(x, w, 1e-6)
        torch.testing.assert_close(got.float(), exp.float(), atol=5e-2, rtol=5e-2)
    # an aligned offset view (8-byte, off=4) is STILL routed to CUDA.
    x_aligned_r = rbase.narrow(0, 4, S * D).view(S, D)
    assert x_aligned_r.data_ptr() % 8 == 0
    assert mod._rms_onepass_supported(x_aligned_r, w) is True
