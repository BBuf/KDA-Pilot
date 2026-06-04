# Verbatim copy of python/sglang/jit_kernel/diffusion/cutedsl/utils.py
# (see docs/baseline_source.md). No functional edits.
import cutlass
import torch

WARP_SIZE = 32

TORCH_TO_CUTE_DTYPE = {
    torch.float16: cutlass.Float16,
    torch.bfloat16: cutlass.BFloat16,
    torch.float32: cutlass.Float32,
}
