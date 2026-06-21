# KDA Prompt: gemm__kernel2__57e9da75e7

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `MiniMaxAI/MiniMax-M2.7`
- Model folder: `llm/minimax_m27/b200`
- Kernel category: `gemm`
- Max observed GPU share: `4.60%`
- Kernel name: `void cutlass::Kernel2<cutlass_80_simt_sgemm_64x64_8x5_tn_align1>(cutlass_80_simt_sgemm_64x64_8x5_tn_align1::Params)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `sharegpt_low`: 2.33% GPU, calls=496, mean=30.08 us
- `sharegpt_mid`: 3.94% GPU, calls=2976, mean=27.05 us
- `sharegpt_high`: 4.60% GPU, calls=2480, mean=30.14 us

## Promoted Shape Samples

1. `aten::to` via `external_id=31546`: `{"Concrete Inputs":["","3","False","False",""],"Input Dims":[[1],[],[],[],[]],"Input Strides":[[1],[],[],[],[]],"Input type":["long int","Scalar","Scalar","Scalar",""]}`
2. `aten::view` via `external_id=38022`: `{"Concrete Inputs":["","[-1, 128]"],"Input Dims":[[59,1,128],[]],"Input Strides":[[1024,128,1],[]],"Input type":["c10::BFloat16","ScalarList"]}`
3. `sglang::store_cache` via `external_id=56711`: `{"Concrete Inputs":["","","","","","256","0","4148736"],"Input Dims":[[212,128],[212,128],[4148736,128],[4148736,128],[212],[],[],[]],"Input Strides":[[128,1],[1024,1],[128,1],[128,1],[1],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","c10::BFloat16","long int","Scalar","Scalar","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
