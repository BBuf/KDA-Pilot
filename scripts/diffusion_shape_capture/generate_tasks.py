"""Generate per-kernel KDA task folders for diffusion non-gemm/attention ops.

Produces 8 kernel families x 2 archs = 16 task folders under `kernels/`, each with
the same shape as the existing `b200_fa4_mha__*` and `b200_int8_scaled_mm__*`
tasks: prompt.md, interface.md, benchmark.py, README.md, src/{__init__.py,
register.py}, tests/test_correctness.py, docs/, profile/, ncu/.

Run from the repo root.
"""

from __future__ import annotations

import os
import textwrap
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent
KERNELS_DIR = REPO_ROOT / "kernels"


@dataclass(frozen=True)
class Family:
    slug: str  # short slug used in folder name
    title: str  # human title
    op_type: str  # registered op type
    sglang_targets: list[str]  # list of sglang module:function entry points wrapped
    cute_dsl: bool  # CuTe-DSL kernels (CUDA 12.5+; relevant to B200)
    is_cuda_kernel: bool  # native CUDA kernel (qknorm_rope)
    test_file: str  # the sglang test we will derive correctness from
    description: str  # short kernel description
    shape_table_md: str  # markdown table of canonical shapes
    config_axes: list[str]  # axes that vary (dispatch knobs)


FAMILIES: list[Family] = [
    Family(
        slug="diffusion_qknorm_rope__multi_shape",
        title="Fused QKNorm + RoPE (CUDA, in-place)",
        op_type="qknorm_rope_inplace",
        sglang_targets=[
            "sglang.jit_kernel.diffusion.qknorm_rope:fused_inplace_qknorm_rope",
        ],
        cute_dsl=False,
        is_cuda_kernel=True,
        test_file="python/sglang/jit_kernel/tests/diffusion/test_qknorm_rope.py",
        description=(
            "Fuse per-head RMS normalization on Q and K with RoPE position rotation in a single "
            "in-place CUDA kernel. Baseline is the current SGLang `fused_inplace_qknorm_rope` "
            "CUDA implementation (templated by head_dim, rope_dim, is_neox, dtype)."
        ),
        shape_table_md="""\
| Preset | Model | dtype | total_tokens (B*S) | num_heads_q | num_heads_k | head_dim | rope_dim | is_neox | notes |
|---|---|---|---:|---:|---:|---:|---:|---|---|
| flux | FLUX.1-dev | bfloat16 | 4608 | 24 | 24 | 128 | 128 | False | 1024^2 @ patch=2; 4096 image + 512 text tokens |
| flux2 | FLUX.2-dev | bfloat16 | 4608 | 24 | 24 | 128 | 128 | False | 1024^2 @ patch=2; ~4608 joint tokens |
| qwen | Qwen-Image-2512 | bfloat16 | 4352 | 24 | 24 | 128 | 128 | True | 1024^2 transformer joint qkv |
| qwen-edit | Qwen-Image-Edit-2511 | bfloat16 | 4608 | 24 | 24 | 128 | 128 | True | image + edit conditioning |
| zimage | Z-Image-Turbo | bfloat16 | 4096 | 24 | 24 | 128 | 128 | False | residual-form modulation pipeline |
| wan-ti2v | Wan2.2-TI2V-5B | bfloat16 | 75600 | 24 | 24 | 128 | 128 | False | 720p, 81 frames, patch=(1,2,2) |
| wan-t2v | Wan2.2-T2V-A14B | bfloat16 | 75600 | 40 | 40 | 128 | 128 | False | 720p, 81 frames, A14B branch |
| wan-i2v | Wan2.2-I2V-A14B | bfloat16 | 75600 | 40 | 40 | 128 | 128 | False | 720p, 81 frames, image conditioning |
| ltx2 | LTX-2 | bfloat16 | 65520 | 24 | 24 | 128 | 96 | False | 1536x1024, 121 frames, split rotary, rope_dim<head_dim |
| hunyuanvideo | HunyuanVideo | bfloat16 | 33280 | 24 | 24 | 128 | 128 | False | 848x480, 65 frames |
| mova-720p | MOVA-720p | bfloat16 | 65536 | 24 | 24 | 128 | 128 | False | 720p talking-face, 193 frames |
| helios | Helios-Base | bfloat16 | 8448 | 16 | 16 | 128 | 128 | False | 640x384, 33 frames |
""",
        config_axes=[
            "head_dim (64 / 128 / 256)",
            "rope_dim (64 / 96 / 128, <= head_dim)",
            "is_neox (True / False)",
            "dtype (bfloat16 / float16)",
            "total_tokens range (4096 - 75600)",
            "num_heads (16 / 24 / 32 / 40)",
        ],
    ),
    Family(
        slug="diffusion_norm_infer__multi_shape",
        title="Inference-only LN/RMSN 2-pass kernel",
        op_type="layer_or_rms_norm_infer",
        sglang_targets=[
            "sglang.jit_kernel.diffusion.triton.norm:norm_infer",
            "sglang.jit_kernel.diffusion.triton.rmsnorm_onepass:triton_one_pass_rms_norm",
        ],
        cute_dsl=False,
        is_cuda_kernel=False,
        test_file="python/sglang/jit_kernel/tests/diffusion/test_qwen_image_modulation.py",
        description=(
            "Optimize the two SGLang diffusion inference-only norm kernels: `norm_infer` "
            "(2-pass LN/RMSN baseline) and `triton_one_pass_rms_norm` (tiled one-pass RMSN). "
            "Both consume 2D row tensors and run pure forward on the diffusion path."
        ),
        shape_table_md="""\
| Preset | Model | dtype | M (rows = B*S) | N (hidden) | norm_type | notes |
|---|---|---|---:|---:|---|---|
| flux | FLUX.1-dev | bfloat16 | 4608 | 3072 | layer | adaLN pre-norm path |
| flux2 | FLUX.2-dev | bfloat16 | 4608 | 3072 | layer | flux2 dit |
| qwen | Qwen-Image-2512 | bfloat16 | 4352 | 3072 | rms | RMSN pre-attn |
| qwen-edit | Qwen-Image-Edit-2511 | bfloat16 | 4608 | 3072 | rms | edit conditioning |
| zimage | Z-Image-Turbo | bfloat16 | 4096 | 3072 | layer | Z-Image modulation |
| wan-ti2v | Wan2.2-TI2V-5B | bfloat16 | 75600 | 3072 | rms | 720p video |
| wan-t2v | Wan2.2-T2V-A14B | bfloat16 | 75600 | 5120 | rms | A14B |
| wan-i2v | Wan2.2-I2V-A14B | bfloat16 | 75600 | 5120 | rms | A14B image |
| ltx2 | LTX-2 | bfloat16 | 65520 | 2048 | rms | 1536x1024 121 frames |
| hunyuanvideo | HunyuanVideo | bfloat16 | 33280 | 3072 | layer | 848x480 65 frames |
| mova-720p | MOVA-720p | bfloat16 | 65536 | 3072 | layer | 720p video |
| helios | Helios-Base | bfloat16 | 8448 | 2048 | layer | 640x384 33 frames |
""",
        config_axes=[
            "M (rows) in 1024..100000",
            "N (hidden) in 1024..8192",
            "norm_type (layer/rms)",
            "has_weight / has_bias",
            "dtype (bfloat16 / float16 / float32)",
        ],
    ),
    Family(
        slug="diffusion_group_norm_silu__multi_shape",
        title="Fused GroupNorm + SiLU for diffusion VAE",
        op_type="group_norm_silu",
        sglang_targets=[
            "sglang.jit_kernel.diffusion.triton.group_norm_silu:triton_group_norm_silu",
            "sglang.jit_kernel.diffusion.group_norm_silu:apply_group_norm_silu",
        ],
        cute_dsl=False,
        is_cuda_kernel=False,
        test_file="python/sglang/jit_kernel/tests/diffusion/test_group_norm_silu.py",
        description=(
            "Optimize the fused GroupNorm+SiLU path used by SGLang diffusion VAEs. The Triton "
            "kernel has a one-pass and a chunked implementation gated by group_size, plus a "
            "scalar-affine fast path. Inputs are 2D, 3D, 4D, or 5D depending on whether the "
            "VAE is image (2D/3D) or video (3D/5D)."
        ),
        shape_table_md="""\
| Preset | Model | dtype | x shape | num_groups | group_size | dimensionality | notes |
|---|---|---|---|---:|---:|---|---|
| flux | FLUX.1-dev | bfloat16 | (1, 128, 1024, 1024) | 32 | 4 | 4D | VAE decoder upsample stage |
| flux | FLUX.1-dev | bfloat16 | (1, 256, 512, 512) | 32 | 8 | 4D | VAE decoder mid |
| flux | FLUX.1-dev | bfloat16 | (1, 512, 256, 256) | 32 | 16 | 4D | VAE decoder block |
| flux2 | FLUX.2-dev | bfloat16 | (1, 128, 1024, 1024) | 32 | 4 | 4D | similar VAE decoder |
| qwen | Qwen-Image-2512 | bfloat16 | (1, 128, 1024, 1024) | 32 | 4 | 4D | Qwen-VAE decoder |
| zimage | Z-Image-Turbo | bfloat16 | (1, 128, 1024, 1024) | 32 | 4 | 4D | Z-Image VAE decoder |
| wan-ti2v | Wan2.2-TI2V-5B | bfloat16 | (1, 128, 21, 90, 160) | 32 | 4 | 5D | causal 3D VAE 720p decoder |
| wan-t2v | Wan2.2-T2V-A14B | bfloat16 | (1, 128, 21, 90, 160) | 32 | 4 | 5D | same 3D VAE shape |
| wan-i2v | Wan2.2-I2V-A14B | bfloat16 | (1, 128, 21, 90, 160) | 32 | 4 | 5D | I2V 3D VAE |
| ltx2 | LTX-2 | bfloat16 | (1, 128, 31, 64, 96) | 32 | 4 | 5D | LTX video VAE decoder |
| hunyuanvideo | HunyuanVideo | bfloat16 | (1, 128, 17, 60, 106) | 32 | 4 | 5D | 848x480 65f VAE |
| mova-720p | MOVA-720p | bfloat16 | (1, 128, 49, 90, 160) | 32 | 4 | 5D | 193f 720p VAE |
| helios | Helios-Base | bfloat16 | (1, 128, 9, 48, 80) | 32 | 4 | 5D | 33f VAE |
""",
        config_axes=[
            "dimensionality (2D / 3D / 4D / 5D)",
            "num_groups (commonly 32)",
            "channels per group (group_size) in 4..128",
            "spatial size (HxW or DxHxW) per group",
            "dtype (bfloat16 / float16 / float32)",
            "one-pass vs chunked (controlled by _LARGE_GROUP_THRESHOLD)",
            "scalar-affine fast path",
        ],
    ),
    Family(
        slug="diffusion_rotary_embedding__multi_shape",
        title="Standard and LTX-2 split rotary embeddings",
        op_type="rotary_embedding",
        sglang_targets=[
            "sglang.jit_kernel.diffusion.triton.rotary:apply_rotary_embedding",
            "sglang.jit_kernel.diffusion.triton.ltx2_rotary:apply_ltx2_split_rotary_emb",
        ],
        cute_dsl=False,
        is_cuda_kernel=False,
        test_file="python/sglang/jit_kernel/tests/test_rope.py",
        description=(
            "Optimize the two SGLang diffusion RoPE kernels: `apply_rotary_embedding` (standard "
            "interleaved / non-interleaved RoPE used by most DiTs) and `apply_ltx2_split_rotary_emb` "
            "(LTX-2 split rotary that consumes a 4D `(B, H, S, head_dim/2)` cos/sin layout)."
        ),
        shape_table_md="""\
| Preset | Model | kernel | dtype | x layout | total tokens | num_heads | head_dim | interleaved | notes |
|---|---|---|---|---|---:|---:|---:|---|---|
| flux | FLUX.1-dev | apply_rotary_embedding | bfloat16 | (B*S, H, D) | 4608 | 24 | 128 | False | joint qk RoPE |
| flux2 | FLUX.2-dev | apply_rotary_embedding | bfloat16 | (B*S, H, D) | 4608 | 24 | 128 | False | joint qk RoPE |
| qwen | Qwen-Image-2512 | apply_rotary_embedding | bfloat16 | (B*S, H, D) | 4352 | 24 | 128 | True | NeoX RoPE |
| qwen-edit | Qwen-Image-Edit-2511 | apply_rotary_embedding | bfloat16 | (B*S, H, D) | 4608 | 24 | 128 | True | edit RoPE |
| zimage | Z-Image-Turbo | apply_rotary_embedding | bfloat16 | (B*S, H, D) | 4096 | 24 | 128 | False | Z-Image RoPE |
| wan-ti2v | Wan2.2-TI2V-5B | apply_rotary_embedding | bfloat16 | (B*S, H, D) | 75600 | 24 | 128 | False | 720p RoPE |
| wan-t2v | Wan2.2-T2V-A14B | apply_rotary_embedding | bfloat16 | (B*S, H, D) | 75600 | 40 | 128 | False | A14B RoPE |
| wan-i2v | Wan2.2-I2V-A14B | apply_rotary_embedding | bfloat16 | (B*S, H, D) | 75600 | 40 | 128 | False | A14B RoPE |
| ltx2 | LTX-2 | apply_ltx2_split_rotary_emb | bfloat16 | (B, S, inner_dim) | 65520 | 24 | 128 | n/a | rope_dim=96, split half_dim |
| hunyuanvideo | HunyuanVideo | apply_rotary_embedding | bfloat16 | (B*S, H, D) | 33280 | 24 | 128 | False | 848x480 RoPE |
| mova-720p | MOVA-720p | apply_rotary_embedding | bfloat16 | (B*S, H, D) | 65536 | 24 | 128 | False | 720p RoPE |
| helios | Helios-Base | apply_rotary_embedding | bfloat16 | (B*S, H, D) | 8448 | 16 | 128 | False | 640x384 RoPE |
""",
        config_axes=[
            "head_dim (64 / 96 / 128 / 256)",
            "num_heads (16 / 24 / 32 / 40)",
            "interleaved (True / False)",
            "x layout: 3D (S,H,D) vs 4D (B,S,H,D)",
            "cos/sin shape: (S, D) vs (S, D/2) vs (B, H, S, D/2)",
            "split rotary (LTX-2): half_dim != head_dim/2 path",
            "total tokens range (4096 - 75600)",
            "dtype (bfloat16 / float16)",
        ],
    ),
    Family(
        slug="diffusion_fuse_scale_shift__multi_shape",
        title="Fused scale_shift + dual-modulation (Z-Image adaLN)",
        op_type="fuse_scale_shift",
        sglang_targets=[
            "sglang.jit_kernel.diffusion.triton.scale_shift:fuse_scale_shift_kernel",
            "sglang.jit_kernel.diffusion.triton.scale_shift:fuse_layernorm_scale_shift_gate_select01_kernel",
            "sglang.jit_kernel.diffusion.triton.scale_shift:fuse_residual_layernorm_scale_shift_gate_select01_kernel",
        ],
        cute_dsl=False,
        is_cuda_kernel=False,
        test_file="python/sglang/jit_kernel/tests/diffusion/test_qwen_image_modulation.py",
        description=(
            "Optimize the SGLang diffusion fused-modulation Triton kernels: "
            "`fuse_scale_shift_kernel` (x*(1+scale)+shift on 3D BLC inputs with optional 4D scale/shift), "
            "`fuse_layernorm_scale_shift_gate_select01_kernel` (LN + adaLN + gate, dual-modulation per token), "
            "and `fuse_residual_layernorm_scale_shift_gate_select01_kernel` (additional residual+gate input)."
        ),
        shape_table_md="""\
| Preset | Model | dtype | x shape (B,L,C) | scale/shift layout | dual-modulation | residual | notes |
|---|---|---|---|---|---|---|---|
| flux | FLUX.1-dev | bfloat16 | (1, 4608, 3072) | (B,C) | No | No | adaLN modulation in joint attention |
| flux2 | FLUX.2-dev | bfloat16 | (1, 4608, 3072) | (B,C) | No | No | flux2 adaLN |
| qwen | Qwen-Image-2512 | bfloat16 | (1, 4352, 3072) | (B,C) | Yes (select01) | No | dual-modulation select |
| qwen-edit | Qwen-Image-Edit-2511 | bfloat16 | (1, 4608, 3072) | (B,C) | Yes (select01) | No | dual-modulation with edit |
| zimage | Z-Image-Turbo | bfloat16 | (1, 4096, 3072) | (B,C) | Yes (select01) | Yes | residual+gate+dual-modulation |
| wan-ti2v | Wan2.2-TI2V-5B | bfloat16 | (1, 75600, 3072) | (B,F,1,C) | No | No | 4D scale/shift over frames |
| wan-t2v | Wan2.2-T2V-A14B | bfloat16 | (1, 75600, 5120) | (B,F,1,C) | No | No | A14B frames modulation |
| wan-i2v | Wan2.2-I2V-A14B | bfloat16 | (1, 75600, 5120) | (B,F,1,C) | No | No | A14B I2V frames modulation |
| ltx2 | LTX-2 | bfloat16 | (1, 65520, 2048) | (B,C) | No | No | LTX-2 modulation |
| hunyuanvideo | HunyuanVideo | bfloat16 | (1, 33280, 3072) | (B,F,1,C) | No | No | Hunyuan frames modulation |
| mova-720p | MOVA-720p | bfloat16 | (1, 65536, 3072) | (B,F,1,C) | No | No | MOVA frames |
| helios | Helios-Base | bfloat16 | (1, 8448, 2048) | (B,C) | No | No | small video |
""",
        config_axes=[
            "x shape: B in [1,2] * L in [4096..75600] * C in [2048..5120]",
            "scale/shift layout: (B,C) / (1,C) / (B,F,1,C) / scalar",
            "dual-modulation index path (Qwen-Image-Edit / Z-Image)",
            "residual+gate path (Z-Image residual block)",
            "BLOCK_L / BLOCK_C / num_warps / num_stages choice",
            "dtype (bfloat16 / float16 / float32)",
        ],
    ),
    Family(
        slug="diffusion_cutedsl_norm_tanh_mul_add__multi_shape",
        title="CuTe-DSL norm + tanh(scale) + shift (+ second-norm scale)",
        op_type="cutedsl_norm_tanh_mul_add",
        sglang_targets=[
            "sglang.jit_kernel.diffusion.cutedsl.norm_tanh_mul_add_norm_scale:fused_norm_tanh_mul_add",
            "sglang.jit_kernel.diffusion.cutedsl.norm_tanh_mul_add_norm_scale:fused_norm_tanh_mul_add_norm_scale",
        ],
        cute_dsl=True,
        is_cuda_kernel=False,
        test_file="python/sglang/jit_kernel/tests/diffusion/test_fused_norm_scale_shift.py",
        description=(
            "Optimize the CuTe-DSL `fused_norm_tanh_mul_add` and `fused_norm_tanh_mul_add_norm_scale` "
            "kernels used by Z-Image-style residual modulation. The kernels require D%256==0 and "
            "D<=8192 to enable vectorized LDG.128 loads, support layer/rms norm, and operate on "
            "(B,S,D) input with weight/bias and scale/shift in {1, D, 1D, BD, 11D, B1D, 1SD, BSD, BF1D}."
        ),
        shape_table_md="""\
| Preset | Model | dtype | x shape (B,S,D) | scale/shift layout | second norm scale | notes |
|---|---|---|---|---|---|---|
| zimage | Z-Image-Turbo | bfloat16 | (1, 4096, 3072) | (B,1,D) | yes for combined op | primary user |
| qwen | Qwen-Image-2512 | bfloat16 | (1, 4352, 3072) | (B,1,D) | optional | shared with Z-Image modulation |
| qwen-edit | Qwen-Image-Edit-2511 | bfloat16 | (1, 4608, 3072) | (B,1,D) | optional | edit conditioning |
| flux | FLUX.1-dev | bfloat16 | (1, 4608, 3072) | (B,1,D) | optional | adaLN compatibility |
| flux2 | FLUX.2-dev | bfloat16 | (1, 4608, 3072) | (B,1,D) | optional | flux2 |
| wan-ti2v | Wan2.2-TI2V-5B | bfloat16 | (1, 75600, 3072) | (B,F,1,D) | optional | 720p video |
| ltx2 | LTX-2 | bfloat16 | (1, 65520, 2048) | (B,1,D) | optional | LTX-2 modulation |
| hunyuanvideo | HunyuanVideo | bfloat16 | (1, 33280, 3072) | (B,F,1,D) | optional | 848x480 |
| mova-720p | MOVA-720p | bfloat16 | (1, 65536, 3072) | (B,F,1,D) | optional | MOVA 720p |
""",
        config_axes=[
            "D in {2048, 3072, 5120} (multiple of 256, <= 8192)",
            "B*S in 4096..75600",
            "norm_type (layer / rms)",
            "scale/shift layout: 1 / D / 1D / BD / 11D / B1D / 1SD / BSD / BF1D",
            "second-norm scale path enabled vs disabled",
            "dtype (bfloat16 / float16 / float32)",
        ],
    ),
    Family(
        slug="diffusion_cutedsl_norm_scale_shift__multi_shape",
        title="CuTe-DSL norm * (1+scale) + shift (+ residual + gate path)",
        op_type="cutedsl_norm_scale_shift",
        sglang_targets=[
            "sglang.jit_kernel.diffusion.cutedsl.scale_residual_norm_scale_shift:fused_norm_scale_shift",
            "sglang.jit_kernel.diffusion.cutedsl.scale_residual_norm_scale_shift:fused_scale_residual_norm_scale_shift",
        ],
        cute_dsl=True,
        is_cuda_kernel=False,
        test_file="python/sglang/jit_kernel/tests/diffusion/test_fused_norm_scale_shift.py",
        description=(
            "Optimize the CuTe-DSL `fused_norm_scale_shift` and `fused_scale_residual_norm_scale_shift` "
            "kernels. Both apply layer/rms norm followed by an adaLN-style scale-shift, with the "
            "residual variant also computing res_out = residual + gate * x. Shapes share the same "
            "D%256==0 and D<=8192 constraint as the tanh family."
        ),
        shape_table_md="""\
| Preset | Model | dtype | x shape (B,S,D) | scale/shift layout | residual+gate | notes |
|---|---|---|---|---|---|---|
| zimage | Z-Image-Turbo | bfloat16 | (1, 4096, 3072) | (B,1,D) | yes | residual modulation primary use |
| qwen | Qwen-Image-2512 | bfloat16 | (1, 4352, 3072) | (B,1,D) | optional | shared modulation |
| qwen-edit | Qwen-Image-Edit-2511 | bfloat16 | (1, 4608, 3072) | (B,1,D) | optional | edit modulation |
| flux | FLUX.1-dev | bfloat16 | (1, 4608, 3072) | (B,1,D) | optional | adaLN |
| flux2 | FLUX.2-dev | bfloat16 | (1, 4608, 3072) | (B,1,D) | optional | flux2 adaLN |
| wan-ti2v | Wan2.2-TI2V-5B | bfloat16 | (1, 75600, 3072) | (B,F,1,D) | optional | frames modulation |
| wan-t2v | Wan2.2-T2V-A14B | bfloat16 | (1, 75600, 5120) | (B,F,1,D) | optional | A14B frames modulation |
| wan-i2v | Wan2.2-I2V-A14B | bfloat16 | (1, 75600, 5120) | (B,F,1,D) | optional | A14B I2V modulation |
| ltx2 | LTX-2 | bfloat16 | (1, 65520, 2048) | (B,1,D) | optional | LTX-2 modulation |
| hunyuanvideo | HunyuanVideo | bfloat16 | (1, 33280, 3072) | (B,F,1,D) | optional | 848x480 modulation |
| mova-720p | MOVA-720p | bfloat16 | (1, 65536, 3072) | (B,F,1,D) | optional | MOVA modulation |
""",
        config_axes=[
            "D in {2048, 3072, 5120} (multiple of 256, <= 8192)",
            "B*S in 4096..75600",
            "norm_type (layer / rms)",
            "scale/shift layout: 1 / D / 1D / BD / 11D / B1D / 1SD / BSD / BF1D",
            "residual+gate path enabled (Z-Image residual block)",
            "dtype (bfloat16 / float16 / float32)",
        ],
    ),
]


ARCHS = [
    {
        "name": "b200",
        "title": "NVIDIA B200",
        "remote_skill": "ion-b200",
        "remote_host": "ion-b200",
        "remote_repo": "/home/sglang-omni/bbuf/repos/sglang",
        "remote_workspace": "/home/sglang-omni/bbuf/kda_runs",
        "container": "sglang_bbuf",
        "sm": "SM100",
        "ncu_set": "basic",
    },
    {
        "name": "h200",
        "title": "NVIDIA H200",
        "remote_skill": "ion8-h200 (or ion9-h200 as backup)",
        "remote_host": "ion8-h200",
        "remote_repo": "/home/sglang-omni/bbuf/repos/sglang",
        "remote_workspace": "/home/sglang-omni/bbuf/kda_runs",
        "container": "sglang_bbuf",
        "sm": "SM90",
        "ncu_set": "basic",
    },
]


def render_prompt(family: Family, arch: dict) -> str:
    slug = f"{arch['name']}_{family.slug}"
    targets_md = "\n".join(f"- `{t}`" for t in family.sglang_targets)
    config_md = "\n".join(f"- {axis}" for axis in family.config_axes)
    cutedsl_note = ""
    if family.cute_dsl:
        cutedsl_note = (
            "\nThis kernel is implemented in CuTe-DSL and currently requires `D % 256 == 0` "
            "and `D <= 8192`. Candidate implementations must keep these constraints or document "
            "any tightening / loosening in `interface.md`.\n"
        )
    cuda_note = ""
    if family.is_cuda_kernel:
        cuda_note = (
            "\nThe baseline is a native CUDA kernel (templated by head_dim, rope_dim, "
            "is_neox, dtype) loaded via JIT. The optimized candidate must also be a native "
            "C++/CUDA kernel built from workspace-owned `.cu`/`.cuh`/`.cpp`/`.h` sources, "
            "not pure Python.\n"
        )
    arch_title = arch["title"]
    arch_name = arch["name"]
    return textwrap.dedent(
        f"""\
        # KDA Prompt: {slug}

        Optimize the SGLang diffusion `{family.title}` kernel(s) for the full set of
        production diffusion-model shapes captured from the SGLang diffusion benchmark
        skill on {arch_title}. This prompt follows the Kernel Design Agents workflow
        with official Humanize, KernelWiki, and `ncu-report-skill` available.

        This is a multi-shape KDA prompt in the style of
        `BBuf/kernel-design-agents`: first recover the baseline and correctness
        contract, then run profiling-guided optimization, then specialize per shape
        bucket with a dispatcher when measured evidence justifies it.

        ## Kernel Information

        - Kernel folder: `{slug}`
        - Source project: SGLang (`python/sglang/jit_kernel/diffusion/`)
        - Description: {family.description}
        - Hardware target: {arch_title}
        - Wrapped baseline entry points:
        {targets_md}
        - Correctness oracle reference test:
          `{family.test_file}`
        - Promotion target: optimize toward the active hardware performance bound,
          not a fixed speedup multiplier. Report median-latency speedup over the
          current SGLang baseline as the geometric mean of per-shape speedups
          across the configured shape table below, but treat that value as an
          outcome metric rather than a pass/fail threshold.
        {cuda_note}{cutedsl_note}
        ## Workload Cases (Production Shapes)

        This section is populated by
        `scripts/diffusion_shape_capture/distribute_shapes.py` from live SGLang
        diffusion benchmark captures. Do not fill it from model configs or
        analytical shape estimates.

        No live call signatures are bundled in the generator template. Run a
        full-preset sweep with `kernel_shape_capture.py`, then rerun
        `distribute_shapes.py --input <captures.jsonl> --sweep-log <sweep.log>`
        before using this prompt for optimization.

        Humanize/RLCR instruction: do not determine, derive, broaden, or
        reinterpret optimization shapes during plan generation. The workload
        shape set must be exactly the rows inserted by `distribute_shapes.py`
        and the matching `docs/captured_shapes_<arch>.jsonl`.

        ## Configurable Optimization Axes

        Each candidate kernel/family may need different code paths or autotune
        configs for different points in this axis space:

        {config_md}

        The promotion target is per-shape correctness plus hardware-bound
        performance evidence across **all** configured shapes. A candidate is
        target-complete when benchmarks and profiler data show that each important
        shape bucket is close to its active bound (memory bandwidth, compute
        throughput, launch overhead, occupancy, or dependency/latency limit), or
        when a well-supported no-go explains why the remaining gap is not
        reachable inside this task boundary. Per-shape specialization is allowed
        and encouraged when profiler or benchmark evidence shows that one kernel
        cannot cover the whole axis space. See the Shape Specialization Policy
        below.

        ## Environment And Remote Rule

        Use the `{arch['remote_skill']}` remote GPU environment for all {arch_title}
        work. All CUDA, Python, pip, nvcc, build, test, benchmark, and Nsight Compute
        commands must run inside the existing `{arch['container']}` Docker container on
        `{arch['remote_host']}`, with an idle {arch_title} GPU selected.

        Before running GPU work, inspect `nvidia-smi` and choose a GPU with no active
        compute processes and no meaningful memory occupancy. Export that id as
        `REMOTE_GPU_ID` and use it consistently for the baseline, candidate,
        benchmark, profiler, and NCU commands in the current run.

        Use this command pattern for remote execution:

        ```bash
        ssh {arch['remote_host']} 'REMOTE_GPU_ID=<idle-gpu-id>; docker exec {arch['container']} bash -lc "CUDA_VISIBLE_DEVICES=${{REMOTE_GPU_ID}} <command>"'
        ```

        Do not run Python, pip, nvcc, builds, tests, benchmarks, or profiling
        directly on the `{arch['remote_host']}` host.

        When multiple sessions share the same remote container, create a task-owned
        remote workspace under:

        ```text
        {arch['remote_workspace']}/{slug}/<timestamp-or-session-id>
        ```

        Export it as `REMOTE_KDA_DIR`. Keep build outputs, profiler traces, NCU
        reports, captured tensors, and benchmark logs inside that directory.

        Before and after every benchmark or profile run, check GPU state and record
        the selected host, GPU id, and GPU model in `benchmark.csv` or
        `docs/draft.md`.

        ## Workspace Rule

        All work for this kernel task must happen inside the current prompt folder,
        the folder that contains this `prompt.md`.

        Required local files:

        - `src/`: optimized wrapper, native sources (CUDA `.cu`/`.cuh`/`.cpp` for the
          CUDA family, Triton/CuTe-DSL Python for the others), dispatcher code, and
          registration entrypoint.
        - `tests/`: correctness tests adapted from the SGLang reference test under
          `{family.test_file}`.
        - `docs/draft.md`: implementation-plan draft written before code changes.
        - `docs/captured_shapes_<arch>.jsonl`: captured shape JSONL from the diffusion
          benchmark sweep, copied into this folder.
        - `benchmark.csv`: every measured baseline vs candidate comparison.
        - `solutions.jsonl`: every candidate implementation, parent link, status,
          and evidence pointer.
        - `profile/`: profiler traces and summaries.
        - `ncu/`: Nsight Compute reports when collected.

        Keep SGLang checkouts as dependencies to inspect, run, or patch
        temporarily. The optimized implementation and evidence for this task stay
        local to this folder unless intentionally promoted later.

        ## Baseline Recovery And Correctness Harness

        Recover the baseline before writing optimized code:

        1. Inspect the SGLang baseline implementation file(s) corresponding to each
           wrapped entry point in `{family.sglang_targets[0].split(':')[0].replace('.', '/')}.py`.
        2. Build a reproducible baseline harness for every shape in the shape table.
        3. Adapt the SGLang reference correctness test `{family.test_file}` into
           `tests/test_correctness.py` of this folder, parameterized over the
           configured shape buckets.
        4. Capture or generate baseline inputs covering the relevant dtypes and
           layouts above.
        5. Preserve explicit NaN/Inf checks in every validator.
        6. Use dynamic numerical tolerances where applicable
           (SGLang-style: candidate error must not exceed a small multiple of the
           reference BF16/FP16 quantization noise vs FP32).

        The final candidate must pass correctness for every configured shape
        before benchmark claims count.

        ## Benchmark Requirements

        - Use warmup and repeated timing.
        - Report median latency, mean latency, std, min, p10, and p90 per shape.
        - Compare every candidate against the SGLang baseline from the same selected
          idle {arch_title} GPU and container environment.
        - Keep benchmark scripts and raw result logs in this folder.
        - Every claimed improvement must identify the candidate commit or file
          version and the exact command used to produce the result.
        - Use Nsight Compute when a correct candidate is not clearly target-complete
          or when profiler evidence would change the next edit.
        - Final claim must be the geometric mean of per-shape speedups across the
          full shape table, not the best-case shape alone.
        - Final promotion or no-go must include a roofline-style bound analysis:
          estimate the effective bytes moved and useful scalar/vector operations
          for each representative shape bucket, report achieved bandwidth and/or
          FLOP/s, and use profiler metrics to identify the active limiting resource.
          Do not continue RLCR solely to hit a fixed speedup number once the
          evidence shows the candidate is already near the attainable bound.
        - Benchmark the SHIPPING integration, symmetrically. The promotion number
          must come from the exact path the kernel will ship in, with the candidate
          and the baseline going through an IDENTICAL wrapper / dispatch / registration
          layer — only the device kernel may differ. Prefer the in-SGLang drop-in
          (candidate `.cuh` under the real, unchanged public op); never benchmark a
          side overlay that replaces or bypasses the public op against a baseline that
          keeps it.
        - Preserve every production requirement of the public entry point. If the
          SGLang op is a registered custom op (`@register_custom_op`, for torch.compile
          / CUDA-graph compatibility), the shipped integration MUST keep that
          registration. An integration that drops it (e.g. monkey-patching the public
          symbol with a plain Python callable) is NOT a valid promotion arbiter — it
          changes the production contract, so its number is not comparable to the
          baseline's.
        - Decompose every speedup into DEVICE vs HOST. Split the measured delta into
          the device-kernel change (admissible) and the host/integration-layer change
          (wrapper, dispatch, registration). A "win" that comes from removing a
          production-required host layer (e.g. dropping custom-op registration) is a
          FALSE ECONOMY, not a kernel improvement, and must not be claimed. Cross-check
          with a symmetric, same-process, interleaved A/B that isolates the device
          kernel.

        ## Prior Art Research Scope

        Before choosing an implementation strategy, inspect SGLang, CUTLASS/CuTe,
        CUDA samples, PyTorch, vLLM, TensorRT-LLM, FlashInfer, DeepGEMM, and
        public Blackwell or Hopper kernels for directly relevant ideas. Use
        KernelWiki when prior {arch['sm']}, CUTLASS, SGLang, or normalization /
        modulation / RoPE / group-norm evidence can guide a design choice.

        Record reviewed source paths, commits or installed versions, and which
        ideas were kept or rejected in `docs/draft.md` and `solutions.jsonl`.

        ## Optimization Exploration Policy

        Use the KDA-style exploration loop:

        - list candidate optimization directions in `docs/draft.md`;
        - rank them by expected benefit, implementation risk, and how directly
          they attack the measured bottleneck;
        - try each direction for a bounded number of focused iterations;
        - keep, revise, or reject each direction with correctness, benchmark, and
          NCU evidence;
        - maintain parent links in `solutions.jsonl` so later runs can reconstruct
          the search DAG.

        Consider {arch['sm']}-specific optimization paths:

        - `tcgen05` instructions or warp-specialized cooperative MMA where the
          kernel touches a small inner matmul,
        - TMEM / TMA / cluster shapes when the working set exceeds shared memory,
        - persistent or split scheduling along (rows, hidden, frames, groups),
        - vectorized loads/stores (LDG.128 / STG.128) keyed to dtype and stride,
        - shared-memory staging vs register-file pressure tradeoffs,
        - fused-epilogue patterns when the kernel chains norm + scale-shift +
          gate + residual.

        ## Shape Specialization Policy

        Shape-specialized kernels, template/config variants, and a dispatcher or
        autotune table are allowed when measured evidence shows that different
        shape buckets need different CTA, warpgroup, TMEM, or register-pressure
        tradeoffs.

        Record the dispatcher decision table with per-bucket baseline, candidate,
        latency, speedup, and promote/reject reason in `benchmark.csv` and a
        `docs/dispatch.md` note. Do not force a single universal kernel if
        evidence shows that different shape buckets need different tradeoffs.

        The shape buckets to consider include but are not limited to:

        - small image (B*S in 4096..6144, D in 2048..3072) - FLUX/Qwen-Image/Z-Image
        - large video (B*S in 33000..75600, D in 2048..5120) - Wan2.2/HunyuanVideo/MOVA/LTX-2
        - small video (B*S in 8000..16000, D in 2048..3072) - Helios
        - high-channel low-token (Wan A14B with D=5120) vs low-channel high-token (LTX-2 D=2048)

        ## Interface Contract

        Add the candidate under `src/` and expose:

        ```text
        src/register.py
        ```

        with:

        ```python
        KERNEL_SLUG = "{slug}"
        OP_TYPE = "{family.op_type}"

        def optimized_wrapper(*args, **kwargs):
            ...

        def register() -> dict:
            return {{
                "name": KERNEL_SLUG,
                "op_type": OP_TYPE,
                "callable": optimized_wrapper,
                "version": "dev",
                "source": __file__,
            }}
        ```

        `optimized_wrapper` must preserve the recovered SGLang callsite contract and
        fall back to the baseline implementation for unsupported shapes, dtypes,
        layouts, devices, normalization types, or feature flags. See
        `interface.md` for the exact signature contract to be recovered from the
        baseline.

        ## Required Workflow

        1. Confirm the current directory is this kernel folder.
        2. Read `../../external/KernelWiki/SKILL.md` and
           `../../external/ncu-report-skill/SKILL.md` from this kernel folder.
        3. Recover the SGLang baseline path, tensor contract, and exact benchmark
           command for every shape in the shape table.
        4. Copy the captured shape JSONL into `docs/captured_shapes_<arch>.jsonl`.
        5. Write an implementation-plan draft to `docs/draft.md`.
        6. Run official Humanize plan generation on that draft.
        7. Start official Humanize RLCR from this kernel folder.
        8. Do not implement kernels, run long benchmarks, or collect NCU evidence
           before RLCR is active.
        9. Record every candidate in `solutions.jsonl` and every performance result
           in `benchmark.csv`.

        ## Completion Bar

        The work is complete only when:

        - correctness tests pass for every configured shape;
        - every dispatched variant is correct for its assigned shape bucket;
        - {arch_title} benchmark evidence reports geometric-mean median-latency
          speedup over the SGLang baseline across all configured shape buckets;
        - roofline-style analysis and NCU evidence explain the improvement,
          blocker, active hardware bound, and why the final candidate is close to
          the attainable performance limit for the important shape buckets, or a
          well-supported no-go explains why no defensible path remains under the
          available workspace;
        - `prompt.md`, `interface.md`, `benchmark.csv`, and `solutions.jsonl` are
          updated with the final result.
        """
    )


def render_interface(family: Family, arch: dict) -> str:
    slug = f"{arch['name']}_{family.slug}"
    targets_md = "\n".join(f"- `{t}`" for t in family.sglang_targets)
    return textwrap.dedent(
        f"""\
        # Interface: {slug}

        - Kernel slug: `{slug}`
        - Op type: `{family.op_type}`
        - Target GPU: {arch['title']}
        - Wrapped SGLang entry points:
        {targets_md}

        ## Export

        Provide:

        ```text
        src/register.py
        ```

        with:

        ```python
        KERNEL_SLUG = "{slug}"
        OP_TYPE = "{family.op_type}"

        def optimized_wrapper(*args, **kwargs):
            ...

        def register() -> dict:
            return {{
                "name": KERNEL_SLUG,
                "op_type": OP_TYPE,
                "callable": optimized_wrapper,
                "version": "dev",
                "source": __file__,
            }}
        ```

        `optimized_wrapper` must preserve the recovered SGLang callsite contract
        for every wrapped entry point. It must fall back to the baseline
        implementation for any shape, dtype, layout, device, normalization type,
        or feature flag that is not part of the configured shape table.

        The exact public signature for each wrapped entry point should be filled
        after baseline recovery. Typical wrappers for this family accept the same
        positional and keyword arguments as the SGLang baseline (see `prompt.md`),
        plus optional `*, dispatcher_hint=` keyword for dispatcher overrides.

        ## Evidence Requirements

        Before promotion, update this file with:

        - final wrapper signature(s);
        - per-shape dispatch table (which underlying candidate kernel handles
          which shape bucket);
        - fallback cases;
        - PyTorch-FP32 or `_reference()` tolerance methodology used in tests;
        - benchmark command and latency formula;
        - source lineage for copied or ported helper code.
        """
    )


def render_register(slug: str, op_type: str) -> str:
    return textwrap.dedent(
        f"""\
        \"\"\"Registration stub for the {slug} KDA task.

        Agents should replace ``optimized_wrapper`` with the recovered
        benchmark-compatible candidate during implementation.
        \"\"\"

        from __future__ import annotations

        from typing import Any


        KERNEL_SLUG = "{slug}"
        OP_TYPE = "{op_type}"


        def optimized_wrapper(*args: Any, **kwargs: Any) -> Any:
            raise NotImplementedError(
                "Fill optimized_wrapper after recovering the SGLang baseline contract."
            )


        def register() -> dict[str, Any]:
            return {{
                "name": KERNEL_SLUG,
                "op_type": OP_TYPE,
                "callable": optimized_wrapper,
                "version": "dev",
                "source": __file__,
            }}
        """
    )


BENCHMARK_PY_TEMPLATE = """\
#!/usr/bin/env python3
\"\"\"Isolated benchmark scaffold for ``{slug}``.

Fill ``tests/test_correctness.py`` first. This script reuses its cases, baseline,
and candidate callables, then appends summary rows to ``benchmark.csv``.
\"\"\"

from __future__ import annotations

import csv
import importlib.util
import math
import statistics
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

try:
    import torch
except ImportError:  # pragma: no cover
    torch = None


KERNEL_SLUG = "{slug}"
KERNEL_DIR = Path(__file__).resolve().parent


def _load_correctness_module():
    test_py = KERNEL_DIR / "tests" / "test_correctness.py"
    spec = importlib.util.spec_from_file_location("kda_correctness_scaffold", test_py)
    assert spec is not None and spec.loader is not None, test_py
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _sync() -> None:
    if torch is not None and torch.cuda.is_available():
        torch.cuda.synchronize()


def _time_call(fn: Callable[[dict[str, Any]], Any], case: dict[str, Any], *, warmup: int, iters: int) -> list[float]:
    for _ in range(warmup):
        fn(case)
    _sync()
    samples = []
    for _ in range(iters):
        start = time.perf_counter()
        fn(case)
        _sync()
        samples.append((time.perf_counter() - start) * 1e6)
    return samples


def _summary(samples: list[float]) -> dict[str, float]:
    ordered = sorted(samples)

    def pct(p: float) -> float:
        index = min(len(ordered) - 1, max(0, round((len(ordered) - 1) * p)))
        return ordered[index]

    return {{
        "median_us": statistics.median(ordered),
        "mean_us": statistics.mean(ordered),
        "std_us": statistics.pstdev(ordered) if len(ordered) > 1 else 0.0,
        "min_us": ordered[0],
        "p10_us": pct(0.10),
        "p90_us": pct(0.90),
        "p95_us": pct(0.95),
        "max_us": ordered[-1],
    }}


def _geom_mean(values: list[float]) -> float:
    cleaned = [v for v in values if math.isfinite(v) and v > 0]
    if not cleaned:
        return float("nan")
    return math.exp(sum(math.log(v) for v in cleaned) / len(cleaned))


def main() -> int:
    correctness = _load_correctness_module()
    cases = correctness.make_cases()
    if not cases:
        raise SystemExit("No benchmark cases. Fill tests/test_correctness.py first.")

    speedups = []
    csv_path = KERNEL_DIR / "benchmark.csv"
    with csv_path.open("a", newline="") as f:
        writer = csv.writer(f)
        for case in cases:
            warmup = int(case.get("warmup", 25))
            iters = int(case.get("iters", 100))
            baseline_samples = _time_call(correctness.baseline, case, warmup=warmup, iters=iters)
            candidate_samples = _time_call(correctness.candidate, case, warmup=warmup, iters=iters)
            b = _summary(baseline_samples)
            c = _summary(candidate_samples)
            speedup = (b["median_us"] / c["median_us"]) if c["median_us"] > 0 else float("nan")
            speedups.append(speedup)
            now = datetime.now(timezone.utc).isoformat()
            case_name = case.get("name", case.get("shape", "unknown"))
            writer.writerow([
                now,
                case.get("candidate", "baseline_vs_candidate"),
                case_name,
                "median_us",
                f"{{b['median_us']:.6f}}",
                f"{{c['median_us']:.6f}}",
                f"{{speedup:.6f}}x" if math.isfinite(speedup) else "",
                (
                    f"baseline_mean_us={{b['mean_us']:.6f}} cand_mean_us={{c['mean_us']:.6f}} "
                    f"cand_p10={{c['p10_us']:.6f}} cand_p90={{c['p90_us']:.6f}} "
                    f"iters={{iters}} slug={{KERNEL_SLUG}}"
                ),
            ])
            print(case_name, "speedup_x", speedup)
        writer.writerow([
            datetime.now(timezone.utc).isoformat(),
            "geomean",
            "all_configured_shapes",
            "geomean_speedup_x",
            "",
            "",
            f"{{_geom_mean(speedups):.6f}}x",
            f"slug={{KERNEL_SLUG}}",
        ])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
"""


TESTS_PY_TEMPLATE = """\
\"\"\"Correctness scaffold for ``{slug}``.

This file is intentionally skipped unless ``KDA_RUN_CORRECTNESS=1`` is set.

Required agent edits:
- replace ``make_cases()`` with the full configured shape list from
  ``prompt.md``;
- implement ``baseline(case)`` by calling the wrapped SGLang baseline entry
  points listed in ``prompt.md`` (treat that as the semantic oracle for this
  task and cross-check against a PyTorch FP32 reference where practical);
- keep ``candidate(case)`` compatible with ``src/register.py``;
- use dynamic BF16/FP16-aware tolerances where applicable.
\"\"\"

from __future__ import annotations

import importlib.util
import os
from pathlib import Path
from typing import Any

import pytest

try:
    import torch
except ImportError:  # pragma: no cover - CUDA env owns the real run
    torch = None


KERNEL_SLUG = "{slug}"
OP_TYPE = "{op_type}"
KERNEL_DIR = Path(__file__).resolve().parents[1]

pytestmark = pytest.mark.skipif(
    os.environ.get("KDA_RUN_CORRECTNESS") != "1",
    reason="Set KDA_RUN_CORRECTNESS=1 after the SGLang baseline cases are filled.",
)


def _load_register_module():
    register_py = KERNEL_DIR / "src" / "register.py"
    spec = importlib.util.spec_from_file_location(
        f"kda_kernel_{{KERNEL_SLUG}}_register", register_py
    )
    assert spec is not None and spec.loader is not None, register_py
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def make_cases() -> list[dict[str, Any]]:
    \"\"\"Return all configured correctness/benchmark cases.

    The list must cover every shape bucket recorded in ``prompt.md``. Each case
    typically looks like::

        {{
            "name": "flux__bf16__B1S4608D3072",
            "model": "flux",
            "args": (...),
            "kwargs": {{...}},
            "atol": 5e-2,
            "rtol": 5e-2,
            "warmup": 25,
            "iters": 100,
        }}

    Returning an empty list keeps the scaffold skipped.
    \"\"\"

    return []


def baseline(case: dict[str, Any]) -> Any:
    \"\"\"Return the SGLang baseline result for one configured case.\"\"\"

    raise NotImplementedError(
        "Call the SGLang baseline entry point(s) listed in prompt.md as the oracle."
    )


def candidate(case: dict[str, Any]) -> Any:
    module = _load_register_module()
    wrapper = getattr(module, "optimized_wrapper")
    args = case.get("args", ())
    kwargs = case.get("kwargs", {{}})
    return wrapper(*args, **kwargs)


def _assert_no_nan_inf(value: Any, *, path: str) -> None:
    if torch is not None and isinstance(value, torch.Tensor):
        assert not torch.isnan(value).any(), f"{{path}} contains NaN"
        assert not torch.isinf(value).any(), f"{{path}} contains Inf"
    elif isinstance(value, (tuple, list)):
        for i, item in enumerate(value):
            _assert_no_nan_inf(item, path=f"{{path}}[{{i}}]")
    elif isinstance(value, dict):
        for key, item in value.items():
            _assert_no_nan_inf(item, path=f"{{path}}.{{key}}")


def _assert_close(actual: Any, expected: Any, *, case: dict[str, Any], path: str = "out") -> None:
    atol = case.get("atol", 5e-2)
    rtol = case.get("rtol", 5e-2)
    _assert_no_nan_inf(actual, path=path)
    if torch is not None and isinstance(actual, torch.Tensor):
        assert isinstance(expected, torch.Tensor), f"{{path}} expected tensor, got {{type(expected)}}"
        assert actual.shape == expected.shape, f"{{path}} shape {{actual.shape}} != {{expected.shape}}"
        torch.testing.assert_close(actual.float(), expected.float(), atol=atol, rtol=rtol)
        return
    if isinstance(actual, (tuple, list)):
        assert isinstance(expected, type(actual)), f"{{path}} type mismatch"
        assert len(actual) == len(expected), f"{{path}} length mismatch"
        for i, (a_item, e_item) in enumerate(zip(actual, expected)):
            _assert_close(a_item, e_item, case=case, path=f"{{path}}[{{i}}]")
        return
    if isinstance(actual, dict):
        assert isinstance(expected, dict), f"{{path}} expected dict"
        assert actual.keys() == expected.keys(), f"{{path}} keys mismatch"
        for key in actual:
            _assert_close(actual[key], expected[key], case=case, path=f"{{path}}.{{key}}")
        return
    assert actual == expected, f"{{path}} value mismatch"


def test_register_metadata() -> None:
    module = _load_register_module()
    assert hasattr(module, "register")
    spec = module.register()
    assert spec["name"] == KERNEL_SLUG
    assert spec["op_type"] == OP_TYPE
    assert callable(spec["callable"])


def test_correctness_cases() -> None:
    cases = make_cases()
    assert cases, "No correctness cases recovered. Fill make_cases() before optimizing."
    for case in cases:
        expected = baseline(case)
        actual = candidate(case)
        _assert_close(actual, expected, case=case, path=case.get("name", "out"))
"""


README_TEMPLATE = """\
# {slug}

KDA-style task folder for optimizing the SGLang diffusion
**{title}** kernel(s) on {arch_title}.

See `prompt.md` for the task contract, `interface.md` for the expected local
candidate interface, and `tests/test_correctness.py` for the correctness
oracle scaffold.

Wrapped SGLang baseline entry points:
{targets_md}

Reference SGLang test used as the correctness oracle:
`{test_file}`

Promotion target: optimize toward the active hardware performance bound across
all configured shape buckets. Report geometric-mean speedup over the SGLang
baseline, but use roofline-style bandwidth/FLOP/s evidence rather than a fixed
speedup multiplier as the completion criterion.
"""


def write_task(family: Family, arch: dict) -> Path:
    slug = f"{arch['name']}_{family.slug}"
    folder = KERNELS_DIR / slug
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "src").mkdir(exist_ok=True)
    (folder / "tests").mkdir(exist_ok=True)
    (folder / "docs").mkdir(exist_ok=True)
    (folder / "profile").mkdir(exist_ok=True)
    (folder / "ncu").mkdir(exist_ok=True)
    (folder / "prompt.md").write_text(render_prompt(family, arch))
    (folder / "interface.md").write_text(render_interface(family, arch))
    (folder / "benchmark.py").write_text(BENCHMARK_PY_TEMPLATE.format(slug=slug))
    (folder / "tests" / "test_correctness.py").write_text(
        TESTS_PY_TEMPLATE.format(slug=slug, op_type=family.op_type)
    )
    (folder / "src" / "__init__.py").write_text(
        f'"""Local candidate package for the {slug} KDA task."""\n'
    )
    (folder / "src" / "register.py").write_text(render_register(slug, family.op_type))
    targets_md = "\n".join(f"- `{t}`" for t in family.sglang_targets)
    (folder / "README.md").write_text(
        README_TEMPLATE.format(
            slug=slug,
            title=family.title,
            arch_title=arch["title"],
            targets_md=targets_md,
            test_file=family.test_file,
        )
    )
    (folder / "benchmark.csv").touch()
    (folder / "solutions.jsonl").touch()
    return folder


def main() -> None:
    KERNELS_DIR.mkdir(parents=True, exist_ok=True)
    created = []
    for family in FAMILIES:
        for arch in ARCHS:
            folder = write_task(family, arch)
            created.append(folder)
    for folder in created:
        print(folder.relative_to(REPO_ROOT))


if __name__ == "__main__":
    main()
