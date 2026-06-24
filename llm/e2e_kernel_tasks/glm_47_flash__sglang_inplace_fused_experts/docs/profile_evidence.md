# Profile evidence — glm_47_flash__sglang_inplace_fused_experts

**e2e-optimization target: 30.4% of total GPU time** (max across scenarios) on
`zai-org/GLM-4.7-Flash`, from the exact cookbook-aligned profile. Clean Python interface (profiler provenance).

> Triton MoE expert-GEMM (sglang's own fused_experts/fused_moe kernel) — single-GPU optimizable; NOT the comm-fused trtllm MoE path (excluded).

- Model: `zai-org/GLM-4.7-Flash` (slug `glm_47_flash`, tp=1)
- Python interface: `sglang.inplace_fused_experts`
- Kernel family: `fused_moe_triton`  ·  Category: `moe`
- GPU kernel(s): `fused_moe_kernel`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 21.80% |
| random | conc 32 | 30.39% |
| random | conc 100 | 27.34% |
| sharegpt | conc 1 | 20.23% |
| sharegpt | conc 32 | 12.17% |
| sharegpt | conc 100 | 29.47% |

**Peak: 30.4% in `random_mid` (random, concurrency 32).**

## Input shapes (profiler)
- `[[1163106], [], [], [], []]`
- `[[1], []]`
- `[[5102, 2048], [65, 3072, 2048], [65, 2048, 1536], [5102, 5], [5102, 5], [], [],`
- `[[5528, 2048], [65, 3072, 2048], [65, 2048, 1536], [5528, 5], [5528, 5], [], [],`
- `[[], [], [], [], [], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path zai-org/GLM-4.7-Flash --tp 1 --attention-backend triton --reasoning-parser glm45 --tool-call-parser glm47
```
After optimizing, re-run **random_mid** to validate the e2e effect.
