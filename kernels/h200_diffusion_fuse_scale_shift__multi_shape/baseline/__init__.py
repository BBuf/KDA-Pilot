"""Vendored SGLang Triton baseline (CUDA path only; no sglang import).

Provenance: docs/baseline_source.md. This package is the immutable A/B
counterpart for the local correctness and benchmark harnesses.
"""

from .scale_shift import (  # noqa: F401
    fuse_layernorm_scale_shift_gate_select01_kernel,
    fuse_residual_layernorm_scale_shift_gate_select01_kernel,
    fuse_scale_shift_kernel,
)
