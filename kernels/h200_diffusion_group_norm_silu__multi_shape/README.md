# h200_diffusion_group_norm_silu__multi_shape

KDA-style task folder for optimizing the SGLang diffusion
**Fused GroupNorm + SiLU for diffusion VAE** kernel(s) on NVIDIA H200.

See `prompt.md` for the task contract, `interface.md` for the expected local
candidate interface, and `tests/test_correctness.py` for the correctness
oracle scaffold.

Wrapped SGLang baseline entry points:
- `sglang.jit_kernel.diffusion.triton.group_norm_silu:triton_group_norm_silu`
- `sglang.jit_kernel.diffusion.group_norm_silu:apply_group_norm_silu`

Reference SGLang test used as the correctness oracle:
`python/sglang/jit_kernel/tests/diffusion/test_group_norm_silu.py`

Promotion target: optimize toward the active hardware performance bound across
all configured shape buckets. Report geometric-mean speedup over the SGLang
baseline, but use roofline-style bandwidth/FLOP/s evidence rather than a fixed
speedup multiplier as the completion criterion.
