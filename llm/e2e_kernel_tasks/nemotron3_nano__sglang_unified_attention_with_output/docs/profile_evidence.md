# Profile evidence — nemotron3_nano__sglang_unified_attention_with_output

**Why this kernel is an e2e-optimization target:** it is **6.1% of total GPU
time** (max across scenarios) on `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8`, measured by profiling the exact
cookbook deployment. Clean Python interface from profiler provenance.

- Model: `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8` (slug `nemotron3_nano`, tp=1)
- Python interface: `sglang.unified_attention_with_output`
- Category: `quant_gemm`
- GPU kernel(s): `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT`, `void flashinfer::BatchPrefillWithPagedKVCacheKernel<flashinfer::KernelTraits<(flashinfer::`
- Profiler op provenance: `aten::mm`, `sglang::unified_attention_with_output`

## % of GPU time by scenario

| dataset | scenario (concurrency) | % of GPU time |
|---|---|---|
| sharegpt_mid | sharegpt (conc 32) | 6.06% |

**Peak: 6.1% in `sharegpt_mid` (sharegpt, concurrency 32).**

## Input shapes (profiler)
- `[[13193, 2688], [2688, 10304]]`
- `[[13312, 4096], [13312, 2, 128], [13312, 2, 128], [13312, 4096], [], [], [], [],`

## Reproduce the deployment (cookbook-aligned)
```bash
python3 -m sglang.launch_server --model-path nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8 --trust-remote-code --max-running-requests 1024
```

After optimizing, re-run the **sharegpt_mid** scenario to validate the e2e effect:
`bench_serving --dataset-name sharegpt ... --max-concurrency 32`.
