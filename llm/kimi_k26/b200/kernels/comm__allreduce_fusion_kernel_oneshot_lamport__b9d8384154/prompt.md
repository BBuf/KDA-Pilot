# KDA Prompt: comm__allreduce_fusion_kernel_oneshot_lamport__b9d8384154

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`comm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `moonshotai/Kimi-K2.6`
- Model folder: `llm/kimi_k26/b200`
- Kernel category: `comm`
- Max observed GPU share: `37.33%`
- Kernel name: `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 36.01% GPU, calls=8712, mean=78.12 us
- `random_mid`: 11.45% GPU, calls=7744, mean=95.98 us
- `random_high`: 18.31% GPU, calls=7744, mean=98.99 us
- `sharegpt_low`: 37.33% GPU, calls=8712, mean=89.45 us
- `sharegpt_mid`: 30.02% GPU, calls=7744, mean=200.59 us
- `sharegpt_high`: 34.20% GPU, calls=7744, mean=370.01 us

## Promoted Shape Samples

1. `sglang::flashinfer_allreduce_residual_rmsnorm` via `external_id=8946`: `{"Concrete Inputs":["","","","1.0000000000000001e-05","2048","","False","False","False"],"Input Dims":[[38,7168],[38,7168],[7168],[],[],[],[],[],[]],"Input Strides":[[7168,1],[7168,1],[1],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","Scalar","Scalar","","Scalar","Scalar","Scalar"]}`
2. `aten::as_strided` via `external_id=19840`: `{"Concrete Inputs":["","[38, 512]","[2112, 1]","1536"],"Input Dims":[[38,576],[],[],[]],"Input Strides":[[2112,1],[],[],[]],"Input type":["c10::BFloat16","ScalarList","ScalarList","Scalar"]}`
3. `aten::empty` via `external_id=41702`: `{"Concrete Inputs":["[38, 8]","3","","","False",""],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","Scalar","","","Scalar",""]}`
4. `sglang::flashinfer_allreduce_residual_rmsnorm` via `external_id=67599`: `{"Concrete Inputs":["","","","1.0000000000000001e-05","2048","","False","False","False"],"Input Dims":[[15,7168],[15,7168],[7168],[],[],[],[],[],[]],"Input Strides":[[7168,1],[7168,1],[1],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","Scalar","Scalar","","Scalar","Scalar","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
