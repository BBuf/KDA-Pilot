# Profile evidence — glm_46__attention

**e2e-optimization target: 9.3% of total GPU time** (max across scenarios) on
`zai-org/GLM-4.6-FP8`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `zai-org/GLM-4.6-FP8` (slug `glm_46`, tp=8)
- Python interface: `<confirm via capture; profiler family=attention>`
- Kernel family: `attention`  ·  Category: `gemm`
- GPU kernel(s): `kernel_cutlass_kernel_flash_attncuteflash_fwd_sm100FlashAttentionForwardSm100_object_at__t`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 5.31% |
| random | conc 32 | 3.66% |
| random | conc 100 | 4.22% |
| sharegpt | conc 1 | 9.32% |
| sharegpt | conc 32 | 6.87% |
| sharegpt | conc 100 | 7.67% |

**Peak: 9.3% in `sharegpt_low` (sharegpt, concurrency 1).**

## Input shapes (profiler)
- `[[103, 12, 128], [19176, 128, 1, 128], [19176, 128, 1, 128], [], [2], [], [], [1`
- `[[1536, 1536], [], [], []]`
- `[[1971, 12, 128], [19176, 128, 1, 128], [19176, 128, 1, 128], [], [6], [], [], [`
- `[[2027, 12, 128], [19176, 128, 1, 128], [19176, 128, 1, 128], [], [42], [], [], `
- `[[256], [], [], [], []]`
- `[[7276, 12, 128], [19176, 128, 1, 128], [19176, 128, 1, 128], [], [15], [], [], `
- `[[80, 12, 128], [19176, 128, 1, 128], [19176, 128, 1, 128], [], [2], [], [], [1]`
- `[[8125, 12, 128], [19176, 128, 1, 128], [19176, 128, 1, 128], [], [27], [], [], `
- `[[8192, 1536], [], [], [], []]`
- `[[], [], [], [], [], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path zai-org/GLM-4.6-FP8 --tp 8 --reasoning-parser glm45 --tool-call-parser glm45 --attention-backend fa4
```
After optimizing, re-run **sharegpt_low** to validate the e2e effect.
