# Profile evidence — step35_flash__sglang_inplace_fused_experts

**e2e-optimization target: 16.1% of total GPU time** (max across scenarios) on
`stepfun-ai/Step-3.5-Flash`, from the exact cookbook-aligned profile. Clean Python interface (profiler provenance).

> Triton MoE expert-GEMM (sglang's own fused_experts/fused_moe kernel) — single-GPU optimizable; NOT the comm-fused trtllm MoE path (excluded).

- Model: `stepfun-ai/Step-3.5-Flash` (slug `step35_flash`, tp=4)
- Python interface: `sglang.inplace_fused_experts`
- Kernel family: `fused_moe_triton`  ·  Category: `moe`
- GPU kernel(s): `fused_moe_kernel`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 14.66% |
| random | conc 32 | 16.13% |
| random | conc 100 | 14.89% |
| sharegpt | conc 1 | 13.63% |
| sharegpt | conc 32 | 13.10% |
| sharegpt | conc 100 | 15.80% |

**Peak: 16.1% in `random_mid` (random, concurrency 32).**

## Input shapes (profiler)
- `[[16, 4096], [288, 640, 4096], [288, 4096, 320], [16, 8], [16, 8], [], [], [], [`
- `[[38, 4096], [288, 640, 4096], [288, 4096, 320], [38, 8], [38, 8], [], [], [], [`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path stepfun-ai/Step-3.5-Flash --tp 4 --trust-remote-code --reasoning-parser step3p5
```
After optimizing, re-run **random_mid** to validate the e2e effect.
