# KDA Prompt: gemm__cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_1__b4f87b5018

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `MiniMaxAI/MiniMax-M2.7`
- Model folder: `llm/minimax_m27/b200`
- Kernel category: `gemm`
- Max observed GPU share: `3.88%`
- Kernel name: `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_128x64x16_1x1x1_3_tnn_align1_bias_f32_relu`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_high`: 3.88% GPU, calls=496, mean=127.84 us
- `sharegpt_mid`: 3.12% GPU, calls=496, mean=128.52 us

## Promoted Shape Samples

1. `aten::as_strided` via `external_id=23967`: `{"Concrete Inputs":["","[1]","[1]","447"],"Input Dims":[[448],[],[],[]],"Input Strides":[[1],[],[],[]],"Input type":["long int","ScalarList","ScalarList","Scalar"]}`
2. `aten::as_strided` via `external_id=43038`: `{"Concrete Inputs":["","[64824, 1, 64, 128]","[8192, 8192, 128, 1]",""],"Input Dims":[[64824,1,64,128],[],[],[]],"Input Strides":[[8192,128,128,1],[],[],[]],"Input type":["c10::BFloat16","ScalarList","ScalarList",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
