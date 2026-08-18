# FA4 CuTe loses to cuDNN SDPA on diffusion attention shapes (sm_100/sm_103)

**Task:** `diffusion__attention_backend_fa4_vs_cudnn`

**Model:** `Wan2.2-TI2V-5B, Wan2.2-A14B, LingBot-World, MiniMax-H3 image tower`
**Serving command this workload came from (SGLang cookbook recipe):**

```bash
sglang serve <model> (diffusion serving path; sm_100+ resolves to the vendored FA4 CuTe backend by default)
```

**Measured share:** the attention call is 48-70% of one denoise step across these models

## Kernels in scope

- `non-causal self/cross attention, bf16, head_dim 128, very long sequences`

Baseline sources are copied into `baseline/` from SGLang main @ 43226af (python/sglang, editable install) - the same
implementation the deployment above runs. Do not benchmark against a naive
PyTorch reference; the bar is the shipped kernel.

## Why we are asking for this one

- We measured cuDNN 9.19 SDPA beating the vendored FA4 CuTe kernel on all 11 real
  diffusion attention shapes we tried, by 1.24x-1.98x (Wan2.2-5B self 8.90 -> 6.84 ms;
  A14B 112 -> 87 ms; LingBot-506K 1416 -> 1021 ms; H3 image 1.98x), which was worth
  1.132x end-to-end on Wan2.2-5B. We now default sm_100 diffusion attention to cuDNN
  because of it.
- That is a kernel-side gap on your side of the stack: either FA4's tile/stage selection
  is wrong for these shapes, or the diffusion regime (no causal mask, no KV cache,
  100k-500k tokens, head_dim 128) is simply untuned. A kernel-design agent sweeping the
  FA4 configuration space on these exact shapes is the cheapest way to close it.

## Correctness gate

- Beat cuDNN SDPA on the shape table in `bench/workloads.json` (that is the bar, not
  FA4's current number), at equal or better numerics.
- Non-bit-exact is acceptable here (bf16 backend freedom); we validate with PSNR / SSIM
  against a fixed-seed reference (our gate: PSNR mean >=28 dB, min >=25 dB over all
  frames).

## Workload

`bench/workloads.json` holds the frozen call signatures with their real-traffic
call counts, and `tensors/` (where present) holds real input/output/state payloads
captured from the running model. `docs/capture_provenance.md` records exactly how
they were produced, including the GSM8K accuracy of the serving run they came from.

Selection rule, restated: shapes are real, ranked by production call count, split
into real-traffic vs warmup-only, and cover the full (sequence length x
concurrency x dataset) matrix - not a single shape.

## Notes

- Note for reproduction: importing the SGLang diffusion stack disables the cuDNN SDPA
  path globally (`enable_cudnn_sdp(False)`) and pins FA ver 4 on sm_100, so an A/B needs
  that override lifted.

## Deliverable

1. Kernel source in `solution/`, buildable standalone against the copied baseline
   ABI (`baseline/`).
2. Benchmark output per workload row: baseline vs candidate, CUDA-graph timed,
   interleaved A/B - see `../docs/measurement_contract.md`.
3. Correctness-gate output as defined above.
4. If you used Nsight Compute, the report and the bottleneck it identified.
