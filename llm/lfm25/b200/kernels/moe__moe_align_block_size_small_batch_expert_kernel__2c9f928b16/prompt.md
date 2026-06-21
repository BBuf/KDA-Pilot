# KDA Prompt: moe__moe_align_block_size_small_batch_expert_kernel__2c9f928b16

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`moe` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `LiquidAI/LFM2.5-8B-A1B`
- Model folder: `llm/lfm25/b200`
- Kernel category: `moe`
- Max observed GPU share: `5.09%`
- Kernel name: `void moe_align_block_size_small_batch_expert_kernel<int, 256>(int const*, int*, int*, int*, int, int, unsigned long, bool, int)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 5.09% GPU, calls=198, mean=5.20 us

## Promoted Shape Samples

1. `sgl_kernel::moe_align_block_size` via `external_id=1200`: `{"Concrete Inputs":["","33","16","","","","","True"],"Input Dims":[[103,4],[],[],[907],[57],[1],[34],[]],"Input Strides":[[4,1],[],[],[1],[1],[1],[1],[]],"Input type":["int","Scalar","Scalar","int","int","int","int","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
