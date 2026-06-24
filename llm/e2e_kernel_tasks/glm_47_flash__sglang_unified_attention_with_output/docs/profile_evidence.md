# Profile evidence — glm_47_flash__sglang_unified_attention_with_output

**e2e-optimization target: 75.3% of total GPU time** (max across scenarios) on
`zai-org/GLM-4.7-Flash`, from the exact cookbook-aligned profile. Clean Python interface (profiler provenance).

- Model: `zai-org/GLM-4.7-Flash` (slug `glm_47_flash`, tp=1)
- Python interface: `sglang.unified_attention_with_output`
- Kernel family: `attention`  ·  Category: `other`
- GPU kernel(s): `_fwd_kernel`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 32 | 41.11% |
| random | conc 100 | 35.25% |
| sharegpt | conc 1 | 6.51% |
| sharegpt | conc 32 | 75.35% |
| sharegpt | conc 100 | 26.43% |

**Peak: 75.3% in `sharegpt_mid` (sharegpt, concurrency 32).**

## Input shapes (profiler)
- `[[1873326, 1, 576], [], [], []]`
- `[[1], []]`
- `[[24, 20, 576], [24, 1, 576], [24, 1, 512], [24, 10240], [], [], [], [], [], [],`
- `[[32], [32], []]`
- `[[4, 20, 576], [4, 1, 576], [4, 1, 512], [4, 10240], [], [], [], [], [], [], [],`
- `[[5102], [], [5102, 5], [5102, 64], [5102, 1], [1], [5102, 5], [5102, 5], [], []`
- `[[80, 20, 576], [80, 1, 576], [80, 1, 512], [80, 10240], [], [], [], [], [], [],`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path zai-org/GLM-4.7-Flash --tp 1 --attention-backend triton --reasoning-parser glm45 --tool-call-parser glm47
```
After optimizing, re-run **sharegpt_mid** to validate the e2e effect.
