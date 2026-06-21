# KDA Prompt: gemm__kernel2__57e9da75e7

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `stepfun-ai/Step-3.7-Flash-NVFP4`
- Model folder: `llm/step_37_flash/b200`
- Kernel category: `gemm`
- Max observed GPU share: `4.03%`
- Kernel name: `void cutlass::Kernel2<cutlass_80_simt_sgemm_64x64_8x5_tn_align1>(cutlass_80_simt_sgemm_64x64_8x5_tn_align1::Params)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 2.79% GPU, calls=2688, mean=28.00 us
- `random_high`: 4.03% GPU, calls=2688, mean=30.58 us

## Promoted Shape Samples

1. `aten::mm` via `external_id=16035`: `{"Concrete Inputs":["",""],"Input Dims":[[56,4096],[4096,288]],"Input Strides":[[4096,1],[1,4096]],"Input type":["float","float"]}`
2. `aten::mm` via `external_id=35400`: `{"Concrete Inputs":["",""],"Input Dims":[[108,4096],[4096,288]],"Input Strides":[[4096,1],[1,4096]],"Input type":["float","float"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
