# Profile evidence — nemotron3_nano__static_quant_fp8

**Why this kernel is an e2e-optimization target:** it is **4.1% of total GPU
time** (max across scenarios) on `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8`, measured by profiling the exact
cookbook deployment. Profiler role name; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8` (slug `nemotron3_nano`, tp=1)
- Python interface: `<confirm via capture; profiler role=static_quant_fp8>`
- Category: `quant_gemm`
- GPU kernel(s): `_static_quant_fp8`
- Profiler op provenance: `aten::copy_`, `aten::empty`, `aten::to`

## % of GPU time by scenario

| dataset | scenario (concurrency) | % of GPU time |
|---|---|---|
| sharegpt_low | sharegpt (conc 1) | 4.13% |

**Peak: 4.1% in `sharegpt_low` (sharegpt, concurrency 1).**

## Input shapes (profiler)
- `[[1], [1], []]`
- `[[], [], [], [], [], []]`

## Reproduce the deployment (cookbook-aligned)
```bash
python3 -m sglang.launch_server --model-path nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8 --trust-remote-code --max-running-requests 1024
```

After optimizing, re-run the **sharegpt_low** scenario to validate the e2e effect:
`bench_serving --dataset-name sharegpt ... --max-concurrency 1`.
