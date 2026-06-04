# Diffusion Correctness Contract

This document lists the canonical regression grids each diffusion task must
cover in addition to the production workloads in
`diffusion_benchmark_shape_coverage.md`.

Use these grids to populate task-local `bench/correctness.py` tests. The tests
may be implemented against the copied local baseline and an independent
PyTorch/math oracle; they must not import, patch, or monkey-patch SGLang during
task benchmark runtime.

## QKNorm + RoPE

Tasks:

- `b200_diffusion_qknorm_rope__multi_shape`
- `h200_diffusion_qknorm_rope__multi_shape`

Canonical source: `python/sglang/jit_kernel/tests/diffusion/test_qknorm_rope.py`.

Regression grid:

- `batch_size`: every power of two in `[1, 4096]`, plus `x + 1` for each,
  plus `[1, 9, 129, 257, 2049, 4097]`.
- `num_heads`: `[8, 16, 24, 32]`.
- `head_dim`: `[64, 128, 256]`.
- `rope_dim`: `{64: [64], 128: [64, 128], 256: [64, 128, 256]}`.
- `is_neox`: `[False, True]`; when `True`, only valid rotary-lane
  configurations are expected.
- `position_dtype`: `torch.int32` and `torch.int64`.
- `dtype`: `torch.bfloat16`.
- `eps`: `1e-6`.
- Tolerance: `atol=8e-2`, `rtol=1e-2`.

Oracle: SGLang-style Q/K normalization followed by FlashInfer-style RoPE with a
cos/sin cache.

## Norm Infer

Tasks:

- `b200_diffusion_norm_infer__multi_shape`
- `h200_diffusion_norm_infer__multi_shape`

Canonical source:
`python/sglang/jit_kernel/tests/diffusion/test_qwen_image_modulation.py`.

Regression grid for `norm.norm_infer`:

- `batch_size`: `[1, 2, 4]`.
- `seq_len`: `[6, 33, 128, 257]`.
- `hidden_size`: `[512, 1024, 1536, 3072]`.
- `dtype`: `torch.float16`, `torch.bfloat16`, `torch.float32`.
- `eps`: `1e-6`.
- `is_rms_norm`: explicit argument; include LayerNorm rows and RMSNorm rows
  when the local task adapter supports both.
- Tolerance: `atol=5e-2`, `rtol=5e-2` for non-fp32; `1e-5` for fp32.

Cross-check `rmsnorm_onepass.triton_one_pass_rms_norm` on row counts derived
from the same grid and on production per-head rows such as `(4096, 128)` and
`(16384, 128)`.

## GroupNorm + SiLU

Tasks:

- `b200_diffusion_group_norm_silu__multi_shape`
- `h200_diffusion_group_norm_silu__multi_shape`

Canonical source:
`python/sglang/jit_kernel/tests/diffusion/test_group_norm_silu.py`.

Regression grid:

- 2D image case: `(2, 64, 32, 32)`, `num_groups=32`.
- 3D video case: `(1, 64, 4, 16, 16)`, `num_groups=32`.
- Token case: `(4, 128)`, `num_groups=32`.
- Large-tile case: `(1, 128, 20, 256, 256)`, `num_groups=32`.
- `dtype`: `torch.float16`, `torch.bfloat16`, `torch.float32`.
- Tolerance:
  - fp16: `atol=3e-3`, `rtol=3e-3`;
  - bf16: `atol=7e-2`, `rtol=2e-2`;
  - fp32: `atol=1e-5`, `rtol=1e-5`.

Oracle: `silu(group_norm(x, num_groups, weight, bias, eps=1e-5))`.

The wrapper-style `apply_group_norm_silu` path should cover the 2D and 3D rows
for fp16 and bf16.

## Rotary Embedding

Tasks:

- `b200_diffusion_rotary_embedding__multi_shape`
- `h200_diffusion_rotary_embedding__multi_shape`

Canonical source: `python/sglang/jit_kernel/tests/test_rope.py`.

Regression grid for standard `apply_rotary_embedding`:

- `batch_size` / total tokens: powers of two in `[1, 2048]`, plus
  `[1, 129, 2048, 2049]`.
- `num_kv_heads`: `[1, 2, 8]`.
- `gqa_ratio`: `[1, 4, 8]`; `num_qo_heads = num_kv_heads * gqa_ratio`.
- `rope_dim`: `[64, 128, 256, 512]`.
- `is_neox`: `[False, True]`.
- `dtype`: `torch.bfloat16`.
- Include both `torch.int32` and `torch.int64` positions when positions are part
  of the local adapter path.
- Tolerance: `atol=1e-2`, `rtol=1e-2`.

Oracle: FlashInfer-style `apply_rope_with_cos_sin_cache_inplace`.

For `apply_ltx2_split_rotary_emb`, use the production split-rotary rows from
`diffusion_benchmark_shape_coverage.md` as the regression contract.

## Scale Shift

Tasks:

- `b200_diffusion_fuse_scale_shift__multi_shape`
- `h200_diffusion_fuse_scale_shift__multi_shape`

Canonical source:
`python/sglang/jit_kernel/tests/diffusion/test_qwen_image_modulation.py`.

Regression grid:

- `batch_size`: `[1, 2, 4]`.
- `seq_len`: `[6, 33, 128, 257]`.
- `hidden_size`: `[512, 1024, 1536, 3072]`.
- `dtype`: `torch.float16`, `torch.bfloat16`, `torch.float32`.
- `eps`: `1e-6`.
- `scale0`, `shift0`, `gate0`, `scale1`, `shift1`, `gate1`: each shaped
  `(B, C)`.
- `index`: shaped `(B, L)`, covering the dual-modulation select path.
- Residual and residual-gate rows cover
  `fuse_residual_layernorm_scale_shift_gate_select01_kernel`.
- Tolerance: `atol=5e-2`, `rtol=5e-2` for non-fp32; `1e-5` for fp32.

The simple `fuse_scale_shift_kernel` must also cover both 2D `(B, C)` and 4D
`(B, F, 1, C)` scale/shift layouts.

## CuTe DSL Norm + Tanh + Mul + Add

Tasks:

- `b200_diffusion_cutedsl_norm_tanh_mul_add__multi_shape`
- `h200_diffusion_cutedsl_norm_tanh_mul_add__multi_shape`

Canonical source:
`python/sglang/jit_kernel/tests/diffusion/test_fused_norm_scale_shift.py`.

Regression grid:

- `SHAPES = [(B, S, F, D)]`: `[(1, 1024, 8, 3072), (4, 512, 16, 3072)]`.
- `dtype`: `torch.float16`, `torch.bfloat16`, `torch.float32`.
- `norm_type`: `["layer", "rms"]`.
- `affine_mode`: `["D", "NAT"]`.
- `scale/shift` layouts: `["BSD", "1", "1SD", "BD", "B1D", "D", "1D",
  "11D", "BF1D"]`.
- `D % 256 == 0` and `D <= 8192`.
- `eps`: `1e-5`.
- Tolerance: `atol=5e-2`, `rtol=5e-2` for non-fp32; `1e-5` for fp32.

Oracle: layer/RMS norm followed by `* tanh(scale) + shift`. The second
norm-scale variant adds `weight2`, `bias2`, and `scale2` over the same grid.

## CuTe DSL Norm Scale Shift

Tasks:

- `b200_diffusion_cutedsl_norm_scale_shift__multi_shape`
- `h200_diffusion_cutedsl_norm_scale_shift__multi_shape`

Canonical source:
`python/sglang/jit_kernel/tests/diffusion/test_fused_norm_scale_shift.py`.

Regression grid:

- `SHAPES = [(B, S, F, D)]`: `[(1, 1024, 8, 3072), (4, 512, 16, 3072)]`.
- `dtype`: `torch.float16`, `torch.bfloat16`, `torch.float32`.
- `norm_type`: `["layer", "rms"]`.
- `affine_mode`: `["D", "NAT"]`.
- `scale/shift` layouts: `["BSD", "1", "1SD", "BD", "B1D", "D", "1D",
  "11D", "BF1D"]`.
- `BF1D` layout requires `S % F == 0`; include a rejecting validator row for
  non-divisible frames.
- `D % 256 == 0` and `D <= 8192`.
- `eps`: `1e-5`.
- Tolerance: `atol=5e-2`, `rtol=5e-2` for non-fp32; `1e-5` for fp32.

Oracle: `norm(x) * (1 + scale) + shift`, with scale/shift broadcasting across
the listed layouts. The residual variant additionally consumes `residual` and
`gate` and outputs both `y` and `res_out`.
