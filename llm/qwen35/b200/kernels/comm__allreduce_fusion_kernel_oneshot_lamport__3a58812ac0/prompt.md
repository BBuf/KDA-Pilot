# KDA Prompt: comm__allreduce_fusion_kernel_oneshot_lamport__3a58812ac0

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`comm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `nvidia/Qwen3.5-397B-A17B-NVFP4`
- Model folder: `llm/qwen35/b200`
- Kernel category: `comm`
- Max observed GPU share: `41.70%`
- Kernel name: `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 4, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 41.70% GPU, calls=4284, mean=232.40 us
- `random_mid`: 13.54% GPU, calls=3808, mean=61.06 us
- `random_high`: 9.16% GPU, calls=3332, mean=100.12 us
- `sharegpt_low`: 38.25% GPU, calls=4284, mean=91.66 us
- `sharegpt_mid`: 30.38% GPU, calls=3808, mean=164.53 us
- `sharegpt_high`: 9.38% GPU, calls=2856, mean=191.79 us

## Promoted Shape Samples

1. `sglang::flashinfer_allreduce_residual_rmsnorm` via `external_id=5455`: `{"Concrete Inputs":["","","","9.9999999999999995e-07","2048","","False","False","True"],"Input Dims":[[38,4096],[38,4096],[4096],[],[],[],[],[],[]],"Input Strides":[[4096,1],[4096,1],[1],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","Scalar","Scalar","","Scalar","Scalar","Scalar"]}`
2. `aten::view` via `external_id=5463`: `{"Concrete Inputs":["","[-1]"],"Input Dims":[[38,4096],[]],"Input Strides":[[4096,1],[]],"Input type":["c10::BFloat16","ScalarList"]}`
3. `aten::mm` via `external_id=22295`: `{"Concrete Inputs":["",""],"Input Dims":[[38,4096],[4096,4608]],"Input Strides":[[4096,1],[1,4096]],"Input type":["c10::BFloat16","c10::BFloat16"]}`
4. `aten::mm` via `external_id=25493`: `{"Concrete Inputs":["",""],"Input Dims":[[38,4096],[4096,5120]],"Input Strides":[[4096,1],[1,4096]],"Input type":["c10::BFloat16","c10::BFloat16"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
