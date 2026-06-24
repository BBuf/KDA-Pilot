# Profile evidence — nemotron3_super__sglang_nemotron_mamba2_with_output

**e2e-optimization target: 27.3% of total GPU time** (max across scenarios) on
`nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16`, from the exact cookbook-aligned profile. Clean Python interface (profiler provenance).

- Model: `nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16` (slug `nemotron3_super`, tp=4)
- Python interface: `sglang.nemotron_mamba2_with_output`
- Kernel family: `mamba2_ssm`  ·  Category: `other`
- GPU kernel(s): `_chunk_scan_fwd_kernel`, `_chunk_state_fwd_kernel`, `_state_passing_fwd_kernel`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 32 | 18.12% |
| random | conc 100 | 27.25% |
| sharegpt | conc 32 | 18.45% |

**Peak: 27.3% in `random_high` (random, concurrency 100).**

## Input shapes (profiler)
- `[[1, 16384, 2, 128], [], [], []]`
- `[[10240, 4096], [10240, 4096], []]`
- `[[16384, 4096], [16384, 4096], []]`
- `[[16384, 4096], [4096, 4640]]`
- `[[31, 1, 1], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16 --tp 4 --trust-remote-code
```
After optimizing, re-run **random_high** to validate the e2e effect.
