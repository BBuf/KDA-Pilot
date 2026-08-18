# Diffusion attention backend on sm_103: short-sequence FA4 gap + a dispatch that must see layout

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

- **Corrected premise, measured tonight on B300.** Our August campaign found cuDNN 9.19
  SDPA beating the vendored FA4 CuTe kernel by 1.24-1.98x on 11 real diffusion shapes,
  which is why SGLang defaults sm_100+ diffusion attention to cuDNN. That **does not
  reproduce on sm_103 with the current stack**: with the layout the model really uses
  (q/k/v as slices of one fused QKV buffer) FA4 is *faster* on every large shape by
  4-5%. Full table in `docs/profile_evidence.md`, raw numbers in `bench/fa4_*.json`.
- **What is left is real but narrower.** FA4 is **1.24x slower than cuDNN at 24-26
  tokens** (14-16 heads, head_dim 128) - that is MiniMax-H3's audio tower, which FA4
  served 200 times in a single captured request, and it is also the branch a sparse
  backend falls back to. Closing that regime is ask #1.
- **The dispatch predicate has to see the layout, not only the shape**: at 15.6k and
  32.7k tokens cuDNN wins 1.14-1.17x on contiguous tensors and loses 0.95x on
  fused-QKV slices. Ask #2 is a predicate (or a kernel) that does not flip with a
  stride change.
- Ask #3, if you have a B200 handy: re-verify the older 1.24-1.98x gap with the current
  wheel. If it still holds there, FA4's tuning is generation-specific and both of us
  should encode that instead of hard-coding a backend per architecture.

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
