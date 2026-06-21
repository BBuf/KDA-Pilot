# KDA Prompt: comm__comm__9dd2e02622

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`comm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `moonshotai/Kimi-Linear-48B-A3B-Instruct`
- Model folder: `llm/kimi_linear/b200`
- Kernel category: `comm`
- Max observed GPU share: `3.05%`
- Kernel name: `void (anonymous namespace)::all_reduce_two_shot_kernel<__nv_bfloat16, 4u, true>(host::distributed::AllReduceData const*, (anonymous namespace)::AllReduceParams, device::distributed::PullController)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `sharegpt_high`: 3.05% GPU, calls=220, mean=142.70 us

## Promoted Shape Samples

1. `aten::split_with_sizes` via `external_id=156660`: `{"Concrete Inputs":["","[1024, 1024, 1024]","0"],"Input Dims":[[3072,1075],[],[]],"Input Strides":[[1,3336],[],[]],"Input type":["c10::BFloat16","ScalarList","Scalar"]}`
2. `aten::as_strided` via `external_id=157684`: `{"Concrete Inputs":["","[4898, 8, 128, 128]","[131072, 16384, 128, 1]","8345878528"],"Input Dims":[[20,4898,8,128,128],[],[],[]],"Input Strides":[[641990656,131072,16384,128,1],[],[],[]],"Input type":["float","ScalarList","ScalarList","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
