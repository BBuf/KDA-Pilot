# KDA Prompt: comm__allreduce_fusion_kernel_oneshot_lamport__b9d8384154

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`comm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `zai-org/GLM-5.1-FP8`
- Model folder: `llm/glm_51/b200`
- Kernel category: `comm`
- Max observed GPU share: `36.73%`
- Kernel name: `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 35.01% GPU, calls=11360, mean=127.70 us
- `random_mid`: 19.57% GPU, calls=10096, mean=151.19 us
- `random_high`: 24.12% GPU, calls=10096, mean=178.85 us
- `sharegpt_low`: 36.29% GPU, calls=11360, mean=142.74 us
- `sharegpt_mid`: 28.61% GPU, calls=10080, mean=296.23 us
- `sharegpt_high`: 36.73% GPU, calls=10064, mean=465.91 us

## Promoted Shape Samples

1. `sglang::flashinfer_allreduce_residual_rmsnorm` via `external_id=20933`: `{"Concrete Inputs":["","","","1.0000000000000001e-05","2048","","False","False","True"],"Input Dims":[[38,6144],[38,6144],[6144],[],[],[],[],[],[]],"Input Strides":[[6144,1],[6144,1],[1],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","Scalar","Scalar","","Scalar","Scalar","Scalar"]}`
2. `aten::alias` via `external_id=50549`: `{"Concrete Inputs":[""],"Input Dims":[[1,154880]],"Input Strides":[[154880,1]],"Input type":["c10::BFloat16"]}`
3. `aten::empty_strided` via `external_id=73595`: `{"Concrete Inputs":["[32, 1]","[1, 1]","6","0","","False"],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","ScalarList","Scalar","Scalar","","Scalar"]}`
4. `sglang::flashinfer_allreduce_residual_rmsnorm` via `external_id=128277`: `{"Concrete Inputs":["","","","1.0000000000000001e-05","2048","","False","False","True"],"Input Dims":[[192,6144],[192,6144],[6144],[],[],[],[],[],[]],"Input Strides":[[6144,1],[6144,1],[1],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","Scalar","Scalar","","Scalar","Scalar","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
