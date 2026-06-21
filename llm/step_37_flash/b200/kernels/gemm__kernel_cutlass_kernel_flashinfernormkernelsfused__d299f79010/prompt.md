# KDA Prompt: gemm__kernel_cutlass_kernel_flashinfernormkernelsfused__d299f79010

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `stepfun-ai/Step-3.7-Flash-NVFP4`
- Model folder: `llm/step_37_flash/b200`
- Kernel category: `gemm`
- Max observed GPU share: `32.09%`
- Kernel name: `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__tensorptrbf16gmemalign128o409640961_tensorptrbf16gmemalign128o409640961_tensorptrbf16gmemalign_0`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 32.09% GPU, calls=6480, mean=60.88 us

## Promoted Shape Samples

1. `aten::empty_strided` via `external_id=10361`: `{"Concrete Inputs":["[1]","[1]","4","0","",""],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","ScalarList","Scalar","Scalar","",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
