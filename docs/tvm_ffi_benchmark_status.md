# tvm-ffi Benchmark Status

As of 2026-06-01, KernelPilot diffusion promotion requires SGLang
`jit_kernel` / tvm-ffi entry points. Task-local runtime candidates and their
historical benchmark evidence have been removed from the active task folders.

| Task | Arch | Required SGLang target | Valid benchmark status |
| --- | --- | --- | --- |
| diffusion qknorm rope | B200 | `sglang.jit_kernel.diffusion.qknorm_rope:fused_inplace_qknorm_rope` | Valid (2026-06-04): in-tree drop-in arbiter PASS, device geomean 1.0970x @ SGLang `0b65588c1` (register_custom_op preserved, per-side build-cache isolation, enforced >3% materiality gate). Evidence: `kernels/b200_diffusion_qknorm_rope__multi_shape/docs/sglang_jit_export.md` (r9), `benchmark.csv` `GEOMEAN_intree_r9`. |
| diffusion qknorm rope | H200 | `sglang.jit_kernel.diffusion.qknorm_rope:fused_inplace_qknorm_rope` | Blocked: no optimized tvm-ffi candidate is present in the SGLang checkout. |
| diffusion rotary embedding | B200 | `sglang.jit_kernel.diffusion.triton.rotary:apply_rotary_embedding`, `sglang.jit_kernel.diffusion.triton.ltx2_rotary:apply_ltx2_split_rotary_emb` | Blocked: no optimized tvm-ffi candidate is present in the SGLang checkout. |
| diffusion norm infer | H200 | `sglang.jit_kernel.diffusion.triton.norm:norm_infer`, `sglang.jit_kernel.diffusion.triton.rmsnorm_onepass:triton_one_pass_rms_norm` | Blocked: no optimized tvm-ffi candidate is present in the SGLang checkout. |

Benchmark numbers are valid only after the candidate is ported into the SGLang
module path above, one-time JIT setup is run outside timing, and both baseline
and candidate paths are warmed before steady-state timing.
