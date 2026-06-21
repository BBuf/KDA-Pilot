# KDA Prompt: comm__allreduce_fusion_kernel_oneshot_lamport__b9d8384154

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`comm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `nvidia/DeepSeek-R1-0528-FP4-v2`
- Model folder: `llm/deepseek_r1_fp4/b200`
- Kernel category: `comm`
- Max observed GPU share: `34.50%`
- Kernel name: `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 33.21% GPU, calls=8912, mean=93.83 us
- `random_mid`: 8.10% GPU, calls=7920, mean=115.36 us
- `random_high`: 20.45% GPU, calls=7920, mean=129.61 us
- `sharegpt_low`: 32.39% GPU, calls=8912, mean=78.56 us
- `sharegpt_mid`: 32.16% GPU, calls=7888, mean=300.15 us
- `sharegpt_high`: 34.50% GPU, calls=7888, mean=329.82 us

## Promoted Shape Samples

1. `sglang::flashinfer_allreduce_residual_rmsnorm` via `external_id=3533`: `{"Concrete Inputs":["","","","9.9999999999999995e-07","2048","","False","False","True"],"Input Dims":[[39,7168],[39,7168],[7168],[],[],[],[],[],[]],"Input Strides":[[7168,1],[7168,1],[1],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","Scalar","Scalar","","Scalar","Scalar","Scalar"]}`
2. `aten::permute` via `external_id=5305`: `{"Concrete Inputs":["","[1, 0]"],"Input Dims":[[1024,7168],[]],"Input Strides":[[1,1024],[]],"Input type":["unsigned char","ScalarList"]}`
3. `aten::slice` via `external_id=19077`: `{"Concrete Inputs":["","2","128","9223372036854775807","1"],"Input Dims":[[39,16,192],[],[],[],[]],"Input Strides":[[3072,192,1],[],[],[],[]],"Input type":["c10::BFloat16","Scalar","Scalar","Scalar","Scalar"]}`
4. `sglang::flashinfer_allreduce_residual_rmsnorm` via `external_id=86076`: `{"Concrete Inputs":["","","","9.9999999999999995e-07","2048","","False","False","True"],"Input Dims":[[16,7168],[16,7168],[7168],[],[],[],[],[],[]],"Input Strides":[[7168,1],[7168,1],[1],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","Scalar","Scalar","","Scalar","Scalar","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
