# Profile evidence — qwen3__void_cublas_lt_split_kreduce_ker

**e2e-optimization target: 5.4% of total GPU time** (max across scenarios) on
`Qwen/Qwen3-235B-A22B-Instruct-2507`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `Qwen/Qwen3-235B-A22B-Instruct-2507` (slug `qwen3`, tp=8)
- Python interface: `<confirm via capture; profiler family=void_cublas_lt_split_kreduce_ker>`
- Kernel family: `void_cublas_lt_split_kreduce_ker`  ·  Category: `gemm`
- GPU kernel(s): `void cublasLt::splitKreduce_kernel<32, 16, int, float, __nv_bfloat16, float, __nv_bfloat16`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 5.37% |

**Peak: 5.4% in `random_low` (random, concurrency 1).**

## Input shapes (profiler)
- `[[3344], [], [], [], []]`
- `[[38, 1024], [38, 1024], []]`
- `[[48, 1024], [48, 1, 128], [48, 1, 128], [48, 1024], [], [], [], [], [], [], [],`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path Qwen/Qwen3-235B-A22B-Instruct-2507 --tp 8
```
After optimizing, re-run **random_low** to validate the e2e effect.
