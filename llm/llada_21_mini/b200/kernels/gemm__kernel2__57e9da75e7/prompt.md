# KDA Prompt: gemm__kernel2__57e9da75e7

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `inclusionAI/LLaDA2.1-mini`
- Model folder: `llm/llada_21_mini/b200`
- Kernel category: `gemm`
- Max observed GPU share: `12.39%`
- Kernel name: `void cutlass::Kernel2<cutlass_80_simt_sgemm_64x64_8x5_tn_align1>(cutlass_80_simt_sgemm_64x64_8x5_tn_align1::Params)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 12.39% GPU, calls=2128, mean=28.27 us

## Promoted Shape Samples

1. `aten::view_as` via `external_id=7460`: `{"Concrete Inputs":["",""],"Input Dims":[[1],[]],"Input Strides":[[1],[]],"Input type":["bool","bool"]}`
2. `aten::slice` via `external_id=10331`: `{"Concrete Inputs":["","0","1","2","1"],"Input Dims":[[2],[],[],[],[]],"Input Strides":[[1],[],[],[],[]],"Input type":["int","Scalar","Scalar","Scalar","Scalar"]}`
3. `aten::slice` via `external_id=12673`: `{"Concrete Inputs":["","0","0","1","1"],"Input Dims":[[1],[],[],[],[]],"Input Strides":[[1],[],[],[],[]],"Input type":["int","Scalar","Scalar","Scalar","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
