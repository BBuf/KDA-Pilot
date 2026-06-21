# KDA Prompt: gemm__kernel2__57e9da75e7

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `MiniMaxAI/MiniMax-M2.5`
- Model folder: `llm/minimax_m25/b200`
- Kernel category: `gemm`
- Max observed GPU share: `4.10%`
- Kernel name: `void cutlass::Kernel2<cutlass_80_simt_sgemm_64x64_8x5_tn_align1>(cutlass_80_simt_sgemm_64x64_8x5_tn_align1::Params)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 4.10% GPU, calls=3472, mean=26.74 us
- `sharegpt_mid`: 3.66% GPU, calls=2976, mean=27.07 us
- `sharegpt_high`: 3.49% GPU, calls=1984, mean=30.03 us

## Promoted Shape Samples

1. `aten::empty_strided` via `external_id=6694`: `{"Concrete Inputs":["[39, 6, 128]","[768, 128, 1]","5","0","","False"],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","ScalarList","Scalar","Scalar","","Scalar"]}`
2. `aten::as_strided` via `external_id=46792`: `{"Concrete Inputs":["","[64859, 1, 64, 128]","[8192, 8192, 128, 1]",""],"Input Dims":[[64859,1,64,128],[],[],[]],"Input Strides":[[8192,128,128,1],[],[],[]],"Input type":["c10::Half","ScalarList","ScalarList",""]}`
3. `aten::permute` via `external_id=60632`: `{"Concrete Inputs":["","[0, 2, 1, 3]"],"Input Dims":[[64859,64,1,128],[]],"Input Strides":[[8192,128,128,1],[]],"Input type":["c10::Half","ScalarList"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
