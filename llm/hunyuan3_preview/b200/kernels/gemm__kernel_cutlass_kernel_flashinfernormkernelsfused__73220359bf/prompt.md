# KDA Prompt: gemm__kernel_cutlass_kernel_flashinfernormkernelsfused__73220359bf

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `tencent/Hy3-preview`
- Model folder: `llm/hunyuan3_preview/b200`
- Kernel category: `gemm`
- Max observed GPU share: `2.24%`
- Kernel name: `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__tensorptrf16gmemalign128o409640961_tensorptrf16gmemalign128o409640961_tensorptrf16gmemalign16o_0`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 2.24% GPU, calls=11920, mean=3.40 us

## Promoted Shape Samples

1. `sglang::_jit_grouped_topk_op` via `external_id=4539`: `{"Concrete Inputs":["","","","","1","1","8","True","2.8260000000000001"],"Input Dims":[[38,192],[192],[38,8],[38,8],[],[],[],[],[]],"Input Strides":[[192,1],[1],[8,1],[8,1],[],[],[],[],[]],"Input type":["float","float","float","int","Scalar","Scalar","Scalar","Scalar","Scalar"]}`
2. `aten::matmul` via `external_id=6453`: `{"Concrete Inputs":["",""],"Input Dims":[[38,4096],[4096,192]],"Input Strides":[[4096,1],[1,4096]],"Input type":["float","float"]}`
3. `aten::empty_strided` via `external_id=8367`: `{"Concrete Inputs":["[38, 4096]","[4096, 1]","6","0","","False"],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","ScalarList","Scalar","Scalar","","Scalar"]}`
4. `aten::view` via `external_id=5815`: `{"Concrete Inputs":["","[-1, 1, 128]"],"Input Dims":[[38,128],[]],"Input Strides":[[1280,1],[]],"Input type":["c10::Half","ScalarList"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
