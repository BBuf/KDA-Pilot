# KDA Prompt: gemm__kernel_cutlass_kernel_flashinfernormkernelsfused__b25a796c5c

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4`
- Model folder: `llm/nemotron3_ultra/b200`
- Kernel category: `gemm`
- Max observed GPU share: `4.32%`
- Kernel name: `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__tensorptrbf16gmemalign128o819281921_tensorptrbf16gmemalign128o819281921_tensorptrbf16gmemalign_0`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 4.32% GPU, calls=3988, mean=6.88 us

## Promoted Shape Samples

1. `aten::view` via `external_id=12562`: `{"Concrete Inputs":["","[1, 64, 64, 128]"],"Input Dims":[[1,64,8192],[]],"Input Strides":[[524288,8192,1],[]],"Input type":["float","ScalarList"]}`
2. `aten::reshape` via `external_id=8450`: `{"Concrete Inputs":["","[38, 128]"],"Input Dims":[[38,1,128],[]],"Input Strides":[[2304,128,1],[]],"Input type":["c10::BFloat16","ScalarList"]}`
3. `aten::unsqueeze` via `external_id=14544`: `{"Concrete Inputs":["","1"],"Input Dims":[[1],[]],"Input Strides":[[1],[]],"Input type":["long int","Scalar"]}`
4. `aten::empty` via `external_id=6320`: `{"Concrete Inputs":["[552]","3","","","",""],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","Scalar","","","",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
