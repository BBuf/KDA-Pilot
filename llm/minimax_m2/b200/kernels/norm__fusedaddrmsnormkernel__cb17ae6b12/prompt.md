# KDA Prompt: norm__fusedaddrmsnormkernel__cb17ae6b12

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`norm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `MiniMaxAI/MiniMax-M2`
- Model folder: `llm/minimax_m2/b200`
- Kernel category: `norm`
- Max observed GPU share: `2.76%`
- Kernel name: `void flashinfer::norm::FusedAddRMSNormKernel<8u, __half>(__half*, __half*, __half*, unsigned int, unsigned int, unsigned int, float, float)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 2.76% GPU, calls=1488, mean=24.81 us
- `sharegpt_mid`: 2.23% GPU, calls=1984, mean=14.71 us
- `sharegpt_high`: 2.21% GPU, calls=2480, mean=9.20 us

## Promoted Shape Samples

1. `aten::slice` via `external_id=8626`: `{"Concrete Inputs":["","0","0","253","1"],"Input Dims":[[256,2,128],[],[],[],[]],"Input Strides":[[2048,128,1],[],[],[],[]],"Input type":["c10::Half","Scalar","Scalar","Scalar","Scalar"]}`
2. `aten::copy_` via `external_id=6349`: `{"Concrete Inputs":["","","False"],"Input Dims":[[39,1536],[39,1536],[]],"Input Strides":[[1536,1],[1536,1],[]],"Input type":["c10::Half","c10::Half","Scalar"]}`
3. `aten::view` via `external_id=11100`: `{"Concrete Inputs":["","[-1, 256]"],"Input Dims":[[9468,2,128],[]],"Input Strides":[[256,128,1],[]],"Input type":["c10::Half","ScalarList"]}`
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
