# Profile evidence — nemotron3_nano__sglang_flashinfer_bmm_fp8

**Why this kernel is an e2e-optimization target:** it is **20.7% of total GPU
time** (max across scenarios) on `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8`, measured by profiling the exact
cookbook deployment. Clean Python interface from profiler provenance.

- Model: `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8` (slug `nemotron3_nano`, tp=1)
- Python interface: `sglang.flashinfer_bmm_fp8`
- Category: `gemm`
- GPU kernel(s): `_ZN7cutlass13device_kernelINS_4gemm6kernel13GemmUniversalIN4cute5tupleIJiiiiEEENS1_10colle`, `bmm_Bfloat16_E4m3E4m3_Fp32_t128x64x128_s8_et128x64_m256x64x32_c2x1x1_rM_TN_transOut_schPd2`, `bmm_E4m3_E4m3E4m3_Fp32_BtokBfloat16_t128x64x256_s5_et128x64_m256x64x32_c2x1x1_rM_TN_transO`
- Profiler op provenance: `aten::_local_scalar_dense`, `aten::split_with_sizes`, `aten::view`, `sglang::flashinfer_bmm_fp8`

## % of GPU time by scenario

| dataset | scenario (concurrency) | % of GPU time |
|---|---|---|
| random_mid | random (conc 32) | 20.68% |
| random_high | random (conc 100) | 10.70% |
| sharegpt_mid | sharegpt (conc 32) | 8.33% |
| sharegpt_high | sharegpt (conc 100) | 3.78% |

**Peak: 20.7% in `random_mid` (random, concurrency 32).**

## Input shapes (profiler)
- `[[13193, 2688], [2688, 10304], [], [], []]`
- `[[1553, 2688], [2688, 10304], [], [], []]`
- `[[2936, 2688], [2688, 10304], [], [], []]`
- `[[8704, 2688], [2688, 10304], [], [], []]`
- `[[], []]`
- `[[]]`

## Reproduce the deployment (cookbook-aligned)
```bash
python3 -m sglang.launch_server --model-path nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8 --trust-remote-code --max-running-requests 1024
```

After optimizing, re-run the **random_mid** scenario to validate the e2e effect:
`bench_serving --dataset-name random ... --max-concurrency 32`.
