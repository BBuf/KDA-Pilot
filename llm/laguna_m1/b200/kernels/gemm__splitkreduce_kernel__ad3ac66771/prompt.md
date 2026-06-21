# KDA Prompt: gemm__splitkreduce_kernel__ad3ac66771

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `poolside/Laguna-M.1-NVFP4`
- Model folder: `llm/laguna_m1/b200`
- Kernel category: `gemm`
- Max observed GPU share: `2.84%`
- Kernel name: `void cublasLt::splitKreduce_kernel<32, 16, int, float, __nv_bfloat16, float, __nv_bfloat16, false, float, __nv_bfloat16, __nv_bfloat16, true, false, false, false>(cublasLt::cublasSplitKParams<float>, float const*, __nv_bfloat16 const*, float*, __nv_bfloat16*, float const*, float const*, __nv_bfloat16 const*, float const*, __nv_bfloat16*, void*, long, float*, int*, float*, float*, float const*, float const*, float const*, float const*, float const*)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 2.84% GPU, calls=10152, mean=2.87 us

## Promoted Shape Samples

1. `aten::_local_scalar_dense` via `external_id=4675`: `{"Concrete Inputs":[""],"Input Dims":[[]],"Input Strides":[[]],"Input type":["int"]}`
2. `aten::empty` via `external_id=236`: `{"Concrete Inputs":["[2]","3","0","","","0"],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","Scalar","Scalar","","","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
