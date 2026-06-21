# KDA Prompt: norm__fusedaddrmsnormkernel__99f19a4e72

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`norm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `MiniMaxAI/MiniMax-M2.7`
- Model folder: `llm/minimax_m27/b200`
- Kernel category: `norm`
- Max observed GPU share: `3.90%`
- Kernel name: `void flashinfer::norm::FusedAddRMSNormKernel<8u, __nv_bfloat16>(__nv_bfloat16*, __nv_bfloat16*, __nv_bfloat16*, unsigned int, unsigned int, unsigned int, float, float)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 3.90% GPU, calls=992, mean=26.04 us
- `random_mid`: 3.32% GPU, calls=2976, mean=22.82 us
- `random_high`: 2.40% GPU, calls=2976, mean=13.18 us
- `sharegpt_low`: 2.33% GPU, calls=992, mean=15.04 us
- `sharegpt_mid`: 3.28% GPU, calls=3968, mean=16.87 us
- `sharegpt_high`: 2.40% GPU, calls=5952, mean=6.57 us

## Promoted Shape Samples

1. `aten::pad` via `external_id=254`: `{"Concrete Inputs":["","[1, 0]","",""],"Input Dims":[[1],[],[],[]],"Input Strides":[[1],[],[],[]],"Input type":["int","ScalarList","",""]}`
2. `aten::to` via `external_id=6686`: `{"Concrete Inputs":["","","3","False","False",""],"Input Dims":[[1],[],[],[],[],[]],"Input Strides":[[1],[],[],[],[],[]],"Input type":["int","","Scalar","Scalar","Scalar",""]}`
3. `aten::detach_` via `external_id=18508`: `{"Concrete Inputs":[""],"Input Dims":[[1]],"Input Strides":[[1]],"Input type":["long int"]}`
4. `aten::to` via `external_id=31546`: `{"Concrete Inputs":["","3","False","False",""],"Input Dims":[[1],[],[],[],[]],"Input Strides":[[1],[],[],[],[]],"Input type":["long int","Scalar","Scalar","Scalar",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
