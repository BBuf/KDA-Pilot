# KDA Prompt: comm__allreduce_fusion_kernel_oneshot_lamport__b9d8384154

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`comm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `Qwen/Qwen3-Next-80B-A3B-Instruct`
- Model folder: `llm/qwen3_next/b200`
- Kernel category: `comm`
- Max observed GPU share: `44.30%`
- Kernel name: `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 38.78% GPU, calls=6840, mean=95.14 us
- `random_mid`: 16.67% GPU, calls=5320, mean=133.28 us
- `random_high`: 29.99% GPU, calls=4560, mean=557.95 us
- `sharegpt_low`: 44.30% GPU, calls=6840, mean=182.95 us
- `sharegpt_mid`: 31.50% GPU, calls=6080, mean=235.38 us
- `sharegpt_high`: 25.16% GPU, calls=4560, mean=460.45 us

## Promoted Shape Samples

1. `sglang::flashinfer_allreduce_residual_rmsnorm` via `external_id=2450`: `{"Concrete Inputs":["","","","9.9999999999999995e-07","2048","","False","False","True"],"Input Dims":[[38,2048],[38,2048],[2048],[],[],[],[],[],[]],"Input Strides":[[2048,1],[2048,1],[1],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","Scalar","Scalar","","Scalar","Scalar","Scalar"]}`
2. `aten::reshape` via `external_id=2440`: `{"Concrete Inputs":["","[38, 4, 128]"],"Input Dims":[[152,128],[]],"Input Strides":[[128,1],[]],"Input type":["c10::BFloat16","ScalarList"]}`
3. `aten::reshape` via `external_id=12542`: `{"Concrete Inputs":["","[38, -1]"],"Input Dims":[[38,4,128],[]],"Input Strides":[[512,128,1],[]],"Input type":["c10::BFloat16","ScalarList"]}`
4. `aten::reshape` via `external_id=41048`: `{"Concrete Inputs":["","[-1, 128]"],"Input Dims":[[38,4,128],[]],"Input Strides":[[512,128,1],[]],"Input type":["c10::BFloat16","ScalarList"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
