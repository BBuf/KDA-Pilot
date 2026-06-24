# Profile evidence — gemma4__sglang_inplace_fused_experts

**e2e-optimization target: 50.8% of total GPU time** (max across scenarios) on
`google/gemma-4-26B-A4B-it`, from the exact cookbook-aligned profile. Clean Python interface (profiler provenance).

> Triton MoE expert-GEMM (sglang's own fused_experts/fused_moe kernel) — single-GPU optimizable; NOT the comm-fused trtllm MoE path (excluded).

- Model: `google/gemma-4-26B-A4B-it` (slug `gemma4`, tp=1)
- Python interface: `sglang.inplace_fused_experts`
- Kernel family: `fused_moe_triton`  ·  Category: `moe`
- GPU kernel(s): `fused_moe_kernel`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 22.87% |
| random | conc 32 | 45.23% |
| random | conc 100 | 50.81% |
| sharegpt | conc 1 | 21.68% |
| sharegpt | conc 32 | 43.37% |
| sharegpt | conc 100 | 50.02% |

**Peak: 50.8% in `random_high` (random, concurrency 100).**

## Input shapes (profiler)
- `[[11254, 2816], [128, 1408, 2816], [128, 2816, 704], [11254, 8], [11254, 8], [],`
- `[[17, 2816], [128, 1408, 2816], [128, 2816, 704], [17, 8], [17, 8], [], [], [], `
- `[[1785, 2816], [128, 1408, 2816], [128, 2816, 704], [1785, 8], [1785, 8], [], []`
- `[[1902, 2816], [128, 1408, 2816], [128, 2816, 704], [1902, 8], [1902, 8], [], []`
- `[[38, 2816], [128, 1408, 2816], [128, 2816, 704], [38, 8], [38, 8], [], [], [], `
- `[[7081, 2816], [128, 1408, 2816], [128, 2816, 704], [7081, 8], [7081, 8], [], []`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path google/gemma-4-26B-A4B-it --reasoning-parser gemma4 --tool-call-parser gemma4
```
After optimizing, re-run **random_high** to validate the e2e effect.
