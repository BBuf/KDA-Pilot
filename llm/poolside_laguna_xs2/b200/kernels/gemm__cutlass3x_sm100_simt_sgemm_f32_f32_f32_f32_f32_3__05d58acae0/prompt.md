# KDA Prompt: gemm__cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_3__05d58acae0

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `poolside/Laguna-XS.2-FP8`
- Model folder: `llm/poolside_laguna_xs2/b200`
- Kernel category: `gemm`
- Max observed GPU share: `4.88%`
- Kernel name: `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_32x32x16_1x1x1_3_tnn_align1_bias_f32_relu`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `sharegpt_mid`: 4.25% GPU, calls=468, mean=46.28 us
- `sharegpt_high`: 4.88% GPU, calls=468, mean=46.47 us

## Promoted Shape Samples

1. `aten::as_strided` via `external_id=40156`: `{"Concrete Inputs":["","[31]","[0]",""],"Input Dims":[[32],[],[],[]],"Input Strides":[[1],[],[],[]],"Input type":["long int","ScalarList","ScalarList",""]}`
2. `aten::view` via `external_id=42220`: `{"Concrete Inputs":["","[31]"],"Input Dims":[[31],[]],"Input Strides":[[1],[]],"Input type":["long int","ScalarList"]}`
3. `aten::narrow` via `external_id=51125`: `{"Concrete Inputs":["","0","320","41"],"Input Dims":[[361],[],[],[]],"Input Strides":[[1],[],[],[]],"Input type":["long int","Scalar","Scalar","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
