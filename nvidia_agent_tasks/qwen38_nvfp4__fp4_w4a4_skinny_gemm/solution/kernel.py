import torch
from fused_quant import (
    fused_quant,
    silu_small,
    silu_swizzled_4096,
    silu_swizzled_half8_4096,
    silu_swizzled_4369,
    small_quant,
)
from gemm import decode_fp4_gemm, large_fp4_gemm


def fp4_gemm(
    input: torch.Tensor,
    weight: torch.Tensor,
    input_sf: torch.Tensor,
    weight_sf: torch.Tensor,
    alpha: torch.Tensor,
    out_dtype: torch.dtype,
    out_features: int,
) -> torch.Tensor:
    del out_features
    if input.shape[0] <= 9:
        return decode_fp4_gemm(input, weight, input_sf, weight_sf, alpha)
    return large_fp4_gemm(input, weight, input_sf, weight_sf, alpha, out_dtype)


def fp4_quantize(
    input: torch.Tensor,
    global_scale: torch.Tensor,
) -> tuple[torch.Tensor, torch.Tensor]:
    scale_cols = input.shape[1] // 16
    output_numel = input.shape[0] * (input.shape[1] // 2)
    scale_words = 128 * (scale_cols // 4)
    # One backing allocation removes a CUDA-graph allocation node. Both slices
    # stay naturally aligned for every recorded 5120-column workload.
    storage = torch.empty(
        output_numel + scale_words * 4, dtype=torch.uint8, device=input.device
    )
    output = storage[:output_numel].view(input.shape[0], input.shape[1] // 2)
    scale_storage = storage[output_numel:].view(torch.int32).view(
        128, scale_cols // 4
    )
    block_size = 128
    # Give each recorded shape one loop-free wave: the kernel computes M*K/16
    # real blocks and clears 32*(K/64) words of padded scale storage.
    total_work = input.shape[0] * scale_cols + 32 * (scale_cols // 4)
    grid_size = (total_work + block_size - 1) // block_size
    small_quant(
        output,
        scale_storage,
        input,
        global_scale,
        grid_size,
        block_size,
    )
    return output, scale_storage.view(torch.uint8).reshape(128, scale_cols)


def silu_fp4_quantize(
    a: torch.Tensor,
    mask: torch.Tensor,
    a_global_sf: torch.Tensor,
) -> tuple[torch.Tensor, torch.Tensor]:
    tokens = a.shape[1]
    columns = a.shape[2] // 2
    padded_tokens = (tokens + 127) // 128 * 128
    padded_scale_cols = (columns // 16 + 3) // 4 * 4
    output_numel = tokens * (columns // 2)
    scale_words = padded_tokens * (padded_scale_cols // 4)
    # Keep both returned tensors in one graph-pool allocation. Every recorded
    # output extent is 256-byte aligned, so the int32 scale view remains aligned.
    storage = torch.empty(
        output_numel + scale_words * 4, dtype=torch.uint8, device=a.device
    )
    output = storage[:output_numel].view(1, tokens, columns // 2)
    scale_storage = storage[output_numel:].view(torch.int32).view(
        1, padded_tokens, padded_scale_cols // 4
    )
    if tokens == 1:
        silu_small(output, scale_storage, a, a_global_sf, 17, 64)
        scales = (
            scale_storage.view(torch.float8_e4m3fn)
            .view(1, 1, padded_scale_cols // 4, 32, 4, 4)
            .permute(3, 4, 1, 5, 2, 0)
        )
        return output.permute(1, 2, 0), scales
    if tokens == 9:
        silu_small(output, scale_storage, a, a_global_sf, 153, 64)
        scales = (
            scale_storage.view(torch.float8_e4m3fn)
            .view(1, 1, padded_scale_cols // 4, 32, 4, 4)
            .permute(3, 4, 1, 5, 2, 0)
        )
        return output.permute(1, 2, 0), scales
    if tokens == 4096:
        silu_swizzled_half8_4096(output, scale_storage, a, a_global_sf)
        scales = (
            scale_storage.view(torch.float8_e4m3fn)
            .view(
                1,
                padded_tokens // 128,
                padded_scale_cols // 4,
                32,
                4,
                4,
            )
            .permute(3, 4, 1, 5, 2, 0)
        )
        return output.permute(1, 2, 0), scales
    if tokens == 4369:
        silu_swizzled_4369(output, scale_storage, a, a_global_sf)
        scales = (
            scale_storage.view(torch.float8_e4m3fn)
            .view(
                1,
                padded_tokens // 128,
                padded_scale_cols // 4,
                32,
                4,
                4,
            )
            .permute(3, 4, 1, 5, 2, 0)
        )
        return output.permute(1, 2, 0), scales

    work_per_cta = 1024
    grid_size = (tokens * (columns // 16) + work_per_cta - 1) // work_per_cta
    fused_quant(
        output,
        scale_storage,
        a,
        a_global_sf,
        mask,
        grid_size,
        256,
    )
    scales = (
        scale_storage.view(torch.float8_e4m3fn)
        .view(
            1,
            padded_tokens // 128,
            padded_scale_cols // 4,
            32,
            4,
            4,
        )
        .permute(3, 4, 1, 5, 2, 0)
    )
    return output.permute(1, 2, 0), scales


OPS = {
    "qwen38_fp4_gemm": fp4_gemm,
    "qwen38_fp4_quantize": fp4_quantize,
    "qwen38_silu_fp4_quantize": silu_fp4_quantize,
}
