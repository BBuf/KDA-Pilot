"""Correctness harness for ``h200_diffusion_cutedsl_norm_tanh_mul_add__multi_shape``.

Oracle math (recovered from the pinned SGLang source, see docs/baseline_source.md):

    y  = norm(x) * tanh(scale) + shift          # fused_norm_tanh_mul_add
    y2 = norm2(y) * (1 + scale2)                # fused_norm_tanh_mul_add_norm_scale
                                                 # (no tanh on scale2)

where norm is fp32-reference ``torch.layer_norm`` / ``torch.rms_norm`` and the
dual-variant second norm consumes the dtype-quantized ``y`` (mirroring the
kernel dataflow, which stores ``y`` to the output dtype before re-normalizing).

Recovered public contract (validate_3d runs BEFORE broadcast normalization):
``scale``/``shift``/``scale2`` MUST be 3-D ``[1|B, 1|S, D]`` with unit stride
on D. 1-D/2-D/4-D layouts from the sister-family grid raise ValueError at this
pair's public boundary and are covered here as rejection-contract tests.

Case enumeration mirrors the live sister test structure at the pinned commit
(``python/sglang/jit_kernel/tests/diffusion/test_fused_norm_scale_shift.py``):
shape x dtype x norm blocks plus affine-mode and index-mode blocks on a default
shape — not a blind full product. Set ``KDA_EXHAUSTIVE=1`` for the full grid.

This file is intentionally skipped unless ``KDA_RUN_CORRECTNESS=1`` is set.
"""

from __future__ import annotations

import importlib.util
import os
import zlib
from pathlib import Path
from typing import Any

import pytest

try:
    import torch
except ImportError:  # pragma: no cover - CUDA env owns the real run
    torch = None


KERNEL_SLUG = "h200_diffusion_cutedsl_norm_tanh_mul_add__multi_shape"
OP_TYPE = "cutedsl_norm_tanh_mul_add"
KERNEL_DIR = Path(__file__).resolve().parents[1]

pytestmark = pytest.mark.skipif(
    os.environ.get("KDA_RUN_CORRECTNESS") != "1",
    reason="Set KDA_RUN_CORRECTNESS=1 to run the GPU correctness harness.",
)

# --- Live-recovered regression enumeration (sister test @ 0689ba84b) ---------
SHAPES = [
    # (B, S, F, D); x is always [B, S, D] — F only shapes the 4-D BF1D layout,
    # which this kernel pair rejects (3-D-only public contract).
    (1, 115200, 1, 3072),  # Hunyuan
    (1, 32760, 1, 1536),  # Wan
    (1, 6, 1, 3072),  # Qwen
    (1, 1024, 8, 3072),
    (4, 512, 16, 3072),
]
DEFAULT_SHAPE = (1, 1024, 8, 3072)
DTYPES = ["float16", "bfloat16", "float32"]
NORM_TYPES = ["layer", "rms"]
AFFINE_MODES = ["D", "NAT"]
# 3-D layouts accepted by this kernel pair's validate_3d:
VALID_INDEX_MODES = ["11D", "B1D", "1SD", "BSD"]
# Sister-family layouts rejected at this pair's public boundary:
REJECTED_INDEX_MODES = ["1", "D", "1D", "BD", "BF1D"]

SHAPE_MAP = {
    "1": lambda B, S, F, D: (1,),
    "D": lambda B, S, F, D: (D,),
    "1D": lambda B, S, F, D: (1, D),
    "BD": lambda B, S, F, D: (B, D),
    "11D": lambda B, S, F, D: (1, 1, D),
    "B1D": lambda B, S, F, D: (B, 1, D),
    "1SD": lambda B, S, F, D: (1, S, D),
    "BSD": lambda B, S, F, D: (B, S, D),
    "BF1D": lambda B, S, F, D: (B, F, 1, D),
}

# --- Captured production signatures (docs/captured_shapes_h200.jsonl) --------
PROD_SEQ_LENS = (4096, 4128)
PROD_D = 3840
PROD_DTYPE = "bfloat16"
PROD_NORM = "rms"
EPS = 1e-5


def _tol(dtype_name: str) -> float:
    return 1e-5 if dtype_name == "float32" else 5e-2


def _torch_dtype(name: str):
    return getattr(torch, name)


def _load_register_module():
    register_py = KERNEL_DIR / "src" / "register.py"
    spec = importlib.util.spec_from_file_location(
        f"kda_kernel_{KERNEL_SLUG}_register", register_py
    )
    assert spec is not None and spec.loader is not None, register_py
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _load_baseline_module():
    import sys

    kdir = str(KERNEL_DIR)
    if kdir not in sys.path:
        sys.path.insert(0, kdir)
    import baseline as vendored_baseline

    return vendored_baseline


# --- Case construction --------------------------------------------------------


def _case(
    *,
    entry: str,
    B: int,
    S: int,
    F: int,
    D: int,
    dtype: str,
    norm_type: str,
    affine_mode: str = "D",
    scale_mode: str = "11D",
    shift_mode: str = "BSD",
    kind: str = "regression",
    bench: bool = False,
) -> dict[str, Any]:
    name = (
        f"{kind}__{entry}__B{B}S{S}F{F}D{D}__{dtype}__{norm_type}"
        f"__aff{affine_mode}__sc{scale_mode}__sh{shift_mode}"
    )
    return {
        "name": name,
        "entry": entry,  # "single" | "dual"
        "B": B,
        "S": S,
        "F": F,
        "D": D,
        "dtype": dtype,
        "norm_type": norm_type,
        "affine_mode": affine_mode,
        "scale_mode": scale_mode,
        "shift_mode": shift_mode,
        "eps": EPS,
        "atol": _tol(dtype),
        "rtol": _tol(dtype),
        "kind": kind,
        "bench": bench,
        "warmup": 25,
        "iters": 100,
        "seed": zlib.crc32(name.encode()) & 0x7FFFFFFF,
    }


def make_cases() -> list[dict[str, Any]]:
    """All configured correctness cases. Benchmark uses only ``bench=True`` ones."""

    cases: list[dict[str, Any]] = []

    # Production: the 4 captured signatures, verbatim.
    for entry in ("single", "dual"):
        for seq_len in PROD_SEQ_LENS:
            cases.append(
                _case(
                    entry=entry,
                    B=1,
                    S=seq_len,
                    F=1,
                    D=PROD_D,
                    dtype=PROD_DTYPE,
                    norm_type=PROD_NORM,
                    affine_mode="D",
                    scale_mode="11D",
                    shift_mode="BSD",
                    kind="production",
                    bench=True,
                )
            )

    exhaustive = os.environ.get("KDA_EXHAUSTIVE") == "1"
    db, ds, df, dd = DEFAULT_SHAPE

    if exhaustive:
        for (B, S, F, D) in SHAPES:
            for dtype in DTYPES:
                for norm_type in NORM_TYPES:
                    for affine_mode in AFFINE_MODES:
                        for mode in VALID_INDEX_MODES:
                            for entry in ("single", "dual"):
                                cases.append(
                                    _case(
                                        entry=entry,
                                        B=B,
                                        S=S,
                                        F=F,
                                        D=D,
                                        dtype=dtype,
                                        norm_type=norm_type,
                                        affine_mode=affine_mode,
                                        scale_mode=mode,
                                        shift_mode="BSD",
                                    )
                                )
    else:
        # Block A (sister structure): shape x dtype x norm, default modes.
        for (B, S, F, D) in SHAPES:
            for dtype in DTYPES:
                for norm_type in NORM_TYPES:
                    for entry in ("single", "dual"):
                        cases.append(
                            _case(
                                entry=entry,
                                B=B,
                                S=S,
                                F=F,
                                D=D,
                                dtype=dtype,
                                norm_type=norm_type,
                            )
                        )
        # Block B: affine NAT (weight/bias None) on the default shape.
        for norm_type in NORM_TYPES:
            for entry in ("single", "dual"):
                cases.append(
                    _case(
                        entry=entry,
                        B=db,
                        S=ds,
                        F=df,
                        D=dd,
                        dtype="bfloat16",
                        norm_type=norm_type,
                        affine_mode="NAT",
                    )
                )
        # Block C1: valid scale layouts (shift fixed BSD) on the default shape.
        for mode in VALID_INDEX_MODES:
            for norm_type in NORM_TYPES:
                for entry in ("single", "dual"):
                    cases.append(
                        _case(
                            entry=entry,
                            B=db,
                            S=ds,
                            F=df,
                            D=dd,
                            dtype="bfloat16",
                            norm_type=norm_type,
                            scale_mode=mode,
                        )
                    )
        # Block C2: valid shift layouts (scale fixed 11D) on the default shape.
        for mode in ("11D", "B1D", "1SD"):
            for norm_type in NORM_TYPES:
                for entry in ("single", "dual"):
                    cases.append(
                        _case(
                            entry=entry,
                            B=db,
                            S=ds,
                            F=df,
                            D=dd,
                            dtype="bfloat16",
                            norm_type=norm_type,
                            shift_mode=mode,
                        )
                    )

    # Small shapes first: fail fast, and keep peak memory low early.
    cases.sort(key=lambda c: (c["kind"] != "production", c["B"] * c["S"] * c["D"]))
    return cases


def _ensure_tensors(case: dict[str, Any]) -> tuple:
    """Build (and cache) the input tensors for a case on the current CUDA device.

    Cached so that baseline/candidate/benchmark all see the SAME inputs and the
    timed region never includes tensor construction.
    """

    if "_args" in case:
        return case["_args"]
    assert torch is not None and torch.cuda.is_available()
    B, S, F, D = case["B"], case["S"], case["F"], case["D"]
    dtype = _torch_dtype(case["dtype"])
    gen = torch.Generator(device="cuda").manual_seed(case["seed"])

    def randn(shape):
        return torch.randn(shape, generator=gen, device="cuda", dtype=dtype)

    def by_mode(mode):
        return randn(SHAPE_MAP[mode](B, S, F, D))

    x = by_mode("BSD")
    if case["affine_mode"] == "NAT":
        weight = bias = None
    else:
        weight = randn((D,))
        bias = randn((D,))
    scale = by_mode(case["scale_mode"])
    shift = by_mode(case["shift_mode"])
    if case["entry"] == "single":
        args = (x, weight, bias, scale, shift, case["norm_type"], case["eps"])
    else:
        if case["affine_mode"] == "NAT":
            weight2 = bias2 = None
        else:
            weight2 = randn((D,))
            bias2 = randn((D,))
        scale2 = by_mode(case["scale_mode"])
        args = (
            x,
            weight,
            bias,
            scale,
            shift,
            weight2,
            bias2,
            scale2,
            case["norm_type"],
            case["eps"],
        )
    case["_args"] = args
    return args


def _free_tensors(case: dict[str, Any]) -> None:
    case.pop("_args", None)
    case.pop("_ref", None)


# --- Entry points -------------------------------------------------------------


def baseline(case: dict[str, Any]) -> Any:
    """Vendored pinned SGLang baseline (the semantic oracle's device twin)."""

    mod = _load_baseline_module()
    args = _ensure_tensors(case)
    if case["entry"] == "single":
        return mod.fused_norm_tanh_mul_add(*args)
    return mod.fused_norm_tanh_mul_add_norm_scale(*args)


def candidate(case: dict[str, Any]) -> Any:
    """Candidate via src/register.py. The wrapper dispatches on arity:
    7 args -> single-norm entry, 10 args -> dual-norm entry (same as the
    public SGLang signatures)."""

    module = _load_register_module()
    wrapper = getattr(module, "optimized_wrapper")
    args = _ensure_tensors(case)
    return wrapper(*args)


def _candidate_available() -> bool:
    try:
        module = _load_register_module()
        return bool(getattr(module, "CANDIDATE_READY", False))
    except Exception:
        return False


# --- FP32 reference oracle ------------------------------------------------------


def _norm_fp32(x32, weight, bias, norm_type: str, eps: float):
    w32 = weight.float() if weight is not None else None
    b32 = bias.float() if bias is not None else None
    if norm_type == "layer":
        return torch.layer_norm(x32, x32.shape[-1:], weight=w32, bias=b32, eps=eps)
    return torch.rms_norm(x32, x32.shape[-1:], weight=w32, eps=eps)


def reference(case: dict[str, Any]) -> Any:
    """FP32 oracle. Dual variant feeds the dtype-quantized y into the second
    norm to mirror the kernel dataflow."""

    if "_ref" in case:
        return case["_ref"]
    args = _ensure_tensors(case)
    dtype = _torch_dtype(case["dtype"])
    if case["entry"] == "single":
        x, weight, bias, scale, shift, norm_type, eps = args
        y32 = _norm_fp32(x.float(), weight, bias, norm_type, eps) * torch.tanh(
            scale.float()
        ) + shift.float()
        case["_ref"] = y32
        return y32
    x, weight, bias, scale, shift, weight2, bias2, scale2, norm_type, eps = args
    y32 = _norm_fp32(x.float(), weight, bias, norm_type, eps) * torch.tanh(
        scale.float()
    ) + shift.float()
    y_quant = y32.to(dtype)
    y2_32 = _norm_fp32(y_quant.float(), weight2, bias2, norm_type, eps) * (
        1 + scale2.float()
    )
    case["_ref"] = (y32, y2_32)
    return case["_ref"]


# --- Assertion helpers ----------------------------------------------------------


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


def _assert_dynamic_tolerance(cand: Any, base: Any, ref: Any, *, path: str = "out") -> None:
    """SGLang-style dynamic bound: candidate error vs the fp32 reference must
    not exceed a small multiple of the baseline's own quantization error."""

    if isinstance(cand, (tuple, list)):
        for i, (c, b, r) in enumerate(zip(cand, base, ref)):
            _assert_dynamic_tolerance(c, b, r, path=f"{path}[{i}]")
        return
    err_c = (cand.float() - ref).abs().max().item()
    err_b = (base.float() - ref).abs().max().item()
    bound = 2.0 * err_b + 1e-6
    assert err_c <= bound, (
        f"{path}: candidate max-err {err_c:.6e} exceeds dynamic bound {bound:.6e} "
        f"(baseline max-err {err_b:.6e})"
    )


# --- Tests ----------------------------------------------------------------------


def test_register_metadata() -> None:
    module = _load_register_module()
    assert hasattr(module, "register")
    spec = module.register()
    assert spec["name"] == KERNEL_SLUG
    assert spec["op_type"] == OP_TYPE
    assert callable(spec["callable"])


def test_baseline_matches_oracle() -> None:
    """AC: vendored baseline passes the tanh-math fp32 oracle on every case."""

    cases = make_cases()
    assert cases, "No correctness cases recovered."
    for i, case in enumerate(cases):
        base = baseline(case)
        ref = reference(case)
        _assert_close(base, ref, case=case, path=case["name"])
        _free_tensors(case)
        if i % 16 == 15:
            torch.cuda.empty_cache()


def test_candidate_cases() -> None:
    """AC: candidate passes oracle + dynamic bound; fallback equals baseline."""

    if not _candidate_available():
        pytest.skip("candidate not implemented yet (src/register.py stub)")
    cases = make_cases()
    for i, case in enumerate(cases):
        base = baseline(case)
        cand = candidate(case)
        ref = reference(case)
        _assert_close(cand, ref, case=case, path=case["name"])
        _assert_dynamic_tolerance(cand, base, ref, path=case["name"])
        _free_tensors(case)
        if i % 16 == 15:
            torch.cuda.empty_cache()


def test_rejected_layouts_raise() -> None:
    """Recovered contract: non-3-D scale/shift layouts raise ValueError."""

    mod = _load_baseline_module()
    B, S, F, D = DEFAULT_SHAPE
    dtype = _torch_dtype("bfloat16")
    x = torch.randn(B, S, D, device="cuda", dtype=dtype)
    shift = torch.randn(B, S, D, device="cuda", dtype=dtype)
    for mode in REJECTED_INDEX_MODES:
        bad = torch.randn(SHAPE_MAP[mode](B, S, F, D), device="cuda", dtype=dtype)
        with pytest.raises(ValueError):
            mod.fused_norm_tanh_mul_add(x, None, None, bad, shift, "rms", EPS)
    if _candidate_available():
        module = _load_register_module()
        for mode in REJECTED_INDEX_MODES:
            bad = torch.randn(SHAPE_MAP[mode](B, S, F, D), device="cuda", dtype=dtype)
            with pytest.raises(ValueError):
                module.optimized_wrapper(x, None, None, bad, shift, "rms", EPS)


def test_out_of_domain_d_raises() -> None:
    """D % 256 != 0 or D > 8192 must raise, never silently compute."""

    mod = _load_baseline_module()
    dtype = _torch_dtype("bfloat16")
    for bad_d in (3848, 8448):
        x = torch.randn(1, 8, bad_d, device="cuda", dtype=dtype)
        sc = torch.randn(1, 1, bad_d, device="cuda", dtype=dtype)
        sh = torch.randn(1, 8, bad_d, device="cuda", dtype=dtype)
        with pytest.raises(ValueError):
            mod.fused_norm_tanh_mul_add(x, None, None, sc, sh, "rms", EPS)
        if _candidate_available():
            module = _load_register_module()
            with pytest.raises(ValueError):
                module.optimized_wrapper(x, None, None, sc, sh, "rms", EPS)


def test_nan_input_is_flagged() -> None:
    """The output validator must flag NaN-contaminated runs, not pass them."""

    case = _case(
        entry="single",
        B=1,
        S=64,
        F=1,
        D=3072,
        dtype="bfloat16",
        norm_type="rms",
    )
    args = list(_ensure_tensors(case))
    args[0][0, 0, 0] = float("nan")
    mod = _load_baseline_module()
    out = mod.fused_norm_tanh_mul_add(*args)
    with pytest.raises(AssertionError, match="NaN"):
        _assert_no_nan_inf(out, path="nan-probe")
    _free_tensors(case)


def test_harness_detects_wrong_math() -> None:
    """Sensitivity guard: tolerances must reject (1+scale) math and tanh(scale2)."""

    case = _case(
        entry="single", B=1, S=256, F=1, D=3072, dtype="bfloat16", norm_type="rms"
    )
    args = _ensure_tensors(case)
    x, weight, bias, scale, shift, norm_type, eps = args
    base = baseline(case)
    wrong = _norm_fp32(x.float(), weight, bias, norm_type, eps) * (
        1 + scale.float()
    ) + shift.float()
    with pytest.raises(AssertionError):
        _assert_close(base, wrong, case=case, path="wrong-single-math")
    _free_tensors(case)

    case2 = _case(
        entry="dual", B=1, S=256, F=1, D=3072, dtype="bfloat16", norm_type="rms"
    )
    args2 = _ensure_tensors(case2)
    (x, weight, bias, scale, shift, weight2, bias2, scale2, norm_type, eps) = args2
    base2 = baseline(case2)
    y32 = _norm_fp32(x.float(), weight, bias, norm_type, eps) * torch.tanh(
        scale.float()
    ) + shift.float()
    wrong_y2 = _norm_fp32(
        y32.to(_torch_dtype(case2["dtype"])).float(), weight2, bias2, norm_type, eps
    ) * torch.tanh(scale2.float())
    with pytest.raises(AssertionError):
        _assert_close(base2, (y32, wrong_y2), case=case2, path="wrong-dual-math")
    _free_tensors(case2)
