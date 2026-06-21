# KDA Prompt: gemm__kernel_cutlass_kernel_flashinfernormkernelsfused__d299f79010

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `inclusionAI/Ling-2.6-flash`
- Model folder: `llm/ling_26/b200`
- Kernel category: `gemm`
- Max observed GPU share: `28.14%`
- Kernel name: `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__tensorptrbf16gmemalign128o409640961_tensorptrbf16gmemalign128o409640961_tensorptrbf16gmemalign_0`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 28.14% GPU, calls=2304, mean=47.79 us

## Promoted Shape Samples

1. `aten::empty` via `external_id=2366`: `{"Concrete Inputs":["[312, 256]","15","","","False",""],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","Scalar","","","Scalar",""]}`
2. `aten::t` via `external_id=1590`: `{"Concrete Inputs":[""],"Input Dims":[[3072,4096]],"Input Strides":[[4096,1]],"Input type":["c10::BFloat16"]}`
3. `sglang::outplace_all_reduce` via `external_id=1588`: `{"Concrete Inputs":["","",""],"Input Dims":[[39,4096],[],[]],"Input Strides":[[4096,1],[],[]],"Input type":["c10::BFloat16","",""]}`
4. `aten::as_strided` via `external_id=2797`: `{"Concrete Inputs":["","[39, 8, 64]","[1536, 192, 1]","128"],"Input Dims":[[39,8,192],[],[],[]],"Input Strides":[[1536,192,1],[],[],[]],"Input type":["c10::BFloat16","ScalarList","ScalarList","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
