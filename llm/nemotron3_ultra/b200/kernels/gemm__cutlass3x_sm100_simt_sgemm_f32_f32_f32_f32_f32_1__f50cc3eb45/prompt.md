# KDA Prompt: gemm__cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_1__f50cc3eb45

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4`
- Model folder: `llm/nemotron3_ultra/b200`
- Kernel category: `gemm`
- Max observed GPU share: `7.62%`
- Kernel name: `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_128x128x16_1x1x1_3_tnn_align1_bias_f32_relu`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_high`: 2.56% GPU, calls=196, mean=617.76 us
- `sharegpt_mid`: 7.62% GPU, calls=196, mean=1215.20 us

## Promoted Shape Samples

1. `aten::mm` via `external_id=103493`: `{"Concrete Inputs":["",""],"Input Dims":[[3585,8192],[8192,512]],"Input Strides":[[8192,1],[1,8192]],"Input type":["float","float"]}`
2. `aten::_local_scalar_dense` via `external_id=90633`: `{"Concrete Inputs":[""],"Input Dims":[[]],"Input Strides":[[]],"Input type":["bool"]}`
3. `aten::mm` via `external_id=148770`: `{"Concrete Inputs":["",""],"Input Dims":[[8911,8192],[8192,512]],"Input Strides":[[8192,1],[1,8192]],"Input type":["float","float"]}`
4. `aten::to` via `external_id=157980`: `{"Concrete Inputs":["","6","0","","","False","False",""],"Input Dims":[[1],[],[],[],[],[],[],[]],"Input Strides":[[1],[],[],[],[],[],[],[]],"Input type":["float","Scalar","Scalar","","","Scalar","Scalar",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
