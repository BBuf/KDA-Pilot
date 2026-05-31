"""Inject canonical-test-shape sections into each diffusion task prompt.

Each SGLang reference test enumerates the shape buckets the kernel must cover
in CI. Surface those enumerations directly inside the task prompt so the agent
sees the regression-shape contract alongside the production-shape contract.

The new section lands as "## Canonical Regression Shapes (from SGLang test)"
just after "## Configurable Optimization Axes". Idempotent: if the section
already exists it is rewritten in place.
"""

from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
KERNELS_DIR = REPO_ROOT / "kernels"

# task-family slug -> markdown block to inject
CANONICAL_SECTIONS: dict[str, str] = {
    "diffusion_qknorm_rope__multi_shape": (
        "## Canonical Regression Shapes (from SGLang test)\n"
        "\n"
        "Source: `python/sglang/jit_kernel/tests/diffusion/test_qknorm_rope.py`.\n"
        "Every candidate must still pass this enumerated grid in nightly /\n"
        "`base-b-kernel-unit-1-gpu-large` CI:\n"
        "\n"
        "- `batch_size` (== total tokens before view): every power of two in `[1, 4096]`\n"
        "  plus `x+1` for each, plus CI-extra `[1, 9, 129, 257, 2049, 4097]`.\n"
        "- `num_heads`: `[8, 16, 24, 32]` (CI subset `[8, 24]`).\n"
        "- `head_dim`: `[64, 128, 256]`.\n"
        "- `rope_dim`: `{64: [64], 128: [64, 128], 256: [64, 128, 256]}` per `head_dim`.\n"
        "- `is_neox`: `[False, True]`; when `True`, only `rope_dim` values yielding a power-of-two\n"
        "  rotary-lane count are valid (see `can_use_fused_inplace_qknorm_rope` gate).\n"
        "- `position_dtype`: `[torch.int32, torch.int64]`.\n"
        "- `dtype`: `torch.bfloat16`; `eps=1e-6`; tolerance `ATOL=8e-2, RTOL=1e-2`.\n"
        "- Oracle: SGLang `fused_inplace_qknorm` + `flashinfer.rope.apply_rope_with_cos_sin_cache_inplace`.\n"
        "\n"
        "The candidate kernel must support every `(batch_size, num_heads, head_dim, rope_dim, is_neox, position_dtype)`\n"
        "tuple above or fall back to the SGLang baseline for the unsupported tail.\n"
    ),
    "diffusion_norm_infer__multi_shape": (
        "## Canonical Regression Shapes (from SGLang test)\n"
        "\n"
        "Source: `python/sglang/jit_kernel/tests/diffusion/test_qwen_image_modulation.py`\n"
        "(this is the file that exercises `norm_infer` end-to-end as part of the Z-Image / Qwen-Image\n"
        "select01 dual-modulation baseline).\n"
        "\n"
        "- `batch_size`: `[1, 2, 4]` (CI subset `[1, 2]`).\n"
        "- `seq_len`: `[6, 33, 128, 257]` (CI subset `[6, 128]`).\n"
        "- `hidden_size`: `[512, 1024, 1536, 3072]` (CI subset `[512, 3072]`).\n"
        "- `dtype`: `[torch.float16, torch.bfloat16, torch.float32]` (CI subset `[fp16, bf16]`).\n"
        "- `eps`: `1e-6`.\n"
        "- `is_rms_norm`: explicit kernel argument; the test uses `False` (LayerNorm).\n"
        "- Tolerance: `(atol=5e-2, rtol=5e-2)` for non-fp32, `1e-5` for fp32.\n"
        "\n"
        "Cross-validate `triton_one_pass_rms_norm` on the same row counts (`M = B*S`) and on per-head tiles\n"
        "`(4096, 128)` / `(16384, 128)` (the live captures from Z-Image).\n"
    ),
    "diffusion_group_norm_silu__multi_shape": (
        "## Canonical Regression Shapes (from SGLang test)\n"
        "\n"
        "Source: `python/sglang/jit_kernel/tests/diffusion/test_group_norm_silu.py`.\n"
        "\n"
        "- 2D / 3D / 5D test cases:\n"
        "  - `(2, 64, 32, 32)`, `num_groups=32`, id=`image_2d`.\n"
        "  - `(1, 64, 4, 16, 16)`, `num_groups=32`, id=`video_3d`.\n"
        "  - `(4, 128)`, `num_groups=32`, id=`token_2d`.\n"
        "- Large-tile bf16 case: `(1, 128, 20, 256, 256)`, `num_groups=32`, id=`large_tile`.\n"
        "- `dtype`: `[torch.float16, torch.bfloat16, torch.float32]`.\n"
        "- Tolerance: `(atol=3e-3, rtol=3e-3)` fp16; `(7e-2, 2e-2)` bf16; `(1e-5, 1e-5)` fp32.\n"
        "- Oracle: `F.silu(F.group_norm(x, num_groups, weight, bias, eps=1e-5))`.\n"
        "- The wrapper test (`apply_group_norm_silu(x, nn.GroupNorm(...), nn.SiLU())`) only runs on the 2D / 3D\n"
        "  shapes and `[fp16, bf16]`.\n"
        "\n"
        "Promotion candidates must clear both the regression grid above and the production VAE shapes in\n"
        "the workload table.\n"
    ),
    "diffusion_rotary_embedding__multi_shape": (
        "## Canonical Regression Shapes (from SGLang test)\n"
        "\n"
        "Source: `python/sglang/jit_kernel/tests/test_rope.py` (standard `apply_rotary_embedding` enumeration).\n"
        "\n"
        "- `batch_size` (== total tokens): `[1, 2, 4, ..., 2048]` (powers of two) plus `[1, 129, 2048, 2049]` CI-extra.\n"
        "- `num_kv_heads`: `[1, 2, 8]` (CI subset `[1, 8]`).\n"
        "- `gqa_ratio`: `[1, 4, 8]` (CI subset `[1, 8]`). `num_qo_heads = num_kv_heads * gqa_ratio`.\n"
        "- `rope_dim`: `[64, 128, 256, 512]` (CI subset `[64, 256]`).\n"
        "- `is_neox`: `[False, True]`.\n"
        "- `dtype`: bfloat16 default plus mixed `[int32, int64]` for the `positions` dtype edge case.\n"
        "- Oracle: FlashInfer `apply_rope_with_cos_sin_cache_inplace`. Tolerance `1e-2` abs/rel.\n"
        "\n"
        "For the LTX-2 split-rotary variant (`apply_ltx2_split_rotary_emb`) there is no dedicated SGLang test;\n"
        "the empirical shapes captured from the `ltx2` benchmark preset are the regression contract.\n"
    ),
    "diffusion_fuse_scale_shift__multi_shape": (
        "## Canonical Regression Shapes (from SGLang test)\n"
        "\n"
        "Source: `python/sglang/jit_kernel/tests/diffusion/test_qwen_image_modulation.py` (covers all three\n"
        "scale-shift Triton entry points: `fuse_scale_shift_kernel`, the `select01` variant and the\n"
        "residual `select01` variant).\n"
        "\n"
        "- `batch_size`: `[1, 2, 4]` (CI subset `[1, 2]`).\n"
        "- `seq_len`: `[6, 33, 128, 257]` (CI subset `[6, 128]`).\n"
        "- `hidden_size`: `[512, 1024, 1536, 3072]` (CI subset `[512, 3072]`).\n"
        "- `dtype`: `[float16, bfloat16, float32]` (CI subset `[fp16, bf16]`).\n"
        "- `eps`: `1e-6`.\n"
        "- `scale0/shift0/gate0/scale1/shift1/gate1`: each shaped `(B, C)`.\n"
        "- `index`: shaped `(B, L)`, bool / int — required by the `select01` dispatch path.\n"
        "- Residual / residual_gate path tested on the same grid via\n"
        "  `fuse_residual_layernorm_scale_shift_gate_select01_kernel`.\n"
        "- Tolerance: `(atol=5e-2, rtol=5e-2)` non-fp32; `1e-5` fp32.\n"
        "\n"
        "The simple `fuse_scale_shift_kernel` accepts both 2D `(B,C)` scale/shift and 4D `(B,F,1,C)` scale/shift\n"
        "(video frames). Cover both layouts during regression.\n"
    ),
    "diffusion_cutedsl_norm_tanh_mul_add__multi_shape": (
        "## Canonical Regression Shapes (from SGLang test)\n"
        "\n"
        "Source: `python/sglang/jit_kernel/tests/diffusion/test_fused_norm_scale_shift.py`\n"
        "(same enumeration as the sister CuTe-DSL `fused_norm_scale_shift` family).\n"
        "\n"
        "- `SHAPES = [(B, S, F, D)]` = `[(1, 1024, 8, 3072), (4, 512, 16, 3072)]`.\n"
        "- `dtype`: `[torch.float16, torch.bfloat16, torch.float32]`.\n"
        "- `norm_type`: `[\"layer\", \"rms\"]`.\n"
        "- `affine_mode`: `[\"D\", \"NAT\"]` (weight/bias as `[D]` tensor or `None`).\n"
        "- `scale/shift` layouts (`index_mode`):\n"
        "  `[\"BSD\", \"1\", \"1SD\", \"BD\", \"B1D\", \"D\", \"1D\", \"11D\", \"BF1D\"]`.\n"
        "- D constraint: `D % 256 == 0` and `D <= 8192`.\n"
        "- `eps`: `1e-5`.\n"
        "- Tolerance: `(atol=5e-2, rtol=5e-2)` non-fp32; `1e-5` fp32.\n"
        "- Oracle: `torch.layer_norm` / `torch.rms_norm` followed by `* tanh(scale) + shift`.\n"
        "\n"
        "The second-norm-scale variant adds `(weight2, bias2, scale2)` over the same shape grid.\n"
    ),
    "diffusion_cutedsl_norm_scale_shift__multi_shape": (
        "## Canonical Regression Shapes (from SGLang test)\n"
        "\n"
        "Source: `python/sglang/jit_kernel/tests/diffusion/test_fused_norm_scale_shift.py`.\n"
        "\n"
        "- `SHAPES = [(B, S, F, D)]` = `[(1, 1024, 8, 3072), (4, 512, 16, 3072)]`.\n"
        "- `dtype`: `[torch.float16, torch.bfloat16, torch.float32]`.\n"
        "- `norm_type`: `[\"layer\", \"rms\"]`.\n"
        "- `affine_mode`: `[\"D\", \"NAT\"]`.\n"
        "- `scale/shift` layouts (`index_mode`):\n"
        "  `[\"BSD\", \"1\", \"1SD\", \"BD\", \"B1D\", \"D\", \"1D\", \"11D\", \"BF1D\"]`.\n"
        "- Frame-divisibility precondition: `S % F == 0` whenever scale/shift use the `BF1D` (4D) layout.\n"
        "  The validator raises `\"S(<S>) must be divisible by F(<F>)\"` otherwise (covered explicitly by\n"
        "  `test_validate_scale_shift_rejects_non_divisible_frames`).\n"
        "- D constraint: `D % 256 == 0` and `D <= 8192`.\n"
        "- `eps`: `1e-5`.\n"
        "- Tolerance: `(atol=5e-2, rtol=5e-2)` non-fp32; `1e-5` fp32.\n"
        "- Oracle: `norm(x) * (1 + scale) + shift` with `_apply_scale_shift` handling 2D/3D/4D layouts.\n"
        "\n"
        "The residual variant `fused_scale_residual_norm_scale_shift` additionally consumes\n"
        "`(residual, gate)` and outputs `(y, res_out)`; `gate_mode` defaults to `B1D` but is parameterized\n"
        "across the same index-mode list.\n"
    ),
}

INSERT_ANCHOR = "## Configurable Optimization Axes"


def patch_one(prompt_path: Path, block: str) -> None:
    text = prompt_path.read_text()
    section_header = "## Canonical Regression Shapes (from SGLang test)"
    if section_header in text:
        # Replace the existing block (everything from header to next H2 header).
        start = text.index(section_header)
        rest = text[start:]
        # Find the next "## " header after the start of this section.
        next_header_idx = rest.find("\n## ", len(section_header))
        if next_header_idx == -1:
            # No next header; replace through end of file.
            new_text = text[:start] + block.rstrip() + "\n"
        else:
            new_text = (
                text[:start]
                + block.rstrip()
                + "\n\n"
                + rest[next_header_idx + 1 :]
            )
    else:
        # Insert just before the "## Configurable Optimization Axes" anchor.
        anchor_idx = text.find(INSERT_ANCHOR)
        if anchor_idx == -1:
            # Fallback: append at end.
            new_text = text.rstrip() + "\n\n" + block.rstrip() + "\n"
        else:
            new_text = (
                text[:anchor_idx].rstrip()
                + "\n\n"
                + block.rstrip()
                + "\n\n"
                + text[anchor_idx:]
            )
    prompt_path.write_text(new_text)


def main() -> None:
    archs = ("b200", "h200")
    for family, block in CANONICAL_SECTIONS.items():
        for arch in archs:
            slug = f"{arch}_{family}"
            prompt_path = KERNELS_DIR / slug / "prompt.md"
            if not prompt_path.exists():
                print(f"missing prompt: {prompt_path}")
                continue
            patch_one(prompt_path, block)
            print(f"patched {slug}")


if __name__ == "__main__":
    main()
