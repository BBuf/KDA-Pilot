# Profile evidence — kimi_linear__activation

**e2e-optimization target: 3.4% of total GPU time** (max across scenarios) on
`moonshotai/Kimi-Linear-48B-A3B-Instruct`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

> Activation (SiLU/GELU+mul). Prior guidance: limited headroom — deprioritize.

- Model: `moonshotai/Kimi-Linear-48B-A3B-Instruct` (slug `kimi_linear`, tp=4)
- Python interface: `<confirm via capture; profiler family=activation>`
- Kernel family: `activation`  ·  Category: `other`
- GPU kernel(s): `void (anonymous namespace)::act_and_mul_kernel<__nv_bfloat16, ((anonymous namespace)::Acti`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 3.37% |

**Peak: 3.4% in `random_low` (random, concurrency 1).**

## Input shapes (profiler)
- `[[1, 38, 8, 128], [1, 38, 8, 128], []]`
- `[[48, 3072], [1, 48, 8, 128], [1, 48, 8], [1, 48, 8, 128], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path moonshotai/Kimi-Linear-48B-A3B-Instruct --tp 4 --trust-remote-code
```
After optimizing, re-run **random_low** to validate the e2e effect.
