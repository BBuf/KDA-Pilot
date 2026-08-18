# Video VAE decode: causal conv3d + GroupNorm/SiLU, layout-aware (Wan2.2 / LTX-2 / H3)

**Target agent:** CAKE / kernel-design  **Task id:** `C3_video_vae_conv3d_groupnorm`

**Model:** `Wan2.2-TI2V-5B, LTX-2, MiniMax-H3 video VAE`
**Serving command this workload came from (SGLang cookbook recipe):**

```bash
sglang serve <model> (VAE decode stage of the diffusion pipeline)
```

**Measured share:** decode stage is 1.7-62% of end-to-end depending on deployment shape (single-GPU offload configs are decode-dominated); `group_norm_silu` is the largest remaining single kernel in our diffusion kernel set

## Kernels in scope

- `diffusion_causal_conv3d_cat_pad`
- `diffusion_group_norm_silu`

Baseline sources are copied into `baseline/` from SGLang main @ 43226af (python/sglang, editable install) - the same
implementation the deployment above runs. Do not benchmark against a naive
PyTorch reference; the bar is the shipped kernel.

## Why we are asking for this one

- Our own fused kernels here are already 2.06x (conv3d cat/pad) and 2.31x
  (group_norm_silu) over the Triton baselines, and we still think the layout is leaving
  the big win on the table: on LTX-2 the pad kernel is only 1-3% of the conv cost, while
  moving the whole decode to `channels_last_3d` is worth ~3x. That needs a conv3d that
  is fast in a layout cuDNN does not prefer, plus a layout-preserving causal pad - a
  kernel-design problem, not a tuning problem.

## Correctness gate

- Bit-exact against the current fused CUDA kernels on the captured rows (we already hold
  a bitwise-exact B300 gate for `causal_conv3d_cat_pad`; keep it).
- Frame-level: `framemd5` identical to the reference decode for the captured video, or
  the whole task is rejected - VAE decode is the last stage, so any drift is visible.

## Workload

`bench/workloads.json` holds the frozen call signatures with their real-traffic
call counts, and `tensors/` (where present) holds real input/output/state payloads
captured from the running model. `docs/capture_provenance.md` records exactly how
they were produced, including the GSM8K accuracy of the serving run they came from.

Selection rule, restated: shapes are real, ranked by production call count, split
into real-traffic vs warmup-only, and cover the full (sequence length x
concurrency x dataset) matrix - not a single shape.

## Notes

- Rows include the strided / non-contiguous inputs that the tiled decoder produces, and
  the tile-batched shapes (we batch VAE tiles; a kernel that only handles one tile per
  launch loses the win).

## Deliverable

1. Kernel source in `solution/`, buildable standalone against the copied baseline
   ABI (`baseline/`).
2. Benchmark output per workload row: baseline vs candidate, CUDA-graph timed,
   interleaved A/B - see `../../docs/measurement_contract.md`.
3. Correctness-gate output as defined above.
4. If you used Nsight Compute, the report and the bottleneck it identified.
