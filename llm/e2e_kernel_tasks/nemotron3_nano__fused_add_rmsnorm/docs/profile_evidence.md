# Profile evidence — nemotron3_nano__fused_add_rmsnorm

**Why this kernel is an e2e-optimization target:** it is **4.4% of total GPU
time** (max across scenarios) on `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8`, measured by profiling the exact
cookbook deployment. Profiler role name; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8` (slug `nemotron3_nano`, tp=1)
- Python interface: `<confirm via capture; profiler role=fused_add_rmsnorm>`
- Category: `gemm`
- GPU kernel(s): `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_a`
- Profiler op provenance: `aten::as_strided`, `aten::copy_`, `aten::view`

## % of GPU time by scenario

| dataset | scenario (concurrency) | % of GPU time |
|---|---|---|
| random_low | random (conc 1) | 4.41% |
| sharegpt_low | sharegpt (conc 1) | 4.44% |

**Peak: 4.4% in `sharegpt_low` (sharegpt, concurrency 1).**

## Input shapes (profiler)
- `[[1, 131072], [], [], []]`
- `[[1, 1], [1, 1], []]`
- `[[1], [1], []]`
- `[[1], []]`

## Reproduce the deployment (cookbook-aligned)
```bash
python3 -m sglang.launch_server --model-path nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8 --trust-remote-code --max-running-requests 1024
```

After optimizing, re-run the **sharegpt_low** scenario to validate the e2e effect:
`bench_serving --dataset-name sharegpt ... --max-concurrency 1`.
