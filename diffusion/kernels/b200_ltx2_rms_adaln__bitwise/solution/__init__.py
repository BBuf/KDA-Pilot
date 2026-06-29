"""Optimized candidate for b200_ltx2_rms_adaln__bitwise.

Staged candidate: shared ``at::rms_norm`` (bit-identical ``normed`` by
construction) followed by one fused, fully bf16-rounded modulation kernel that
reproduces the eager ``normed * (1 + scale) + shift`` with three explicit
round-to-nearest-even barriers. Exposed through the same destination-passing
tvm-ffi ABI and symmetric build as ``baseline/``. No sglang import.
"""
