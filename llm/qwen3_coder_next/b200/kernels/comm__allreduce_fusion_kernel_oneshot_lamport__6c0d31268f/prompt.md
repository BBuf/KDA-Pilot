# KDA Prompt: comm__allreduce_fusion_kernel_oneshot_lamport__6c0d31268f

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`comm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `Qwen/Qwen3-Coder-Next`
- Model folder: `llm/qwen3_coder_next/b200`
- Kernel category: `comm`
- Max observed GPU share: `34.40%`
- Kernel name: `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 2, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 34.40% GPU, calls=1710, mean=57.16 us
- `random_mid`: 13.70% GPU, calls=1520, mean=53.13 us
- `random_high`: 10.58% GPU, calls=1140, mean=132.91 us
- `sharegpt_low`: 20.73% GPU, calls=1710, mean=17.11 us
- `sharegpt_mid`: 26.14% GPU, calls=1520, mean=121.86 us
- `sharegpt_high`: 21.49% GPU, calls=1330, mean=218.84 us

## Promoted Shape Samples

1. `sglang::flashinfer_allreduce_residual_rmsnorm` via `external_id=2434`: `{"Concrete Inputs":["","","","9.9999999999999995e-07","2048","","False","False","True"],"Input Dims":[[38,2048],[38,2048],[2048],[],[],[],[],[],[]],"Input Strides":[[2048,1],[2048,1],[1],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","Scalar","Scalar","","Scalar","Scalar","Scalar"]}`
2. `aten::empty` via `external_id=17588`: `{"Concrete Inputs":["[3040, 256]","15","","","",""],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","Scalar","","","",""]}`
3. `aten::empty` via `external_id=17736`: `{"Concrete Inputs":["[0]","3","","","False",""],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","Scalar","","","Scalar",""]}`
4. `aten::linear` via `external_id=17524`: `{"Concrete Inputs":["","",""],"Input Dims":[[38,2048],[2048,2048],[]],"Input Strides":[[2048,1],[2048,1],[]],"Input type":["c10::BFloat16","c10::BFloat16",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
