# b200_diffusion_cutedsl_norm_tanh_mul_add__multi_shape

KDA-style task folder for optimizing the SGLang diffusion
**CuTe-DSL norm + tanh(scale) + shift (+ second-norm scale)** kernel(s) on NVIDIA B200.

See `prompt.md` for the task contract, `interface.md` for the expected local
candidate interface, and `tests/test_correctness.py` for the correctness
oracle scaffold.

Wrapped SGLang baseline entry points:
- `sglang.jit_kernel.diffusion.cutedsl.norm_tanh_mul_add_norm_scale:fused_norm_tanh_mul_add`
- `sglang.jit_kernel.diffusion.cutedsl.norm_tanh_mul_add_norm_scale:fused_norm_tanh_mul_add_norm_scale`

Reference SGLang test used as the correctness oracle:
`python/sglang/jit_kernel/tests/diffusion/test_fused_norm_scale_shift.py`

Promotion target: optimize toward the active hardware performance bound across
all configured shape buckets. Report geometric-mean speedup over the SGLang
baseline, but use roofline-style bandwidth/FLOP/s evidence rather than a fixed
speedup multiplier as the completion criterion.
