"""Dispatcher + SGLang ``jit_kernel`` driver for the diffusion RoPE candidate.

Public callables preserve the SGLang signatures:
  * ``apply_rotary_embedding(x, cos, sin, interleaved=False)``
  * ``apply_ltx2_split_rotary_emb(x, cos, sin)``

Routing per call (non-recursive 3-level fallback):
  1. CUDA: supported captured-production signatures -> native kernel via ``load_jit``.
  2. SGLang baseline: the original triton kernel, captured at import (never our wrapper).
  3. PyTorch reference: only if the SGLang baseline is unavailable/raises.

Both functions are functional (return a new tensor; never mutate inputs). The native
``.cuh`` is built through SGLang ``jit_kernel`` / tvm-ffi (no ``torch.utils.cpp_extension``,
no ``--use_fast_math``). It is compiled in place from its absolute workspace path via
``load_jit`` (the SGLang ``csrc`` tree is NOT modified; the ``sgl_kernel`` headers still
resolve through ``load_jit``'s default include dirs), so the promoted overlay copy builds
the same way from its own ``_impls`` directory.
"""

from __future__ import annotations

import hashlib
import importlib.util
import logging
import os
import sys
from pathlib import Path

try:
    import torch
except ImportError:  # pragma: no cover - CUDA env owns the real run
    torch = None

logger = logging.getLogger(__name__)

_THIS_DIR = Path(__file__).resolve().parent
if str(_THIS_DIR) not in sys.path:
    sys.path.insert(0, str(_THIS_DIR))

_WORKSPACE_CUH = _THIS_DIR / "csrc" / "rotary_embedding.cuh"

# Records the route taken by the most recent call, for test assertions.
_LAST_DISPATCH: dict[str, str | None] = {"standard": None, "ltx2": None}


# ---------------------------------------------------------------------------
# Shared PyTorch reference (3rd-level fallback)
# ---------------------------------------------------------------------------
def _load_reference():
    spec = importlib.util.spec_from_file_location("kda_rope_reference", _THIS_DIR / "reference.py")
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_ref = _load_reference()


# ---------------------------------------------------------------------------
# Original SGLang baselines, captured at import (never resolves to our wrapper).
# ---------------------------------------------------------------------------
_BASELINES: dict[str, object] = {}


def _capture_baselines() -> None:
    if "standard" not in _BASELINES:
        try:
            from sglang.jit_kernel.diffusion.triton.rotary import apply_rotary_embedding as f

            _BASELINES["standard"] = f
        except Exception:  # pragma: no cover - non-SGLang env
            _BASELINES["standard"] = None
    if "ltx2" not in _BASELINES:
        try:
            from sglang.jit_kernel.diffusion.triton.ltx2_rotary import apply_ltx2_split_rotary_emb as g

            _BASELINES["ltx2"] = g
        except Exception:  # pragma: no cover
            _BASELINES["ltx2"] = None


_capture_baselines()


# ---------------------------------------------------------------------------
# JIT module (built via SGLang load_jit / make_cpp_args)
# ---------------------------------------------------------------------------
_SOURCE_HASH: "str | None" = None


def _source_hash() -> str:
    # Computed once per process (the .cuh is stable within a process; a fresh
    # process re-reads it). Avoids per-call file I/O on the hot path.
    global _SOURCE_HASH
    if _SOURCE_HASH is None:
        _SOURCE_HASH = hashlib.sha1(_WORKSPACE_CUH.read_bytes()).hexdigest()[:12]
    return _SOURCE_HASH


def _build_jit_module(dtype, src_hash, profile):
    from sglang.jit_kernel.utils import load_jit, make_cpp_args

    args = make_cpp_args(dtype)
    targ = f"{args}"
    # Profiling build adds -lineinfo so NCU can map SASS back to source.
    # Still NO --use_fast_math (kept consistent with the SGLang jit_kernel build).
    extra_cuda_cflags = ["-lineinfo"] if profile else None
    markers = [*args, src_hash] + (["lineinfo"] if profile else [])
    # load_jit joins cuda_files under <sglang>/jit_kernel/csrc, but pathlib keeps an
    # absolute path as-is, so passing the workspace .cuh's absolute path compiles it
    # in place (no write into the SGLang checkout). sgl_kernel headers it #includes
    # still resolve via load_jit's default include dirs.
    return load_jit(
        "kda_rotary_embedding",
        *markers,  # template args + source hash (+ lineinfo) -> rebuild on change
        cuda_files=[str(_WORKSPACE_CUH)],
        cuda_wrappers=[
            ("standard_rope", f"StandardRopeKernel<{targ}>::run"),
            ("ltx2_split_rope", f"Ltx2SplitRopeKernel<{targ}>::run"),
        ],
        extra_cuda_cflags=extra_cuda_cflags,
    )


_jit_loader = None  # SGLang cache_once-wrapped builder, created lazily (sglang import stays lazy)


def _jit_module(dtype):
    global _jit_loader
    if _jit_loader is None:
        from sglang.jit_kernel.utils import cache_once

        _jit_loader = cache_once(_build_jit_module)
    profile = os.environ.get("KDA_PROFILE", "") in ("1", "true", "True")
    return _jit_loader(dtype, _source_hash(), profile)  # cache_once keys on (dtype, hash, profile)


# ---------------------------------------------------------------------------
# Dispatch gates (optimized scope: bf16 + interleaved=False, production buckets)
# ---------------------------------------------------------------------------
# Captured production buckets -- the ONLY signatures routed to the CUDA candidate;
# anything else falls back. Broadening this requires benchmark evidence and a
# docs/dispatch.md entry first.
_STD_X_SHAPE = (1, 27030, 24, 128)
_STD_COS_SHAPE = (27030, 64)
_LTX2_X_SHAPES = frozenset({
    (1, 126, 2048),
    (1, 1536, 2048),
    (1, 1536, 4096),
    (1, 6144, 2048),
    (1, 6144, 4096),
})


def _supported_standard(x, cos, sin, interleaved) -> bool:
    if torch is None or not isinstance(x, torch.Tensor):
        return False
    if interleaved:
        return False
    if not (x.is_cuda and cos.is_cuda and sin.is_cuda):
        return False
    if not (x.device == cos.device == sin.device):
        return False
    if x.dtype != torch.bfloat16 or cos.dtype != torch.float32 or sin.dtype != torch.float32:
        return False
    if tuple(x.shape) != _STD_X_SHAPE or not x.is_contiguous():
        return False
    if tuple(cos.shape) != _STD_COS_SHAPE or tuple(sin.shape) != _STD_COS_SHAPE:
        return False
    if not (cos.is_contiguous() and sin.is_contiguous()):
        return False
    return True


def _supported_ltx2(x, cos, sin) -> bool:
    if torch is None or not isinstance(x, torch.Tensor):
        return False
    if not (x.is_cuda and cos.is_cuda and sin.is_cuda):
        return False
    if not (x.device == cos.device == sin.device):
        return False
    if not (x.dtype == torch.bfloat16 and cos.dtype == torch.bfloat16 and sin.dtype == torch.bfloat16):
        return False
    if x.dim() != 3 or tuple(x.shape) not in _LTX2_X_SHAPES or not x.is_contiguous():
        return False
    if cos.dim() != 4 or sin.dim() != 4 or cos.shape != sin.shape:
        return False
    B, S, inner = (int(v) for v in x.shape)
    cb, num_heads, cs, half = (int(v) for v in cos.shape)
    if (cb, num_heads, cs) != (B, 32, S):
        return False
    if half not in (32, 64) or inner != num_heads * 2 * half:
        return False
    # Captured non-contiguous (B,H,S,half) layout: last stride 1, head stride half,
    # seq stride num_heads*half. Reject contiguous / non-captured strides.
    for t in (cos, sin):
        if t.is_contiguous():
            return False
        if t.stride(3) != 1 or t.stride(1) != half or t.stride(2) != num_heads * half:
            return False
    return True


# ---------------------------------------------------------------------------
# Public callables
# ---------------------------------------------------------------------------
def apply_rotary_embedding(x, cos, sin, interleaved=False):
    if _supported_standard(x, cos, sin, interleaved):
        try:
            out = torch.empty_like(x)
            head, dim = int(x.shape[-2]), int(x.shape[-1])
            _jit_module(x.dtype).standard_rope(out.reshape(-1, head, dim), x.reshape(-1, head, dim), cos, sin)
            _LAST_DISPATCH["standard"] = "cuda"
            return out
        except Exception as exc:  # pragma: no cover - exercised on GPU
            logger.warning("standard CUDA path failed; falling back: %s", exc)
    return _fallback_standard(x, cos, sin, interleaved)


def _fallback_standard(x, cos, sin, interleaved):
    base = _BASELINES.get("standard")
    if base is not None:
        try:
            result = base(x, cos, sin, interleaved)
            _LAST_DISPATCH["standard"] = "baseline"
            return result
        except Exception as exc:  # pragma: no cover
            logger.warning("standard baseline failed; using reference: %s", exc)
    _LAST_DISPATCH["standard"] = "reference"
    return _ref.standard_rope_reference(x, cos, sin, interleaved)


def apply_ltx2_split_rotary_emb(x, cos, sin):
    if _supported_ltx2(x, cos, sin):
        try:
            out = torch.empty_like(x)
            _jit_module(x.dtype).ltx2_split_rope(out, x, cos, sin)
            _LAST_DISPATCH["ltx2"] = "cuda"
            return out
        except Exception as exc:  # pragma: no cover - exercised on GPU
            logger.warning("ltx2 CUDA path failed; falling back: %s", exc)
    return _fallback_ltx2(x, cos, sin)


def _fallback_ltx2(x, cos, sin):
    base = _BASELINES.get("ltx2")
    if base is not None:
        try:
            result = base(x, cos, sin)
            _LAST_DISPATCH["ltx2"] = "baseline"
            return result
        except Exception as exc:  # pragma: no cover
            logger.warning("ltx2 baseline failed; using reference: %s", exc)
    _LAST_DISPATCH["ltx2"] = "reference"
    return _ref.ltx2_split_rope_reference(x, cos, sin)


def optimized_wrapper(*args, **kwargs):
    """Compatibility entry: dispatch to the right public API by the cos rank."""
    cos = args[1] if len(args) > 1 else kwargs.get("cos")
    if torch is not None and isinstance(cos, torch.Tensor) and cos.dim() == 4:
        return apply_ltx2_split_rotary_emb(*args, **kwargs)
    return apply_rotary_embedding(*args, **kwargs)
