# KDA Prompt: gemm__kernel2__57e9da75e7

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4`
- Model folder: `llm/nemotron3_ultra/b200`
- Kernel category: `gemm`
- Max observed GPU share: `9.14%`
- Kernel name: `void cutlass::Kernel2<cutlass_80_simt_sgemm_64x64_8x5_tn_align1>(cutlass_80_simt_sgemm_64x64_8x5_tn_align1::Params)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 8.82% GPU, calls=1568, mean=35.72 us
- `sharegpt_low`: 9.14% GPU, calls=1568, mean=35.57 us

## Promoted Shape Samples

1. `aten::mm` via `external_id=17438`: `{"Concrete Inputs":["",""],"Input Dims":[[4,8192],[8192,512]],"Input Strides":[[8192,1],[1,8192]],"Input type":["float","float"]}`
2. `aten::as_strided` via `external_id=130158`: `{"Concrete Inputs":["","[1]","[1]","0"],"Input Dims":[[1],[],[],[]],"Input Strides":[[1],[],[],[]],"Input type":["int","ScalarList","ScalarList","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
