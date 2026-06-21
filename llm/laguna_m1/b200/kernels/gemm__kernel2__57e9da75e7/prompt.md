# KDA Prompt: gemm__kernel2__57e9da75e7

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `poolside/Laguna-M.1-NVFP4`
- Model folder: `llm/laguna_m1/b200`
- Kernel category: `gemm`
- Max observed GPU share: `3.69%`
- Kernel name: `void cutlass::Kernel2<cutlass_80_simt_sgemm_64x64_8x5_tn_align1>(cutlass_80_simt_sgemm_64x64_8x5_tn_align1::Params)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 2.80% GPU, calls=3752, mean=28.30 us
- `random_high`: 3.69% GPU, calls=3216, mean=30.41 us

## Promoted Shape Samples

1. `aten::to` via `external_id=6722`: `{"Concrete Inputs":["","6","0","","","True","False",""],"Input Dims":[[1],[],[],[],[],[],[],[]],"Input Strides":[[1],[],[],[],[],[],[],[]],"Input type":["float","Scalar","Scalar","","","Scalar","Scalar",""]}`
2. `aten::permute` via `external_id=19143`: `{"Concrete Inputs":["","[0, 2, 1, 3]"],"Input Dims":[[62193,64,1,128],[]],"Input Strides":[[8192,128,128,1],[]],"Input type":["c10::BFloat16","ScalarList"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
