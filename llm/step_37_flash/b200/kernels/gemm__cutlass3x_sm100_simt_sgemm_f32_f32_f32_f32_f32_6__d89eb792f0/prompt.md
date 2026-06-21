# KDA Prompt: gemm__cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_6__d89eb792f0

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `stepfun-ai/Step-3.7-Flash-NVFP4`
- Model folder: `llm/step_37_flash/b200`
- Kernel category: `gemm`
- Max observed GPU share: `4.48%`
- Kernel name: `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_64x64x16_1x1x1_3_tnn_align1_bias_f32_relu`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `sharegpt_mid`: 4.48% GPU, calls=336, mean=461.83 us

## Promoted Shape Samples

1. `aten::transpose` via `external_id=75207`: `{"Concrete Inputs":["","0","1"],"Input Dims":[[4096,160],[],[]],"Input Strides":[[160,1],[],[]],"Input type":["c10::BFloat16","Scalar","Scalar"]}`
2. `aten::mm` via `external_id=74681`: `{"Concrete Inputs":["",""],"Input Dims":[[8510,4096],[4096,288]],"Input Strides":[[4096,1],[1,4096]],"Input type":["float","float"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
