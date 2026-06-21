# KDA Prompt: comm__allreduce_fusion_kernel_oneshot_lamport__b9d8384154

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`comm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `deepseek-ai/DeepSeek-V3.1`
- Model folder: `llm/deepseek_v31/b200`
- Kernel category: `comm`
- Max observed GPU share: `35.26%`
- Kernel name: `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 33.11% GPU, calls=8912, mean=95.43 us
- `random_mid`: 13.78% GPU, calls=7920, mean=135.21 us
- `random_high`: 22.28% GPU, calls=7920, mean=144.59 us
- `sharegpt_low`: 35.26% GPU, calls=8912, mean=112.87 us
- `sharegpt_mid`: 30.39% GPU, calls=7904, mean=268.07 us
- `sharegpt_high`: 34.66% GPU, calls=7888, mean=405.95 us

## Promoted Shape Samples

1. `sglang::flashinfer_allreduce_residual_rmsnorm` via `external_id=3421`: `{"Concrete Inputs":["","","","9.9999999999999995e-07","2048","","False","False","False"],"Input Dims":[[39,7168],[39,7168],[7168],[],[],[],[],[],[]],"Input Strides":[[7168,1],[7168,1],[1],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","Scalar","Scalar","","Scalar","Scalar","Scalar"]}`
2. `aten::view` via `external_id=13127`: `{"Concrete Inputs":["","[-1]"],"Input Dims":[[39,7168],[]],"Input Strides":[[7168,1],[]],"Input type":["c10::BFloat16","ScalarList"]}`
3. `sglang::flashinfer_allreduce_residual_rmsnorm` via `external_id=13119`: `{"Concrete Inputs":["","","","9.9999999999999995e-07","2048","","False","False","True"],"Input Dims":[[39,7168],[39,7168],[7168],[],[],[],[],[],[]],"Input Strides":[[7168,1],[7168,1],[1],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","Scalar","Scalar","","Scalar","Scalar","Scalar"]}`
4. `sglang::flashinfer_allreduce_residual_rmsnorm` via `external_id=88986`: `{"Concrete Inputs":["","","","9.9999999999999995e-07","2048","","False","False","False"],"Input Dims":[[16,7168],[16,7168],[7168],[],[],[],[],[],[]],"Input Strides":[[7168,1],[7168,1],[1],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","Scalar","Scalar","","Scalar","Scalar","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
