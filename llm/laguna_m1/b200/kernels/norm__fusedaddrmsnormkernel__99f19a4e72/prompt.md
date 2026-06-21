# KDA Prompt: norm__fusedaddrmsnormkernel__99f19a4e72

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`norm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `poolside/Laguna-M.1-NVFP4`
- Model folder: `llm/laguna_m1/b200`
- Kernel category: `norm`
- Max observed GPU share: `2.73%`
- Kernel name: `void flashinfer::norm::FusedAddRMSNormKernel<8u, __nv_bfloat16>(__nv_bfloat16*, __nv_bfloat16*, __nv_bfloat16*, unsigned int, unsigned int, unsigned int, float, float)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 2.36% GPU, calls=3360, mean=26.58 us
- `sharegpt_mid`: 2.73% GPU, calls=4480, mean=31.22 us

## Promoted Shape Samples

1. `aten::to` via `external_id=6722`: `{"Concrete Inputs":["","6","0","","","True","False",""],"Input Dims":[[1],[],[],[],[],[],[],[]],"Input Strides":[[1],[],[],[],[],[],[],[]],"Input type":["float","Scalar","Scalar","","","Scalar","Scalar",""]}`
2. `aten::empty_strided` via `external_id=41589`: `{"Concrete Inputs":["[1]","[1]","6","0","","False"],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","ScalarList","Scalar","Scalar","","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
