# Profile evidence — nemotron3_nano__linear_gemm

**Why this kernel is an e2e-optimization target:** it is **26.7% of total GPU
time** (max across scenarios) on `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8`, measured by profiling the exact
cookbook deployment. Profiler role name; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8` (slug `nemotron3_nano`, tp=1)
- Python interface: `<confirm via capture; profiler role=linear_gemm>`
- Category: `gemm`
- GPU kernel(s): `_ZN7cutlass13device_kernelINS_4gemm6kernel13GemmUniversalIN4cute5tupleIJiiiiEEENS1_10colle`, `nvjet_sm100_tss_32x64_64x16_4x1_v_bz_splitK_TNN`, `nvjet_sm100_tst_128x8_64x12_2x1_v_bz_TNT`, `nvjet_sm100_tst_64x8_64x16_4x1_v_bz_splitK_TNT`
- Profiler op provenance: `aten::_index_put_impl_`, `aten::_local_scalar_dense`, `aten::add`, `aten::as_strided`, `aten::copy_`, `aten::empty_strided`

## % of GPU time by scenario

| dataset | scenario (concurrency) | % of GPU time |
|---|---|---|
| random_low | random (conc 1) | 26.59% |
| sharegpt_low | sharegpt (conc 1) | 26.74% |
| sharegpt_high | sharegpt (conc 100) | 2.56% |

**Peak: 26.7% in `sharegpt_low` (sharegpt, concurrency 1).**

## Input shapes (profiler)
- `[[1, 131072], [], []]`
- `[[1, 1], [1, 1], []]`
- `[[127], [127], []]`
- `[[1], [1], []]`
- `[[1], [], []]`
- `[[1], []]`
- `[[1]]`
- `[[21622009], [], [], []]`
- `[[249], [], [], [], []]`
- `[[250, 262148], [], [], [], []]`
- `[[2], [2], []]`
- `[[41], []]`

## Reproduce the deployment (cookbook-aligned)
```bash
python3 -m sglang.launch_server --model-path nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8 --trust-remote-code --max-running-requests 1024
```

After optimizing, re-run the **sharegpt_low** scenario to validate the e2e effect:
`bench_serving --dataset-name sharegpt ... --max-concurrency 1`.
