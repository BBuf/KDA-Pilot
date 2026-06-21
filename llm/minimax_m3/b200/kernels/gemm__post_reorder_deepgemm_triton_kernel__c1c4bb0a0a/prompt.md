# KDA Prompt: gemm__post_reorder_deepgemm_triton_kernel__c1c4bb0a0a

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `MiniMaxAI/MiniMax-M3-MXFP8`
- Model folder: `llm/minimax_m3/b200`
- Kernel category: `gemm`
- Max observed GPU share: `2.78%`
- Kernel name: `post_reorder_deepgemm_triton_kernel`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 2.78% GPU, calls=4104, mean=22.66 us

## Promoted Shape Samples

1. `aten::fill_` via `external_id=39996`: `{"Concrete Inputs":["","971"],"Input Dims":[[],[]],"Input Strides":[[],[]],"Input type":["long int","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
