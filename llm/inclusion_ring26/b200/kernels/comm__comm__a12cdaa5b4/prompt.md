# KDA Prompt: comm__comm__a12cdaa5b4

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`comm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `inclusionAI/Ring-2.6-1T`
- Model folder: `llm/inclusion_ring26/b200`
- Kernel category: `comm`
- Max observed GPU share: `12.20%`
- Kernel name: `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 8u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 9.01% GPU, calls=9016, mean=99.93 us
- `random_high`: 4.55% GPU, calls=1288, mean=647.84 us
- `sharegpt_mid`: 12.20% GPU, calls=9016, mean=117.67 us
- `sharegpt_high`: 5.99% GPU, calls=1288, mean=789.18 us

## Promoted Shape Samples

1. `sglang::outplace_all_reduce` via `external_id=25643`: `{"Concrete Inputs":["","",""],"Input Dims":[[38,8192],[],[]],"Input Strides":[[8192,1],[],[]],"Input type":["c10::BFloat16","",""]}`
2. `aten::as_strided` via `external_id=25055`: `{"Concrete Inputs":["","[38, 576]","[2112, 1]","1536"],"Input Dims":[[38,2112],[],[],[]],"Input Strides":[[2112,1],[],[],[]],"Input type":["c10::BFloat16","ScalarList","ScalarList","Scalar"]}`
3. `aten::view` via `external_id=74272`: `{"Concrete Inputs":["","[-1, 8, 128]"],"Input Dims":[[38,8,128],[]],"Input Strides":[[1024,128,1],[]],"Input type":["float","ScalarList"]}`
4. `sglang::outplace_all_reduce` via `external_id=156261`: `{"Concrete Inputs":["","",""],"Input Dims":[[17,8192],[],[]],"Input Strides":[[8192,1],[],[]],"Input type":["c10::BFloat16","",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
