# Sol-Attn on sm_103 + the sub-block backend's dense fallback (MiniMax-H3)

**Task:** `minimax_h3__sparse_backend_fallback`

**Model:** `MiniMaxAI/MiniMax-H3 (NVlabs Sol-Attn as the sparse backend)`
**Serving command this workload came from (SGLang cookbook recipe):**

```bash
sglang serve <H3 snapshot> --attention-backend sol_attn --component-attention-backends '{"text_encoder":"fa"}'
```

**Measured share:** H3 step budget: attention 48% / GEMM 35% / NCCL a2a 8%

## Kernels in scope

- `sparse attention backend selection + dense fallback path`

Baseline sources are copied into `baseline/` from SGLang main @ 43226af (python/sglang, editable install) - the same
implementation the deployment above runs. Do not benchmark against a naive
PyTorch reference; the bar is the shipped kernel.

## Why we are asking for this one

- We benchmarked all three sparse backends on B300 on top of our cache schedule: sub-
  block BSA 10.37 s (fast, but deadlocks - task `minimax_h3__sm103_block_sparse_attention`), flex/cube 13.38 s with LPIPS 0.522
  (loses on both axes), and NVlabs Sol-Attn (Triton) 12.87 s / LPIPS 0.365 - i.e. Sol-
  Attn is *slower than our dense cuDNN baseline* on B300. The 1.15x in its own report is
  against FA3 on H200; our dense baseline is cuDNN, which is faster, so the Triton
  implementation cannot win. A CuTe sm_103 implementation is what would make it
  competitive.
- Second, smaller item in the same file: with a sparse backend active, sequences below
  the backend's `min_seq_len` take a slow fallback - H3's audio-tower steps go 44 ms ->
  191 ms and eat most of the sparse win (net gain drops to 7.1%). Fixing the fallback is
  worth roughly 10.37 s -> ~9 s.

## Correctness gate

- Same LPIPS budget as C1 (mean <=0.35 / max <=0.42) and no regression on the non-sparse
  branch: audio-tower step time must stay at the dense-path 44 ms.

## Workload

`bench/workloads.json` holds the frozen call signatures with their real-traffic
call counts, and `tensors/` (where present) holds real input/output/state payloads
captured from the running model. `docs/capture_provenance.md` records exactly how
they were produced, including the GSM8K accuracy of the serving run they came from.

Selection rule, restated: shapes are real, ranked by production call count, split
into real-traffic vs warmup-only, and cover the full (sequence length x
concurrency x dataset) matrix - not a single shape.

## Notes

- Install/repro detail: with `--attention-backend sol_attn` the CUDA platform resolver
  never runs, so `set_fa_ver(4)` is never called and the dense guard raises ImportError
  on Blackwell. We work around it by calling
  `current_platform._prepare_flash_attention_for_blackwell()` before building the dense
  impl.

## Deliverable

1. Kernel source in `solution/`, buildable standalone against the copied baseline
   ABI (`baseline/`).
2. Benchmark output per workload row: baseline vs candidate, CUDA-graph timed,
   interleaved A/B - see `../docs/measurement_contract.md`.
3. Correctness-gate output as defined above.
4. If you used Nsight Compute, the report and the bottleneck it identified.
