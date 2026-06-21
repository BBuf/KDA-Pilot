# KDA Prompt: gemm__kernel2__57e9da75e7

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `MiniMaxAI/MiniMax-M2`
- Model folder: `llm/minimax_m2/b200`
- Kernel category: `gemm`
- Max observed GPU share: `5.05%`
- Kernel name: `void cutlass::Kernel2<cutlass_80_simt_sgemm_64x64_8x5_tn_align1>(cutlass_80_simt_sgemm_64x64_8x5_tn_align1::Params)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 2.15% GPU, calls=248, mean=28.27 us
- `random_mid`: 4.42% GPU, calls=1984, mean=29.76 us
- `sharegpt_low`: 2.23% GPU, calls=248, mean=30.07 us
- `sharegpt_mid`: 3.05% GPU, calls=1488, mean=26.79 us
- `sharegpt_high`: 5.05% GPU, calls=1736, mean=30.05 us

## Promoted Shape Samples

1. `aten::empty` via `external_id=236`: `{"Concrete Inputs":["[2]","3","0","","","0"],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","Scalar","Scalar","","","Scalar"]}`
2. `aten::slice` via `external_id=8626`: `{"Concrete Inputs":["","0","0","253","1"],"Input Dims":[[256,2,128],[],[],[],[]],"Input Strides":[[2048,128,1],[],[],[],[]],"Input type":["c10::Half","Scalar","Scalar","Scalar","Scalar"]}`
3. `aten::as_strided` via `external_id=30046`: `{"Concrete Inputs":["","[64]","[1]","0"],"Input Dims":[[16384],[],[],[]],"Input Strides":[[1],[],[],[]],"Input type":["long int","ScalarList","ScalarList","Scalar"]}`
4. `aten::slice` via `external_id=36587`: `{"Concrete Inputs":["","0","0","59","1"],"Input Dims":[[64,2,128],[],[],[],[]],"Input Strides":[[2048,128,1],[],[],[],[]],"Input type":["c10::Half","Scalar","Scalar","Scalar","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
