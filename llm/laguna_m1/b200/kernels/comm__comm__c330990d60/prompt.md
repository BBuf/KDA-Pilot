# KDA Prompt: comm__comm__c330990d60

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`comm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `poolside/Laguna-M.1-NVFP4`
- Model folder: `llm/laguna_m1/b200`
- Kernel category: `comm`
- Max observed GPU share: `7.04%`
- Kernel name: `void (anonymous namespace)::all_reduce_two_shot_kernel<__nv_bfloat16, 8u, true>(host::distributed::AllReduceData const*, (anonymous namespace)::AllReduceParams, device::distributed::PullController)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 2.04% GPU, calls=1128, mean=68.40 us
- `random_high`: 7.04% GPU, calls=7896, mean=23.63 us
- `sharegpt_high`: 6.88% GPU, calls=7896, mean=22.03 us

## Promoted Shape Samples

1. `aten::copy_` via `external_id=9433`: `{"Concrete Inputs":["","","True"],"Input Dims":[[14],[14],[]],"Input Strides":[[1],[1],[]],"Input type":["int","int","Scalar"]}`
2. `aten::view` via `external_id=24542`: `{"Concrete Inputs":["","[244, 1024]"],"Input Dims":[[244,1024],[]],"Input Strides":[[1024,1],[]],"Input type":["c10::BFloat16","ScalarList"]}`
3. `aten::_to_copy` via `external_id=61718`: `{"Concrete Inputs":["","3","0","","","True",""],"Input Dims":[[7],[],[],[],[],[],[]],"Input Strides":[[1],[],[],[],[],[],[]],"Input type":["int","Scalar","Scalar","","","Scalar",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
