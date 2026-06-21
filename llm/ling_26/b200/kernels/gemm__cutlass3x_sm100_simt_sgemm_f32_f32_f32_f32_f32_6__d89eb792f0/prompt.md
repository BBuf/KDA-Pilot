# KDA Prompt: gemm__cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_6__d89eb792f0

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `inclusionAI/Ling-2.6-flash`
- Model folder: `llm/ling_26/b200`
- Kernel category: `gemm`
- Max observed GPU share: `6.66%`
- Kernel name: `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_64x64x16_1x1x1_3_tnn_align1_bias_f32_relu`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 6.66% GPU, calls=124, mean=459.04 us
- `sharegpt_mid`: 6.29% GPU, calls=124, mean=544.50 us

## Promoted Shape Samples

1. `aten::mm` via `external_id=19289`: `{"Concrete Inputs":["",""],"Input Dims":[[9780,4096],[4096,256]],"Input Strides":[[4096,1],[1,4096]],"Input type":["float","float"]}`
2. `aten::view` via `external_id=19217`: `{"Concrete Inputs":["","[22]"],"Input Dims":[[22],[]],"Input Strides":[[1],[]],"Input type":["long int","ScalarList"]}`
3. `aten::as_strided` via `external_id=20357`: `{"Concrete Inputs":["","[9780, 8, 128]","[1536, 192, 1]","0"],"Input Dims":[[9780,8,192],[],[],[]],"Input Strides":[[1536,192,1],[],[],[]],"Input type":["c10::BFloat16","ScalarList","ScalarList","Scalar"]}`
4. `aten::mm` via `external_id=65869`: `{"Concrete Inputs":["",""],"Input Dims":[[12199,4096],[4096,256]],"Input Strides":[[4096,1],[1,4096]],"Input type":["float","float"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
