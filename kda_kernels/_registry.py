"""Auto-generated. Lists every kda_kernels swap point.

Regenerate via the export tool when adding / removing a swap point.

Format: dict mapping `<sglang_module>:<sglang_function_name>` ->
`<kda_family_package>:<kda_function_name>`. install() iterates this
dict; for each entry it checks `KDA_OPTIMIZED_<fn>` on the kda family
package and swaps the attribute on the sglang module if True.
"""

KERNEL_REGISTRY = {
    "sglang.jit_kernel.diffusion.qknorm_rope:fused_inplace_qknorm_rope": "kda_kernels.diffusion.qknorm_rope:fused_inplace_qknorm_rope",
    "sglang.jit_kernel.diffusion.triton.norm:norm_infer": "kda_kernels.diffusion.norm_infer:norm_infer",
    "sglang.jit_kernel.diffusion.triton.rmsnorm_onepass:triton_one_pass_rms_norm": "kda_kernels.diffusion.norm_infer:triton_one_pass_rms_norm",
    "sglang.jit_kernel.diffusion.triton.group_norm_silu:triton_group_norm_silu": "kda_kernels.diffusion.group_norm_silu:triton_group_norm_silu",
    "sglang.jit_kernel.diffusion.group_norm_silu:apply_group_norm_silu": "kda_kernels.diffusion.group_norm_silu:apply_group_norm_silu",
    "sglang.jit_kernel.diffusion.triton.rotary:apply_rotary_embedding": "kda_kernels.diffusion.rotary_embedding:apply_rotary_embedding",
    "sglang.jit_kernel.diffusion.triton.ltx2_rotary:apply_ltx2_split_rotary_emb": "kda_kernels.diffusion.rotary_embedding:apply_ltx2_split_rotary_emb",
    "sglang.jit_kernel.diffusion.triton.scale_shift:fuse_scale_shift_kernel": "kda_kernels.diffusion.fuse_scale_shift:fuse_scale_shift_kernel",
    "sglang.jit_kernel.diffusion.triton.scale_shift:fuse_layernorm_scale_shift_gate_select01_kernel": "kda_kernels.diffusion.fuse_scale_shift:fuse_layernorm_scale_shift_gate_select01_kernel",
    "sglang.jit_kernel.diffusion.triton.scale_shift:fuse_residual_layernorm_scale_shift_gate_select01_kernel": "kda_kernels.diffusion.fuse_scale_shift:fuse_residual_layernorm_scale_shift_gate_select01_kernel",
    "sglang.jit_kernel.diffusion.cutedsl.norm_tanh_mul_add_norm_scale:fused_norm_tanh_mul_add": "kda_kernels.diffusion.cutedsl_norm_tanh_mul_add:fused_norm_tanh_mul_add",
    "sglang.jit_kernel.diffusion.cutedsl.norm_tanh_mul_add_norm_scale:fused_norm_tanh_mul_add_norm_scale": "kda_kernels.diffusion.cutedsl_norm_tanh_mul_add:fused_norm_tanh_mul_add_norm_scale",
    "sglang.jit_kernel.diffusion.cutedsl.scale_residual_norm_scale_shift:fused_norm_scale_shift": "kda_kernels.diffusion.cutedsl_norm_scale_shift:fused_norm_scale_shift",
    "sglang.jit_kernel.diffusion.cutedsl.scale_residual_norm_scale_shift:fused_scale_residual_norm_scale_shift": "kda_kernels.diffusion.cutedsl_norm_scale_shift:fused_scale_residual_norm_scale_shift",
}
