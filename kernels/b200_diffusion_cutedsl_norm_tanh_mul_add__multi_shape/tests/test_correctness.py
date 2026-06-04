"""Correctness harness for ``b200_diffusion_cutedsl_norm_tanh_mul_add__multi_shape``.

Runs only with ``KDA_RUN_CORRECTNESS=1`` on a CUDA box (the ion-b200
``sglang_bbuf`` container). Covers:

- the 4 captured zimage production signatures (bf16, rms, bias=None,
  scale/scale2 ``[1,1,D]``, shift ``[1,S,D]``, D=3840, S in {4096, 4128});
- the canonical regression grid: (B,S,D) from [(1,1024,3072), (4,512,3072)]
  x dtypes {fp16, bf16, fp32} x norm {layer, rms} x affine {weighted, plain}
  x scale/shift layouts {11D, B1D, 1SD, BSD}, for both entry points
  (the second entry point adds weight2/bias2/scale2 over the same grid);
- contract-rejection cases: the public wrappers validate scale/shift/scale2 as
  3-D ``[1|B, 1|S, D]`` tensors, so layouts ``[1]``, ``[D]``, ``[1,D]``,
  ``[B,D]``, ``[B,F,1,D]`` must raise ValueError, as must unsupported D,
  dtype, norm_type, and non-contiguous last dims;
- validator self-tests (NaN injection, wrong-eps oracle sensitivity) and the
  ``KDA_REQUIRE_CANDIDATE=1`` anti-silent-fallback guard.

Oracle: fp32 torch reference emulating the baseline's rounding semantics
(norm result rounded to the I/O dtype before modulation; ``y`` rounded before
the second norm). The frozen CuTe-DSL baseline lives in ``baseline/``.
"""

from __future__ import annotations

import hashlib
import importlib.util
import os
import sys
from pathlib import Path
from typing import Any

import pytest

try:
    import torch
except ImportError:  # pragma: no cover - CUDA env owns the real run
    torch = None


KERNEL_SLUG = "b200_diffusion_cutedsl_norm_tanh_mul_add__multi_shape"
OP_TYPE = "cutedsl_norm_tanh_mul_add"
KERNEL_DIR = Path(__file__).resolve().parents[1]

pytestmark = pytest.mark.skipif(
    os.environ.get("KDA_RUN_CORRECTNESS") != "1",
    reason="Set KDA_RUN_CORRECTNESS=1 inside the remote CUDA container.",
)

if str(KERNEL_DIR) not in sys.path:
    sys.path.insert(0, str(KERNEL_DIR))


def _load_register_module():
    register_py = KERNEL_DIR / "src" / "register.py"
    spec = importlib.util.spec_from_file_location(
        f"kda_kernel_{KERNEL_SLUG}_register", register_py
    )
    assert spec is not None and spec.loader is not None, register_py
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_REGISTER_MODULE = None


def _register_module():
    global _REGISTER_MODULE
    if _REGISTER_MODULE is None:
        _REGISTER_MODULE = _load_register_module()
    return _REGISTER_MODULE


def _baseline_module():
    import baseline

    return baseline


# ---------------------------------------------------------------------------
# Case construction
# ---------------------------------------------------------------------------

_PRODUCTION_D = 3840
_GRID_SHAPES = [(1, 1024, 8, 3072), (4, 512, 16, 3072)]  # (B, S, F, D)
_GRID_DTYPES = ["float16", "bfloat16", "float32"]
_GRID_NORMS = ["layer", "rms"]
_GRID_AFFINE = ["weighted", "plain"]  # weighted: weight (+bias for layer); plain: None
_GRID_MODES = ["11D", "B1D", "1SD", "BSD"]  # 3-D layouts accepted by validate_3d
_EPS = 1e-5


def _mode_shape(mode: str, B: int, S: int, D: int) -> tuple[int, ...]:
    return {
        "1": (1,),
        "D": (D,),
        "1D": (1, D),
        "BD": (B, D),
        "11D": (1, 1, D),
        "B1D": (B, 1, D),
        "1SD": (1, S, D),
        "BSD": (B, S, D),
    }[mode]


def make_cases() -> list[dict[str, Any]]:
    """All configured correctness/benchmark cases.

    Production cases carry ``bench=True`` (the benchmark uses only those);
    grid cases are correctness-only. Tensors are materialized lazily via
    ``_materialize`` and freed per-case to bound GPU memory.
    """

    cases: list[dict[str, Any]] = []
    # Captured zimage production signatures (verbatim shape table).
    for variant in ("v1", "v2"):
        for S in (4096, 4128):
            cases.append(
                {
                    "name": f"zimage__{variant}__B1_S{S}_D{_PRODUCTION_D}__bf16_rms",
                    "variant": variant,
                    "B": 1,
                    "S": S,
                    "D": _PRODUCTION_D,
                    "dtype": "bfloat16",
                    "norm_type": "rms",
                    "affine": "weighted",  # weight=[D], bias=None (rms has no bias)
                    "mode_scale": "11D",
                    "mode_shift": "1SD",
                    "eps": _EPS,
                    "atol": 5e-2,
                    "rtol": 5e-2,
                    "bench": True,
                    "warmup": 50,
                    "iters": 200,
                }
            )
    # Canonical regression grid (adapted from the sister-family SGLang test).
    for B, S, _F, D in _GRID_SHAPES:
        for dtype in _GRID_DTYPES:
            for norm_type in _GRID_NORMS:
                for affine in _GRID_AFFINE:
                    for mode in _GRID_MODES:
                        for variant in ("v1", "v2"):
                            is_fp32 = dtype == "float32"
                            cases.append(
                                {
                                    "name": (
                                        f"grid__{variant}__B{B}_S{S}_D{D}__"
                                        f"{dtype}_{norm_type}_{affine}_{mode}"
                                    ),
                                    "variant": variant,
                                    "B": B,
                                    "S": S,
                                    "D": D,
                                    "dtype": dtype,
                                    "norm_type": norm_type,
                                    "affine": affine,
                                    "mode_scale": mode,
                                    "mode_shift": mode,
                                    "eps": _EPS,
                                    "atol": 1e-5 if is_fp32 else 5e-2,
                                    "rtol": 1e-5 if is_fp32 else 5e-2,
                                    "bench": False,
                                    "warmup": 5,
                                    "iters": 20,
                                }
                            )
    # Independent scale/shift layout combinations (modes intentionally untied).
    B, S, _F, D = _GRID_SHAPES[1]
    for variant in ("v1", "v2"):
        for mode_scale, mode_shift in (
            ("11D", "BSD"), ("B1D", "1SD"), ("1SD", "11D"), ("BSD", "B1D"),
        ):
            cases.append(
                {
                    "name": f"mix__{variant}__B{B}_S{S}_D{D}__bf16_rms_{mode_scale}sc_{mode_shift}sh",
                    "variant": variant,
                    "B": B,
                    "S": S,
                    "D": D,
                    "dtype": "bfloat16",
                    "norm_type": "rms",
                    "affine": "weighted",
                    "mode_scale": mode_scale,
                    "mode_shift": mode_shift,
                    "eps": _EPS,
                    "atol": 5e-2,
                    "rtol": 5e-2,
                    "bench": False,
                    "warmup": 5,
                    "iters": 20,
                }
            )
    return cases


def _torch_dtype(name: str):
    return {
        "float16": torch.float16,
        "bfloat16": torch.bfloat16,
        "float32": torch.float32,
    }[name]


def _materialize(case: dict[str, Any]) -> dict[str, Any]:
    """Build (and cache) the input tensors for a case on the CUDA device."""

    if "_tensors" in case:
        return case["_tensors"]
    assert torch is not None and torch.cuda.is_available()
    B, S, D = case["B"], case["S"], case["D"]
    dtype = _torch_dtype(case["dtype"])
    gen = torch.Generator(device="cuda")
    # Stable digest-derived seed: identical tensor data across processes/runs
    # (Python's hash() is process-randomized and would break exact replay).
    gen.manual_seed(int.from_bytes(hashlib.sha256(case["name"].encode()).digest()[:4], "little"))

    def rand(shape, *, offset=0.0, scale_=1.0):
        t = torch.randn(shape, generator=gen, device="cuda", dtype=torch.float32)
        return (t * scale_ + offset).to(dtype).contiguous()

    x = rand((B, S, D))
    if case["affine"] == "weighted":
        weight = rand((D,), offset=1.0, scale_=0.2)
        bias = rand((D,), scale_=0.2) if case["norm_type"] == "layer" else None
    else:
        weight, bias = None, None
    scale = rand(_mode_shape(case["mode_scale"], B, S, D))
    shift = rand(_mode_shape(case["mode_shift"], B, S, D))
    tensors: dict[str, Any] = {
        "x": x,
        "weight": weight,
        "bias": bias,
        "scale": scale,
        "shift": shift,
    }
    if case["variant"] == "v2":
        if case["affine"] == "weighted":
            tensors["weight2"] = rand((D,), offset=1.0, scale_=0.2)
            tensors["bias2"] = (
                rand((D,), scale_=0.2) if case["norm_type"] == "layer" else None
            )
        else:
            tensors["weight2"], tensors["bias2"] = None, None
        tensors["scale2"] = rand(_mode_shape(case["mode_scale"], B, S, D))
    case["_tensors"] = tensors
    return tensors


def _release(case: dict[str, Any]) -> None:
    case.pop("_tensors", None)


def _call_args(case: dict[str, Any]) -> tuple:
    t = _materialize(case)
    if case["variant"] == "v1":
        return (
            t["x"],
            t["weight"],
            t["bias"],
            t["scale"],
            t["shift"],
            case["norm_type"],
            case["eps"],
        )
    return (
        t["x"],
        t["weight"],
        t["bias"],
        t["scale"],
        t["shift"],
        t["weight2"],
        t["bias2"],
        t["scale2"],
        case["norm_type"],
        case["eps"],
    )


# ---------------------------------------------------------------------------
# Callables under test (contract shared with benchmark.py)
# ---------------------------------------------------------------------------


def baseline(case: dict[str, Any]) -> Any:
    """Frozen CuTe-DSL baseline copy (raw callables, see docs/baseline_source.md)."""

    mod = _baseline_module()
    args = _call_args(case)
    if case["variant"] == "v1":
        return mod.fused_norm_tanh_mul_add(*args)
    return mod.fused_norm_tanh_mul_add_norm_scale(*args)


def candidate(case: dict[str, Any]) -> Any:
    module = _register_module()
    wrapper = getattr(module, "optimized_wrapper")
    return wrapper(*_call_args(case))


# ---------------------------------------------------------------------------
# fp32 reference oracle (emulates baseline rounding semantics)
# ---------------------------------------------------------------------------


def _norm_f32(xf, weight, bias, norm_type: str, eps: float):
    if norm_type == "rms":
        n = xf * torch.rsqrt(xf.pow(2).mean(dim=-1, keepdim=True) + eps)
        # Baseline rms applies weight only; a provided bias is IGNORED.
        if weight is not None:
            n = n * weight.float()
        return n
    mean = xf.mean(dim=-1, keepdim=True)
    var = (xf - mean).pow(2).mean(dim=-1, keepdim=True)
    n = (xf - mean) * torch.rsqrt(var + eps)
    # Baseline layer norm applies affine only when BOTH weight and bias are
    # tensors; one-sided affine degrades to plain normalization.
    if weight is not None and bias is not None:
        n = n * weight.float() + bias.float()
    return n


def reference(case: dict[str, Any]) -> Any:
    t = _materialize(case)
    dtype = _torch_dtype(case["dtype"])
    eps = case["eps"]
    xf = t["x"].float()
    n = _norm_f32(xf, t["weight"], t["bias"], case["norm_type"], eps)
    # Baseline rounds the normalized result to the I/O dtype before modulation.
    n = n.to(dtype).float()
    y = (n * torch.tanh(t["scale"].float()) + t["shift"].float()).to(dtype)
    if case["variant"] == "v1":
        return y
    # Second norm consumes the dtype-rounded y.
    n2 = _norm_f32(y.float(), t["weight2"], t["bias2"], case["norm_type"], eps)
    n2 = n2.to(dtype).float()
    y2 = (n2 * (1.0 + t["scale2"].float())).to(dtype)
    return y, y2


# ---------------------------------------------------------------------------
# Validators
# ---------------------------------------------------------------------------


def _assert_no_nan_inf(value: Any, *, path: str) -> None:
    if torch is not None and isinstance(value, torch.Tensor):
        assert not torch.isnan(value).any(), f"{path} contains NaN"
        assert not torch.isinf(value).any(), f"{path} contains Inf"
    elif isinstance(value, (tuple, list)):
        for i, item in enumerate(value):
            _assert_no_nan_inf(item, path=f"{path}[{i}]")


def _as_tuple(value: Any) -> tuple:
    return value if isinstance(value, tuple) else (value,)


def _assert_close(actual: Any, expected: Any, *, case: dict[str, Any], path: str) -> None:
    atol, rtol = case["atol"], case["rtol"]
    _assert_no_nan_inf(actual, path=path)
    a_t, e_t = _as_tuple(actual), _as_tuple(expected)
    assert len(a_t) == len(e_t), f"{path}: arity {len(a_t)} != {len(e_t)}"
    for i, (a, e) in enumerate(zip(a_t, e_t)):
        assert a.shape == e.shape, f"{path}[{i}]: shape {a.shape} != {e.shape}"
        assert a.dtype == e.dtype, f"{path}[{i}]: dtype {a.dtype} != {e.dtype}"
        torch.testing.assert_close(
            a.float(), e.float(), atol=atol, rtol=rtol, msg=lambda m: f"{path}[{i}]: {m}"
        )


def _max_abs_err(actual: Any, expected: Any) -> float:
    errs = [
        (a.float() - e.float()).abs().max().item()
        for a, e in zip(_as_tuple(actual), _as_tuple(expected))
    ]
    return max(errs)


_DTYPE_EPS = {"float16": 2.0**-10, "bfloat16": 2.0**-7, "float32": 2.0**-23}


def _assert_dynamic_noise_bound(case, cand_out, base_out, ref_out) -> None:
    """Candidate error vs fp32 reference must stay within a small multiple of the
    baseline's own quantization noise (SGLang-style dynamic tolerance)."""

    err_c = _max_abs_err(cand_out, ref_out)
    err_b = _max_abs_err(base_out, ref_out)
    ref_mag = max(
        r.float().abs().max().item() for r in _as_tuple(ref_out)
    )
    floor = 4.0 * _DTYPE_EPS[case["dtype"]] * max(1.0, ref_mag)
    limit = max(2.0 * err_b, floor)
    assert err_c <= limit, (
        f"{case['name']}: candidate max-abs-err {err_c:.3e} exceeds dynamic bound "
        f"{limit:.3e} (baseline err {err_b:.3e}, floor {floor:.3e})"
    )


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


def test_register_metadata() -> None:
    module = _register_module()
    assert hasattr(module, "register")
    spec = module.register()
    assert spec["name"] == KERNEL_SLUG
    assert spec["op_type"] == OP_TYPE
    assert callable(spec["callable"])


def test_baseline_matches_reference() -> None:
    """Frozen baseline copy vs fp32 oracle on every configured case."""

    cases = make_cases()
    assert cases, "No correctness cases configured."
    failures = []
    for case in cases:
        try:
            base_out = baseline(case)
            ref_out = reference(case)
            _assert_close(base_out, ref_out, case=case, path=f"baseline:{case['name']}")
        except AssertionError as exc:  # collect, report all
            failures.append(f"{case['name']}: {exc}")
        finally:
            _release(case)
    assert not failures, "baseline-vs-reference failures:\n" + "\n".join(failures[:20])


def test_candidate_matches_baseline_and_reference(monkeypatch) -> None:
    """Candidate wrapper vs baseline copy and fp32 oracle, with the dynamic
    quantization-noise bound, on every configured case.

    When the native module is available, ``KDA_REQUIRE_CANDIDATE=1`` is forced
    for the whole run: every configured case is native-eligible by design, so
    the native path itself is what gets validated — a silent fallback cannot
    make this test pass."""

    if _register_module().native_available():
        monkeypatch.setenv("KDA_REQUIRE_CANDIDATE", "1")
    cases = make_cases()
    failures = []
    for case in cases:
        try:
            base_out = baseline(case)
            cand_out = candidate(case)
            ref_out = reference(case)
            _assert_close(cand_out, base_out, case=case, path=f"cand-vs-base:{case['name']}")
            _assert_close(cand_out, ref_out, case=case, path=f"cand-vs-ref:{case['name']}")
            _assert_dynamic_noise_bound(case, cand_out, base_out, ref_out)
        except AssertionError as exc:
            failures.append(f"{case['name']}: {exc}")
        finally:
            _release(case)
    assert not failures, "candidate failures:\n" + "\n".join(failures[:20])


def test_fast_path_fires_on_production_signatures(monkeypatch) -> None:
    """All 4 captured production signatures must take the native fast path
    (no silent fallback) once the native candidate is built."""

    module = _register_module()
    if not module.native_available():
        pytest.skip("native CUDA candidate not built yet (pre-implementation phase)")
    monkeypatch.setenv("KDA_REQUIRE_CANDIDATE", "1")
    for case in [c for c in make_cases() if c["bench"]]:
        before = module.fast_path_hits()
        out = candidate(case)
        _assert_no_nan_inf(out, path=case["name"])
        assert module.fast_path_hits() == before + 1, (
            f"{case['name']}: fast path did not fire "
            f"(last fallback reason: {module.last_fallback_reason()})"
        )
        _release(case)


def _production_v1_args(D_override=None, **overrides):
    """Build a production-like v1 arg tuple with optional invalid mutations."""

    D = D_override or 512
    B, S = 1, 8
    dtype = torch.bfloat16
    x = torch.randn(B, S, D, device="cuda", dtype=dtype)
    weight = torch.randn(D, device="cuda", dtype=dtype)
    scale = torch.randn(1, 1, D, device="cuda", dtype=dtype)
    shift = torch.randn(1, S, D, device="cuda", dtype=dtype)
    args = {
        "x": x,
        "weight": weight,
        "bias": None,
        "scale": scale,
        "shift": shift,
        "norm_type": "rms",
        "eps": 1e-5,
    }
    args.update(overrides)
    return (
        args["x"], args["weight"], args["bias"], args["scale"], args["shift"],
        args["norm_type"], args["eps"],
    )


_REJECTION_BUILDERS = {
    # D contract: not a multiple of 256 / above 8192.
    "bad_D_not_mult_256": lambda: _production_v1_args(D_override=100),
    "bad_D_above_8192": lambda: _production_v1_args(D_override=8448),
    # Non-3-D scale layouts rejected by the public contract (validate_3d).
    "mode_1_scalar_scale": lambda: _production_v1_args(
        scale=torch.randn(1, device="cuda", dtype=torch.bfloat16)
    ),
    "mode_D_scale": lambda: _production_v1_args(
        scale=torch.randn(512, device="cuda", dtype=torch.bfloat16)
    ),
    "mode_1D_scale": lambda: _production_v1_args(
        scale=torch.randn(1, 512, device="cuda", dtype=torch.bfloat16)
    ),
    "mode_BD_scale": lambda: _production_v1_args(
        scale=torch.randn(1, 512, device="cuda", dtype=torch.bfloat16).reshape(1, 512)
    ),
    "mode_BF1D_scale": lambda: _production_v1_args(
        scale=torch.randn(1, 2, 1, 512, device="cuda", dtype=torch.bfloat16)
    ),
    # Misc contract violations.
    "bad_norm_type": lambda: _production_v1_args(norm_type="instance"),
    "non_contiguous_last_dim": lambda: _production_v1_args(
        x=torch.randn(1, 512, 8, device="cuda", dtype=torch.bfloat16).transpose(1, 2)
    ),
    "wrong_weight_shape": lambda: _production_v1_args(
        weight=torch.randn(256, device="cuda", dtype=torch.bfloat16)
    ),
    "fp64_dtype": lambda: _production_v1_args(
        x=torch.randn(1, 8, 512, device="cuda", dtype=torch.float64)
    ),
}


@pytest.mark.parametrize("kind", sorted(_REJECTION_BUILDERS))
def test_contract_rejections_baseline(kind: str) -> None:
    """The baseline copy preserves upstream ValueError behavior."""

    args = _REJECTION_BUILDERS[kind]()
    with pytest.raises(ValueError):
        _baseline_module().fused_norm_tanh_mul_add(*args)


@pytest.mark.parametrize("kind", sorted(_REJECTION_BUILDERS))
def test_contract_rejections_candidate(kind: str) -> None:
    """The candidate wrapper reproduces the same rejection contract (it must
    not 'support' inputs the public op rejects)."""

    args = _REJECTION_BUILDERS[kind]()
    module = _register_module()
    with pytest.raises(ValueError):
        module.optimized_wrapper(*args)


def test_require_candidate_guard_raises_on_fallback(monkeypatch) -> None:
    """With KDA_REQUIRE_CANDIDATE=1, a signature that cannot take the native
    fast path raises instead of silently using the baseline."""

    module = _register_module()
    monkeypatch.setenv("KDA_REQUIRE_CANDIDATE", "1")
    # CPU tensors are never fast-path eligible (and not baseline-runnable either):
    # the guard must trip before any fallback.
    x = torch.randn(1, 8, 512, dtype=torch.bfloat16)
    weight = torch.randn(512, dtype=torch.bfloat16)
    scale = torch.randn(1, 1, 512, dtype=torch.bfloat16)
    shift = torch.randn(1, 8, 512, dtype=torch.bfloat16)
    with pytest.raises(RuntimeError, match="KDA_REQUIRE_CANDIDATE"):
        module.optimized_wrapper(x, weight, None, scale, shift, "rms", 1e-5)


def test_nan_injection_selftest() -> None:
    """The NaN/Inf validator must detect corrupted outputs."""

    t = torch.zeros(4, 4, device="cuda")
    t[1, 2] = float("nan")
    with pytest.raises(AssertionError, match="NaN"):
        _assert_no_nan_inf(t, path="selftest")
    t2 = torch.zeros(4, 4, device="cuda")
    t2[0, 0] = float("inf")
    with pytest.raises(AssertionError, match="Inf"):
        _assert_no_nan_inf(t2, path="selftest")


def test_wrong_eps_probe_detects_mismatch() -> None:
    """Oracle sensitivity self-test: comparing the baseline (eps=1e-5) against
    a deliberately wrong-eps reference must FAIL, proving the grid can detect
    real numerical deviations."""

    case = {
        "name": "probe__v1__wrong_eps",
        "variant": "v1",
        "B": 1,
        "S": 64,
        "D": 1024,
        "dtype": "bfloat16",
        "norm_type": "rms",
        "affine": "plain",
        "mode_scale": "11D",
        "mode_shift": "11D",
        "eps": _EPS,
        "atol": 5e-2,
        "rtol": 5e-2,
        "bench": False,
    }
    # Make x small in magnitude so eps dominates the rms denominator and the
    # wrong-eps reference deviates well beyond tolerance.
    t = _materialize(case)
    t["x"] = (torch.randn_like(t["x"].float()) * 1e-3).to(t["x"].dtype)
    base_out = baseline(case)
    wrong = dict(case, eps=1e-1)
    wrong["_tensors"] = t
    ref_wrong = reference(wrong)
    with pytest.raises(AssertionError):
        _assert_close(base_out, ref_wrong, case=case, path="probe-wrong-eps")
    _release(case)


def _edge_tensors(B=1, S=64, D=1024, dtype=torch.bfloat16, seed=123):
    gen = torch.Generator(device="cuda")
    gen.manual_seed(seed)

    def rand(shape, offset=0.0, sc=1.0):
        t = torch.randn(shape, generator=gen, device="cuda", dtype=torch.float32)
        return (t * sc + offset).to(dtype).contiguous()

    return {
        "x": rand((B, S, D)),
        "w": rand((D,), offset=1.0, sc=0.2),
        "b": rand((D,), sc=0.2),
        "w2": rand((D,), offset=1.0, sc=0.2),
        "scale": rand((1, 1, D)),
        "shift": rand((1, S, D)),
        "scale2": rand((1, 1, D)),
    }


def test_affine_edge_semantics() -> None:
    """Baseline applies layer affine only when BOTH weight and bias are
    tensors, and rms ignores bias entirely. Candidate must reproduce this for
    one-sided / extraneous affine arguments."""

    t = _edge_tensors()
    base_mod = _baseline_module()
    reg = _register_module()
    edge_cases = [
        ("layer_weight_only_degrades_to_plain", "layer", t["w"], None),
        ("layer_bias_only_degrades_to_plain", "layer", None, t["b"]),
        ("rms_bias_is_ignored", "rms", t["w"], t["b"]),
    ]
    for name, norm_type, w, b in edge_cases:
        ref_n = _norm_f32(t["x"].float(), w, b, norm_type, _EPS)
        ref_n = ref_n.to(t["x"].dtype).float()
        ref = (ref_n * torch.tanh(t["scale"].float()) + t["shift"].float()).to(t["x"].dtype)
        out_base = base_mod.fused_norm_tanh_mul_add(
            t["x"], w, b, t["scale"], t["shift"], norm_type, _EPS
        )
        out_cand = reg.optimized_wrapper(
            t["x"], w, b, t["scale"], t["shift"], norm_type, _EPS
        )
        torch.testing.assert_close(
            out_base.float(), ref.float(), atol=5e-2, rtol=5e-2,
            msg=lambda m, n=name: f"{n} baseline-vs-ref: {m}",
        )
        torch.testing.assert_close(
            out_cand.float(), out_base.float(), atol=5e-2, rtol=5e-2,
            msg=lambda m, n=name: f"{n} candidate-vs-baseline: {m}",
        )


def test_second_norm_affine_pattern_routing(monkeypatch) -> None:
    """v2 with MATCHING effective affine patterns is native-eligible; a
    differing pattern (public-valid) must fall back to the baseline without
    the guard and raise under KDA_REQUIRE_CANDIDATE=1."""

    t = _edge_tensors()
    base_mod = _baseline_module()
    reg = _register_module()

    args_match = (
        t["x"], t["w"], None, t["scale"], t["shift"], t["w2"], None, t["scale2"], "rms", _EPS,
    )
    out_base = base_mod.fused_norm_tanh_mul_add_norm_scale(*args_match)
    out_cand = reg.optimized_wrapper(*args_match)
    for i, (c, b) in enumerate(zip(out_cand, out_base)):
        torch.testing.assert_close(
            c.float(), b.float(), atol=5e-2, rtol=5e-2,
            msg=lambda m, j=i: f"match-pattern out[{j}]: {m}",
        )

    # weight present for norm1, absent for norm2: effective patterns differ.
    args_diff = (
        t["x"], t["w"], None, t["scale"], t["shift"], None, None, t["scale2"], "rms", _EPS,
    )
    out_base2 = base_mod.fused_norm_tanh_mul_add_norm_scale(*args_diff)
    out_cand2 = reg.optimized_wrapper(*args_diff)  # falls back, must match
    for i, (c, b) in enumerate(zip(out_cand2, out_base2)):
        torch.testing.assert_close(
            c.float(), b.float(), atol=5e-2, rtol=5e-2,
            msg=lambda m, j=i: f"diff-pattern out[{j}]: {m}",
        )
    monkeypatch.setenv("KDA_REQUIRE_CANDIDATE", "1")
    with pytest.raises(RuntimeError, match="KDA_REQUIRE_CANDIDATE"):
        reg.optimized_wrapper(*args_diff)


def test_fallback_valid_signatures(monkeypatch) -> None:
    """Public-valid but native-ineligible inputs: without the guard the
    candidate must behave exactly like the baseline (same outputs or the same
    exception type); with the guard it must raise RuntimeError."""

    B, S, D = 1, 32, 512
    t = _edge_tensors(B=B, S=S, D=D)
    base_mod = _baseline_module()
    reg = _register_module()

    arr = torch.randn(B * S * D + 4, device="cuda", dtype=torch.bfloat16)
    x_misaligned = arr[4:4 + B * S * D].view(B, S, D)  # base offset 8 bytes

    wide = torch.randn(1, S, D + 4, device="cuda", dtype=torch.bfloat16)
    scale_odd_stride = wide[:, :, :D]  # [1, S, D], seq stride D+4 (not 8-aligned)

    fallback_args = {
        "mixed_dtype_scale": (
            t["x"], t["w"], None, t["scale"].to(torch.float16), t["shift"], "rms", _EPS,
        ),
        "misaligned_x_base": (
            x_misaligned, t["w"], None, t["scale"], t["shift"], "rms", _EPS,
        ),
        "scale_outer_stride_unaligned": (
            t["x"], t["w"], None, scale_odd_stride, t["shift"], "rms", _EPS,
        ),
    }
    for name, args in fallback_args.items():
        base_exc, cand_exc = None, None
        out_base = out_cand = None
        try:
            out_base = base_mod.fused_norm_tanh_mul_add(*args)
        except Exception as exc:  # noqa: BLE001 - behavior comparison
            base_exc = type(exc)
        try:
            out_cand = reg.optimized_wrapper(*args)
        except Exception as exc:  # noqa: BLE001
            cand_exc = type(exc)
        assert (base_exc is None) == (cand_exc is None), (
            f"{name}: baseline {base_exc} vs candidate {cand_exc}"
        )
        if base_exc is not None:
            assert cand_exc is base_exc, f"{name}: exception type mismatch"
        else:
            torch.testing.assert_close(
                out_cand.float(), out_base.float(), atol=5e-2, rtol=5e-2,
                msg=lambda m, n=name: f"{n}: {m}",
            )
        monkeypatch.setenv("KDA_REQUIRE_CANDIDATE", "1")
        with pytest.raises(RuntimeError, match="KDA_REQUIRE_CANDIDATE"):
            reg.optimized_wrapper(*args)
        monkeypatch.delenv("KDA_REQUIRE_CANDIDATE")


def test_correctness_cases(monkeypatch) -> None:
    """Scaffold-compat entry point: candidate vs baseline on all cases."""

    test_candidate_matches_baseline_and_reference(monkeypatch)
