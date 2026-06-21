# KDA Prompt: gemm__cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_1__b4f87b5018

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `MiniMaxAI/MiniMax-M2`
- Model folder: `llm/minimax_m2/b200`
- Kernel category: `gemm`
- Max observed GPU share: `3.02%`
- Kernel name: `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_128x64x16_1x1x1_3_tnn_align1_bias_f32_relu`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_high`: 2.89% GPU, calls=248, mean=126.08 us
- `sharegpt_mid`: 2.40% GPU, calls=248, mean=126.88 us
- `sharegpt_high`: 3.02% GPU, calls=248, mean=125.84 us

## Promoted Shape Samples

1. `aten::view` via `external_id=22811`: `{"Concrete Inputs":["","[-1, 256]"],"Input Dims":[[2797,2,128],[]],"Input Strides":[[2048,128,1],[]],"Input type":["c10::Half","ScalarList"]}`
2. `aten::view` via `external_id=41346`: `{"Concrete Inputs":["","[-1, 12, 128]"],"Input Dims":[[3027,1536],[]],"Input Strides":[[1536,1],[]],"Input type":["c10::Half","ScalarList"]}`
3. `aten::slice` via `external_id=57540`: `{"Concrete Inputs":["","0","-1","9223372036854775807","1"],"Input Dims":[[256],[],[],[],[]],"Input Strides":[[1],[],[],[],[]],"Input type":["long int","Scalar","Scalar","Scalar","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
