# Profile evidence — ring_25_1t__void_at_native_unrolled_elementw

**e2e-optimization target: 5.0% of total GPU time** (max across scenarios) on
`inclusionAI/Ring-2.5-1T`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `inclusionAI/Ring-2.5-1T` (slug `ring_25_1t`, tp=8)
- Python interface: `<confirm via capture; profiler family=void_at_native_unrolled_elementw>`
- Kernel family: `void_at_native_unrolled_elementw`  ·  Category: `memory_bound`
- GPU kernel(s): `void at::native::unrolled_elementwise_kernel<at::native::direct_copy_kernel_cuda(at::Tenso`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 100 | 4.96% |

**Peak: 5.0% in `random_high` (random, concurrency 100).**

## Input shapes (profiler)
- `[[16384, 8192], [16384, 8192], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path inclusionAI/Ring-2.5-1T --tp 8 --trust-remote-code
```
After optimizing, re-run **random_high** to validate the e2e effect.
