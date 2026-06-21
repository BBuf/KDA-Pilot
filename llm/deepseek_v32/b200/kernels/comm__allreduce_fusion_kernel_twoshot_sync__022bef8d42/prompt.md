# KDA Prompt: comm__allreduce_fusion_kernel_twoshot_sync__022bef8d42

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`comm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `nvidia/DeepSeek-V3.2-NVFP4`
- Model folder: `llm/deepseek_v32/b200`
- Kernel category: `comm`
- Max observed GPU share: `7.20%`
- Kernel name: `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_twoshot_sync<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 4, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>, std::array<int, 4>, std::array<int, 4>)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_high`: 2.31% GPU, calls=484, mean=83.85 us
- `sharegpt_high`: 7.20% GPU, calls=968, mean=108.67 us

## Promoted Shape Samples

1. `aten::_to_copy` via `external_id=44405`: `{"Concrete Inputs":["","6","","","","False",""],"Input Dims":[[31],[],[],[],[],[],[]],"Input Strides":[[1],[],[],[],[],[],[]],"Input type":["float","Scalar","","","","Scalar",""]}`
2. `detach_` via `external_id=132757`: `{"Concrete Inputs":[""],"Input Dims":[[34]],"Input Strides":[[1]],"Input type":["int"]}`
3. `aten::as_strided` via `external_id=140515`: `{"Concrete Inputs":["","[]","[]","16"],"Input Dims":[[65],[],[],[]],"Input Strides":[[1],[],[],[]],"Input type":["long int","ScalarList","ScalarList","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
