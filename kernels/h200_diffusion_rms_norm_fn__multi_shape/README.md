# h200_diffusion_rms_norm_fn__multi_shape

KDA-style task folder for optimizing the SGLang diffusion
**Flash-attn-style 1-pass LN/RMSN with optional residual** kernel(s) on NVIDIA H200.

See `prompt.md` for the task contract, `interface.md` for the expected local
candidate interface, and `tests/test_correctness.py` for the correctness
oracle scaffold.

Wrapped SGLang baseline entry points:
- `sglang.jit_kernel.diffusion.triton.norm:rms_norm_fn`

Reference SGLang test used as the correctness oracle:
`python/sglang/jit_kernel/tests/test_rmsnorm.py`

Promotion target: optimize toward the active hardware performance bound across
all configured shape buckets. Report geometric-mean speedup over the SGLang
baseline, but use roofline-style bandwidth/FLOP/s evidence rather than a fixed
speedup multiplier as the completion criterion.
