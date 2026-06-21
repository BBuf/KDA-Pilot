# KDA Prompt: comm__allreduce_fusion_kernel_oneshot_lamport__b9d8384154

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`comm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `Qwen/Qwen3-235B-A22B-Instruct-2507`
- Model folder: `llm/qwen3/b200`
- Kernel category: `comm`
- Max observed GPU share: `20.02%`
- Kernel name: `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 18.52% GPU, calls=13464, mean=9.58 us
- `random_mid`: 5.66% GPU, calls=10472, mean=14.01 us
- `random_high`: 10.01% GPU, calls=10472, mean=19.65 us
- `sharegpt_low`: 20.02% GPU, calls=13464, mean=10.38 us
- `sharegpt_mid`: 9.59% GPU, calls=10472, mean=17.26 us

## Promoted Shape Samples

1. `aten::slice` via `external_id=271`: `{"Concrete Inputs":["","0","1","2","1"],"Input Dims":[[2],[],[],[],[]],"Input Strides":[[1],[],[],[],[]],"Input type":["int","Scalar","Scalar","Scalar","Scalar"]}`
2. `aten::item` via `external_id=7269`: `{"Concrete Inputs":[""],"Input Dims":[[]],"Input Strides":[[]],"Input type":["long int"]}`
3. `aten::permute` via `external_id=20515`: `{"Concrete Inputs":["","[0, 2, 1, 3]"],"Input Dims":[[26751,64,1,128],[]],"Input Strides":[[8192,128,128,1],[]],"Input type":["c10::BFloat16","ScalarList"]}`
4. `aten::as_strided` via `external_id=23504`: `{"Concrete Inputs":["","[26751, 1, 64, 128]","[8192, 8192, 128, 1]",""],"Input Dims":[[26751,1,64,128],[],[],[]],"Input Strides":[[8192,128,128,1],[],[],[]],"Input type":["c10::BFloat16","ScalarList","ScalarList",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
