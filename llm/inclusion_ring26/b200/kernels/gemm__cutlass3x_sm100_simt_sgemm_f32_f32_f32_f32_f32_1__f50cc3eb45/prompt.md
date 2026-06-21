# KDA Prompt: gemm__cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_1__f50cc3eb45

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `inclusionAI/Ring-2.6-1T`
- Model folder: `llm/inclusion_ring26/b200`
- Kernel category: `gemm`
- Max observed GPU share: `8.74%`
- Kernel name: `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_128x128x16_1x1x1_3_tnn_align1_bias_f32_relu`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 7.41% GPU, calls=608, mean=1219.38 us
- `random_high`: 8.08% GPU, calls=1216, mean=1219.07 us
- `sharegpt_high`: 8.74% GPU, calls=1216, mean=1219.36 us

## Promoted Shape Samples

1. `aten::mm` via `external_id=33685`: `{"Concrete Inputs":["",""],"Input Dims":[[16384,8192],[8192,256]],"Input Strides":[[8192,1],[1,8192]],"Input type":["float","float"]}`
2. `sgl_kernel::sgl_per_token_quant_fp8` via `external_id=33091`: `{"Concrete Inputs":["","",""],"Input Dims":[[16384,8192],[16384,8192],[16384,1]],"Input Strides":[[8192,1],[8192,1],[1,1]],"Input type":["c10::BFloat16","c10::Float8_e4m3fn","float"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
