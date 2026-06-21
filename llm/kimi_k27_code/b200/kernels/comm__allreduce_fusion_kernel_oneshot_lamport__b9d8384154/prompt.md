# KDA Prompt: comm__allreduce_fusion_kernel_oneshot_lamport__b9d8384154

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`comm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `moonshotai/Kimi-K2.7-Code`
- Model folder: `llm/kimi_k27_code/b200`
- Kernel category: `comm`
- Max observed GPU share: `48.82%`
- Kernel name: `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 30.47% GPU, calls=8712, mean=50.00 us
- `random_mid`: 12.17% GPU, calls=7744, mean=96.26 us
- `random_high`: 16.86% GPU, calls=7744, mean=101.82 us
- `sharegpt_low`: 48.82% GPU, calls=8712, mean=1249.78 us
- `sharegpt_mid`: 45.58% GPU, calls=7744, mean=1271.49 us
- `sharegpt_high`: 28.88% GPU, calls=7744, mean=201.87 us

## Promoted Shape Samples

1. `sglang::_run_activation_inplace` via `external_id=8944`: `{"Concrete Inputs":["","",""],"Input Dims":[[],[38,512],[38,256]],"Input Strides":[[],[512,1],[256,1]],"Input type":["","c10::BFloat16","c10::BFloat16"]}`
2. `sglang::flashinfer_allreduce_residual_rmsnorm` via `external_id=8954`: `{"Concrete Inputs":["","","","1.0000000000000001e-05","2048","","False","False","False"],"Input Dims":[[38,7168],[38,7168],[7168],[],[],[],[],[],[]],"Input Strides":[[7168,1],[7168,1],[1],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","Scalar","Scalar","","Scalar","Scalar","Scalar"]}`
3. `aten::view` via `external_id=302`: `{"Concrete Inputs":["","[-1, 8, 128]"],"Input Dims":[[38,8,128],[]],"Input Strides":[[2048,256,1],[]],"Input type":["c10::BFloat16","ScalarList"]}`
4. `sglang::flashinfer_allreduce_residual_rmsnorm` via `external_id=312`: `{"Concrete Inputs":["","","","1.0000000000000001e-05","2048","","False","False","True"],"Input Dims":[[38,7168],[38,7168],[7168],[],[],[],[],[],[]],"Input Strides":[[7168,1],[7168,1],[1],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","Scalar","Scalar","","Scalar","Scalar","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
