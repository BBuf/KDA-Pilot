# KDA Prompt: gemm__cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_1__b4f87b5018

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4`
- Model folder: `llm/nemotron3_ultra/b200`
- Kernel category: `gemm`
- Max observed GPU share: `10.45%`
- Kernel name: `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_128x64x16_1x1x1_3_tnn_align1_bias_f32_relu`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 10.45% GPU, calls=196, mean=1965.22 us
- `random_high`: 9.79% GPU, calls=196, mean=2367.78 us
- `sharegpt_high`: 9.46% GPU, calls=196, mean=1655.60 us

## Promoted Shape Samples

1. `aten::mm` via `external_id=47120`: `{"Concrete Inputs":["",""],"Input Dims":[[12203,8192],[8192,512]],"Input Strides":[[8192,1],[1,8192]],"Input type":["float","float"]}`
2. `aten::view` via `external_id=44868`: `{"Concrete Inputs":["","[1, 96, 64, 8192]"],"Input Dims":[[1,96,64,64,128],[]],"Input Strides":[[50331648,524288,8192,128,1],[]],"Input type":["float","ScalarList"]}`
3. `nccl:_all_gather_base` via `external_id=49300`: `{"Concrete Inputs":[""],"Input Dims":[[12203,2048]],"Input Strides":[[2048,1]],"Input type":["c10::BFloat16"]}`
4. `aten::squeeze` via `external_id=81479`: `{"Concrete Inputs":["","0"],"Input Dims":[[1,64,121,128],[]],"Input Strides":[[991232,15488,128,1],[]],"Input type":["float","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
