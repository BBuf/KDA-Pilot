# Write a new sm_103 sub-block block-sparse attention kernel (MiniMax-H3 video DiT)

**Task:** `minimax_h3__sm103_block_sparse_attention`

**Model:** `MiniMaxAI/MiniMax-H3 (video+audio DiT, 8x B300, sp/ulysses 8)`
**Serving command this workload came from (SGLang cookbook recipe):**

```bash
sglang serve <MiniMax-H3 snapshot> --model-variant fl2va --performance-mode speed --num-gpus 8 --sp-degree 8 --ulysses-degree 8
```

**Measured share:** the sparse arm is the only backend that beats our cache-only default on B300: 10.37 s vs 11.16 s per video (3.97x vs 3.69x over Diffusers)

## Kernels in scope

- `block-sparse forward attention on sm_103 (FusedAttnFwdSm100 lineage)`

Baseline sources are copied into `baseline/` from SGLang main @ 43226af (python/sglang, editable install) - the same
implementation the deployment above runs. Do not benchmark against a naive
PyTorch reference; the bar is the shipped kernel.

## Why we are asking for this one

- The existing sub-block BSA kernel deadlocks on SM103 roughly once every four requests,
  which is why we ship it as an experiment instead of the default. We root-caused it to
  the register-pool re-allocation protocol (`setmaxnreg USETMAXREG.TRY_ALLOC.CTAPOOL`):
  a scheduler warp that exits or spins out of phase never releases its registers, the
  remaining warpgroups spin in the TRY_ALLOC retry loop, and the MMA that is gated by
  the same protocol never writes its completion flag. Two rounds of kernel-side fixes
  (named-barrier ID overflow, 512-barrier lockstep exit) did not remove it.
- This is a new-kernel task, not a port: we want a sub-block BSA forward that is correct
  and deadlock-free on sm_103 with the H3 shapes below, and at least as fast as the
  current sparse arm.

## Correctness gate

- 100 consecutive requests with no hang (the failure rate we measured is ~25% per
  request, so 100 clean runs is the bar) plus deterministic output across runs.
- Numerics: LPIPS budget of the shipped arm (mean <=0.35 / max <=0.42 on our 3-prompt
  reference set) - the sparse arm is lossy by construction, so the gate is a quality
  budget, not bit-exactness.
- Named barrier IDs must come from the reserved enum, not from raw integers: the first
  bug we found was a raw ID + 8 offset wrapping past hardware barrier 16 back onto
  `__syncthreads`.

## Workload

`bench/workloads.json` holds the frozen call signatures with their real-traffic
call counts, and `tensors/` (where present) holds real input/output/state payloads
captured from the running model. `docs/capture_provenance.md` records exactly how
they were produced, including the GSM8K accuracy of the serving run they came from.

Selection rule, restated: shapes are real, ranked by production call count, split
into real-traffic vs warmup-only, and cover the full (sequence length x
concurrency x dataset) matrix - not a single shape.

## Notes

- Forensics that pinned it, in case you want to reproduce: py-spy main stack
  `cuLaunchKernel` identifies the culprit rank vs `cuMemcpyDtoDAsync` on the waiters
  (7-vs-1 split); the hung CTA's 16 warps sit at EXIT / TRY_ALLOC / NANOSLEEP.SYNCS
  under cuda-gdb with lineinfo.
- A second, independent lever sits next to this one: under the sub-block backend the
  non-sparse branch falls back to a slow path (audio-tower steps go 44 ms -> 191 ms),
  which eats most of the sparse win. See task `minimax_h3__sparse_backend_fallback`.

## Deliverable

1. Kernel source in `solution/`, buildable standalone against the copied baseline
   ABI (`baseline/`).
2. Benchmark output per workload row: baseline vs candidate, CUDA-graph timed,
   interleaved A/B - see `../docs/measurement_contract.md`.
3. Correctness-gate output as defined above.
4. If you used Nsight Compute, the report and the bottleneck it identified.
