"""Correctness oracle for ``h200_diffusion_norm_infer__multi_shape``.

Skipped unless ``KDA_RUN_CORRECTNESS=1`` (the real run needs a CUDA H200 and the
pinned SGLang checkout on ``PYTHONPATH``). The SGLang baseline is the semantic
oracle; a high-precision FP64 torch reference is used for dynamic, dtype-aware
tolerances:

  err(out) = max|out.double() - fp64_reference|
  pass if  err(candidate) <= tol_mult * err(baseline) + tol_abs       (both dtypes)
  and, for fp32 inputs, additionally err(candidate) <= 1e-5            (hard ceiling)

The CUDA fast path must intercept ONLY the six captured production shapes; every
other shape/dtype/layout/flag must fall back to the SGLang baseline (asserted via
the candidate's dispatch-path recorder and its ``supported_*`` gate predicates).
"""

from __future__ import annotations

import importlib.util
import os
import zlib
from pathlib import Path
from typing import Any

import pytest

# Make the SGLang diffusion baseline importable BEFORE importing the candidate
# (the candidate wrapper binds the baseline at import time for its fallback path).
from _baseline_env import get_baselines, install_platform_shim  # noqa: E402

try:
    import torch
except ImportError:  # pragma: no cover - CUDA env owns the real run
    torch = None


KERNEL_SLUG = "h200_diffusion_norm_infer__multi_shape"
OP_TYPE = "layer_or_rms_norm_infer"
KERNEL_DIR = Path(__file__).resolve().parents[1]

pytestmark = pytest.mark.skipif(
    os.environ.get("KDA_RUN_CORRECTNESS") != "1",
    reason="Set KDA_RUN_CORRECTNESS=1 on a CUDA H200 with the pinned SGLang on PYTHONPATH.",
)


# --------------------------------------------------------------------------- #
# Module loading
# --------------------------------------------------------------------------- #
def _load_register_module():
    install_platform_shim()
    register_py = KERNEL_DIR / "src" / "register.py"
    spec = importlib.util.spec_from_file_location(
        f"kda_kernel_{KERNEL_SLUG}_register", register_py
    )
    assert spec is not None and spec.loader is not None, register_py
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# --------------------------------------------------------------------------- #
# Case table
# --------------------------------------------------------------------------- #
# The six captured production shapes are the ONLY performance/interception shapes.
_CAPTURED = [
    dict(name="helios__ln__f32__M8640_N5120", fn="norm_infer", dtype="float32",
         M=8640, N=5120, has_weight=True, has_bias=True, is_rms_norm=False),
    dict(name="hunyuanvideo__rms__bf16__M648720_N128", fn="rms", dtype="bfloat16",
         M=648720, N=128, has_weight=True, has_bias=False, is_rms_norm=True),
    dict(name="hunyuanvideo__rms__bf16__M1320_N128", fn="rms", dtype="bfloat16",
         M=1320, N=128, has_weight=True, has_bias=False, is_rms_norm=True),
    dict(name="hunyuanvideo__rms__bf16__M650040_N128", fn="rms", dtype="bfloat16",
         M=650040, N=128, has_weight=True, has_bias=False, is_rms_norm=True),
    dict(name="zimage__rms__bf16__M16384_N128", fn="rms", dtype="bfloat16",
         M=16384, N=128, has_weight=True, has_bias=False, is_rms_norm=True),
    dict(name="zimage__rms__bf16__M4096_N128", fn="rms", dtype="bfloat16",
         M=4096, N=128, has_weight=True, has_bias=False, is_rms_norm=True),
]


def _dt(name: str):
    return {"float32": torch.float32, "float16": torch.float16, "bfloat16": torch.bfloat16}[name]


def _default_tol(dtype_name: str) -> dict:
    # abs_ceiling: a hard absolute error ceiling that applies ONLY to
    # well-conditioned inputs (the real captured workload). It is disabled
    # (None) for ill-conditioned adversarial inputs, where even the SGLang
    # baseline cannot reach it (var->0 makes rstd~1/sqrt(eps) amplify fp32
    # cancellation); there the candidate is judged purely against the baseline.
    if dtype_name == "float32":
        return dict(tol_mult=4.0, tol_abs=2e-6, abs_ceiling=1e-5)
    if dtype_name == "float16":
        return dict(tol_mult=3.0, tol_abs=1.0 / 256, abs_ceiling=None)
    return dict(tol_mult=3.0, tol_abs=1.0 / 64, abs_ceiling=None)  # bfloat16


def make_cases() -> list[dict[str, Any]]:
    """All configured cases.

    - ``perf``: exactly the six captured shapes (CUDA fast path), no inferred/broadened shapes.
    - ``adversarial``: the captured helios FP32 LayerNorm shape with degenerate rows (CUDA path).
    - ``regression``: canonical SGLang test grid (CI subset) + one-pass cross-checks -> all FALL BACK.
    """
    cases: list[dict[str, Any]] = []

    for c in _CAPTURED:
        case = dict(c)
        case.update(kind="perf", eps=1e-6, init="randn", expect_path="cuda",
                    noncontig=False, warmup=25, iters=100)
        case.update(_default_tol(c["dtype"]))
        cases.append(case)

    # Adversarial FP32 LayerNorm at the captured helios shape (still the CUDA path).
    for adv in ("zeros", "near_const", "large", "tiny_var", "mixed_adv"):
        case = dict(name=f"helios_adv_{adv}__ln__f32__M8640_N5120", fn="norm_infer",
                    dtype="float32", M=8640, N=5120, has_weight=True, has_bias=True,
                    is_rms_norm=False, kind="adversarial", eps=1e-6, init=adv,
                    expect_path="cuda", noncontig=False, warmup=0, iters=0)
        case.update(_default_tol("float32"))  # strict abs_ceiling=1e-5 applies to adversarial too
        cases.append(case)

    # Canonical regression grid (CI subset) -> NOT captured -> fallback to baseline.
    full = os.environ.get("KDA_FULL_GRID") == "1"
    batch = [1, 2, 4] if full else [1, 2]
    seqs = [6, 33, 128, 257] if full else [6, 128]
    hiddens = [512, 1024, 1536, 3072] if full else [512, 3072]
    dtypes = ["float16", "bfloat16", "float32"] if full else ["float16", "bfloat16"]
    for b in batch:
        for s in seqs:
            for h in hiddens:
                for d in dtypes:
                    m = b * s
                    case = dict(name=f"grid__ln__{d}__B{b}_S{s}_H{h}", fn="norm_infer",
                                dtype=d, M=m, N=h, has_weight=True, has_bias=True,
                                is_rms_norm=False, kind="regression", eps=1e-6,
                                init="randn", expect_path="fallback", noncontig=False,
                                warmup=0, iters=0)
                    case.update(_default_tol(d))
                    cases.append(case)

    # One-pass RMS cross-checks on non-captured (D != 128) shapes -> fallback.
    for (m, d, dt) in [(768, 64, "bfloat16"), (2048, 256, "bfloat16"), (4096, 64, "float16")]:
        case = dict(name=f"rmsxcheck__rms__{dt}__M{m}_N{d}", fn="rms", dtype=dt,
                    M=m, N=d, has_weight=True, has_bias=False, is_rms_norm=True,
                    kind="regression", eps=1e-6, init="randn", expect_path="fallback",
                    noncontig=False, warmup=0, iters=0)
        case.update(_default_tol(dt))
        cases.append(case)

    return cases


# --------------------------------------------------------------------------- #
# Input construction (deterministic per case name)
# --------------------------------------------------------------------------- #
def _seed(name: str) -> int:
    return zlib.adler32(name.encode()) & 0x7FFFFFFF


def _make_x(case: dict[str, Any], gen) -> "torch.Tensor":
    M, N = case["M"], case["N"]
    dt = _dt(case["dtype"])
    init = case.get("init", "randn")
    f32 = torch.float32
    if init == "randn":
        x = torch.randn(M, N, generator=gen, device="cuda", dtype=f32)
    elif init == "zeros":
        x = torch.zeros(M, N, device="cuda", dtype=f32)
    elif init == "near_const":
        x = torch.full((M, N), 0.123, device="cuda", dtype=f32)
        x += 1e-4 * torch.randn(M, N, generator=gen, device="cuda", dtype=f32)
    elif init == "large":
        x = 1e3 * torch.randn(M, N, generator=gen, device="cuda", dtype=f32)
    elif init == "tiny_var":
        x = torch.full((M, N), 2.0, device="cuda", dtype=f32)
        x += 1e-6 * torch.randn(M, N, generator=gen, device="cuda", dtype=f32)
    elif init == "mixed_adv":
        # Stripe degenerate row-blocks across the captured shape.
        x = torch.randn(M, N, generator=gen, device="cuda", dtype=f32)
        q = M // 4
        x[0:q] = 0.0
        x[q:2 * q] = 5.0
        x[2 * q:3 * q] = 1e3 * x[2 * q:3 * q]
        x[3 * q:] = 2.0 + 1e-6 * x[3 * q:]
    else:
        raise ValueError(init)
    x = x.to(dt)
    if case.get("noncontig"):
        x = torch.empty(M, N + 8, device="cuda", dtype=dt)[:, :N]
        x.copy_(torch.randn(M, N, generator=gen, device="cuda", dtype=f32).to(dt))
    return x


def build_inputs(case: dict[str, Any]) -> dict[str, Any]:
    gen = torch.Generator(device="cuda").manual_seed(_seed(case["name"]))
    N = case["N"]
    dt = _dt(case["dtype"])
    x = _make_x(case, gen)
    weight = (torch.randn(N, generator=gen, device="cuda", dtype=torch.float32).to(dt)
              if case.get("has_weight") else None)
    bias = (torch.randn(N, generator=gen, device="cuda", dtype=torch.float32).to(dt)
            if case.get("has_bias") else None)
    return dict(x=x, weight=weight, bias=bias, eps=case["eps"],
                is_rms_norm=case.get("is_rms_norm", False))


# --------------------------------------------------------------------------- #
# Calls: baseline / candidate / fp64 reference
# --------------------------------------------------------------------------- #
def call_baseline(case, inp):
    base_norm_infer, base_rms = get_baselines()
    if case["fn"] == "norm_infer":
        return base_norm_infer(inp["x"], inp["weight"], inp["bias"], inp["eps"],
                               inp["is_rms_norm"])
    return base_rms(inp["x"], inp["weight"], inp["eps"])


def call_candidate(case, inp):
    mod = _load_register_module()
    if case["fn"] == "norm_infer":
        return mod.norm_infer(inp["x"], inp["weight"], inp["bias"], inp["eps"],
                              inp["is_rms_norm"])
    return mod.triton_one_pass_rms_norm(inp["x"], inp["weight"], inp["eps"])


def reference(case, inp) -> "torch.Tensor":
    x = inp["x"].double()
    eps = case["eps"]
    w = inp["weight"].double() if inp["weight"] is not None else None
    b = inp["bias"].double() if inp["bias"] is not None else None
    if case["fn"] == "rms" or case.get("is_rms_norm", False):
        rstd = torch.rsqrt((x * x).mean(-1, keepdim=True) + eps)
        y = x * rstd
        if w is not None:
            y = y * w
        if b is not None:
            y = y + b
        return y
    mean = x.mean(-1, keepdim=True)
    var = ((x - mean) ** 2).mean(-1, keepdim=True)  # biased (/N), matches baseline
    y = (x - mean) * torch.rsqrt(var + eps)
    if w is not None:
        y = y * w
    if b is not None:
        y = y + b
    return y


# --------------------------------------------------------------------------- #
# Assertions
# --------------------------------------------------------------------------- #
def _check_accuracy(case, cand, base, ref) -> None:
    name = case["name"]
    assert torch.isfinite(cand).all(), f"{name}: candidate has NaN/Inf"
    assert torch.isfinite(base).all(), f"{name}: baseline has NaN/Inf"
    assert cand.shape == base.shape, f"{name}: shape {cand.shape} != {base.shape}"
    assert cand.dtype == base.dtype, f"{name}: dtype {cand.dtype} != {base.dtype}"
    err_base = (base.double() - ref).abs().max().item()
    err_cand = (cand.double() - ref).abs().max().item()
    bound = case["tol_mult"] * err_base + case["tol_abs"]
    assert err_cand <= bound, (
        f"{name}: err_cand={err_cand:.3e} > {bound:.3e} (tol_mult*err_base + tol_abs; "
        f"err_base={err_base:.3e})"
    )
    ceiling = case.get("abs_ceiling")
    if ceiling is not None:
        assert err_cand <= ceiling, (
            f"{name}: err_cand={err_cand:.3e} > {ceiling:.3e} absolute ceiling "
            f"(well-conditioned inputs)"
        )


# --------------------------------------------------------------------------- #
# Tests
# --------------------------------------------------------------------------- #
def test_register_metadata() -> None:
    mod = _load_register_module()
    assert hasattr(mod, "register")
    spec = mod.register()
    assert spec["name"] == KERNEL_SLUG
    assert spec["op_type"] == OP_TYPE
    assert callable(spec["callable"])
    assert hasattr(mod, "EXPORTS"), "register.py must expose EXPORTS for promotion"
    assert set(mod.EXPORTS.keys()) == {"norm_infer", "triton_one_pass_rms_norm"}


def test_make_cases_are_exactly_captured_for_perf() -> None:
    perf = [c for c in make_cases() if c["kind"] == "perf"]
    got = {(c["fn"], c["dtype"], c["M"], c["N"]) for c in perf}
    expected = {
        ("norm_infer", "float32", 8640, 5120),
        ("rms", "bfloat16", 648720, 128),
        ("rms", "bfloat16", 1320, 128),
        ("rms", "bfloat16", 650040, 128),
        ("rms", "bfloat16", 16384, 128),
        ("rms", "bfloat16", 4096, 128),
    }
    assert got == expected, f"perf set must be EXACTLY the six captured shapes; got {got}"


@pytest.mark.parametrize("case", [c for c in make_cases() if c["kind"] in ("perf", "adversarial")],
                         ids=lambda c: c["name"])
def test_perf_shape_correctness(case) -> None:
    assert torch.cuda.is_available()
    inp = build_inputs(case)
    base = call_baseline(case, inp)
    cand = call_candidate(case, inp)
    ref = reference(case, inp)
    _check_accuracy(case, cand, base, ref)
    mod = _load_register_module()
    path = mod.last_dispatch(case["fn"])
    assert path == case["expect_path"], f"{case['name']}: dispatch {path} != {case['expect_path']}"


@pytest.mark.parametrize("case", [c for c in make_cases() if c["kind"] == "regression"],
                         ids=lambda c: c["name"])
def test_regression_fallback_matches_baseline(case) -> None:
    assert torch.cuda.is_available()
    inp = build_inputs(case)
    base = call_baseline(case, inp)
    cand = call_candidate(case, inp)
    ref = reference(case, inp)
    _check_accuracy(case, cand, base, ref)
    mod = _load_register_module()
    assert mod.last_dispatch(case["fn"]) == "fallback", (
        f"{case['name']}: non-captured shape must fall back to baseline"
    )


def test_fallback_gate_rejects_noncaptured() -> None:
    """The dispatch gate must reject everything that is not an exact captured signature."""
    mod = _load_register_module()
    f32, bf16, f16 = torch.float32, torch.bfloat16, torch.float16

    def t(M, N, dt, device="cuda", contig=True):
        x = torch.randn(M, N, device=device, dtype=torch.float32).to(dt)
        if not contig:
            x = torch.empty(M, N + 8, device=device, dtype=dt)[:, :N]
        return x

    # norm_infer gate: captured is (8640,5120,f32, weight+bias, is_rms_norm=False).
    w5120 = torch.randn(5120, device="cuda", dtype=f32)
    b5120 = torch.randn(5120, device="cuda", dtype=f32)
    assert mod.supported_norm_infer(t(8640, 5120, f32), w5120, b5120, 1e-6, False) is True
    assert mod.supported_norm_infer(t(8640, 5120, f16), w5120.half(), b5120.half(), 1e-6, False) is False  # dtype
    assert mod.supported_norm_infer(t(256, 5120, f32), w5120, b5120, 1e-6, False) is False  # M
    assert mod.supported_norm_infer(t(8640, 5120, f32), w5120, b5120, 1e-6, True) is False  # is_rms_norm
    assert mod.supported_norm_infer(t(8640, 5120, f32), None, b5120, 1e-6, False) is False  # missing weight
    assert mod.supported_norm_infer(t(8640, 5120, f32, contig=False), w5120, b5120, 1e-6, False) is False  # layout
    assert mod.supported_norm_infer(t(8640, 5120, f32, device="cpu"), w5120.cpu(), b5120.cpu(), 1e-6, False) is False  # device
    assert mod.supported_norm_infer(t(8640, 5120, f32), w5120, b5120, 1e-5, False) is False  # eps != captured 1e-6
    assert mod.supported_norm_infer(t(8640, 5120, f32), w5120.reshape(1, 5120), b5120, 1e-6, False) is False  # weight rank (1,N)
    assert mod.supported_norm_infer(t(8640, 5120, f32), w5120, b5120.reshape(5120, 1), 1e-6, False) is False  # bias rank (N,1)

    # rms gate: captured is (M in {1320,4096,16384,648720,650040}, 128, bf16, weight).
    w128 = torch.randn(128, device="cuda", dtype=f32).to(bf16)
    assert mod.supported_rms(t(4096, 128, bf16), w128, 1e-6) is True
    assert mod.supported_rms(t(4096, 128, f16), w128.to(f16), 1e-6) is False  # dtype
    assert mod.supported_rms(t(4097, 128, bf16), w128, 1e-6) is False  # M not captured
    assert mod.supported_rms(t(4096, 64, bf16), torch.randn(64, device="cuda", dtype=f32).to(bf16), 1e-6) is False  # N
    assert mod.supported_rms(t(4096, 128, bf16, contig=False), w128, 1e-6) is False  # layout
    assert mod.supported_rms(t(4096, 128, bf16, device="cpu"), w128.cpu(), 1e-6) is False  # device
    assert mod.supported_rms(t(4096, 128, bf16), w128, 1e-5) is False  # eps != captured 1e-6
    assert mod.supported_rms(t(4096, 128, bf16), w128.reshape(1, 128), 1e-6) is False  # weight rank (1,128)
    assert mod.supported_rms(t(4096, 128, bf16), w128.reshape(128, 1), 1e-6) is False  # weight rank (128,1)


def test_registry_callable_routes_both_entry_points() -> None:
    """register()['callable'] must preserve BOTH wrapped callsite contracts:
    triton_one_pass_rms_norm(x, w, eps) AND norm_infer(x, weight, bias, eps, is_rms_norm)."""
    assert torch.cuda.is_available()
    mod = _load_register_module()
    reg_callable = mod.register()["callable"]
    base_norm_infer, base_rms = get_baselines()

    # RMS callsite (x, w, eps) routed through the single registry callable.
    rms_case = next(c for c in make_cases() if c["fn"] == "rms" and c["kind"] == "perf")
    inp = build_inputs(rms_case)
    out = reg_callable(inp["x"], inp["weight"], inp["eps"])
    base = base_rms(inp["x"], inp["weight"], inp["eps"])
    _check_accuracy(rms_case, out, base, reference(rms_case, inp))
    assert mod.last_dispatch("rms") == "cuda", "registry callable must route RMS (x,w,eps) to the RMS CUDA path"

    # norm_infer callsite (x, weight, bias, eps, is_rms_norm) routed through the same callable.
    ln_case = next(c for c in make_cases() if c["fn"] == "norm_infer" and c["kind"] == "perf")
    inp2 = build_inputs(ln_case)
    out2 = reg_callable(inp2["x"], inp2["weight"], inp2["bias"], inp2["eps"], inp2["is_rms_norm"])
    base2 = base_norm_infer(inp2["x"], inp2["weight"], inp2["bias"], inp2["eps"], inp2["is_rms_norm"])
    _check_accuracy(ln_case, out2, base2, reference(ln_case, inp2))
    assert mod.last_dispatch("norm_infer") == "cuda", "registry callable must route norm_infer to the LN CUDA path"


def test_registry_callable_norm_infer_optional_none_bias() -> None:
    """register()['callable'] must route the valid norm_infer(x, weight, None, eps=...)
    form (optional bias = None) to norm_infer (which falls back to the baseline since
    bias=None is not a captured signature), NOT mis-route it to the RMS path."""
    assert torch.cuda.is_available()
    mod = _load_register_module()
    reg_callable = mod.register()["callable"]
    base_norm_infer, _ = get_baselines()
    torch.manual_seed(0)
    x = torch.randn(256, 512, device="cuda", dtype=torch.float32)  # non-captured + bias=None -> fallback
    w = torch.randn(512, device="cuda", dtype=torch.float32)
    out = reg_callable(x, w, None, eps=1e-6)  # (x, weight, None, eps=) must reach norm_infer
    base = base_norm_infer(x, w, None, 1e-6, False)
    assert mod.last_dispatch("norm_infer") == "fallback", "None-bias norm_infer must route to norm_infer (fallback)"
    assert torch.isfinite(out).all()
    torch.testing.assert_close(out.float(), base.float(), atol=1e-5, rtol=1e-5)
