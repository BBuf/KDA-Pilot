"""Correctness harness for ``h200_diffusion_cutedsl_norm_tanh_mul_add__multi_shape``.

Oracle math (recovered from the pinned SGLang source, see docs/baseline_source.md):

    y  = norm(x) * tanh(scale) + shift          # fused_norm_tanh_mul_add
    y2 = norm2(y) * (1 + scale2)                # fused_norm_tanh_mul_add_norm_scale
                                                 # (no tanh on scale2)

where norm is fp32-reference ``torch.layer_norm`` / ``torch.rms_norm``.
Verification is compositional: ``y`` is checked against the pure stage-1
oracle (with the kernel's storage-dtype boundary at the norm output mirrored,
and a backward-error model for the cancelling epilogue add); the dual
variant's ``y2`` is checked against ``norm2(actual_y) * (1 + scale2)`` so
stage-2 math is verified without inheriting stage-1's gain-amplified rounding.
See ``reference_y`` / ``reference_y2_given`` / ``_assert_close_modeled``.

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
# "D": weight+bias tensors; "W": weight only, bias=None (the captured
# production RMS signature); "NAT": both None.
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


_REGISTER_MODULE = None


def _load_register_module():
    """Load src/register.py ONCE per process (module-level cache), mirroring
    the vendored baseline's sys.modules caching — otherwise the candidate
    side pays an artificial per-call import tax in timed loops."""

    global _REGISTER_MODULE
    if _REGISTER_MODULE is not None:
        return _REGISTER_MODULE
    register_py = KERNEL_DIR / "src" / "register.py"
    spec = importlib.util.spec_from_file_location(
        f"kda_kernel_{KERNEL_SLUG}_register", register_py
    )
    assert spec is not None and spec.loader is not None, register_py
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    _REGISTER_MODULE = module
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

    # Production: the 4 captured signatures, verbatim. The captured RMS calls
    # have weight=[D] but bias=None (arg2/arg6 are None) — affine mode "W".
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
                    affine_mode="W",
                    scale_mode="11D",
                    shift_mode="BSD",
                    kind="production",
                    bench=True,
                )
            )

    exhaustive = os.environ.get("KDA_EXHAUSTIVE") == "1"
    db, ds, df, dd = DEFAULT_SHAPE

    if exhaustive:
        # Every accepted scale layout (x shift=BSD) AND every accepted shift
        # layout (x scale=11D) across the full recovered axes, so each valid
        # 3-D layout is exercised in both operand positions on every
        # shape/dtype/norm/affine/entry combination.
        layout_pairs = [(m, "BSD") for m in VALID_INDEX_MODES] + [
            ("11D", m) for m in VALID_INDEX_MODES if m != "BSD"
        ]
        for (B, S, F, D) in SHAPES:
            for dtype in DTYPES:
                for norm_type in NORM_TYPES:
                    for affine_mode in AFFINE_MODES:
                        for scale_mode, shift_mode in layout_pairs:
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
                                        scale_mode=scale_mode,
                                        shift_mode=shift_mode,
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
    affine = case["affine_mode"]
    if affine == "NAT":
        weight = bias = None
    elif affine == "W":
        weight, bias = randn((D,)), None
    else:
        weight = randn((D,))
        bias = randn((D,))
    scale = by_mode(case["scale_mode"])
    shift = by_mode(case["shift_mode"])
    if case["entry"] == "single":
        args = (x, weight, bias, scale, shift, case["norm_type"], case["eps"])
    else:
        if affine == "NAT":
            weight2 = bias2 = None
        elif affine == "W":
            weight2, bias2 = randn((D,)), None
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
    case.pop("_err_scale", None)


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
    """True when the promoted candidate is wired in.

    Only the INTENTIONAL stub state (``CANDIDATE_READY = False`` in
    ``src/register.py``) may skip the candidate tests. Import/JIT/registration
    errors while loading a READY candidate must PROPAGATE and fail the suite —
    swallowing them here would report a broken promoted fast path as harmless
    skips (review finding, round 5)."""

    module = _load_register_module()
    return bool(getattr(module, "CANDIDATE_READY", False))


# --- FP32 reference oracle ------------------------------------------------------


def _norm_fp32(x32, weight, bias, norm_type: str, eps: float):
    w32 = weight.float() if weight is not None else None
    b32 = bias.float() if bias is not None else None
    if norm_type == "layer":
        return torch.layer_norm(x32, x32.shape[-1:], weight=w32, bias=b32, eps=eps)
    return torch.rms_norm(x32, x32.shape[-1:], weight=w32, eps=eps)


def _norm_quantized(t32, w, b, norm_type: str, eps: float, dtype):
    # Kernel boundary: the norm output (incl. weight/bias) is stored to the
    # element dtype in registers before the epilogue uses it.
    return _norm_fp32(t32, w, b, norm_type, eps).to(dtype).float()


def reference_y(case: dict[str, Any]) -> Any:
    """Pure FP32 oracle for the first stage: ``y = norm(x)*tanh(scale)+shift``.

    Mirrors only the kernel's storage-dtype boundary at the norm output (a
    no-op for fp32); all arithmetic stays fp32. Also stashes the epilogue-add
    error scale ``|n*tanh(scale)| + |shift|``: where the add cancels, dtype
    term-rounding leaves an absolute residue proportional to the TERM
    magnitude, not the result (observed: 1/15.7M bf16 elements at 0.0565 vs
    the 0.05 static bound, ion8-h200 run1).
    """

    if "_ref" in case:
        return case["_ref"]
    args = _ensure_tensors(case)
    dtype = _torch_dtype(case["dtype"])
    x, weight, bias, scale, shift = args[0], args[1], args[2], args[3], args[4]
    norm_type, eps = case["norm_type"], case["eps"]
    n_q = _norm_quantized(x.float(), weight, bias, norm_type, eps, dtype)
    t = n_q * torch.tanh(scale.float())
    y32 = t + shift.float()
    case["_err_scale"] = t.abs() + shift.float().abs()
    case["_ref"] = y32
    return y32


def reference_y2_given(case: dict[str, Any], y_actual) -> tuple:
    """Compositional stage-2 oracle: ``y2 = norm2(y_actual) * (1 + scale2)``.

    The dual kernel re-norms its own (dtype-quantized) ``y``; a y2 reference
    computed from the pure-oracle y would inherit y's legitimate rounding
    AMPLIFIED by the second norm's per-channel gain ``factor2*w2*(1+scale2)``
    (observed: 35/354M bf16 elements at the max-|gain| channel, ion8-h200
    run2/run3). Verifying stage 2 against the implementation's ACTUAL y
    isolates stage-2 math; combined with the stage-1 oracle check on y this
    composes to end-to-end correctness. Returns ``(y2_ref32, err_scale)``.
    """

    args = _ensure_tensors(case)
    dtype = _torch_dtype(case["dtype"])
    weight2, bias2, scale2 = args[5], args[6], args[7]
    norm_type, eps = case["norm_type"], case["eps"]
    n2_q = _norm_quantized(y_actual.float(), weight2, bias2, norm_type, eps, dtype)
    s2 = 1 + scale2.float()
    y2_32 = n2_q * s2
    return y2_32, y2_32.abs()


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


def _assert_close_modeled(
    actual: Any,
    expected: Any,
    err_scale: Any,
    *,
    case: dict[str, Any],
    path: str = "out",
) -> None:
    """Oracle comparison with a backward-error model.

    Per element: ``|a - e| <= atol + rtol * max(|e|, err_scale)`` where
    ``err_scale`` is the magnitude of the epilogue operands (``|n*tanh(scale)|
    + |shift|`` for y; ``|n2*(1+scale2)|`` for y2). For the bulk of elements
    ``err_scale ~ |e|`` and this is exactly assert_close; it only widens where
    the epilogue add cancels, where dtype term-rounding leaves an absolute
    residue proportional to the term magnitude (observed: 35/354M bf16
    elements at the largest-|weight| channel, ion8-h200 run2). The 5e-2/1e-5
    coefficients are the task's hard tolerance contract.
    """

    if isinstance(actual, (tuple, list)):
        for i, (a_item, e_item, s_item) in enumerate(zip(actual, expected, err_scale)):
            _assert_close_modeled(a_item, e_item, s_item, case=case, path=f"{path}[{i}]")
        return
    atol = case.get("atol", 5e-2)
    rtol = case.get("rtol", 5e-2)
    _assert_no_nan_inf(actual, path=path)
    assert actual.shape == expected.shape, f"{path} shape {actual.shape} != {expected.shape}"
    a32 = actual.float()
    diff = (a32 - expected).abs()
    tol = atol + rtol * torch.maximum(expected.abs(), err_scale)
    violations = diff > tol
    if violations.any():
        worst = (diff - tol).argmax()
        idx = tuple(int(v) for v in torch.unravel_index(worst, diff.shape))
        raise AssertionError(
            f"{path}: {int(violations.sum())}/{diff.numel()} elements exceed the "
            f"modeled tolerance; worst at {idx}: |a-e|={diff[idx].item():.6e} > "
            f"tol={tol[idx].item():.6e} (e={expected[idx].item():.6e}, "
            f"err_scale={err_scale[idx].item():.6e}, atol={atol}, rtol={rtol})"
        )


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


def _assert_dynamic_tolerance_stage2(
    cand_pair, base_pair, *, case: dict[str, Any], path: str = "out"
) -> None:
    """Dynamic bound for the dual op's second output, consistent with the
    compositional oracle: each side's y2 is measured against the stage-2
    reference computed from ITS OWN y, and the candidate's stage-2 noise must
    not exceed a small multiple of the baseline's stage-2 noise."""

    ref2_c, _ = reference_y2_given(case, cand_pair[0])
    ref2_b, _ = reference_y2_given(case, base_pair[0])
    err_c = (cand_pair[1].float() - ref2_c).abs().max().item()
    err_b = (base_pair[1].float() - ref2_b).abs().max().item()
    bound = 2.0 * err_b + 1e-6
    assert err_c <= bound, (
        f"{path}[y2]: candidate stage-2 max-err {err_c:.6e} exceeds dynamic bound "
        f"{bound:.6e} (baseline stage-2 max-err {err_b:.6e})"
    )


# --- Tests ----------------------------------------------------------------------


def test_register_metadata() -> None:
    module = _load_register_module()
    assert hasattr(module, "register")
    spec = module.register()
    assert spec["name"] == KERNEL_SLUG
    assert spec["op_type"] == OP_TYPE
    assert callable(spec["callable"])


def _check_against_oracle(out: Any, case: dict[str, Any]) -> None:
    """Stage-1 y vs the pure oracle; dual y2 vs the compositional stage-2 oracle."""

    if case["entry"] == "single":
        ref_y = reference_y(case)
        _assert_close_modeled(out, ref_y, case["_err_scale"], case=case, path=case["name"])
        return
    y_out, y2_out = out
    ref_y = reference_y(case)
    _assert_close_modeled(
        y_out, ref_y, case["_err_scale"], case=case, path=f"{case['name']}[y]"
    )
    ref_y2, err_scale2 = reference_y2_given(case, y_out)
    _assert_close_modeled(
        y2_out, ref_y2, err_scale2, case=case, path=f"{case['name']}[y2]"
    )


def test_baseline_matches_oracle() -> None:
    """AC: vendored baseline passes the tanh-math fp32 oracle on every case."""

    cases = make_cases()
    assert cases, "No correctness cases recovered."
    for i, case in enumerate(cases):
        base = baseline(case)
        _check_against_oracle(base, case)
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
        _check_against_oracle(cand, case)
        # Dynamic bound vs the baseline's own quantization noise: stage-1 y
        # against the pure oracle; dual y2 against the stage-2 reference of
        # each side's own y (compositional, see _assert_dynamic_tolerance_stage2).
        ref_y = reference_y(case)
        if case["entry"] == "single":
            _assert_dynamic_tolerance(cand, base, ref_y, path=case["name"])
        else:
            _assert_dynamic_tolerance(cand[0], base[0], ref_y, path=f"{case['name']}[y]")
            _assert_dynamic_tolerance_stage2(cand, base, case=case, path=case["name"])
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


def _prod_family_args(*, S: int = 128, dual: bool = False, with_eps: bool = True):
    """Production-family tensors (bf16/rms/D=3840/weight-only/scale 11D/shift
    full) at an arbitrary row count, as a plain args tuple."""

    D = PROD_D
    dt = _torch_dtype(PROD_DTYPE)
    x = torch.randn(1, S, D, device="cuda", dtype=dt)
    w = torch.randn(D, device="cuda", dtype=dt)
    sc = torch.randn(1, 1, D, device="cuda", dtype=dt)
    sh = torch.randn(1, S, D, device="cuda", dtype=dt)
    args = [x, w, None, sc, sh]
    if dual:
        args += [torch.randn(D, device="cuda", dtype=dt), None,
                 torch.randn(1, 1, D, device="cuda", dtype=dt)]
    args.append(PROD_NORM)
    if with_eps:
        args.append(EPS)
    return tuple(args)


def test_dispatch_branch_contract() -> None:
    """AC: the CUDA fast path engages for exactly the production signature
    family; every other gate falls back. Uses the wrapper's own
    dispatch_decision (the same predicate optimized_wrapper consumes)."""

    if not _candidate_available():
        pytest.skip("candidate not implemented yet (src/register.py stub)")
    module = _load_register_module()
    decide = module.dispatch_decision

    # Fast dispatch: the 4 captured signatures (exact case tensors).
    for case in [c for c in make_cases() if c["kind"] == "production"]:
        args = _ensure_tensors(case)
        expected = "fast_single" if case["entry"] == "single" else "fast_dual"
        assert decide(*args) == expected, case["name"]
        _free_tensors(case)
    # Same-family row-count probe (any B*S is in scope per the plan).
    assert decide(*_prod_family_args(S=128)) == "fast_single"
    assert decide(*_prod_family_args(S=128, dual=True)) == "fast_dual"
    # Default-eps positional arities stay on the fast path.
    assert decide(*_prod_family_args(S=64, with_eps=False)) == "fast_single"
    assert decide(*_prod_family_args(S=64, dual=True, with_eps=False)) == "fast_dual"

    # Fallback gates: one mutation per probe.
    D = PROD_D
    dt = _torch_dtype(PROD_DTYPE)
    base = _prod_family_args(S=32)
    x, w, _b, sc, sh, _n, _e = base

    def swapped(**kw):
        d = dict(x=x, weight=w, bias=None, scale=sc, shift=sh, norm="rms", eps=EPS)
        d.update(kw)
        return (d["x"], d["weight"], d["bias"], d["scale"], d["shift"], d["norm"], d["eps"])

    assert decide(*swapped(x=x.float(), scale=sc.float(), shift=sh.float(), weight=w.float())) == "fallback_single"  # dtype
    assert decide(*swapped(norm="layer")) == "fallback_single"  # norm type
    bad_d = torch.randn(1, 32, 3072, device="cuda", dtype=dt)
    assert decide(bad_d, torch.randn(3072, device="cuda", dtype=dt), None,
                  torch.randn(1, 1, 3072, device="cuda", dtype=dt), bad_d.clone(),
                  "rms", EPS) == "fallback_single"  # D != 3840
    assert decide(*swapped(bias=torch.randn(D, device="cuda", dtype=dt))) == "fallback_single"  # bias present
    assert decide(*swapped(weight=None)) == "fallback_single"  # weight absent
    assert decide(*swapped(scale=torch.randn(1, 32, D, device="cuda", dtype=dt))) == "fallback_single"  # scale 1SD
    assert decide(*swapped(shift=torch.randn(1, 1, D, device="cuda", dtype=dt))) == "fallback_single"  # shift 11D
    cpu = tuple(t.cpu() if isinstance(t, torch.Tensor) else t for t in base)
    assert decide(*cpu) == "fallback_single"  # CPU tensors
    # Dual-only gates.
    dual = _prod_family_args(S=32, dual=True)
    (dx, dw, _db, dsc, dsh, dw2, _db2, dsc2, dn, de) = dual
    assert decide(dx, dw, None, dsc, dsh, dw2, torch.randn(D, device="cuda", dtype=dt),
                  dsc2, dn, de) == "fallback_dual"  # bias2 present
    assert decide(dx, dw, None, dsc, dsh, dw2, None,
                  torch.randn(1, 32, D, device="cuda", dtype=dt), dn, de) == "fallback_dual"  # scale2 1SD
    # Keyword-style call routes to the baseline.
    assert decide(x, w, None, sc, sh, "rms", eps=EPS) == "fallback_single"


def test_default_eps_contract() -> None:
    """Blocking fix: 6-arg single and 9-arg dual calls (eps defaulting to
    1e-5) must compute identically to their explicit-eps forms, on both the
    fast path and the fallback path."""

    if not _candidate_available():
        pytest.skip("candidate not implemented yet (src/register.py stub)")
    module = _load_register_module()
    torch.manual_seed(20260604)

    # Fast path: production-family single, 6 args vs 7 args.
    args7 = _prod_family_args(S=96)
    out_default = module.optimized_wrapper(*args7[:-1])
    out_explicit = module.optimized_wrapper(*args7)
    assert torch.equal(out_default, out_explicit)
    base = _load_baseline_module().fused_norm_tanh_mul_add(*args7[:-1])
    assert torch.isfinite(out_default.float()).all()
    assert out_default.shape == base.shape

    # Fast path: dual, 9 args vs 10 args.
    argsd = _prod_family_args(S=96, dual=True)
    y_d, y2_d = module.optimized_wrapper(*argsd[:-1])
    y_e, y2_e = module.optimized_wrapper(*argsd)
    assert torch.equal(y_d, y_e) and torch.equal(y2_d, y2_e)

    # Fallback path (fp32): default-eps must route to baseline and match it.
    D = PROD_D
    xf = torch.randn(1, 64, D, device="cuda", dtype=torch.float32)
    wf = torch.randn(D, device="cuda", dtype=torch.float32)
    scf = torch.randn(1, 1, D, device="cuda", dtype=torch.float32)
    shf = torch.randn(1, 64, D, device="cuda", dtype=torch.float32)
    out_fb = module.optimized_wrapper(xf, wf, None, scf, shf, "rms")
    out_bl = _load_baseline_module().fused_norm_tanh_mul_add(xf, wf, None, scf, shf, "rms")
    assert torch.equal(out_fb, out_bl)

    # Wrong arity surfaces the BASELINE's own contract error (torch custom
    # ops raise RuntimeError for missing arguments; plain TypeError also
    # acceptable) — the wrapper must not mask or replace it.
    with pytest.raises((TypeError, RuntimeError)):
        _load_baseline_module().fused_norm_tanh_mul_add(xf, wf, None, scf, shf)
    with pytest.raises((TypeError, RuntimeError)):
        module.optimized_wrapper(xf, wf, None, scf, shf)


def test_misaligned_view_falls_back() -> None:
    """A contiguous-but-misaligned view (offset slice) must NOT take the
    128-bit-vector fast path (task8 review required change)."""

    if not _candidate_available():
        pytest.skip("candidate not implemented yet (src/register.py stub)")
    module = _load_register_module()
    D = PROD_D
    dt = _torch_dtype(PROD_DTYPE)
    # Slice a fresh (256B-aligned) buffer at element offset 4: 4 elems * 2B =
    # 8 bytes — contiguous but NOT 16-byte aligned for 128-bit vectors.
    buf = torch.randn(4 + 32 * D, device="cuda", dtype=dt)
    x_mis = buf[4 : 4 + 32 * D].view(1, 32, D)
    assert x_mis.is_contiguous() and x_mis.data_ptr() % 16 != 0
    w = torch.randn(D, device="cuda", dtype=dt)
    sc = torch.randn(1, 1, D, device="cuda", dtype=dt)
    sh = torch.randn(1, 32, D, device="cuda", dtype=dt)
    assert module.dispatch_decision(x_mis, w, None, sc, sh, "rms", EPS) == "fallback_single"
    # The vendored baseline itself REJECTS misaligned tensors (CuTe-DSL
    # from_dlpack assumed_align=32), so the fallback must surface the same
    # error rather than silently computing on the misaligned fast path.
    with pytest.raises(Exception) as base_err:
        _load_baseline_module().fused_norm_tanh_mul_add(x_mis, w, None, sc, sh, "rms", EPS)
    with pytest.raises(Exception) as cand_err:
        module.optimized_wrapper(x_mis, w, None, sc, sh, "rms", EPS)
    assert type(cand_err.value) is type(base_err.value), (
        f"fallback error {type(cand_err.value)} != baseline error {type(base_err.value)}"
    )


def test_fast_path_non_default_eps() -> None:
    """Fast path must honor a non-default eps numerically (task8 optional)."""

    if not _candidate_available():
        pytest.skip("candidate not implemented yet (src/register.py stub)")
    case = _case(
        entry="dual",
        B=1,
        S=96,
        F=1,
        D=PROD_D,
        dtype=PROD_DTYPE,
        norm_type=PROD_NORM,
        affine_mode="W",
        scale_mode="11D",
        shift_mode="BSD",
    )
    case["eps"] = 3e-4  # rebuilds args + oracle with the overridden eps
    base = baseline(case)
    cand = candidate(case)
    _check_against_oracle(cand, case)
    ref_y = reference_y(case)
    _assert_dynamic_tolerance(cand[0], base[0], ref_y, path="non-default-eps[y]")
    _assert_dynamic_tolerance_stage2(cand, base, case=case, path="non-default-eps")
    _free_tensors(case)


def test_fallback_equals_baseline() -> None:
    """Non-production signatures must route to the vendored baseline and
    return bitwise-identical outputs (fallback wiring guard)."""

    if not _candidate_available():
        pytest.skip("candidate not implemented yet (src/register.py stub)")
    probes = [
        _case(entry="single", B=1, S=64, F=1, D=3072, dtype="float32", norm_type="rms"),
        _case(entry="single", B=1, S=64, F=1, D=3840, dtype="bfloat16", norm_type="layer"),
        _case(entry="dual", B=2, S=64, F=1, D=3072, dtype="float16", norm_type="rms"),
    ]
    for case in probes:
        base = baseline(case)
        cand = candidate(case)
        if case["entry"] == "single":
            assert torch.equal(cand, base), f"{case['name']}: fallback differs from baseline"
        else:
            assert torch.equal(cand[0], base[0]) and torch.equal(cand[1], base[1]), (
                f"{case['name']}: fallback differs from baseline"
            )
        _free_tensors(case)


def test_inputs_not_mutated() -> None:
    """Cached-input A/B is only valid if neither side mutates its inputs."""

    case = _case(
        entry="dual",
        B=1,
        S=128,
        F=1,
        D=PROD_D,
        dtype=PROD_DTYPE,
        norm_type=PROD_NORM,
        affine_mode="W",
        scale_mode="11D",
        shift_mode="BSD",
    )
    args = _ensure_tensors(case)
    snapshots = [a.clone() if isinstance(a, torch.Tensor) else a for a in args]
    baseline(case)
    if _candidate_available():
        candidate(case)
    torch.cuda.synchronize()
    for got, snap in zip(args, snapshots):
        if isinstance(got, torch.Tensor):
            assert torch.equal(got, snap), "input tensor was mutated by a kernel call"
    _free_tensors(case)


def test_y2_dynamic_bound_detects_perturbation() -> None:
    """Sensitivity probe for the stage-2 dynamic bound: a synthetic candidate
    that matches the baseline's y but perturbs ONLY y2 must fail the bound.
    Runs in baseline-only mode (no candidate implementation needed)."""

    case = _case(
        entry="dual", B=1, S=256, F=1, D=3072, dtype="bfloat16", norm_type="rms"
    )
    base = baseline(case)
    ref2_b, _ = reference_y2_given(case, base[0])
    err_b = (base[1].float() - ref2_b).abs().max().item()
    delta = 10.0 * (2.0 * err_b + 1e-6)
    perturbed = (base[0], base[1] + delta)  # y identical, y2 shifted
    with pytest.raises(AssertionError, match=r"\[y2\]"):
        _assert_dynamic_tolerance_stage2(perturbed, base, case=case, path="y2-probe")
    # Sanity: the unperturbed pair passes its own bound.
    _assert_dynamic_tolerance_stage2(base, base, case=case, path="y2-probe-clean")
    _free_tensors(case)


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
    reference_y(case)  # populates case["_err_scale"] for the modeled checker
    wrong = _norm_fp32(x.float(), weight, bias, norm_type, eps) * (
        1 + scale.float()
    ) + shift.float()
    with pytest.raises(AssertionError):
        _assert_close_modeled(
            base, wrong, case["_err_scale"], case=case, path="wrong-single-math"
        )
    _free_tensors(case)

    case2 = _case(
        entry="dual", B=1, S=256, F=1, D=3072, dtype="bfloat16", norm_type="rms"
    )
    args2 = _ensure_tensors(case2)
    (x, weight, bias, scale, shift, weight2, bias2, scale2, norm_type, eps) = args2
    base2 = baseline(case2)
    y_dev = base2[0]
    ref_y2, err_scale2 = reference_y2_given(case2, y_dev)
    # Wrong stage-2 math: tanh(scale2) instead of (1 + scale2).
    wrong_y2 = _norm_quantized(
        y_dev.float(), weight2, bias2, norm_type, eps, _torch_dtype(case2["dtype"])
    ) * torch.tanh(scale2.float())
    with pytest.raises(AssertionError):
        _assert_close_modeled(
            base2[1], wrong_y2, err_scale2, case=case2, path="wrong-dual-math"
        )
    # Sanity: the correct stage-2 reference DOES match.
    _assert_close_modeled(
        base2[1], ref_y2, err_scale2, case=case2, path="correct-dual-math"
    )
    _free_tensors(case2)
