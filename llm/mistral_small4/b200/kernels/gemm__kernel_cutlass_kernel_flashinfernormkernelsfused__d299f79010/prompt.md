# KDA Prompt: gemm__kernel_cutlass_kernel_flashinfernormkernelsfused__d299f79010

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `mistralai/Mistral-Small-4-119B-2603`
- Model folder: `llm/mistral_small4/b200`
- Kernel category: `gemm`
- Max observed GPU share: `3.67%`
- Kernel name: `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__tensorptrbf16gmemalign128o409640961_tensorptrbf16gmemalign128o409640961_tensorptrbf16gmemalign_0`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 3.67% GPU, calls=648, mean=2.90 us

## Promoted Shape Samples

1. `aten::split_with_sizes` via `external_id=2318`: `{"Concrete Inputs":["","[256, 64]","-1"],"Input Dims":[[38,320],[],[]],"Input Strides":[[1344,1],[],[]],"Input type":["c10::BFloat16","ScalarList","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
