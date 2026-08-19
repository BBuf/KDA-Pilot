# DSA sparse attention: indexer logits, top-k transform, sparse MLA (DeepSeek-V4-Flash)

**Task:** `deepseek_v4_flash__dsa_sparse_attention`

**Model:** `deepseek-ai/DeepSeek-V4-Flash`
**Serving command this workload came from (SGLang cookbook recipe):**

```bash
sglang serve --model-path deepseek-ai/DeepSeek-V4-Flash --tp 4
```

**Measured share:** the DSA front end is **8.46%** of serving GPU time as a cluster of 20 kernels (no single one above 1%), the sparse attention core **7.50%**, and the mHC TileLang kernels **8.06%** - measured with CUDA graphs enabled at random 1k/256 concurrency 16, TP4. Per-kernel table in `docs/profile_evidence.md`.

## Kernels in scope

- `dsa_indexer_paged_mqa_logits_*`
- `dsa_topk_transform`
- `dsa_tilelang_sparse_attention`
- `dsa_compress_*`
- `dsa_fused_q_indexer_rope_hadamard_quant`

Baseline sources are copied into `baseline/` from SGLang main @ 43226af (python/sglang, editable install) - the same
implementation the deployment above runs. Do not benchmark against a naive
PyTorch reference; the bar is the shipped kernel.

## Why we are asking for this one

- Your KDA 1.5 table reports 29.95x on DSA sparse attention vs 22.99x for human SOTA.
  This task points that at the actual SGLang production path and shapes instead of a
  standalone benchmark, so a win is directly shippable.
- Our sparse-MLA / indexer path is a mix of TileLang, Triton, DeepGEMM and CuTe-DSL,
  chosen per shape at runtime - the dispatch itself is a target.

## Correctness gate

- The top-k transform must produce the same *set* of selected indices; an approximate
  selection changes model output and is not acceptable, even if logits stay within
  tolerance.
- Sparse attention output compared against the dense reference on the captured index
  sets.

## Workload

`bench/workloads.json` holds the frozen call signatures with their real-traffic
call counts, and `tensors/` (where present) holds real input/output/state payloads
captured from the running model. `docs/capture_provenance.md` records exactly how
they were produced, including the GSM8K accuracy of the serving run they came from.

Selection rule, restated: shapes are real, ranked by production call count, split
into real-traffic vs warmup-only, and cover the full (sequence length x
concurrency x dataset) matrix - not a single shape.

## Notes

- Which of the wrapped entry points actually fires depends on shape and on the
  MoE/indexer flags; `docs/profile_evidence.md` lists the call counts we measured, so
  you can see what is real on the recommended path and what is dead.

## Deliverable

1. Kernel source in `solution/`, buildable standalone against the copied baseline
   ABI (`baseline/`).
2. Benchmark output per workload row: baseline vs candidate, CUDA-graph timed,
   interleaved A/B - see `../docs/measurement_contract.md`.
3. Correctness-gate output as defined above.
4. If you used Nsight Compute, the report and the bottleneck it identified.
