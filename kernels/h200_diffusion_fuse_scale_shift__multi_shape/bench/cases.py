"""Case enumeration for correctness and benchmarking.

Three suites:
- "production": exactly the 15 rows of docs/captured_shapes_h200.jsonl, rebuilt
  verbatim (shapes, dtypes, strides incl. the non-contiguous fp32 scale, kwargs).
- "grid": the canonical regression grid from the SGLang oracle test
  (test_qwen_image_modulation.py), extended per the task prompt to also cover
  fuse_scale_shift_kernel layouts (2D/3D/4D/scalar, scale_constant in {0,1},
  mixed bf16-x/fp32-scale, non-contiguous scale).
- "negative": out-of-contract signatures (error parity / fallback parity).

CI subset (env KDA_CI=1) mirrors the upstream get_ci_test_range subsets.
"""

from __future__ import annotations

import json
import os
import zlib
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable

import torch

KERNEL_DIR = Path(__file__).resolve().parents[1]
SHAPES_JSONL = KERNEL_DIR / "docs" / "captured_shapes_h200.jsonl"

OP_SCALE_SHIFT = "scale_shift"
OP_SELECT01 = "select01"
OP_RESIDUAL = "residual_select01"

_DTYPE_FROM_STR = {
    "torch.float32": torch.float32,
    "torch.float16": torch.float16,
    "torch.bfloat16": torch.bfloat16,
    "torch.int32": torch.int32,
    "torch.int64": torch.int64,
    "torch.bool": torch.bool,
}
_DTYPE_SHORT = {
    torch.float32: "fp32",
    torch.float16: "fp16",
    torch.bfloat16: "bf16",
    torch.int32: "i32",
    torch.int64: "i64",
    torch.bool: "bool",
}

EPS = 1e-6


def _ci_enabled() -> bool:
    return os.environ.get("KDA_CI", "0") == "1"


def _grid_axes():
    if _ci_enabled():
        return (
            [torch.float16, torch.bfloat16],
            [1, 2],
            [6, 128],
            [512, 3072],
        )
    return (
        [torch.float16, torch.bfloat16, torch.float32],
        [1, 2, 4],
        [6, 33, 128, 257],
        [512, 1024, 1536, 3072],
    )


@dataclass
class Case:
    case_id: str
    op: str  # OP_SCALE_SHIFT | OP_SELECT01 | OP_RESIDUAL
    suite: str  # "production" | "grid" | "negative"
    build: Callable[[torch.device], tuple[list, dict]]
    x_dtype: torch.dtype
    # negative-case kind: "" (normal compare), "error_parity", "fallback_parity"
    kind: str = ""
    expected_errors: tuple = ()
    notes: str = ""
    meta: dict = field(default_factory=dict)
    # Optional (atol, rtol) replacing the dtype default for the fixed
    # candidate-vs-baseline check. Used by ill-conditioned cases where two
    # CORRECT implementations legitimately diverge beyond the default (the
    # dynamic cross-check stays primary and scales with the baseline's own
    # conditioning error).
    tol_override: tuple | None = None


def _seed_for(case_id: str) -> int:
    return zlib.crc32(case_id.encode()) & 0x7FFFFFFF


def _gen(device: torch.device, seed: int) -> torch.Generator:
    g = torch.Generator(device=device)
    g.manual_seed(seed)
    return g


def _randn(shape, dtype, device, g) -> torch.Tensor:
    # randn does not support int dtypes; callers use _index for those.
    return torch.randn(tuple(shape), generator=g, device=device, dtype=torch.float32).to(dtype)


def _index(shape, dtype, device, g) -> torch.Tensor:
    t = torch.randint(0, 2, tuple(shape), generator=g, device=device, dtype=torch.int64)
    # The select01 contract domain is values in {0, 1}; guarantee BOTH branches
    # are exercised even on tiny shapes where randint could be constant.
    if t.numel() >= 2:
        flat = t.view(-1)
        flat[0] = 0
        flat[1] = 1
    return t.to(dtype)


def _default_strides(shape) -> tuple[int, ...]:
    strides = [1] * len(shape)
    acc = 1
    for i in range(len(shape) - 1, -1, -1):
        strides[i] = acc
        acc *= max(int(shape[i]), 1)
    return tuple(strides)


def _strided(shape, strides, dtype, device, g) -> torch.Tensor:
    """Build a tensor with EXACT shape+strides via as_strided over a base buffer."""
    needed = 1 + sum((s - 1) * st for s, st in zip(shape, strides) if s > 0)
    if dtype in (torch.int32, torch.int64, torch.bool):
        base = _index((int(needed),), dtype, device, g)
    else:
        base = torch.randn(
            int(needed), generator=g, device=device, dtype=torch.float32
        ).to(dtype)
    return base.as_strided(tuple(shape), tuple(strides))


def _build_from_spec(spec: Any, device, g):
    """Build one argument from a captured JSONL tensor spec (or pass literals through).

    Strides are reproduced EXACTLY when given — even for tensors PyTorch reports
    as contiguous (production captures carry padded strides on size-1 dims, e.g.
    (1,1,3072)/(18432,3072,1) slices of packed adaLN buffers), so dispatcher
    stride predicates see the real production values.
    """
    if spec is None or isinstance(spec, (int, float, bool, str)):
        return spec
    assert isinstance(spec, dict), spec
    dtype = _DTYPE_FROM_STR[spec["dtype"]]
    shape = spec["shape"]
    strides = spec.get("strides")
    if strides and tuple(strides) != _default_strides(shape):
        t = _strided(shape, strides, dtype, device, g)
    elif dtype in (torch.int32, torch.int64, torch.bool):
        t = _index(shape, dtype, device, g)
    else:
        t = _randn(shape, dtype, device, g)
    if spec.get("contiguous", True):
        assert t.is_contiguous(), (shape, strides)
    return t


# ---------------------------------------------------------------------------
# Production suite: the 15 captured rows, verbatim.
# ---------------------------------------------------------------------------

_KERNEL_TO_OP = {
    "scale_shift.fuse_scale_shift_kernel": OP_SCALE_SHIFT,
    "scale_shift.fuse_layernorm_scale_shift_gate_select01_kernel": OP_SELECT01,
    "scale_shift.fuse_residual_layernorm_scale_shift_gate_select01_kernel": OP_RESIDUAL,
}

# Keyword argument order for rebuilding select01 calls (x is positional arg0).
_SELECT01_KW_ORDER = [
    "weight", "bias", "scale0", "shift0", "gate0",
    "scale1", "shift1", "gate1", "index", "eps",
]
_RESIDUAL_KW_ORDER = [
    "residual", "residual_gate", "weight", "bias", "scale0", "shift0", "gate0",
    "scale1", "shift1", "gate1", "index", "eps",
]


def load_production_rows() -> list[dict]:
    rows = []
    with open(SHAPES_JSONL) as fh:
        for line in fh:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    if len(rows) != 15:
        raise RuntimeError(f"expected exactly 15 captured rows, got {len(rows)}")
    return rows


def production_case_id(i: int, row: dict) -> str:
    op = _KERNEL_TO_OP[row["kernel"]]
    x = row["args"][0]
    b, l, c = x["shape"]
    layout = ""
    if op == OP_SCALE_SHIFT:
        sc = row["args"][1]
        layout = "x".join(str(d) for d in sc["shape"])
        layout += "" if sc.get("contiguous", True) else "NC"
        layout += _DTYPE_SHORT[_DTYPE_FROM_STR[sc["dtype"]]]
    preset = row.get("model", "?").split("/")[-1]
    return f"prod{i:02d}_{op}_B{b}L{l}C{c}_{layout}_{preset}"


def _make_production_case(i: int, row: dict) -> Case:
    op = _KERNEL_TO_OP[row["kernel"]]
    cid = production_case_id(i, row)
    x_dtype = _DTYPE_FROM_STR[row["args"][0]["dtype"]]

    def build(device, _row=row, _op=op, _cid=cid):
        g = _gen(device, _seed_for(_cid))
        args = [_build_from_spec(a, device, g) for a in _row["args"]]
        kwargs = {}
        kw = _row.get("kwargs") or {}
        order = (
            _SELECT01_KW_ORDER if _op == OP_SELECT01
            else _RESIDUAL_KW_ORDER if _op == OP_RESIDUAL
            else list(kw.keys())
        )
        for k in order:
            if k in kw:
                kwargs[k] = _build_from_spec(kw[k], device, g)
        return args, kwargs

    return Case(
        case_id=cid, op=op, suite="production", build=build, x_dtype=x_dtype,
        meta={"jsonl_index": i, "model": row.get("model"), "kernel": row["kernel"]},
    )


def production_cases() -> list[Case]:
    return [_make_production_case(i, row) for i, row in enumerate(load_production_rows())]


# ---------------------------------------------------------------------------
# Canonical regression grid.
# ---------------------------------------------------------------------------

def _frames_for(L: int) -> int:
    for f in (2, 3, 4):
        if L % f == 0:
            return f
    return 1


def _ss_layout_args(layout, B, L, C, dtype, device, g):
    """Build (scale, shift) for one fuse_scale_shift layout class."""
    if layout == "rowwise_bc":
        return _randn((B, C), dtype, device, g), _randn((B, C), dtype, device, g)
    if layout == "rowwise_1c":
        return _randn((1, C), dtype, device, g), _randn((1, C), dtype, device, g)
    if layout == "pertoken":
        return _randn((B, L, C), dtype, device, g), _randn((B, L, C), dtype, device, g)
    if layout == "frame4d":
        F = _frames_for(L)
        return (
            _randn((B, F, 1, C), dtype, device, g),
            _randn((B, L, C), dtype, device, g),  # baseline 4D path needs per-token shift
        )
    if layout == "scalar":
        return _randn((), dtype, device, g), _randn((), dtype, device, g)
    if layout == "b1c":
        return _randn((B, 1, C), dtype, device, g), _randn((B, 1, C), dtype, device, g)
    if layout == "1lc":
        return _randn((1, L, C), dtype, device, g), _randn((1, L, C), dtype, device, g)
    if layout == "mixed_fp32_11c":
        # wan-i2v/t2v pattern: fp32 (1,1,C) scale + per-token shift in x dtype
        return (
            _randn((1, 1, C), torch.float32, device, g),
            _randn((B, L, C), dtype, device, g),
        )
    if layout == "mixed_fp32_nc":
        # wan-ti2v pattern: fp32 NON-CONTIGUOUS (B,L,C) scale (padded row stride)
        pad_row = 6 * C  # mirrors the captured stride pattern (18432 = 6*3072)
        scale = _strided((B, L, C), (L * pad_row, pad_row, 1), torch.float32, device, g)
        return scale, _randn((B, L, C), dtype, device, g)
    raise ValueError(layout)


_SS_FULL_LAYOUTS = ["rowwise_bc", "rowwise_1c", "pertoken", "frame4d", "scalar"]
_SS_SINGLE_CONST_LAYOUTS = ["b1c", "1lc"]  # const=0 only, to bound case count
_SS_MIXED_LAYOUTS = ["mixed_fp32_11c", "mixed_fp32_nc"]  # bf16 x only, const=0


def _make_ss_grid_case(dtype, B, L, C, layout, const) -> Case:
    cid = (
        f"grid_ss_{_DTYPE_SHORT[dtype]}_B{B}L{L}C{C}_{layout}_c{int(const)}"
    )

    def build(device, _cid=cid, _dt=dtype, _B=B, _L=L, _C=C, _layout=layout, _const=const):
        g = _gen(device, _seed_for(_cid))
        x = _randn((_B, _L, _C), _dt, device, g)
        scale, shift = _ss_layout_args(_layout, _B, _L, _C, _dt, device, g)
        return [x, scale, shift], {"scale_constant": _const}

    return Case(case_id=cid, op=OP_SCALE_SHIFT, suite="grid", build=build, x_dtype=dtype)


_INDEX_DTYPES = [torch.int32, torch.int64, torch.bool]


def _make_sel_grid_case(op, dtype, B, L, C, with_affine) -> Case:
    tag = "aff" if with_affine else "noaff"
    cid = f"grid_{op}_{_DTYPE_SHORT[dtype]}_B{B}L{L}C{C}_{tag}"
    idx_dtype = _INDEX_DTYPES[_seed_for(cid) % len(_INDEX_DTYPES)]

    def build(device, _cid=cid, _op=op, _dt=dtype, _B=B, _L=L, _C=C,
              _aff=with_affine, _idt=idx_dtype):
        g = _gen(device, _seed_for(_cid))
        x = _randn((_B, _L, _C), _dt, device, g)
        kwargs = {
            "weight": _randn((_C,), _dt, device, g) if _aff else None,
            "bias": _randn((_C,), _dt, device, g) if _aff else None,
            "scale0": _randn((_B, _C), _dt, device, g),
            "shift0": _randn((_B, _C), _dt, device, g),
            "gate0": _randn((_B, _C), _dt, device, g),
            "scale1": _randn((_B, _C), _dt, device, g),
            "shift1": _randn((_B, _C), _dt, device, g),
            "gate1": _randn((_B, _C), _dt, device, g),
            "index": _index((_B, _L), _idt, device, g),
            "eps": EPS,
        }
        if _op == OP_RESIDUAL:
            kwargs = {
                "residual": _randn((_B, _L, _C), _dt, device, g),
                "residual_gate": _randn((_B, _L, _C), _dt, device, g),
                **kwargs,
            }
        return [x], kwargs

    return Case(
        case_id=cid, op=op, suite="grid", build=build, x_dtype=dtype,
        meta={"index_dtype": str(idx_dtype)},
    )


def _make_sel_offset_case(op, dtype, B, L, C, offset: float) -> Case:
    """LayerNorm rows whose input carries a large constant offset relative to
    its spread — exposes uncentered-variance cancellation in fp32."""
    cid = f"grid_{op}_{_DTYPE_SHORT[dtype]}_B{B}L{L}C{C}_offset{int(offset)}_noaff"

    def build(device, _cid=cid, _op=op, _dt=dtype, _B=B, _L=L, _C=C, _off=offset):
        g = _gen(device, _seed_for(_cid))
        narrow = (_randn((_B, _L, _C), torch.float32, device, g) * 0.1)
        if _op == OP_RESIDUAL:
            # The offset reaches the normalized tensor via residual + gate*x.
            x = narrow.to(_dt)
            residual = (narrow + _off).to(_dt)
            residual_gate = _randn((_B, _L, _C), _dt, device, g)
        else:
            x = (narrow + _off).to(_dt)
        kwargs = {
            "weight": None,
            "bias": None,
            "scale0": _randn((_B, _C), _dt, device, g),
            "shift0": _randn((_B, _C), _dt, device, g),
            "gate0": _randn((_B, _C), _dt, device, g),
            "scale1": _randn((_B, _C), _dt, device, g),
            "shift1": _randn((_B, _C), _dt, device, g),
            "gate1": _randn((_B, _C), _dt, device, g),
            "index": _index((_B, _L), torch.int32, device, g),
            "eps": EPS,
        }
        if _op == OP_RESIDUAL:
            kwargs = {"residual": residual, "residual_gate": residual_gate, **kwargs}
        return [x], kwargs

    # At offset/spread ~1e4 the mean dominates fp32 rounding: two CORRECT
    # centered implementations differ by ~1e-2 in normalized units purely
    # from reduction order, so the fixed check is relaxed; the dynamic
    # cross-check (budgeted by the baseline's own error vs the fp32
    # reference) is what rejects uncentered-variance failures here.
    return Case(case_id=cid, op=op, suite="grid", build=build, x_dtype=dtype,
                notes=f"constant offset {offset} vs spread 0.1",
                tol_override=(5e-2, 5e-2))


def _offset_cases() -> list[Case]:
    B, L, C = 2, 128, 1024
    return [
        _make_sel_offset_case(OP_SELECT01, torch.float32, B, L, C, 1000.0),
        _make_sel_offset_case(OP_RESIDUAL, torch.float32, B, L, C, 1000.0),
        _make_sel_offset_case(OP_SELECT01, torch.bfloat16, B, L, C, 1000.0),
    ]


def grid_cases() -> list[Case]:
    dtypes, batches, seqs, hiddens = _grid_axes()
    cases: list[Case] = []
    for dt in dtypes:
        for B in batches:
            for L in seqs:
                for C in hiddens:
                    for layout in _SS_FULL_LAYOUTS:
                        for const in (0, 1.0):
                            cases.append(_make_ss_grid_case(dt, B, L, C, layout, const))
                    for layout in _SS_SINGLE_CONST_LAYOUTS:
                        cases.append(_make_ss_grid_case(dt, B, L, C, layout, 0))
                    if dt == torch.bfloat16:
                        for layout in _SS_MIXED_LAYOUTS:
                            cases.append(_make_ss_grid_case(dt, B, L, C, layout, 0))
                    for op in (OP_SELECT01, OP_RESIDUAL):
                        for aff in (False, True):
                            cases.append(_make_sel_grid_case(op, dt, B, L, C, aff))
    cases.extend(_offset_cases())
    return cases


# ---------------------------------------------------------------------------
# Negative suite: out-of-contract signatures.
# error_parity: baseline and wrapper must raise the same exception type.
# fallback_parity: baseline supports it; wrapper must route to fallback and match.
# ---------------------------------------------------------------------------

def _neg(case_id, op, build, kind, expected_errors=(), notes="", x_dtype=torch.bfloat16):
    return Case(
        case_id=case_id, op=op, suite="negative", build=build, x_dtype=x_dtype,
        kind=kind, expected_errors=expected_errors, notes=notes,
    )


def negative_cases() -> list[Case]:
    B, L, C = 2, 33, 512

    def b_fp64(device):
        g = _gen(device, 1)
        x = torch.randn((B, L, C), generator=g, device=device, dtype=torch.float64)
        s = torch.randn((B, C), generator=g, device=device, dtype=torch.float64)
        sh = torch.randn((B, C), generator=g, device=device, dtype=torch.float64)
        return [x, s, sh], {"scale_constant": 0}

    def b_fp32x_narrow_scale(device):
        # Baseline promotes mixed dtypes fine; the native packet loader cannot
        # widen a narrower modulation dtype, so the route must decline.
        g = _gen(device, 10)
        x = _randn((B, L, C), torch.float32, device, g)
        s = _randn((B, C), torch.bfloat16, device, g)
        sh = _randn((B, C), torch.bfloat16, device, g)
        return [x, s, sh], {"scale_constant": 0}

    def b_noncontig_x(device):
        g = _gen(device, 2)
        x = _randn((B, L, 2 * C), torch.bfloat16, device, g)[:, :, :C]
        s = _randn((B, C), torch.bfloat16, device, g)
        sh = _randn((B, C), torch.bfloat16, device, g)
        return [x, s, sh], {"scale_constant": 0}

    def b_scale_5d(device):
        g = _gen(device, 3)
        x = _randn((B, L, C), torch.bfloat16, device, g)
        s = _randn((B, 1, 1, 1, C), torch.bfloat16, device, g)
        sh = _randn((B, L, C), torch.bfloat16, device, g)
        return [x, s, sh], {"scale_constant": 0}

    def b_cpu(device):
        g = _gen(torch.device("cpu"), 4)
        x = torch.randn((B, L, C), generator=g, dtype=torch.bfloat16)
        s = torch.randn((B, C), generator=g, dtype=torch.bfloat16)
        sh = torch.randn((B, C), generator=g, dtype=torch.bfloat16)
        return [x, s, sh], {"scale_constant": 0}

    def b_4d_bad_frames(device):
        g = _gen(device, 5)
        x = _randn((B, 33, C), torch.bfloat16, device, g)
        s = _randn((B, 2, 1, C), torch.bfloat16, device, g)  # 33 % 2 != 0
        sh = _randn((B, 33, C), torch.bfloat16, device, g)
        return [x, s, sh], {"scale_constant": 0}

    def b_4d_shift_not_pertoken(device):
        g = _gen(device, 6)
        F = 3
        x = _randn((B, 33, C), torch.bfloat16, device, g)
        s = _randn((B, F, 1, C), torch.bfloat16, device, g)
        sh = _randn((B, F, 1, C), torch.bfloat16, device, g)  # not reshapeable to (B*L, C)
        return [x, s, sh], {"scale_constant": 0}

    def _sel_kwargs(device, g, dt=torch.bfloat16):
        return {
            "weight": None,
            "bias": None,
            "scale0": _randn((B, C), dt, device, g),
            "shift0": _randn((B, C), dt, device, g),
            "gate0": _randn((B, C), dt, device, g),
            "scale1": _randn((B, C), dt, device, g),
            "shift1": _randn((B, C), dt, device, g),
            "gate1": _randn((B, C), dt, device, g),
            "index": _index((B, L), torch.int32, device, g),
            "eps": EPS,
        }

    def b_index_3d(device):
        g = _gen(device, 7)
        x = _randn((B, L, C), torch.bfloat16, device, g)
        kw = _sel_kwargs(device, g)
        kw["index"] = _index((B, L, 1), torch.int32, device, g)
        return [x], kw

    def b_weight_2d(device):
        g = _gen(device, 8)
        x = _randn((B, L, C), torch.bfloat16, device, g)
        kw = _sel_kwargs(device, g)
        kw["weight"] = _randn((2, C), torch.bfloat16, device, g)
        return [x], kw

    def b_residual_mismatch(device):
        g = _gen(device, 9)
        x = _randn((B, L, C), torch.bfloat16, device, g)
        kw = _sel_kwargs(device, g)
        kw = {
            "residual": _randn((B, L + 1, C), torch.bfloat16, device, g),
            "residual_gate": _randn((B, L, C), torch.bfloat16, device, g),
            **kw,
        }
        return [x], kw

    return [
        _neg("neg_ss_fp64", OP_SCALE_SHIFT, b_fp64, "fallback_parity",
             notes="fp64 in-contract for baseline; native must decline", x_dtype=torch.float64),
        _neg("neg_ss_fp32x_bf16scale", OP_SCALE_SHIFT, b_fp32x_narrow_scale,
             "fallback_parity",
             notes="fp32 x with narrower bf16 modulation; native must decline",
             x_dtype=torch.float32),
        _neg("neg_ss_noncontig_x", OP_SCALE_SHIFT, b_noncontig_x, "error_parity",
             (AssertionError,), "baseline asserts x contiguous"),
        _neg("neg_ss_scale_5d", OP_SCALE_SHIFT, b_scale_5d, "error_parity",
             (ValueError,), "scale rank > 4"),
        _neg("neg_ss_cpu", OP_SCALE_SHIFT, b_cpu, "error_parity",
             (AssertionError,), "baseline asserts CUDA/XPU device"),
        _neg("neg_ss_4d_bad_frames", OP_SCALE_SHIFT, b_4d_bad_frames, "error_parity",
             (AssertionError,), "L %% num_frames != 0"),
        _neg("neg_ss_4d_shift_not_pertoken", OP_SCALE_SHIFT, b_4d_shift_not_pertoken,
             "error_parity", (RuntimeError,), "4D shift not per-token reshapeable"),
        _neg("neg_sel_index_3d", OP_SELECT01, b_index_3d, "error_parity",
             (ValueError,), "index must be 2D"),
        _neg("neg_sel_weight_2d", OP_SELECT01, b_weight_2d, "error_parity",
             (ValueError,), "weight must be 1D [C]"),
        _neg("neg_res_shape_mismatch", OP_RESIDUAL, b_residual_mismatch, "error_parity",
             (ValueError,), "residual shape mismatch"),
    ]


def all_cases(suites: tuple[str, ...] = ("production", "grid", "negative")) -> list[Case]:
    cases: list[Case] = []
    if "production" in suites:
        cases.extend(production_cases())
    if "grid" in suites:
        cases.extend(grid_cases())
    if "negative" in suites:
        cases.extend(negative_cases())
    return cases
