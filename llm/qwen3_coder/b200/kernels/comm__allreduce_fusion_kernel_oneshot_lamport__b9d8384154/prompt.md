# KDA Prompt: comm__allreduce_fusion_kernel_oneshot_lamport__b9d8384154

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`comm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8`
- Model folder: `llm/qwen3_coder/b200`
- Kernel category: `comm`
- Max observed GPU share: `22.61%`
- Kernel name: `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 22.61% GPU, calls=8856, mean=16.52 us
- `random_high`: 13.45% GPU, calls=7872, mean=30.30 us
- `sharegpt_low`: 21.68% GPU, calls=8856, mean=15.65 us
- `sharegpt_mid`: 8.94% GPU, calls=6888, mean=24.76 us
- `sharegpt_high`: 13.27% GPU, calls=6888, mean=33.43 us

## Promoted Shape Samples

1. `aten::as_strided` via `external_id=300`: `{"Concrete Inputs":["","[1, 38]","[0, 1]",""],"Input Dims":[[4097,38],[],[],[]],"Input Strides":[[8196,1],[],[],[]],"Input type":["int","ScalarList","ScalarList",""]}`
2. `aten::copy_` via `external_id=21868`: `{"Concrete Inputs":["","","True"],"Input Dims":[[1],[1],[]],"Input Strides":[[1],[1],[]],"Input type":["long int","long int","Scalar"]}`
3. `aten::empty` via `external_id=35578`: `{"Concrete Inputs":["[0]","4","","","False",""],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","Scalar","","","Scalar",""]}`
4. `aten::empty_strided` via `external_id=40444`: `{"Concrete Inputs":["[17]","[1]","4","0","","False"],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","ScalarList","Scalar","Scalar","","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
