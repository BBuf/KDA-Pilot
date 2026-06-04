"""Apply the in-SGLang drop-in patch to an isolated sglang worktree.

Inserts a native CUDA fast path INSIDE the existing public custom ops in
python/sglang/jit_kernel/diffusion/cutedsl/norm_tanh_mul_add_norm_scale.py —
the @torch.library.custom_op registrations, fake registrations, validation,
and CuTe-DSL fallback all stay byte-identical for non-fast-path signatures.

Usage: python apply_export.py <sglang_worktree_root>
"""

import sys
from pathlib import Path

NATIVE_BLOCK = '''

# ---- Native CUDA fast path (KDA h200 norm_tanh_mul_add promotion) ----------
# bf16 / rms / weight-only production signatures run a native kernel
# (csrc/diffusion/norm_tanh_mul_add.cuh); everything else stays on the
# CuTe-DSL path below. The public custom-op registration is unchanged.

from sglang.jit_kernel.utils import cache_once as _kda_cache_once
from sglang.jit_kernel.utils import load_jit as _kda_load_jit


@_kda_cache_once  # module-level cache: load_jit must not re-enter per call
def _native_norm_tanh_module():
    return _kda_load_jit(
        "norm_tanh_mul_add",
        cuda_files=["diffusion/norm_tanh_mul_add.cuh"],
        cuda_wrappers=[
            ("single", "NormTanhMulAddSingleKernel<bf16_t>::run"),
            ("dual", "NormTanhMulAddDualKernel<bf16_t>::run"),
        ],
    )


def _native_aligned16(t: torch.Tensor) -> bool:
    return t.data_ptr() % 16 == 0


def _native_vec_ok(t: Optional[torch.Tensor], D: int) -> bool:
    return (
        t is not None
        and t.is_cuda
        and t.dtype is torch.bfloat16
        and t.shape == (D,)
        and t.stride(-1) == 1
        and _native_aligned16(t)
    )


def _native_fast_ok(x, weight, bias, scale, shift, norm_type) -> bool:
    if norm_type != "rms" or bias is not None:
        return False
    # Device gate: only CUDA tensors may enter the native launcher; CPU or
    # device-mismatched calls continue through the original CuTe-DSL path,
    # preserving its fallback/error behavior exactly.
    if not (x.is_cuda and scale.is_cuda and shift.is_cuda):
        return False
    if x.dtype is not torch.bfloat16 or not x.is_contiguous():
        return False
    B, S, D = x.shape
    if D != 3840:
        # Production-only scope (KDA DEC-1): the kernel itself accepts any
        # D % 256 == 0 <= 8192, but only the captured Z-Image family has
        # benchmark evidence; other D stay on the CuTe-DSL path.
        return False
    if B * S > 2**31 - 1:
        return False
    if not (_native_aligned16(x) and _native_aligned16(shift)):
        return False
    if not _native_vec_ok(weight, D):
        return False
    if not (
        scale.dtype is torch.bfloat16
        and scale.shape == (1, 1, D)
        and scale.stride(-1) == 1
        and _native_aligned16(scale)
    ):
        return False
    return (
        shift.dtype is torch.bfloat16
        and shift.shape == (B, S, D)
        and shift.is_contiguous()
    )
# ---------------------------------------------------------------------------

'''

# Single-op site: `y = empty_like` is followed DIRECTLY by the scale
# broadcast (the dual op interposes `y2 = empty_like`), making this two-line
# pattern unique to the single op.
SINGLE_HOOK = '''        y = torch.empty_like(x)  # create output tensor
        scale = broadcast_tensor_for_bsfd(scale, *x.shape)  # handle various shapes
'''
SINGLE_HOOK_NEW = '''        if _native_fast_ok(x, weight, bias, scale, shift, norm_type):
            y_native = torch.empty_like(x)
            _native_norm_tanh_module().single(
                x.view(-1, D), weight, scale.view(D), shift.view(-1, D),
                y_native.view(-1, D), float(eps))
            return y_native
        y = torch.empty_like(x)  # create output tensor
        scale = broadcast_tensor_for_bsfd(scale, *x.shape)  # handle various shapes
'''

DUAL_HOOK = '''        y = torch.empty_like(x)  # create output tensor
        y2 = torch.empty_like(x)  # create output tensor
'''
DUAL_HOOK_NEW = '''        if (
            _native_fast_ok(x, weight, bias, scale, shift, norm_type)
            and bias2 is None
            and _native_vec_ok(weight2, x.shape[-1])
            and scale2.is_cuda
            and scale2.dtype is torch.bfloat16
            and scale2.shape == (1, 1, x.shape[-1])
            and scale2.stride(-1) == 1
            and _native_aligned16(scale2)
        ):
            y_native = torch.empty_like(x)
            y2_native = torch.empty_like(x)
            _native_norm_tanh_module().dual(
                x.view(-1, D), weight, scale.view(D), shift.view(-1, D),
                weight2, scale2.view(D), y_native.view(-1, D),
                y2_native.view(-1, D), float(eps))
            return y_native, y2_native
        y = torch.empty_like(x)  # create output tensor
        y2 = torch.empty_like(x)  # create output tensor
'''

ANCHOR = "_COMPILE_CACHE = {}"


def main() -> int:
    root = Path(sys.argv[1])
    target = root / "python/sglang/jit_kernel/diffusion/cutedsl/norm_tanh_mul_add_norm_scale.py"
    src = target.read_text()
    assert ANCHOR in src, "anchor not found"
    assert src.count(DUAL_HOOK) == 1, "dual hook site not unique"
    assert src.count(SINGLE_HOOK) == 1, "single hook site not unique"
    src = src.replace(ANCHOR, ANCHOR + NATIVE_BLOCK, 1)
    src = src.replace(DUAL_HOOK, DUAL_HOOK_NEW, 1)
    src = src.replace(SINGLE_HOOK, SINGLE_HOOK_NEW, 1)
    target.write_text(src)
    print(f"patched {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
