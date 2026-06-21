# KDA Prompt: gemm__gemma_qkv_rmsnorm_kernel__c9e8af2caa

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `google/gemma-4-26B-A4B-it`
- Model folder: `llm/gemma4/b200`
- Kernel category: `gemm`
- Max observed GPU share: `8.57%`
- Kernel name: `_gemma_qkv_rmsnorm_kernel`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 8.57% GPU, calls=270, mean=13.03 us

## Promoted Shape Samples

1. `aten::_reshape_alias` via `external_id=889`: `{"Concrete Inputs":["","[38, 8, 256]","[8192, 256, 1]"],"Input Dims":[[38,2048],[],[]],"Input Strides":[[8192,1],[],[]],"Input type":["c10::BFloat16","ScalarList","ScalarList"]}`
2. `aten::matmul` via `external_id=1782`: `{"Concrete Inputs":["",""],"Input Dims":[[38,2816],[2816,8192]],"Input Strides":[[2816,1],[1,2816]],"Input type":["c10::BFloat16","c10::BFloat16"]}`
3. `aten::as_strided` via `external_id=3513`: `{"Concrete Inputs":["","[1]","[0]",""],"Input Dims":[[2049],[],[],[]],"Input Strides":[[1],[],[],[]],"Input type":["long int","ScalarList","ScalarList",""]}`
4. `aten::view` via `external_id=1206`: `{"Concrete Inputs":["","[-1, 2048]"],"Input Dims":[[516544,8,256],[]],"Input Strides":[[2048,256,1],[]],"Input type":["c10::BFloat16","ScalarList"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
