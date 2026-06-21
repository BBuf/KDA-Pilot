# KDA Prompt: comm__allreduce_fusion_kernel_twoshot_sync__c36567c3ee

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`comm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `zai-org/GLM-5.1-FP8`
- Model folder: `llm/glm_51/b200`
- Kernel category: `comm`
- Max observed GPU share: `15.77%`
- Kernel name: `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_twoshot_sync<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>, std::array<int, 8>, std::array<int, 8>)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_high`: 15.77% GPU, calls=1248, mean=945.84 us
- `sharegpt_high`: 13.39% GPU, calls=1248, mean=1370.14 us

## Promoted Shape Samples

1. `sglang::flashinfer_allreduce_residual_rmsnorm` via `external_id=127298`: `{"Concrete Inputs":["","","","1.0000000000000001e-05","2048","","False","False","True"],"Input Dims":[[1566,6144],[1566,6144],[6144],[],[],[],[],[],[]],"Input Strides":[[6144,1],[6144,1],[1],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","Scalar","Scalar","","Scalar","Scalar","Scalar"]}`
2. `sglang::flashinfer_allreduce_residual_rmsnorm` via `external_id=115361`: `{"Concrete Inputs":["","","","1.0000000000000001e-05","2048","","False","False","False"],"Input Dims":[[1566,6144],[1566,6144],[6144],[],[],[],[],[],[]],"Input Strides":[[6144,1],[6144,1],[1],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","Scalar","Scalar","","Scalar","Scalar","Scalar"]}`
3. `sglang::flashinfer_allreduce_residual_rmsnorm` via `external_id=290949`: `{"Concrete Inputs":["","","","1.0000000000000001e-05","2048","","False","False","True"],"Input Dims":[[1269,6144],[1269,6144],[6144],[],[],[],[],[],[]],"Input Strides":[[6144,1],[6144,1],[1],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","Scalar","Scalar","","Scalar","Scalar","Scalar"]}`
4. `aten::slice` via `external_id=291257`: `{"Concrete Inputs":["","0","0","48","1"],"Input Dims":[[48],[],[],[],[]],"Input Strides":[[1],[],[],[],[]],"Input type":["int","Scalar","Scalar","Scalar","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
