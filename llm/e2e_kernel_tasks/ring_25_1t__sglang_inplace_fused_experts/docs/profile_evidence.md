# Profile evidence — ring_25_1t__sglang_inplace_fused_experts

**e2e-optimization target: 32.3% of total GPU time** (max across scenarios) on
`inclusionAI/Ring-2.5-1T`, from the exact cookbook-aligned profile. Clean Python interface (profiler provenance).

> Triton MoE expert-GEMM (sglang's own fused_experts/fused_moe kernel) — single-GPU optimizable; NOT the comm-fused trtllm MoE path (excluded).

- Model: `inclusionAI/Ring-2.5-1T` (slug `ring_25_1t`, tp=8)
- Python interface: `sglang.inplace_fused_experts`
- Kernel family: `fused_moe_triton`  ·  Category: `moe`
- GPU kernel(s): `fused_moe_kernel`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 12.89% |
| random | conc 32 | 30.99% |
| random | conc 100 | 32.31% |
| sharegpt | conc 1 | 13.29% |
| sharegpt | conc 32 | 29.19% |
| sharegpt | conc 100 | 30.42% |

**Peak: 32.3% in `random_high` (random, concurrency 100).**

## Input shapes (profiler)
- `[[14375, 8192], [256, 512, 8192], [256, 8192, 256], [14375, 8], [14375, 8], [], `
- `[[16384, 8192], [256, 512, 8192], [256, 8192, 256], [16384, 8], [16384, 8], [], `
- `[[256, 8192], [], [], []]`
- `[[3330, 8192], [256, 512, 8192], [256, 8192, 256], [3330, 8], [3330, 8], [], [],`
- `[[39, 8192], [256, 512, 8192], [256, 8192, 256], [39, 8], [39, 8], [], [], [], [`
- `[[44, 256], [], [], [], [], [], []]`
- `[[44, 8192], [256, 512, 8192], [256, 8192, 256], [44, 8], [44, 8], [], [], [], [`
- `[[9780, 8192], [256, 512, 8192], [256, 8192, 256], [9780, 8], [9780, 8], [], [],`
- `[[], [], [], [], [], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path inclusionAI/Ring-2.5-1T --tp 8 --trust-remote-code
```
After optimizing, re-run **random_high** to validate the e2e effect.
