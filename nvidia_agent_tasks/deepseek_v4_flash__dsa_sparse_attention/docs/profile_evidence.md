# Profile evidence: DeepSeek-V4-Flash

## The pipeline, and where each captured op sits in it

`forward_c4_indexer` runs this chain per layer, per forward pass. Every stage below is
now captured (an earlier pass missed two of them, see "corrections"):

| # | stage | captured op | real calls |
| --- | --- | --- | ---: |
| 1 | KV compression, both levels (`compress_ratio` 4 **and** 128) | `dsa_compress_forward` | 183527 |
| 1b | RMSNorm + RoPE + store into the paged KV cache | `dsa_compress_norm_rope_store` | 183526 |
| 2 | q-side indexer: RoPE + Hadamard + quant, one kernel | `dsa_fused_q_indexer_rope_hadamard_quant` | 62164 |
| 3 | **indexer logits** - the default implementation, imported straight from the `deep_gemm` package | `dsa_indexer_logits_deepgemm_DEFAULT` | 62164 |
| 3b | schedule planner for stage 3 (not a compute kernel) | `dsa_paged_mqa_logits_metadata` | 2964 |
| 4 | select the top-512 pages | `dsa_topk_transform_v2` (long ctx) / `dsa_topk_transform` (short) | 59808 / 2356 |
| 5 | **sparse attention core** - `flash_mla_sparse_fwd` from `sgl_kernel` | `dsa_sparse_attention_flash_mla_alt` | 4825 |

GSM8K accuracy of the capture runs: **1.000** (16-shot, 16-way) and **0.980** (200
questions, 5-shot). Real tensors for every stage are in `bench/tensors/`.

## Measured GPU-time share (the denominator this task was missing)

Torch profiler, **CUDA graphs enabled** (i.e. the real deployment, not the capture
configuration), TP4 on B300, random 1024-in / 256-out at concurrency 16. Full table in
`../docs/profiles/kernel_shapes_dsv4_full.json`; 99.3% of GPU time accounted for:

| block | share | note |
| --- | ---: | --- |
| GEMM (deep_gemm fp8/fp4, nvjet, cublas) | 30.3% | vendor, not in scope |
| MoE (trtllm bmm / routing / finalize) | 18.0% | vendor, excluded by design |
| collectives (trtllm mnnvl allreduce) | 16.8% | excluded by design |
| **mHC hyper-connections (TileLang)** | **8.06%** | `mhc_pre_big_fuse_with_norm` 4.69% + `mhc_post` 3.37% - our code, see below |
| **DSA front end, aggregate over 20 kernels** | **8.46%** | biggest single one is 0.93% |
| **sparse MLA attention core** | **7.50%** | `flash_fwd_splitkv_mla_fp8_sparse` 4.87% + combine 2.63% |
| quant | 5.34% | |

Read that carefully, because it changes what to optimize:

* **No single DSA front-end kernel clears 1% of GPU time.** As a *cluster* the front end
  is 8.46% across 20 kernels, so the win here is **fusion and launch-count reduction**,
  not a faster individual kernel. The obvious first move is stages 1 and 1b: they are
  back-to-back, share the same `plan`, and fire the same number of times (183527 each).
* The **sparse attention core is 7.50%** and is vendor CUDA (`flash_mla`), so that one is
  a straight "beat the vendor kernel" target on the captured index sets.
* **mHC is the largest non-vendor block at 8.06%** and it is TileLang, i.e. exactly the
  kind of code a kernel agent can rewrite. It is DeepSeek-V4's manifold-constrained
  hyper-connections, not part of DSA at all - we scoped it into this task because it
  showed up while measuring the denominator. Shapes: `bench/workloads_mhc.json`
  (155,492 real calls per entry point, 34 distinct signatures), tensors:
  `bench/tensors_mhc/`.

## Corrections to the first pass (kept visible on purpose)

* Stages 3 and 5 were **missing** from the first capture. The default indexer-logits
  implementation is imported *directly from the `deep_gemm` package*
  (`from deep_gemm import fp8_paged_mqa_logits`), bypassing SGLang's own wrapper, and the
  sparse core comes from `sgl_kernel`. We had wrapped only the SGLang-side wrappers, so
  both read as "0 calls". They are captured now.
* Still 0 calls on the cookbook recipe, and therefore **not** targets:
  `tilelang_sparse_fwd`, `dpsk_v4_fp8_attention_fwd`, `triton_sparse_mla_fwd`,
  `tilelang_fp8_paged_mqa_logits`, the CuTe-DSL and split DeepGEMM logits wrappers, and
  `fp8_fp4_paged_mqa_logits` (that one needs `--enable-deepseek-v4-fp4-indexer`).
* `dsa_paged_mqa_logits_metadata` is a **planner**, not a compute kernel: its only inputs
  are `seq_lens`, `page_size` and `num_sm`. Do not spend time on it.

## Shape families

See `../SHAPES.md`. The two that matter most: `scores[T, 262208]` non-contiguous into the
top-k transform, and the two compression levels (`compress_ratio` 4 and 128) that make
stages 1/1b run twice per layer with different geometry.
