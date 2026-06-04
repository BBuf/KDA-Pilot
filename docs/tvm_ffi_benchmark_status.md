# tvm-ffi Benchmark Status

As of 2026-06-01, KernelPilot diffusion promotion requires SGLang
`jit_kernel` / tvm-ffi entry points. Task-local runtime candidates and their
historical benchmark evidence have been removed from the active task folders.

| Task | Arch | Required SGLang target | Valid benchmark status |
| --- | --- | --- | --- |
| diffusion qknorm rope | B200 | `sglang.jit_kernel.diffusion.qknorm_rope:fused_inplace_qknorm_rope` | Blocked: no optimized tvm-ffi candidate is present in the SGLang checkout. |
| diffusion qknorm rope | H200 | `sglang.jit_kernel.diffusion.qknorm_rope:fused_inplace_qknorm_rope` | Blocked: no optimized tvm-ffi candidate is present in the SGLang checkout. |
| diffusion rotary embedding | B200 | `sglang.jit_kernel.diffusion.triton.rotary:apply_rotary_embedding`, `sglang.jit_kernel.diffusion.triton.ltx2_rotary:apply_ltx2_split_rotary_emb` | Blocked: no optimized tvm-ffi candidate is present in the SGLang checkout. |
| diffusion norm infer | H200 | `sglang.jit_kernel.diffusion.triton.norm:norm_infer`, `sglang.jit_kernel.diffusion.triton.rmsnorm_onepass:triton_one_pass_rms_norm` | Done: in-tree tvm-ffi candidate validated via the dispatch-symmetric env-toggle arbiter (wall geomean 1.4458x over 6 captured shapes, oracle 288/288, torch.compile smoke OK); shipping patch at `kernels/h200_diffusion_norm_infer__multi_shape/docs/sglang_export.patch`. |

Benchmark numbers are valid only after the candidate is ported into the SGLang
module path above, one-time JIT setup is run outside timing, and both baseline
and candidate paths are warmed before steady-state timing.
