# Gated DeltaNet chunk prefill + fused recurrent decode (Qwen3-Next-80B-A3B)

**Target agent:** KDA 1.5  **Task id:** `A5_qwen3_next__gdn_prefill`

**Model:** `Qwen/Qwen3-Next-80B-A3B-Instruct`
**Serving command this workload came from (SGLang cookbook recipe):**

```bash
python -m sglang.launch_server --model Qwen/Qwen3-Next-80B-A3B-Instruct --tp 8 --host 0.0.0.0 --port 8000
```

**Measured share:** linear_gemm 44.3% / rmsnorm 6.8% in the earlier sweep; the GDN kernels themselves are measured per call in this capture (see profile_evidence.md)

## Kernels in scope

- `gdn_chunk_prefill`
- `gdn_chunk_delta_h`
- `gdn_chunk_o`
- `gdn_recompute_w_u`
- `gdn_fused_recurrent_decode`
- `kda_chunk_prefill`
- `kda_fused_recurrent_decode`

Baseline sources are copied into `baseline/` from SGLang main @ 43226af (python/sglang, editable install) - the same
implementation the deployment above runs. Do not benchmark against a naive
PyTorch reference; the bar is the shipped kernel.

## Why we are asking for this one

- This is the exact kernel family in your KDA 1.5 table (GDN prefill 6.10x). On SGLang
  main the Blackwell-specific work is partial: `linear/gdn_blackwell` and your own
  `linear/kda_nvidia_prefill` (KDA_prefill, 2.3-2.9x vs FLA on B200 - already vendored
  in our tree) cover some paths, while the FLA Triton chunk kernels still carry Hopper
  and the non-Blackwell fallbacks.
- Two model families share these kernels (Qwen3-Next GDN, Kimi-Linear/K3 KDA), so one
  kernel win lands twice.

## Correctness gate

- State-carrying: chained final-state comparison over the 16 consecutive captured decode
  steps. Per-step output tolerance is explicitly NOT the gate - we have shipped a state
  kernel that passed per-step and drifted in the state.
- Prefill: output plus `final_state` against the FLA baseline on the captured ragged
  `cu_seqlens`.

## Workload

`bench/workloads.json` holds the frozen call signatures with their real-traffic
call counts, and `tensors/` (where present) holds real input/output/state payloads
captured from the running model. `docs/capture_provenance.md` records exactly how
they were produced, including the GSM8K accuracy of the serving run they came from.

Selection rule, restated: shapes are real, ranked by production call count, split
into real-traffic vs warmup-only, and cover the full (sequence length x
concurrency x dataset) matrix - not a single shape.

## Notes

- Gate/beta buffers are padded to a multiple of 16, so their sequence dim is LARGER than
  q/k/v's - a real-workload detail that synthetic shapes miss.
- `initial_state` is fp32 while q/k/v/g are bf16, and decode inputs can be non-
  contiguous slices of a fused QKV buffer.

## Deliverable

1. Kernel source in `solution/`, buildable standalone against the copied baseline
   ABI (`baseline/`).
2. Benchmark output per workload row: baseline vs candidate, CUDA-graph timed,
   interleaved A/B - see `../../docs/measurement_contract.md`.
3. Correctness-gate output as defined above.
4. If you used Nsight Compute, the report and the bottleneck it identified.
