# KDA Prompt: comm__comm__a12cdaa5b4

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`comm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `inclusionAI/Ring-2.5-1T`
- Model folder: `llm/ring_25_1t/b200`
- Kernel category: `comm`
- Max observed GPU share: `31.39%`
- Kernel name: `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 8u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 31.39% GPU, calls=11592, mean=67.27 us
- `random_mid`: 11.38% GPU, calls=10304, mean=80.52 us
- `sharegpt_low`: 30.75% GPU, calls=11592, mean=64.91 us
- `sharegpt_mid`: 8.41% GPU, calls=10304, mean=67.60 us
- `sharegpt_high`: 9.06% GPU, calls=1288, mean=474.98 us

## Promoted Shape Samples

1. `sglang::outplace_all_reduce` via `external_id=1558`: `{"Concrete Inputs":["","",""],"Input Dims":[[39,8192],[],[]],"Input Strides":[[8192,1],[],[]],"Input type":["c10::BFloat16","",""]}`
2. `aten::view` via `external_id=1550`: `{"Concrete Inputs":["","[-1, 1024]"],"Input Dims":[[39,1024],[]],"Input Strides":[[1024,1],[]],"Input type":["c10::BFloat16","ScalarList"]}`
3. `aten::as_strided` via `external_id=36839`: `{"Concrete Inputs":["","[0]","[1]","0"],"Input Dims":[[0,1],[],[],[]],"Input Strides":[[1,1],[],[],[]],"Input type":["long int","ScalarList","ScalarList","Scalar"]}`
4. `sglang::outplace_all_reduce` via `external_id=132927`: `{"Concrete Inputs":["","",""],"Input Dims":[[44,8192],[],[]],"Input Strides":[[8192,1],[],[]],"Input type":["c10::BFloat16","",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
