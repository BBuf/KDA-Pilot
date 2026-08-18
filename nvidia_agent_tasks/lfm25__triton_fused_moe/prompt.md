# Triton fused MoE GEMM at real serving token counts (LFM2.5-8B-A1B + GLM-4.7-Flash)

**Task:** `lfm25__triton_fused_moe`

**Model:** `LiquidAI/LFM2.5-8B-A1B (primary), zai-org/GLM-4.7-Flash (second shape family)`
**Serving command this workload came from (SGLang cookbook recipe):**

```bash
python3 -m sglang.launch_server --model-path LiquidAI/LFM2.5-8B-A1B --trust-remote-code --attention-backend flashinfer --reasoning-parser qwen3 --tool-call-parser lfm2
```

**Measured share:** 50.5% of total serving GPU time on LFM2.5 (peak: random, concurrency 32); 30.4% on GLM-4.7-Flash

## Kernels in scope

- `triton_fused_moe_gemm`
- `triton_moe_act_and_mul`
- `triton_moe_sum_reduce`
- `moe_align_block_size`

Baseline sources are copied into `baseline/` from SGLang main @ 43226af (python/sglang, editable install) - the same
implementation the deployment above runs. Do not benchmark against a naive
PyTorch reference; the bar is the shipped kernel.

## Why we are asking for this one

- You already measured this one: 1.13x-5.6x on H200 through the same
  `fused_experts_impl` dispatch path. This task supplies the missing half - the real
  per-call token counts and expert-routing shapes from two production models, so the win
  can be claimed at the concurrency that matters.
- Please re-run at >=64 captured tokens with CUDA graphs enabled: our serving profiles
  land there, and the 1/16-token rows in the table you shared are not representative of
  steady-state serving.

## Correctness gate

- Stateless, so exact-shape output comparison per row. `moe_align_block_size` output
  must stay a valid permutation (a wrong sort silently corrupts only some experts).
- Rows carry the real routing distribution (`topk_ids`, `sorted_token_ids`,
  `expert_ids`, `num_tokens_post_padded`); do not regenerate routing uniformly - real
  routing is skewed and that changes the tile occupancy.

## Workload

`bench/workloads.json` holds the frozen call signatures with their real-traffic
call counts, and `tensors/` (where present) holds real input/output/state payloads
captured from the running model. `docs/capture_provenance.md` records exactly how
they were produced, including the GSM8K accuracy of the serving run they came from.

Selection rule, restated: shapes are real, ranked by production call count, split
into real-traffic vs warmup-only, and cover the full (sequence length x
concurrency x dataset) matrix - not a single shape.

## Notes

- Expert weight tensors are metadata-only in the payload (they are far too large to
  ship); their shape/dtype/scale layout is recorded so you can allocate equivalents. The
  activation side - where the distribution matters - is real.
- `triton_fused_moe_gemm` in this capture: 427,506 real calls / 1,138 distinct
  signatures on LFM2.5, 223,652 calls on GLM-4.7-Flash.

## Deliverable

1. Kernel source in `solution/`, buildable standalone against the copied baseline
   ABI (`baseline/`).
2. Benchmark output per workload row: baseline vs candidate, CUDA-graph timed,
   interleaved A/B - see `../docs/measurement_contract.md`.
3. Correctness-gate output as defined above.
4. If you used Nsight Compute, the report and the bottleneck it identified.
