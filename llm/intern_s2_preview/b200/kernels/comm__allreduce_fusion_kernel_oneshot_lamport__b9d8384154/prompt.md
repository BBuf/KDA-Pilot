# KDA Prompt: comm__allreduce_fusion_kernel_oneshot_lamport__b9d8384154

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`comm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `internLM/Intern-S2-Preview`
- Model folder: `llm/intern_s2_preview/b200`
- Kernel category: `comm`
- Max observed GPU share: `39.88%`
- Kernel name: `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 39.70% GPU, calls=5688, mean=88.36 us
- `random_mid`: 18.49% GPU, calls=4424, mean=115.66 us
- `random_high`: 13.27% GPU, calls=3792, mean=122.68 us
- `sharegpt_low`: 39.88% GPU, calls=5688, mean=86.23 us
- `sharegpt_mid`: 34.90% GPU, calls=5056, mean=213.53 us
- `sharegpt_high`: 33.66% GPU, calls=4424, mean=375.66 us

## Promoted Shape Samples

1. `sglang::flashinfer_allreduce_residual_rmsnorm` via `external_id=7368`: `{"Concrete Inputs":["","","","9.9999999999999995e-07","2048","","False","False","True"],"Input Dims":[[38,2048],[38,2048],[2048],[],[],[],[],[],[]],"Input Strides":[[2048,1],[2048,1],[1],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","Scalar","Scalar","","Scalar","Scalar","Scalar"]}`
2. `sglang::flashinfer_allreduce_residual_rmsnorm` via `external_id=39533`: `{"Concrete Inputs":["","","","9.9999999999999995e-07","2048","","False","False","True"],"Input Dims":[[274,2048],[274,2048],[2048],[],[],[],[],[],[]],"Input Strides":[[2048,1],[2048,1],[1],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","Scalar","Scalar","","Scalar","Scalar","Scalar"]}`
3. `sglang::flashinfer_allreduce_residual_rmsnorm` via `external_id=81767`: `{"Concrete Inputs":["","","","9.9999999999999995e-07","2048","","False","False","True"],"Input Dims":[[17,2048],[17,2048],[2048],[],[],[],[],[],[]],"Input Strides":[[2048,1],[2048,1],[1],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","Scalar","Scalar","","Scalar","Scalar","Scalar"]}`
4. `aten::empty` via `external_id=88554`: `{"Concrete Inputs":["[512]","3","","","",""],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","Scalar","","","",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
