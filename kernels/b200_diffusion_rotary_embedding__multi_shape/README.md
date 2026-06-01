# b200_diffusion_rotary_embedding__multi_shape

KDA-style task folder for optimizing the SGLang diffusion
**Standard and LTX-2 split rotary embeddings** kernel(s) on NVIDIA B200.

See `prompt.md` for the task contract, `interface.md` for the expected local
candidate interface, and `tests/test_correctness.py` for the correctness
oracle scaffold.

Wrapped SGLang baseline entry points:
- `sglang.jit_kernel.diffusion.triton.rotary:apply_rotary_embedding`
- `sglang.jit_kernel.diffusion.triton.ltx2_rotary:apply_ltx2_split_rotary_emb`

Correctness oracle (see `interface.md`): the **SGLang diffusion Triton baseline itself**
(`apply_rotary_embedding` / `apply_ltx2_split_rotary_emb`, the production reference) plus a
PyTorch FP32 cross-check, with dynamic BF16-aware tolerances. Note: the SGLang test
`python/sglang/jit_kernel/tests/test_rope.py` exercises a *different* function
(`apply_rope_inplace`, LLM q/k RoPE) and is style guidance only, not a direct oracle here.

Promotion target: optimize toward the active hardware performance bound across
all configured shape buckets. Report geometric-mean speedup over the SGLang
baseline, but use roofline-style bandwidth/FLOP/s evidence rather than a fixed
speedup multiplier as the completion criterion.
