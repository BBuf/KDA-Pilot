# Profile evidence: FP8 fused MoE (GLM-4.5-FP8, TP=8, B300)

## Where the GPU time goes

Torch profiler over a steady-state window of `sglang.bench_serving --dataset-name random
--random-input-len 1024 --random-output-len 256 --num-prompts 32 --max-concurrency 16`,
served with the cookbook command and **CUDA graphs on** (the deployment configuration -
the capture runs that produced the tensors disable them, the profile does not).
Rank 0 of 8, 9.63 s of GPU time, 98.7% of it accounted for by the 21 kernels above 0.2%:

| share | kernel | calls | belongs to |
| ---: | --- | ---: | --- |
| **51.53%** | `fused_moe_kernel` | 81,168 | the expert GEMM, both arms |
| 6.17% | `per_token_quant_fp8_cta_kernel` | 167,719 | activation quant inside the dispatch |
| 5.74% | `fmhaSm100fKernel_...PagedKvCausal...` | 40,296 | attention |
| 4.24% | `cutlass ... GemmUniversal` | 40,204 | dense projections |
| 3.12% | `cutlass ... GemmUniversal` | 42,826 | dense projections |
| 3.09% | `trtllm_mnnvl_allreduce::oneshotAllreduceFusion` | 37,698 | TP collectives |
| 2.78% | `cutlass_80_tensorop_s1688gemm_64x64_32x6_tn` | 40,139 | dense projections |
| 2.70% | `trtllm_mnnvl_allreduce::rmsNormLamport` | 45,567 | TP collectives |
| 2.35% | `_router_triton_kernel` | 40,584 | MoE routing |
| 2.25% | `unrolled_elementwise_kernel` (`aten::copy_`) | 41,040 | - |
| 2.23% | `trtllm_mnnvl_allreduce::twoshotAllreduceKernel` | 45,750 | TP collectives |
| 1.96% | `triton_per_fused_copy__mul_sum_0` | 39,694 | the MoE weighted sum |
| 1.63% | `act_and_mul_kernel` | 41,952 | SiLU-and-mul between the two GEMMs |
| 1.61% | `cublasLt::splitKreduce_kernel` | 40,228 | dense projections |
| 1.55% | `fused_rope_kernel` | 41,952 | attention |
| 1.54% | `moe_align_block_size_kernel` | 30,705 | MoE alignment |
| 1.24% | `store_kvcache` | 41,952 | attention |
| 1.16% | `fused_qknorm_warp` | 41,952 | attention |
| 0.80% | `_moe_align_small_numel_kernel` | 9,879 | MoE alignment |
| 0.65% | `count_and_sort_expert_tokens_kernel` | 30,705 | MoE alignment |
| 0.31% | `fmhaSm103aKernel_...VarSeqQ128Kv1` | 1,656 | attention |

Two numbers follow, and the task is scoped against both:

* **51.5%** - `fused_moe_kernel` alone. This is what `triton_fused_moe_gemm` times.
* **64.3%** - that plus the per-token FP8 quant (6.17%), SiLU-and-mul (1.63%), the three
  alignment kernels (1.54 + 0.80 + 0.65 = 2.99%) and the weighted sum (1.96%). This is
  what `moe_fused_experts_fp8` times, and it is the level at which the intermediate
  buffer between the two GEMMs can be removed rather than just written faster.

The MoE routing kernel (2.35%) is deliberately *not* counted: it selects the experts and
runs before the dispatch, and it is a separate optimization target.

## `workloads.json`

| op | real calls | distinct signatures | rows kept | rows with real tensors |
| --- | ---: | ---: | ---: | ---: |
| `triton_fused_moe_gemm` | 1,604,864 | 178 | 8 | 8 |
| `moe_fused_experts_fp8` | 802,432 | 89 | 9 | 9 |

The GEMM is called twice per dispatch (up and down), which is why its call count is
exactly twice the dispatch's.

Token counts covered, from the four operating points: 1, 11, 13, 14, 15, 16, 24, 26, 32
and 16,271 hidden rows (146,439 after expert expansion on the down GEMM). Single-token
decode is 199,360 of the calls - a candidate that only wins on the large tile wins on
the rare case.

Call counts are real traffic only: every call observed before a capture-group label was
active (start-up, CUDA-graph capture, autotune) is kept separately in the
`warmup_only_shapes` section of the source manifest and never enters a workload row.
This capture recorded **0** warmup-only signatures for these two ops, because the FP8
MoE only runs once real requests arrive. See `../../docs/workload_capture.md`.

Expert weights are metadata-only in the payload - a single `[161, 384, 5120]` FP8 weight
is 316 MB - and their shape, dtype and per-output-channel scale layout are recorded. The
activation and routing side is real, which is where the distribution matters: real
routing is skewed and that changes tile occupancy.
