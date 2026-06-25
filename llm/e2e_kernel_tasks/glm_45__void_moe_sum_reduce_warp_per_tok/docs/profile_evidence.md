# Profile evidence — glm_45__void_moe_sum_reduce_warp_per_tok

**e2e-optimization target: 3.3% of total GPU time** (max across scenarios) on
`zai-org/GLM-4.5-FP8`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `zai-org/GLM-4.5-FP8` (slug `glm_45`, tp=8)
- Python interface: `<confirm via capture; profiler family=void_moe_sum_reduce_warp_per_tok>`
- Kernel family: `void_moe_sum_reduce_warp_per_tok`  ·  Category: `moe`
- GPU kernel(s): `void moe_sum_reduce_warp_per_token_vec_kernel<8>(c10::BFloat16 const*, c10::BFloat16*, lon`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 32 | 3.26% |
| random | conc 100 | 2.58% |
| sharegpt | conc 32 | 3.22% |

**Peak: 3.3% in `random_mid` (random, concurrency 32).**

## Input shapes (profiler)
- `[[1], []]`
- `[[2560, 1536], [2560, 1, 128], [2560, 1, 128], [2560, 1536], [], [], [], [], [],`
- `[[26], [], [], [], [], [], [], []]`
- `[[7639, 1536], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path zai-org/GLM-4.5-FP8 --tp 8 --reasoning-parser glm45 --tool-call-parser glm45 --attention-backend fa4
```
After optimizing, re-run **random_mid** to validate the e2e effect.
