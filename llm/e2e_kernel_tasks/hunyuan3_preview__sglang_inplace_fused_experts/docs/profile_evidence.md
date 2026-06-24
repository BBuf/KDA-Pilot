# Profile evidence — hunyuan3_preview__sglang_inplace_fused_experts

**e2e-optimization target: 34.7% of total GPU time** (max across scenarios) on
`tencent/Hy3-preview`, from the exact cookbook-aligned profile. Clean Python interface (profiler provenance).

> Triton MoE expert-GEMM (sglang's own fused_experts/fused_moe kernel) — single-GPU optimizable; NOT the comm-fused trtllm MoE path (excluded).

- Model: `tencent/Hy3-preview` (slug `hunyuan3_preview`, tp=8)
- Python interface: `sglang.inplace_fused_experts`
- Kernel family: `fused_moe_triton`  ·  Category: `moe`
- GPU kernel(s): `fused_moe_kernel`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 15.84% |
| random | conc 32 | 34.73% |
| random | conc 100 | 20.95% |
| sharegpt | conc 1 | 12.37% |
| sharegpt | conc 32 | 21.16% |
| sharegpt | conc 100 | 18.92% |

**Peak: 34.7% in `random_mid` (random, concurrency 32).**

## Input shapes (profiler)
- `[[1210, 4096], [192, 384, 4096], [192, 4096, 192], [1210, 8], [1210, 8], [], [],`
- `[[1220, 4096], [192, 384, 4096], [192, 4096, 192], [1220, 8], [1220, 8], [], [],`
- `[[1220, 4096], [384, 4096], []]`
- `[[15, 4096], [192, 384, 4096], [192, 4096, 192], [15, 8], [15, 8], [], [], [], [`
- `[[33056, 64, 1, 128], [], [], []]`
- `[[38, 4096], [192, 384, 4096], [192, 4096, 192], [38, 8], [38, 8], [], [], [], [`
- `[[5067, 4096], [192, 384, 4096], [192, 4096, 192], [5067, 8], [5067, 8], [], [],`
- `[[5067, 4096], [384, 4096], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path tencent/Hy3-preview --tp 8 --speculative-algorithm EAGLE --speculative-num-steps 3 --speculative-eagle-topk 1
```
After optimizing, re-run **random_mid** to validate the e2e effect.
