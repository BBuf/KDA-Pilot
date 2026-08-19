# Mamba-2 SSM chunk scan + causal conv1d (NVIDIA Nemotron-3-Nano-30B-A3B-FP8)

**Task:** `nemotron3_nano__mamba2_ssm`

**Model:** `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8`
**Serving command this workload came from (SGLang cookbook recipe):**

```bash
python3 -m sglang.launch_server --model-path nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8 --trust-remote-code --max-running-requests 1024 --host 0.0.0.0 --port 30000
```

**Measured share:** **55.8%** of total serving GPU time (cookbook-aligned profiler sweep, peak scenario ShareGPT at concurrency 32; 22.7-55.8% across the six scenarios). Tonight's capture confirms the call counts and shapes on the same recipe.

## Kernels in scope

- `mamba2_chunk_scan_combined_fwd`
- `mamba2_chunk_scan`
- `mamba2_chunk_state`
- `mamba2_chunk_state_varlen`
- `mamba2_chunk_cumsum`
- `mamba2_state_passing`
- `causal_conv1d_prefill`
- `causal_conv1d_decode`

Baseline sources are copied into `baseline/` from SGLang main @ 43226af (python/sglang, editable install) - the same
implementation the deployment above runs. Do not benchmark against a naive
PyTorch reference; the bar is the shipped kernel.

## Why we are asking for this one

- This is the single largest optimizable kernel family in our whole 50-model sweep after
  attention, and it is 100% Triton - the upstream FLA / mamba-ssm reference lowered to
  Triton, never rewritten for Blackwell.
- It is the same algorithmic shape as the GDN prefill your KDA 1.5 table reports 6.10x
  on, so the transfer should be direct.
- It is NVIDIA's own model, and the operating point below is the one from the SGLang
  cookbook page for it.

## Correctness gate

- `causal_conv1d_decode` and the combined chunk-scan carry state. The gate is the
  **chained final-state** comparison over the 16 consecutive captured decode steps, not
  a per-step output tolerance - see `docs/anti_hack_contract.md`.
- Prefill rows (varlen, chunked) must match on both the output and the returned varlen
  states.

## Workload

`bench/workloads.json` holds the frozen call signatures with their real-traffic
call counts, and `tensors/` (where present) holds real input/output/state payloads
captured from the running model. `docs/capture_provenance.md` records exactly how
they were produced, including the GSM8K accuracy of the serving run they came from.

Selection rule, restated: shapes are real, ranked by production call count, split
into real-traffic vs warmup-only, and cover the full (sequence length x
concurrency x dataset) matrix - not a single shape.

## Notes

- `_mamba_chunk_scan_combined_fwd` is the whole-op entry point: a candidate may replace
  the entire chunk pipeline (cumsum -> chunk_state -> state_passing -> chunk_scan ->
  varlen states) with one kernel, which is where we expect the win.
- Nemotron-3-Nano's MoE does NOT go through the Triton fused-MoE path on B300 (verified
  in this capture: 0 calls), so do not spend effort there for this model.

## Deliverable

1. Kernel source in `solution/`, buildable standalone against the copied baseline
   ABI (`baseline/`).
2. Benchmark output per workload row: baseline vs candidate, CUDA-graph timed,
   interleaved A/B - see `../docs/measurement_contract.md`.
3. Correctness-gate output as defined above.
4. If you used Nsight Compute, the report and the bottleneck it identified.
