# FP8 fused MoE at GLM-4.5's 161-expert geometry (GLM-4.5-FP8, TP=8)

**Task:** `glm45__fp8_fused_moe`

**Model:** `zai-org/GLM-4.5-FP8`
**Serving command this workload came from (SGLang cookbook recipe):**

```bash
python3 -m sglang.launch_server --model-path zai-org/GLM-4.5-FP8 --trust-remote-code \
    --reasoning-parser glm45 --tool-call-parser glm45 --moe-runner-backend triton --tp 8
```

**Measured share:** **51.5%** of total serving GPU time is the expert GEMM alone
(`fused_moe_kernel`), and **64.3%** is the whole MoE dispatch once the per-token FP8
activation quant (6.2%), SiLU-and-mul (1.6%), block-size alignment (3.0%) and the
weighted sum (2.0%) are counted with it - torch-profiler sweep on 8x B300 at
random 1024/256, concurrency 16, CUDA graphs on. Details in `docs/profile_evidence.md`.

## Kernels in scope

- `triton_fused_moe_gemm` - `invoke_fused_moe_kernel` in its FP8 arm
- `moe_fused_experts_fp8` - `fused_experts_impl`, the whole dispatch

Baseline sources are copied into `baseline/` from SGLang main @ 43226af (python/sglang,
editable install) - the same implementation the deployment above runs. Do not benchmark
against a naive PyTorch reference; the bar is the shipped kernel.

## Why we are asking for this one

- This is the largest single kernel share in any task in this set. Half of a GLM-4.5
  deployment's GPU time is one Triton kernel, and the FP8 arm is a different kernel from
  the bf16 arm in `lfm25__triton_fused_moe`: weights are FP8 with per-output-channel
  scales, and the activation is quantized per token before the tile loop.
- Two levels are timed because two different wins are available. At
  `triton_fused_moe_gemm` the target is the tile schedule under real, skewed routing. At
  `moe_fused_experts_fp8` the intermediate `[tokens*9, 384]` buffer between the two GEMMs
  can be removed entirely - that traffic is why the quant and act kernels show up in the
  profile at all.
- Both operating extremes are in the row set: single-token decode (`A[1, 5120]`, 199,360
  real calls) and a 146,439-row prefill tile. A candidate tuned only for the large tile
  will lose the decode case, which is where the calls are.

## Geometry (as captured, not as documented)

| | value |
| --- | --- |
| experts | 161 = 160 routed + the shared expert fused in as expert 160 |
| top-k | 9 (8 routed + shared) |
| hidden | 5120 |
| gate/up width | 384, interleaved as two 192-wide halves (`gate_up_interleaved=True`) |
| w1 / w2 | `[161, 384, 5120]` / `[161, 5120, 192]`, `float8_e4m3fn` |
| scales | per output channel: `w1_scale[161, 384, 1]`, `w2_scale[161, 5120, 1]`, float32 |
| activation | SiLU, `routed_scaling_factor=2.5`, `per_channel_quant=True`, `block_shape=None` |

## One thing to check before claiming a win

The shipped SGLang has **no tuned Triton config for this geometry on B300**: it looks for
`configs/triton_3_7_1/E=161,N=192,device_name=NVIDIA_B300_SXM6_AC,dtype=fp8_w8a8,per_channel_quant=True.json`,
does not find it, and prints *"Using default MoE kernel config. Performance might be
sub-optimal!"*. The 51.5% share above was measured in that state, so it is the real
deployment number - but part of any speedup measured against this baseline would just be
the missing tuning. Generate the config with SGLang's own tuner
(`benchmark/kernels/fused_moe_triton`) and report both numbers.

## Correctness gate

- Stateless, so exact-shape output comparison per row, `torch.testing.assert_close` at
  the rtol/atol SGLang's own MoE test uses (1e-5 / 1e-5, `test/registered/moe/
  test_triton_fused_moe.py:45-49`).
- `moe_fused_experts_fp8` runs with `inplace=True` in production: the returned tensor
  must alias `hidden_states` and every call must overwrite it. The harness restores the
  in-place inputs between iterations, so a candidate that quietly caches the output is
  caught by the gate rather than rewarded by the timer.
- Routing is real (`topk_ids`, `topk_weights`, `sorted_token_ids`, `expert_ids`,
  `num_tokens_post_padded` come from the captured serving run). Do not regenerate routing
  uniformly - real routing is skewed and that is what sets tile occupancy.

## Workload

`bench/workloads.json` holds the frozen call signatures with their real-traffic
call counts, and `tensors/` holds real input/output payloads captured from the running
model - every row in this task has one. `docs/capture_provenance.md` records exactly how
they were produced, including the GSM8K accuracy of the serving run they came from.

Selection rule, restated: shapes are real, ranked by production call count, split
into real-traffic vs warmup-only, and cover the full (sequence length x
concurrency x dataset) matrix - not a single shape.

## Notes

- Expert weight tensors are metadata-only in the payload (a single `[161, 384, 5120]`
  FP8 weight is 316 MB); their shape, dtype and scale layout are recorded so you can
  allocate equivalents. Weight-only preprocessing is allowed as long as the prepared call
  still reads live hidden states and live routing on every invocation.
- `filter_expert=False` and `mul_routed_weight=False` on the up GEMM in this capture -
  the routing weight is applied on the down GEMM. Keep that split; moving it changes
  which arm the tolerance applies to.
- 1,604,864 real calls of the GEMM across 178 distinct signatures, 802,432 calls of the
  dispatch across 89 signatures, in one four-point capture.

## Deliverable

1. Kernel source in `solution/`, buildable standalone against the copied baseline
   ABI (`baseline/`).
2. Benchmark output per workload row: baseline vs candidate, CUDA-graph timed,
   interleaved A/B - see `../docs/measurement_contract.md`.
3. Correctness-gate output as defined above.
4. If you used Nsight Compute, the report and the bottleneck it identified.
