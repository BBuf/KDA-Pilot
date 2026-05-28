# b200_diffusion_norm_infer__multi_shape

KDA-style task folder for optimizing the SGLang diffusion
**Inference-only LN/RMSN 2-pass kernel** kernel(s) on NVIDIA B200.

See `prompt.md` for the task contract, `interface.md` for the expected local
candidate interface, and `tests/test_correctness.py` for the correctness
oracle scaffold.

Wrapped SGLang baseline entry points:
- `sglang.jit_kernel.diffusion.triton.norm:norm_infer`
- `sglang.jit_kernel.diffusion.triton.rmsnorm_onepass:triton_one_pass_rms_norm`

Reference SGLang test used as the correctness oracle:
`python/sglang/jit_kernel/tests/diffusion/test_qwen_image_modulation.py`

Promotion target: optimize toward the active hardware performance bound across
all configured shape buckets. Report geometric-mean speedup over the SGLang
baseline, but use roofline-style bandwidth/FLOP/s evidence rather than a fixed
speedup multiplier as the completion criterion.
