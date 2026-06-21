# KDA Prompt: comm__comm__a12cdaa5b4

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`comm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `MiniMaxAI/MiniMax-M2.7`
- Model folder: `llm/minimax_m27/b200`
- Kernel category: `comm`
- Max observed GPU share: `17.19%`
- Kernel name: `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 8u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 17.19% GPU, calls=9000, mean=12.65 us
- `random_high`: 7.47% GPU, calls=7000, mean=17.46 us
- `sharegpt_low`: 15.36% GPU, calls=9000, mean=10.94 us
- `sharegpt_mid`: 3.51% GPU, calls=6000, mean=11.94 us
- `sharegpt_high`: 4.23% GPU, calls=4000, mean=17.22 us

## Promoted Shape Samples

1. `aten::empty_strided` via `external_id=4358`: `{"Concrete Inputs":["[]","[]","3","0","","False"],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","ScalarList","Scalar","Scalar","","Scalar"]}`
2. `aten::detach_` via `external_id=18508`: `{"Concrete Inputs":[""],"Input Dims":[[1]],"Input Strides":[[1]],"Input type":["long int"]}`
3. `aten::to` via `external_id=31546`: `{"Concrete Inputs":["","3","False","False",""],"Input Dims":[[1],[],[],[],[]],"Input Strides":[[1],[],[],[],[]],"Input type":["long int","Scalar","Scalar","Scalar",""]}`
4. `aten::view` via `external_id=38022`: `{"Concrete Inputs":["","[-1, 128]"],"Input Dims":[[59,1,128],[]],"Input Strides":[[1024,128,1],[]],"Input type":["c10::BFloat16","ScalarList"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
